import csv, re
from pathlib import Path
ROOT = Path("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman")
LOCS = ["frFR","deDE","esES","esMX","ptBR","ruRU","itIT","koKR","zhCN","zhTW"]
lf = {}
for line in open("listfile.csv", encoding="utf-8", errors="replace"):
    a,_,b = line.rstrip("\n").partition(";")
    if a.isdigit(): lf[int(a)] = b
dur = {}
for f in ("/home/loadren/Documents/Code/EchoesOfAzeroth_QuelThalas/Tracks.lua",):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
        if m: dur.setdefault(int(m.group(1)), float(m.group(2)))
import subprocess
old = subprocess.run(["git","-C",str(ROOT),"show","HEAD:Tracks.lua"],capture_output=True,text=True).stdout
for line in old.splitlines():
    m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
    if m: dur.setdefault(int(m.group(1)), float(m.group(2)))
for r in csv.reader(open("durations_za.csv")):
    if r and r[0].isdigit() and not r[1].startswith("error"): dur.setdefault(int(r[0]), float(r[1]))
def stem(f): return lf[f].split("/")[-1].rsplit(".",1)[0]
def ids(rgx):
    r = re.compile(rgx, re.I)
    return sorted(f for f,p in lf.items() if p.lower().startswith("sound/music/") and p.lower().endswith(".mp3") and r.search(p.split("/")[-1]))
WORDS = {"zandalarilament":"ZandalariLament","zuldazarintro":"ZuldazarIntro","zuldazarbazaar":"ZuldazarBazaar","zuldazarjungle":"ZuldazarJungle","ataldazar":"AtalDazar","cityofgold":"CityOfGold","zandalaritroll":"ZandalariTroll","zandalarforever":"ZandalarForever","maintheme":"MainTheme","bloodmagic":"BloodMagic","bloodsacrifice":"BloodSacrifice","nazmirvoid":"NazmirVoid","nazmirswamp":"NazmirSwamp","heartofsethraliss":"HeartOfSethraliss","nagaincursion":"NagaIncursion","altarbloodgod":"AltarBloodGod","cacheofmadness":"CacheOfMadness","templebethek":"TempleBethekk","devilsterrace":"DevilsTerrace","terracedevils":"TerraceDevils","thecoil":"TheCoil","bethekk":"Bethekk","mandokir":"Mandokir","loa":"Loa","zuldazar":"Zuldazar","drum":"Drum","voldun":"Voldun","sethrak":"Sethrak","akunda":"Akunda","bwonsamdi":"Bwonsamdi","paku":"Paku","shadra":"Shadra"}
def sym(prefix, f, strip=""):
    s = stem(f)
    if strip: s = re.sub(strip, "", s, flags=re.I)
    if prefix in ("BFA_", "CATA_ZG_"):
        parts = [WORDS.get(x.lower(), x.upper() if (len(x) <= 2 or re.match(r"^UU\d+$", x, re.I)) else x.capitalize()) for x in s.split("_") if x]
        return prefix + "".join(parts)
    s = re.sub(r"[^A-Za-z0-9]+", "", s)
    return prefix + s
