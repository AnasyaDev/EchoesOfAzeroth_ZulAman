import csv, collections, re, sys
lf = {}
for line in open("listfile.csv", encoding="utf-8", errors="replace"):
    a,_,b = line.rstrip("\n").partition(";")
    if a.isdigit(): lf[int(a)] = b
kits = collections.defaultdict(list)
for r in csv.DictReader(open("SoundKitEntry.csv", encoding="utf-8")):
    kits[int(r["SoundKitID"])].append(int(r["FileDataID"]))
zm = {int(r["ID"]): r for r in csv.DictReader(open("ZoneMusic.csv", encoding="utf-8"))}
zim = {int(r["ID"]): r for r in csv.DictReader(open("ZoneIntroMusicTable.csv", encoding="utf-8"))}
areas = {int(r["ID"]): r for r in csv.DictReader(open("areatable.csv", encoding="utf-8"))}
children = collections.defaultdict(list)
for i, a in areas.items(): children[int(a["ParentAreaID"])].append(i)
def stem(f): return lf.get(f, "?").split("/")[-1].rsplit(".",1)[0]
def fam(fdids):
    d = collections.OrderedDict()
    for f in sorted(fdids):
        s = stem(f)
        m = re.match(r"MUS_1\d\d_(.+)_([A-Z])$", s)
        if m: d.setdefault(m.group(1).replace("_"," "), []).append(m.group(2))
        else:
            m2 = re.match(r"(.+?)(\d{2})$", s)
            if m2: d.setdefault(m2.group(1)+"##", []).append(m2.group(2))
            else: d.setdefault(s, [])
    out = []
    for k,v in d.items():
        if k.endswith("##"): out.append(k[:-2] + (v[0]+"…"+v[-1] if len(v)>2 else "/".join(v)))
        elif v: out.append(f"{k} {'/'.join(v)}")
        else: out.append(k)
    return " + ".join(out)
def native(i):
    z = int(areas[i]["ZoneMusic"])
    if not z: return "—", ""
    r = zm[z]; fd=set()
    for k in (int(r["Sounds_0"]), int(r["Sounds_1"])): fd |= set(kits.get(k, []))
    return fam(fd), r["SetName"]
def intro(i):
    x = int(areas[i]["IntroSound"])
    if not x: return ""
    z = zim.get(x)
    if not z: return f"ZIM{x}?"
    return f'{z["Name"]}→{",".join(stem(f) for f in kits.get(int(z["SoundID"]),[]))}'
def dump(root, depth=0):
    a = areas[root]; nat, setname = native(root)
    print("  "*depth + f'{root:>6} "{a["AreaName_lang"]}" ({a["ZoneName"]}) cont={a["ContinentID"]} zm={a["ZoneMusic"]} [{setname}] {nat} intro={intro(root)}')
    for c in sorted(children.get(root, [])): dump(c, depth+1)

print("################ rows matching Aman/Coiled/Utek/Ulatek/Tokka/Hex Lord/Amanizar/Zeb/Atal")
for i,a in sorted(areas.items()):
    if re.search(r"aman|coiled|utek|ulatek|tokka|amanizar|zeb'|zeb|atal", a["ZoneName"]+" "+a["AreaName_lang"], re.I):
        print(f'{i:>6} "{a["AreaName_lang"]}" ({a["ZoneName"]}) cont={a["ContinentID"]} parent={a["ParentAreaID"]} zm={a["ZoneMusic"]}')
print()
for root in (16365,):
    print(f"################ TREE {root} (Coiled Isle)"); dump(root); print()
# Midnight Zul'Aman: any root-level area named Zul'Aman on a non-legacy continent
za_roots = [i for i,a in areas.items() if a["AreaName_lang"]=="Zul'Aman" and a["ParentAreaID"]=="0"]
print("Zul'Aman roots:", [(i, areas[i]["ContinentID"], areas[i]["ZoneName"]) for i in za_roots])
for i in za_roots:
    print(f"################ TREE {i} Zul'Aman cont={areas[i]['ContinentID']}"); dump(i); print()
# Coiled Isle instances: find continents whose root areas mention Utek/Vault
print("################ continents with Atal'Utek / Vault areas")
for i,a in sorted(areas.items()):
    if re.search(r"utek|vault|amani foothold|cursed depths|profaned|ruuk|seal of wrath|underbelly|restless bones", a["AreaName_lang"], re.I) and a["ParentAreaID"]=="0":
        print(f"################ TREE {i} cont={a['ContinentID']}"); dump(i); print()
print("################ TBC Ghostlands 3433 tree"); dump(3433); print()
print("################ TBC Zul'Aman raid areas (continent 568)")
for i,a in sorted(areas.items()):
    if a["ContinentID"]=="568" and a["ParentAreaID"]=="0": dump(i)
print()
print("################ Zul'Gurub (continent 309 / 859) roots")
for i,a in sorted(areas.items()):
    if a["ContinentID"] in ("309","859") and a["ParentAreaID"]=="0": dump(i)
print()
print("################ UiMap children of 2437 / 2512 / 2585")
for r in csv.DictReader(open("UiMap.csv", encoding="utf-8")):
    if r["ParentUiMapID"] in ("2437","2512","2585") or r["ID"] in ("2437","2512","2585","2568"):
        print(f'  {r["ID"]:>5} "{r["Name_lang"]}" parent={r["ParentUiMapID"]} type={r["Type"]} flags={r["Flags"]} system={r["System"]}')
print("################ Map rows")
for r in csv.DictReader(open("Map.csv", encoding="utf-8")):
    if re.search(r"aman|coiled|utek|ulatek|tokka", r["MapName_lang"]+" "+r["Directory"], re.I):
        print(f'  {r["ID"]:>5} {r["Directory"]:<28} "{r["MapName_lang"]}" type={r["MapType"]} inst={r["InstanceType"]} exp={r["ExpansionID"]} area={r["AreaTableID"]} parent={r["ParentMapID"]}')
print("################ Midnight music families (MUS_120 / MUS_121) matching troll/amani/coiled keywords")
fams = collections.Counter()
for f,p in lf.items():
    m = re.search(r"/(MUS_1[0-9]{2}_[A-Za-z0-9_]+?)_([A-Z]|Stinger\d*|H\d?)\.mp3$", p)
    if m and re.search(r"aman|amani|zeb|loa|troll|atal|coiled|utek|ulatek|tokka|tortollan|naga|serpent|kithix|malacrass|hex|vault|mire|lurk|fang|whisper|wrath|121_", m.group(1), re.I):
        fams[m.group(1)] += 1
for k,v in sorted(fams.items()): print(f"  {v:>2} {k}")
print("################ all MUS_121 families")
f121 = collections.Counter()
for f,p in lf.items():
    m = re.search(r"/(MUS_121_[A-Za-z0-9_]+?)_([A-Z]|Stinger\d*|H\d?)\.mp3$", p)
    if m: f121[m.group(1)] += 1
for k,v in sorted(f121.items()): print(f"  {v:>2} {k}")
