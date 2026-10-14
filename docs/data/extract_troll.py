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
areas = {int(r["ID"]): r for r in csv.DictReader(open("areatable.csv", encoding="utf-8"))}
areas_by_zm = collections.defaultdict(list)
for i,a in areas.items():
    if int(a["ZoneMusic"]): areas_by_zm[int(a["ZoneMusic"])].append(a["AreaName_lang"])
known = {}
for f in ("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", "/home/loadren/Documents/Code/EchoesOfAzeroth_QuelThalas/Tracks.lua"):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
        if m: known.setdefault(int(m.group(1)), float(m.group(2)))
inplugin = set()
for line in open("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", encoding="utf-8"):
    m = re.match(r"\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*(\d+),", line)
    if m: inplugin.add(int(m.group(1)))
KW = r"troll|zul|gurub|farrak|drak|gundrak|amani|darkspear|durotar|echoisle|echo_isle|zandalar|zuldazar|dazar|nazmir|voldun|vol_dun|sethraliss|kingsrest|kings_rest|atal|hakkar|_loa|voodoo|zeb|senjin|thunderisle|thunder_isle|hinterland|jintha|vilebranch|witherbark|revantusk|shadowpine|skullsplitter|bloodscalp|mossflayer|drakkari|frostmane|farraki|sandfury|gurubashi|ulatek|ula_tek|coiled|mlurkkr|tokka|zuljan|soulcoiler|venomous"
rows = []
for f, p in lf.items():
    pl = p.lower()
    if not (pl.startswith("sound/music/") and pl.endswith(".mp3")): continue
    if not re.search(KW, pl): continue
    ks = sorted(kit_of.get(f, []))
    zms = sorted(set().union(*[zm_by_kit.get(k, set()) for k in ks])) if ks else []
    ar = sorted(set(sum([areas_by_zm.get(z, []) for z in zms], [])))
    rows.append((p, f, known.get(f), f in inplugin, ar))
rows.sort(key=lambda r: r[0].lower())
# group by folder/family
def family(p):
    parts = p.split("/")
    base = parts[-1].rsplit(".",1)[0]
    m = re.match(r"(MUS_\d+_[A-Za-z0-9]+(?:_[A-Za-z0-9]+)*?)(?:_[A-Z]\d?|_UU\d+|_H\d?|_Stinger\d*|_\d+|_v\d)?$", base, re.I)
    fam = m.group(1) if m else base
    return "/".join(parts[2:-1]) + " :: " + fam
groups = collections.OrderedDict()
for r in rows: groups.setdefault(family(r[0]), []).append(r)
print(f"{len(rows)} troll-keyword music files in {len(groups)} families\n")
for g, rs in groups.items():
    have = sum(1 for r in rs if r[2] is not None); inp = sum(1 for r in rs if r[3])
    allareas = sorted(set(sum([r[4] for r in rs], [])))
    print(f"## {g}  ({len(rs)} files, {inp} in plugin, {have} with duration)  areas={allareas[:8]}{'…' if len(allareas)>8 else ''}")
    for p, f, d, ip, ar in rs:
        print(f"    {f:>8} {p.split('/')[-1]:<44} dur={'%.1f'%d if d else '?':<6} {'PLUGIN' if ip else ''}")