SECTIONS = [
 ("TBC > Zul'Aman raid (ZoneMusic 371/372): AMB = walk, BTL = battle, VCT = victory", [(sym("ZA_", f, r"^ZA_zulaman_"), f) for f in ids(r"^ZA_zulaman_")]),
 ("Vanilla > Zul'Farrak set (also Jintha'Alor, Echo Isles, Frostmane)", [(sym("ZF_", f, r"^ZF"), f) for f in ids(r"^ZF(Quiet|Rally)")]),
 ("Vanilla > Jungle set (Stranglethorn troll ruins, Witherbark Village)", [(sym("CL_", f), f) for f in ids(r"^(Day|Night)Jungle0\d")]),
 ("Vanilla > Zul'Gurub", [("ZG_VooDoo", 53254)]),
 ("Wrath > Zul'Drak walk, altar intros, Northrend troll general", [(sym("", f).replace("ZDGeneral","ZD_General").replace("ZDHarKoa","ZD_HarKoa").replace("ZDMamToth","ZD_MamToth").replace("ZDQuetzLun","ZD_QuetzLun").replace("ZDRhunok","ZD_Rhunok").replace("ZDSseratus","ZD_Sseratus").replace("NRTroll","NR_Troll"), f) for f in ids(r"^ZD_") + ids(r"^NR_Troll_General")]),
 ("TBC > Zangarmarsh (general walk, Coilfang)", [(sym("ZM_", f, r"^ZA_"), f) for f in ids(r"^ZA_(General|Coilfang)WalkUni")]),
 ("TBC > Ghostlands dark set (Amani Catacombs)", [(sym("", f).replace("GLEversong","GL_Eversong"), f) for f in ids(r"^GL_EversongDarkWalkUni")]),
 ("Cataclysm > Zul'Gurub (The Coil, Bethekk, Blood God, Cache of Madness, Mandokir, Devil's Terrace)", [(sym("CATA_ZG_", f, r"^MUS_41_ZA_"), f) for f in ids(r"^MUS_41_ZA_(?!devilsterrace|terracedevils)")]),
 ("Cataclysm > Stranglethorn (Gurubashi)", [(sym("CATA_", f, r"^MUS_"), f) for f in ids(r"^MUS_Stranglethorn(Vale)?_GU0[1-4]")]),
 ("Cataclysm > Durotar / Darkspear Strand", [(sym("CATA_", f, r"^MUS_"), f) for f in ids(r"^MUS_Durotar[A-D]_GU")]),
 ("MoP > Zandalari, Isle of Thunder, troll battle", [(sym("MOP_", f, r"^MUS_52_"), f) for f in ids(r"^MUS_52_(Zandalari_[12]_[ABC]_0\d|ZandalariProphecy|ThunderIsle_[ABC]_0\d|TrollBattle_[AB]_0\d)")]),
 ("BfA > Zuldazar, Dazar'alor, Atal'Dazar", [(sym("BFA_", f, r"^mus_8\d\d?_"), f) for f in ids(r"^mus_80_(zuldazar_[12]_[a-h]|zuldazarintro_[a-h]|zuldazarjungle_[a-s]|zuldazarbazaar_\d_h|zuldazar_drum|zandalarilament_[a-h]|ataldazar_[a-h]|cityofgold_[a-h])") + ids(r"^mus_815_zandalaritroll_\d_[a-c]") + ids(r"^mus_81_zandalarforever_[a-j]")]),
 ("BfA > Loa of Zandalar", [(sym("BFA_", f, r"^mus_80_"), f) for f in ids(r"^mus_80_loa_(akunda|bwonsamdi|paku|shadra|maintheme)_[a-h]")]),
 ("BfA > Nazmir (swamp, blood trolls, void)", [(sym("BFA_", f, r"^mus_80_"), f) for f in ids(r"^mus_80_(nazmirswamp|bloodmagic|bloodsacrifice|nazmirvoid)_[a-h]")]),
 ("BfA > Vol'dun, Sethrak, Sethraliss", [(sym("BFA_", f, r"^mus_80_"), f) for f in ids(r"^mus_80_(voldun_[a-h]|sethrak_\d_[a-h]|heartofsethraliss_\d_[a-h])")]),
 ("BfA > Naga incursion", [(sym("BFA_", f, r"^mus_80_"), f) for f in ids(r"^mus_80_nagaincursion_[a-h]")]),
 ("Midnight 12.0 > Zul'Aman native families (mixed packs only)", [(sym("MN_", f, r"^MUS_120_"), f) for f in ids(r"^MUS_120_(ZulAman|Amanizar_Village|ZebAlar|Halazzi_Loa|Janalai_Loa|Nalorakk_Loa|Akilzon_Loa|AtalAman|AtalAbasi|Twilights_Blade)_[A-Z]\.mp3$")]),
 ("Midnight 12.1 > The Coiled Isle native families (mixed packs only)", [(sym("MN_", f, r"^MUS_121_"), f) for f in ids(r"^MUS_121_(Coiled_Isle|Serpents_Tail|Whispering_March|Mlurkkr_Mire|Venomous_Abyss|Tokkas_Landing)_[A-Z]\.mp3$")]),
]
L = ["local _, ns = ...", "",
"-- ============================================================",
"-- Track catalog — FileDataIDs from the wowdev community listfile",
"-- (build 12.1.0.69814), grouped by era and source.  Durations were",
"-- measured with ffprobe on the files served by wago.tools.",
"--",
"-- Prefixes: ZA_ Zul'Aman raid (TBC), ZF_ Zul'Farrak (Vanilla),",
"-- CL_ Classic jungle set, ZG_ Zul'Gurub (Vanilla), ZD_/NR_ Zul'Drak",
"-- and Northrend trolls (Wrath), ZM_ Zangarmarsh (TBC), GL_ Ghostlands",
"-- (TBC), CATA_/MOP_/BFA_ later troll music (optional packs),",
"-- MN_ Midnight native music (mixed packs only).",
"-- ============================================================", "", "ns.Tracks = {", ""]
rows = []; seenf=set(); seens=set()
for comment, rr in SECTIONS:
    L.append(f"    -- {comment} " + "-"*max(3, 64-len(comment)))
    for s, f in rr:
        assert f in dur, (s, f, stem(f))
        assert f not in seenf and s not in seens, (s, f)
        seenf.add(f); seens.add(s)
        L.append(f"    {s:<32} = {f},"); rows.append((s,f))
    L.append("")
