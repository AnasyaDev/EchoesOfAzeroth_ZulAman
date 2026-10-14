import csv, collections, re
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
known = {}
for f in ("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", "/home/loadren/Documents/Code/EchoesOfAzeroth_QuelThalas/Tracks.lua"):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
        if m: known.setdefault(int(m.group(1)), float(m.group(2)))
for r in csv.reader(open("durations_za.csv")):
    if r and r[0].isdigit() and not r[1].startswith("error"): known.setdefault(int(r[0]), float(r[1]))
inplugin = set()
for line in open("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", encoding="utf-8"):
    m = re.match(r"\s*[A-Za-z_][A-Za-z0-9_]*\s*=\s*(\d+),", line)
    if m: inplugin.add(int(m.group(1)))
PLACES = r"zul'?farrak|zul'?gurub|gundrak|drak'?tharon|zul'?drak|echo isles|darkspear|sen'?jin|jintha|shadra'?alor|revantusk village|agol'?watha|zun'?watha|seradane|atal'?hakkar|sunken temple|gurubashi|zul'?kunda|zul'?mamwe|balia'?mah|ziata'?jai|bal'?lal|kal'?ai|mizjah|zuuldaia|nazmir|vol'?dun|zuldazar|dazar'?alor|atal'?dazar|king'?s rest|isle of thunder|thunder isle|isle of giants|zeb'?tula|za'?tual|zandalari|shrine of shadra|temple of rezan|throne of rezan|temple of the prophet|conqueror's terrace|court of bones|zeb'?halak|drakil'?jin|jintha'?kalar|zim'?torga|zim'?abwa|zim'?rhuk|altar of (mam'?toth|quetz'?lun|rhunok|sseratus|har'?koa)|gundrak|voltarus|kilnara|hakkar|nazwatha|port of zem'?lan|golden isle|tal'?aman|tal'?farrak|atal'?jani|atal'?gral|zeb'?ahari|garden of the loa|terrace of the fang|temple of kimbul|heart of sethraliss|temple of sethraliss|sanctuary of the devoted|zul'?toa|scalefang|rakjan|kraal|mugambala|grand bazaar|bay of kings|walk of kings|halls of opulence|loa's sanctum|path of the ancestors|krag'?wa|antul'?mita|primal wetlands|torga's rest|nazwatha|zul'?ja|xibala|zul'?nazman|hinterlands|lower sumprushes|upper sumprushes|the briny muck|forgotten mire|sra'?vess|zangarmarsh|tor'?watha|zeb'?nowa|zeb'?sora|zeb'?tela|amani pass|amani catacombs|shadowpine|witherbark|skullsplitter|bloodscalp|mossflayer|frostmane|zul'?aman|amani'?zar|zeb'?alar|coiled isle|tokka|mlurkkr|vaults of atal'?utek|zul'?jan|ula'?tek|venomous abyss|kindo'?jan|tidebound grotto|gnarldor|venomfall"
sets = collections.OrderedDict()
for i, a in sorted(areas.items()):
    if not re.search(PLACES, a["AreaName_lang"], re.I): continue
    z = int(a["ZoneMusic"])
    if not z: continue
    sets.setdefault(z, []).append(f'{i}:{a["AreaName_lang"]}(c{a["ContinentID"]})')
print(f"{len(sets)} ZoneMusic sets used by troll places\n")
for z, ar in sets.items():
    r = zm[z]; fd = set()
    for k in (int(r["Sounds_0"]), int(r["Sounds_1"])): fd |= set(kits.get(k, []))
    print(f'## ZoneMusic {z} "{r["SetName"]}"  areas={ar[:7]}{"…" if len(ar)>7 else ""}')
    for f in sorted(fd):
        d = known.get(f)
        print(f"    {f:>8} {lf.get(f,'?').split('/')[-1]:<44} dur={'%.1f'%d if d else '?':<6} {'PLUGIN' if f in inplugin else ''}")
# intros for those places
print("\n## Intros (ZoneIntroMusicTable) of troll places")
for i, a in sorted(areas.items()):
    if re.search(PLACES, a["AreaName_lang"], re.I) and int(a["IntroSound"]):
        zr = zim.get(int(a["IntroSound"]))
        if zr:
            files = [lf.get(f,'?').split('/')[-1] for f in kits.get(int(zr["SoundID"]), [])]
            print(f'    {i} {a["AreaName_lang"]} -> {zr["Name"]}: {files}')
