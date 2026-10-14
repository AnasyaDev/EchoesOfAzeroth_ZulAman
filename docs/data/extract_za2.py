import csv, collections, re
lf = {}
for line in open("listfile.csv", encoding="utf-8", errors="replace"):
    a,_,b = line.rstrip("\n").partition(";")
    if a.isdigit(): lf[int(a)] = b
kit_of = collections.defaultdict(set); kits = collections.defaultdict(list)
for r in csv.DictReader(open("SoundKitEntry.csv", encoding="utf-8")):
    kit_of[int(r["FileDataID"])].add(int(r["SoundKitID"])); kits[int(r["SoundKitID"])].append(int(r["FileDataID"]))
zm = {int(r["ID"]): r for r in csv.DictReader(open("ZoneMusic.csv", encoding="utf-8"))}
zm_by_kit = collections.defaultdict(set)
for z, r in zm.items():
    for k in (r["Sounds_0"], r["Sounds_1"]):
        if int(k): zm_by_kit[int(k)].add(z)
zim = {int(r["ID"]): r for r in csv.DictReader(open("ZoneIntroMusicTable.csv", encoding="utf-8"))}
zim_by_kit = collections.defaultdict(list)
for i, r in zim.items(): zim_by_kit[int(r["SoundID"])].append(r["Name"])
areas = {int(r["ID"]): r for r in csv.DictReader(open("areatable.csv", encoding="utf-8"))}
areas_by_zm = collections.defaultdict(list)
for i,a in areas.items():
    if int(a["ZoneMusic"]): areas_by_zm[int(a["ZoneMusic"])].append(f'{i}:{a["AreaName_lang"]}')
# known durations in the ZA plugin
known = {}
for line in open("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", encoding="utf-8"):
    m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
    if m: known[int(m.group(1))] = float(m.group(2))
for line in open("/home/loadren/Documents/Code/EchoesOfAzeroth_QuelThalas/Tracks.lua", encoding="utf-8"):
    m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
    if m: known.setdefault(int(m.group(1)), float(m.group(2)))
def show(rgx, title):
    print(f"\n===== {title}  [{rgx}]")
    for f, p in sorted(lf.items(), key=lambda kv: kv[1].lower()):
        if re.search(rgx, p, re.I):
            ks = sorted(kit_of.get(f, []))
            zms = sorted(set().union(*[zm_by_kit.get(k, set()) for k in ks])) if ks else []
            ar = sorted(set(sum([areas_by_zm.get(z, []) for z in zms], [])))
            intros = sorted(set(sum([zim_by_kit.get(k, []) for k in ks], [])))
            d = known.get(f)
            print(f"{f:>8} {p.split('/')[-1]:<40} dur={d if d is not None else '?':<6} zm={zms} areas={ar[:6]}{'…' if len(ar)>6 else ''} intros={intros}")
show(r"ZONEMUSIC/Zulaman/", "TBC Zul'Aman folder")
show(r"MUS_41_ZA_|ZulGurubVooDoo|ZG_VoodooMoment|zulgurub", "Zul'Gurub (Classic + Cataclysm)")
show(r"ZONEMUSIC/ZangarMarsh/", "TBC Zangarmarsh folder")
show(r"GL_EversongDarkWalk", "Ghostlands dark set")
show(r"MUS_121_", "Midnight 12.1 families")
show(r"MUS_120_(ZulAman|Amanizar_Village|ZebAlar|Halazzi_Loa|Janalai_Loa|Nalorakk_Loa|Akilzon_Loa|AtalAman|AtalAbasi|Twilights_Blade|Troll_Combat|Gloom_Mire)_", "Midnight 12.0 Zul'Aman families")
# candidates lacking durations -> for measurement
cands = []
for f, p in lf.items():
    if re.search(r"ZONEMUSIC/Zulaman/|MUS_41_ZA_|ZulGurubVooDoo|ZONEMUSIC/ZangarMarsh/|GL_EversongDarkWalk|MUS_121_|MUS_120_(ZulAman|Amanizar_Village|ZebAlar|Halazzi_Loa|Janalai_Loa|Nalorakk_Loa|Akilzon_Loa|AtalAman|AtalAbasi|Twilights_Blade|Troll_Combat|Gloom_Mire)_", p, re.I) and f not in known and p.lower().endswith(".mp3"):
        cands.append(f)
open("za_candidates.txt","w").write(",".join(str(f) for f in sorted(cands)))
print(f"\n{len(cands)} files without a known duration -> za_candidates.txt")