L.append("}"); L += ["", "-- Durations in seconds, keyed by FileDataID.", "", "ns.TrackDurations = {"]
for s,f in rows: L.append(f"    [{f}] = {dur[f]:6.1f},  -- {s}")
L.append("}")
(ROOT/"Tracks.lua").write_text("\n".join(L)+"\n", encoding="utf-8")
print("Tracks.lua:", len(rows), "tracks")
# ---------------- Locale ----------------
areas = {int(r["ID"]): r["AreaName_lang"] for r in csv.DictReader(open("areatable.csv", encoding="utf-8"))}
loc = {l: {int(r["ID"]): r["AreaName_lang"] for r in csv.DictReader(open(f"areatable_{l}.csv", encoding="utf-8"))} for l in LOCS}
NAMES = [("ZULAMAN",15947),("THE_COILED_ISLE",16365),("VAULTS_OF_ATAL_UTEK",16535),("ATAL_AMAN",16194),("THE_RING_OF_GLORY",16781)]
SUBS = [
 ("AMANI_ZAR_VILLAGE",16183),("WITHERBARK_BLUFFS",16202),("TORNTUSK_OVERLOOK",16586),
 ("TEMPLE_OF_AKILZON",16184),("AKILZONS_REACH",16187),("TEMPLE_OF_JANALAI",16185),("TEMPLE_OF_HALAZZI",16186),
 ("SPIRITPAW_BOROUGH",16188),("NALORAKKS_PROWL",16189),("SPIRITPAW_BACKWOODS",16190),
 ("SPEAKERS_REST",16191),("BROKEN_THRONE",16192),("REVANTUSK_SEDGE",16193),
 ("ATAL_AMAN",16194),("TALONSTRIKE_TERRACE",16382),("SWIFTCLAW_TERRACE",16383),("RAGEMAW_TERRACE",16384),("FIREWING_TERRACE",16385),("WARLORDS_STAIR",16386),("ALTAR_OF_MALACRASS",16670),
 ("ATAL_ABASI",16195),("LEECH_BOG",16197),("MAISARA_DEEPS",16199),("THE_SKYBRIDGE",16380),("HERMITS_MOORING",16721),
 ("ZEB_ALAR_LUMBERYARD",16200),("BITTERBARK",16201),
 ("TOKKAS_LANDING",16774),("TOKKAS_FOLLY",16830),
 ("OFIS_HUT",16775),("MLURKKR_MIRE",16776),("CLOUDLIGHT_BEACON",16777),("WRECK_OF_PAKUS_TALON",16778),("WRECK_OF_TORGAS_BEAK",16779),
 ("ZAIL_ZAR_SPAN",16769),("GATE_OF_THE_EASTERN_FANG",16785),("THE_FANGS",16789),("PATH_OF_WHISPERS",16790),("GATE_OF_THE_SERPENTS_EYE",16791),("VENOM_RISE",16792),("BLISTERING_TERRACE",16793),("THE_SERPENTS_TAIL",16795),
 ("THE_ALTAR_OF_WRATH",16771),("THE_WHISPERING_MARSH",16780),("THE_RING_OF_GLORY",16781),("DEFIANT_RING",16782),
 ("CRYPT_OF_THE_DENIED",16755),("CRYPT_OF_THE_LOST_MASON",16992),("KINS_REST",16993),("BLISTERING_VAULT",16994),("TOMB_OF_THE_LOST_PRIEST",16995),("CRYPT_OF_THE_LOST_WARRIOR",16996),("CRYPT_OF_THE_DISGRACED",16997),
 ("VAULTS_OF_ATAL_UTEK",17316),("AMANI_FOOTHOLD",17650),("NORTHERN_AMANI_BULWARK",17729),("EASTERN_AMANI_OUTPOST",17730),
]
def lua_str(s):
    out = []
    for ch in s:
        if ch == '"': out.append('\\"')
        elif ch == '\\': out.append('\\\\')
        elif ord(ch) < 128: out.append(ch)
        else: out.append("".join(f"\\{b}" for b in ch.encode("utf-8")))
    return '"' + "".join(out) + '"'
def line(prefix, key, text, width):
    s = f"    {prefix}.{key:<{width}} = {lua_str(text)}"
    if any(ord(c) >= 128 for c in text): s += f"  -- {text}"
    return s
W = max(len(k) for k,_ in SUBS)
O = ["local _, ns = ...", "",
"-- ============================================================",
"-- Localization: AreaTable.AreaName_lang values of build 12.1.0.69814",
"-- for every client locale, so they match GetSubZoneText() exactly.",
"-- Non-ASCII characters are written as UTF-8 byte escapes.",
"-- ============================================================", "", "local names = {"]
for k,i in NAMES: O.append(f"    {k:<{W}} = {lua_str(areas[i])},")
O += ["}", "", "local subzones = {"]
for k,i in SUBS: O.append(f"    {k:<{W}} = {lua_str(areas[i])},")
O += ["}", "", "local locale = GetLocale()", ""]
first = True
for l in LOCS:
    O.append(("if " if first else "elseif ") + f'locale == "{l}" then'); first = False
    for k,i in NAMES: O.append(line("names", k, loc[l][i], W))
    O.append("")
    for k,i in SUBS: O.append(line("subzones", k, loc[l][i], W))
    O.append("")
O += ["end", "", "ns.L = setmetatable(names, {", "    __index = function(_, key) return key end,", "})", "",
"ns.SubzoneNames = subzones", "", "ns.SubzoneKeys = {}", "for key, localizedName in pairs(subzones) do", "    ns.SubzoneKeys[localizedName] = key", "end"]
(ROOT/"Locale.lua").write_text("\n".join(O)+"\n", encoding="utf-8")
for l in ["enUS"]+LOCS:
    src = areas if l=="enUS" else loc[l]
    by = {}
    for k,i in SUBS: by.setdefault(src[i], set()).add(k)
    bad = {t:ks for t,ks in by.items() if len(ks)>1}
    if bad: print("COLLISION", l, bad)
print("Locale.lua:", len(SUBS), "subzones")
