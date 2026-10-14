import csv, collections, re
from pathlib import Path
OUT = Path("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/docs/PLAN.md")
LOCS = ["frFR","deDE","esES","esMX","ptBR","ruRU","itIT","koKR","zhCN","zhTW"]
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
loc = {l: {int(r["ID"]): r["AreaName_lang"] for r in csv.DictReader(open(f"areatable_{l}.csv", encoding="utf-8"))} for l in LOCS}
dur = {}; inplugin = {}
for f in ("/home/loadren/Documents/Code/EchoesOfAzeroth_ZulAman/Tracks.lua", "/home/loadren/Documents/Code/EchoesOfAzeroth_QuelThalas/Tracks.lua"):
    for line in open(f, encoding="utf-8"):
        m = re.match(r"\s*\[(\d+)\]\s*=\s*([0-9.]+)", line)
        if m: dur.setdefault(int(m.group(1)), float(m.group(2)))
        m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(\d+),", line)
        if m and "ZulAman" in f: inplugin[int(m.group(2))] = m.group(1)
for r in csv.reader(open("durations_za.csv")):
    if r and r[0].isdigit() and not r[1].startswith("error"): dur.setdefault(int(r[0]), float(r[1]))
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
    if not z: return "—"
    r = zm[z]; fd=set()
    for k in (int(r["Sounds_0"]), int(r["Sounds_1"])): fd |= set(kits.get(k, []))
    return fam(fd)
def intro(i):
    x = int(areas[i]["IntroSound"])
    if not x: return ""
    z = zim.get(x)
    return ", ".join(stem(f) for f in kits.get(int(z["SoundID"]),[])) if z else ""
def en(i): return areas[i]["AreaName_lang"]
def fr(i): return loc["frFR"].get(i,"?")
def dstr(f):
    d = dur.get(f); return f"{d:.1f}" if d else "à mesurer"

ROLE = {
 15947:"Racine : forêt amani (« Forest General »)",
 16730:"Anse de chasse (« Forest Prey »), kit natif = placeholder Shadowlands",
 16196:"Côte funéraire (zm = 0)", 16198:"Sanctuaire de Kulzi (zm = 0)", 16203:"Camp (zm = 0)", 16204:"Sanctuaire de Filo (zm = 0)",
 16348:"Profondeurs (zm = 0)", 16352:"Cryptes (zm = 0)", 16367:"Vallée (zm = 0)", 16375:"Tanière, micro-carte 2580 (zm = 0)",
 16379:"Détroit (zm = 0)", 16418:"Guet (zm = 0)", 16567:"Crypte, micro-carte 2583 (zm = 0)", 16568:"Puits (zm = 0)", 16598:"La Souche (zm = 0)",
 16841:"Tombe de Mun'jin (« SpeakersRestMicro », zm = 0)", 16860:"Mer (zm = 0)", 17720:"Mer (zm = 0)",
 16183:"Hub principal amani (« Hub AmaniZar »)", 16202:"Village Witherbark (« Hub General »)", 16586:"Belvédère Torntusk (« Hub General »)",
 16184:"Temple du loa aigle Akil'zon", 16187:"Domaine d'Akil'zon", 16185:"Temple du loa faucon-dragon Jan'alai", 16186:"Temple du loa lynx Halazzi",
 16188:"Bourg des Spiritpaw, tribu de l'ours (« Nalorakk Temple »)", 16189:"Rôderie de Nalorakk", 16190:"Bois des Spiritpaw",
 16191:"Repos de l'Orateur, occupé par la Lame du Crépuscule", 16192:"Trône brisé (Atal'Kaldan), base de la Lame du Crépuscule", 16193:"Sedge des Revantusk, même kit",
 16194:"Cité-temple, autel de Malacrass (intro AtalAman_H)", 16382:"Terrasse (hérite d'Atal'Aman)", 16383:"Terrasse", 16384:"Terrasse", 16385:"Terrasse", 16386:"Escalier du seigneur de guerre", 16670:"Autel de Malacrass",
 16195:"Marais d'Atal'Abasi (« Swamp »)", 16197:"Tourbière", 16199:"Profondeurs de Maisara", 16380:"Pont du ciel", 16721:"Mouillage de l'ermite",
 16200:"Scierie de Zeb'Alar (« Lumber »)", 16201:"Bitterbark, même kit",
 16365:"Racine : forêt de l'île (« Forest General »)",
 16783:"Épave (zm = 0)", 16784:"Entrée du gouffre Gnarldor (zm = 0)", 16786:"Porte ouest (zm = 0)", 16787:"Le Forum (intro Coiled_Isle_H, zm = 0)", 16788:"Épave (zm = 0)", 16824:"Dent de Sargoth (zm = 0)", 16897:"Arche du plongeur (zm = 0)", 17718:"Mer (zm = 0)", 17719:"Mer (zm = 0)",
 16774:"Hub tortollan du capitaine Tokka : kit natif = SILENCE (Silent_310)", 16830:"Folie de Tokka, même silence",
 16775:"Hutte d'Ofi (« Mire »)", 16776:"Mangrove aux murlocs et gnarldins", 16777:"Balise (« Mire »)", 16778:"Épave de la Serre de Paku (« Mire »)", 16779:"Épave du Bec de Torga (« Mire »)",
 16769:"Passerelle de Zail'Zar (« Venom Exterior »)", 16785:"Porte du Croc est", 16789:"Les Crocs", 16790:"Chemin des murmures", 16791:"Porte de l'Œil du serpent (intro Serpents_Tail_E)", 16792:"Montée du venin", 16793:"Terrasse cloquante (intro)", 16795:"Queue du serpent (intro), fief des Enfants d'Ula'tek",
 16771:"Autel de la colère (« Spirit »)", 16780:"Marais murmurant (« Spirit »)", 16781:"Anneau de gloire, arène d'événement (carte 2633)", 16782:"Anneau défiant",
 16755:"Crypte (zm = 0, micro-carte 2639)", 16992:"Crypte (zm = 0, 2643)", 16993:"Repos des proches (zm = 0, 2645)", 16994:"Caveau (zm = 0)", 16995:"Tombe (zm = 0, 2642)", 16996:"Crypte (zm = 0, 2641)", 16997:"Crypte (zm = 0, 2644)",
 17316:"Entrée extérieure des Chambres fortes (« Venom Vaults »)",
 16535:"Racine des Chambres fortes (carte monde 2916 / UiMap 2509)", 17650:"Hub amani (« Vaults Hub »)", 17729:"Hub amani nord", 17730:"Hub amani est",
 16977:"Couvée de Ruuk'Jar (zm = 0)", 16978:"Caveau des os agités (zm = 0)", 16979:"Mausolée profané (zm = 0)", 16990:"Le Bas-Ventre (« BigMicro », zm = 0)", 17022:"Profondeurs maudites (zm = 0)", 17023:"Sceau de la colère (zm = 0)",
}
PROP = {}
def prop(ids, p):
    for i in ids: PROP[i] = p
prop([15947,16730,16196,16198,16203,16204,16348,16352,16367,16375,16379,16418,16567,16568,16598,16841,16860,17720], "AMANI")
prop([16183,16202,16586], "TROLL_VILLAGE")
prop([16184,16187], "SHRINE_AKILZON"); prop([16185], "SHRINE_JANALAI"); prop([16186], "SHRINE_HALAZZI"); prop([16188,16189,16190], "SHRINE_NALORAKK")
prop([16191,16192,16193], "BLOOD_CULT")
prop([16194,16382,16383,16384,16385,16386,16670], "CITY_OF_GOLD")
prop([16195,16197,16199,16380,16721], "NAZMIR_SWAMP")
prop([16200,16201], "GURUBASHI")
prop([16365,16783,16784,16786,16787,16788,16824,16897,17718,17719], "ZULDAZAR_JUNGLE")
prop([16774,16830], "DARKSPEAR_COAST")
prop([16775,16776,16777,16778,16779], "ZANGARMARSH")
prop([16769,16785,16789,16790,16791,16792,16793,16795], "SERPENT_COIL")
prop([16771,16780,16781,16782], "DRAKKARI")
prop([16755,16992,16993,16994,16995,16996,16997], "AMANI_CATACOMBS")
prop([17316,16535,16977,16978,16979,16990,17022,17023], "BLOOD_GOD")
prop([17650,17729,17730], "AMANI")

ZA_GROUPS = [
 ("A. Forêt et lieux sans musique propre (héritent de la racine)", [15947,16730,16196,16198,16203,16204,16348,16352,16367,16375,16379,16418,16567,16568,16598,16841,16860,17720]),
 ("B. Villages (hubs)", [16183,16202,16586]),
 ("C. Temples des loa", [16184,16187,16185,16186,16188,16189,16190]),
 ("D. Occupation de la Lame du Crépuscule", [16191,16192,16193]),
 ("E. Atal'Aman, la cité-temple", [16194,16382,16383,16384,16385,16386,16670]),
 ("F. Marais", [16195,16197,16199,16380,16721]),
 ("G. Scierie", [16200,16201]),
]
CI_GROUPS = [
 ("A. Forêt et lieux sans musique propre", [16365,16783,16784,16786,16787,16788,16824,16897,17718,17719]),
 ("B. Hub tortollan (silence natif)", [16774,16830]),
 ("C. Mangrove", [16775,16776,16777,16778,16779]),
 ("D. Venin : les Enfants d'Ula'tek", [16769,16785,16789,16790,16791,16792,16793,16795]),
 ("E. Esprits", [16771,16780,16781,16782]),
 ("F. Cryptes et tombes", [16755,16992,16993,16994,16995,16996,16997]),
 ("G. Chambres fortes d'Atal'Utek, entrée extérieure", [17316]),
]
VA_GROUPS = [("Chambres fortes d'Atal'Utek (Map 2916, monde ouvert, UiMap 2509)", [16535,17650,17729,17730,16977,16978,16979,16990,17022,17023])]

# catalogue troll toutes époques : (titre, note, [fdid...])
def ids(rgx):
    r = re.compile(rgx, re.I)
    return sorted(f for f,p in lf.items() if p.lower().startswith("sound/music/") and p.lower().endswith(".mp3") and r.search(p.split("/")[-1]))
CATALOG = [
 ("Amani, raid Zul'Aman (TBC)", "Le set de marche AMB10–15 est réutilisé par Blizzard pour Strangleronce, Hinterlands, Îles de l'Écho, Zul'Farrak, Temple englouti, Zul'Gurub Cata : c'est le « son troll universel ». BTL = combat, VCT = victoire.", ids(r"^ZA_zulaman_")),
 ("Zul'Farrak, Sombrelance et Jintha'Alor (Vanilla)", "Le vrai set des trolls de Zul'Farrak, joué aussi à Jintha'Alor, Bal'lal/Ziata'jai, aux Îles de l'Écho et chez les Frostmane. Absent du plugin, qui utilise Tanaris en substitut pour « Sandfury ».", ids(r"^ZF(Quiet|Rally)")),
 ("Jungle (Vanilla)", "Set générique des ruines trolls de Strangleronce (Zul'Mamwe, Kal'ai, Mizjah) et de Witherbark Village.", ids(r"^(Day|Night)Jungle0\d")),
 ("Sombrelance, côte de Durotar (Cataclysm)", "Darkspear Strand ; dans le plugin (pack Darkspear).", ids(r"^MUS_Durotar[A-D]_GU")),
 ("Gurubashi, Strangleronce (Cataclysm)", "Arène des Gurubashi et vallée ; dans le plugin.", [441768,441769,441770,441771,441772,441773,441774,441775]),
 ("Zul'Gurub (Cataclysm)", "La Spirale (The Coil, Venoxis le serpent), Temple de Bethekk, Autel du dieu sanglant, Cache de la folie, Domaine de Mandokir, Terrasse du Diable. Blizzard réutilise thecoil/templebethek pour le Temple du Croc de Vol'dun (serpents). Absent du plugin, sauf ZulGurubVooDoo.", ids(r"^MUS_41_ZA_") + [53254]),
 ("Drakkari, Zul'Drak et Drak'Tharon (Wrath)", "Marche jour/nuit, intros des autels de loa (Har'koa le léopard, Rhunok l'ours, Quetz'lun, Mam'toth, Sseratus le serpent) ; dans le plugin.", ids(r"^ZD_") + ids(r"^NR_Troll_General")),
 ("Zandalari, Île du Tonnerre (MoP)", "Dans le plugin.", ids(r"^MUS_52_(Zandalari|ThunderIsle_[ABC]_0|TrollBattle)")),
 ("Zandalari, Zuldazar et Atal'Dazar (BfA)", "Jungle, ville d'or, temples, lamentation, Zandalar Forever ; dans le plugin sauf cityofgold et bazaar.", ids(r"^mus_80_(zuldazar|zandalarilament|ataldazar|cityofgold)") + ids(r"^mus_815_zandalaritroll") + ids(r"^mus_81_zandalarforever")),
 ("Loa de Zandalar (BfA)", "Thèmes d'Akunda, Bwonsamdi, Paku, Shadra et thème principal des loa. Absent du plugin.", ids(r"^mus_80_loa_") + [2146263]),
 ("Nazmir (BfA)", "Marais des trolls de sang, magie du sang, Nazwatha (Vide). Absent du plugin.", ids(r"^mus_80_(nazmirswamp|bloodmagic|bloodsacrifice|nazmirvoid)")),
 ("Vol'dun et Sethraliss (BfA)", "Désert des Sethrak, Sanctuaire des Dévoués, Cœur de Sethraliss (loa serpent). Absent du plugin.", ids(r"^mus_80_(voldun|sethrak|heartofsethraliss)")),
 ("Naga (BfA)", "Incursions naga d'Atal'Gral et de la Grève de Krag'wa ; l'île a des naga.", ids(r"^mus_80_nagaincursion")),
 ("Zangarmarsh (TBC)", "Mangrove : marche générale et Coilfang.", ids(r"^ZA_(General|Coilfang)WalkUni")),
 ("Terres Fantômes, set sombre (TBC)", "Catacombes amani, An'daroth, ziggourats ; dans le plugin Quel'Thalas.", ids(r"^GL_EversongDarkWalkUni")),
 ("Zul'Aman (Midnight 12.0)", "Familles natives, dans le plugin.", ids(r"^MUS_120_(ZulAman|Amanizar_Village|ZebAlar|Halazzi_Loa|Janalai_Loa|Nalorakk_Loa|Akilzon_Loa|AtalAman|AtalAbasi)_")),
 ("Lame du Crépuscule (Midnight 12.0)", "Dans le plugin Quel'Thalas.", ids(r"^MUS_120_Twilights_Blade_")),
 ("Île Annelée (Midnight 12.1)", "Familles natives 12.1 : forêt, Queue du serpent, Marais murmurant, Mangrove, Abîme venimeux, hub Tokka (joué au gouffre Gnarldor, le hub lui-même est silencieux), Enfants d'Ula'tek et Soulcoiler (combat), UlaTek 1–3 (raid), Zul'jan (Autel des Crocs), Naga Lair (Grotte).", ids(r"^MUS_121_(?!RTC)")),
]

PACKS = [
 ("AMANI", "Amani (TBC)", "ZA_zulaman_AMB10–15 (existe : ZULAMAN)", "racine de Zul'Aman, lieux sans musique, hubs des Chambres fortes"),
 ("TROLL_VILLAGE", "Troll Village (Vanilla + TBC)", "kit natif des Îles de l'Écho : ZA_zulaman_AMB11–15 + ZFQuiet1/2/7, ZFQuietShort8, ZFRally9", "Amani'Zar Village, Witherbark Bluffs, Torntusk Overlook"),
 ("SANDFURY", "Zul'Farrak (Vanilla)", "ZFQuiet1/2/7, ZFQuietShort8, intro ZFRally9 ; remplace le substitut Tanaris du pack actuel (ou s'y ajoute)", "pack utilitaire"),
 ("SHRINE_HALAZZI", "Shrine of Har'koa (Wrath)", "intro ZD_HarKoa_Intro01, any ZD_GeneralWalk jour/nuit + NR_Troll_General", "Temple de Halazzi (lynx ↔ Har'koa le léopard des neiges)"),
 ("SHRINE_NALORAKK", "Shrine of Rhunok (Wrath)", "intro ZD_Rhunok_Intro01, même rotation", "Spiritpaw, Nalorakk's Prowl (ours ↔ Rhunok)"),
 ("SHRINE_JANALAI", "Shrine of Quetz'lun (Wrath)", "intro ZD_QuetzLun_Intro01, même rotation", "Temple de Jan'alai (faucon-dragon ↔ Quetz'lun le serpent-vent)"),
 ("SHRINE_AKILZON", "Shrine of Paku (BfA)", "intro mus_80_loa_paku_a, any mus_80_loa_paku_d + ZD rotation", "Temple d'Akil'zon, Akil'zon's Reach (aigle ↔ Paku le ptérrordax)"),
 ("BLOOD_CULT", "Blood Trolls (BfA)", "mus_80_bloodmagic_a–e/h + mus_80_bloodsacrifice_a–d/h + mus_80_nazmirvoid_a–c/h", "Speaker's Rest, Broken Throne, Revantusk Sedge (Lame du Crépuscule) ; alternative TBC : set sombre des Terres Fantômes"),
 ("CITY_OF_GOLD", "Atal'Dazar (BfA)", "mus_80_ataldazar_a–d/h (existe) + mus_80_cityofgold_a/b/h", "Atal'Aman et ses terrasses (Atal ↔ Atal)"),
 ("NAZMIR_SWAMP", "Nazmir (BfA)", "mus_80_nazmirswamp_a–f/h", "Atal'Abasi, Leech Bog, Maisara Deeps, Skybridge, Hermit's Mooring ; alternative TBC : Zangarmarsh"),
 ("GURUBASHI", "Gurubashi (Cataclysm)", "existe", "Zeb'Alar Lumberyard, Bitterbark"),
 ("ZULDAZAR_JUNGLE", "Zuldazar Jungle (BfA)", "mus_80_zuldazarjungle_a–s (existe dans Zandalari BFA, à isoler)", "racine de l'Île Annelée et lieux sans musique ; alternative TBC : Amani"),
 ("DARKSPEAR_COAST", "Darkspear Strand (Cataclysm)", "MUS_DurotarA_GU01, B_GU03/04, C_GU01/02 (kit natif de la côte sombrelance)", "Tokka's Landing, Tokka's Folly (natif = silence : autre option NONE)"),
 ("ZANGARMARSH", "Zangarmarsh (TBC)", "ZA_GeneralWalkUni01–06 + ZA_CoilfangWalkUni01–03", "Mlurkkr Mire, Ofi's Hut, Cloudlight Beacon, épaves"),
 ("SERPENT_COIL", "The Coil (Cataclysm)", "intro MUS_41_ZA_thecoil_UU01, any thecoil_UU02 + templebethek_UU01/02 + bethekk_UU01/02 + ZulGurubVooDoo (kit que Blizzard réutilise au Temple du Croc)", "Zail'Zar Span, Gates, The Fangs, Path of Whispers, Venom Rise, Blistering Terrace, The Serpent's Tail ; alternative : Sethrak (BfA)"),
 ("SETHRAK", "Sethraliss (BfA)", "mus_80_sethrak_1_a/h, 2_a/h + heartofsethraliss_1/2_a/h + voldun_c/e", "alternative pour les lieux du venin"),
 ("DRAKKARI", "Drakkari (Wrath)", "existe", "Altar of Wrath, Whispering Marsh, Ring of Glory, Defiant Ring (esprits) ; alternative : Loa de Zandalar"),
 ("LOA_SPIRITS", "Loa of Zandalar (BfA)", "mus_80_loa_maintheme_a/d/h + bwonsamdi_c/d/h + shadra_d/h + akunda_a/b/c/h", "alternative pour les lieux des esprits"),
 ("AMANI_CATACOMBS", "Amani Catacombs (TBC)", "GL_EversongDarkWalkUni01–04", "les sept cryptes et tombes de l'île"),
 ("BLOOD_GOD", "Altar of the Blood God (Cataclysm)", "intro MUS_41_ZA_altarbloodgod_UU01, any altarbloodgod_UU02/03 + mandokir_UU01/02 + cacheofmadness_UU01/02 + ZA_zulaman_BTL11–15", "Chambres fortes d'Atal'Utek (extérieur et intérieur, hors hubs) ; alternative : Temple englouti = Amani"),
]

L = []; w = L.append
w("# EchoesOfAzeroth_ZulAman — plan de refonte : Zul'Aman et l'Île Annelée")
w("")
w("Rédigé le 16/09/2026 à partir des tables de jeu 12.1.0.69814 (wago.tools : AreaTable en 11 langues, ZoneMusic, SoundKitEntry, ZoneIntroMusicTable, UiMap, Map) et du listfile wowdev. Même méthode que le plan Voidstorm. Les durées non encore mesurées sont marquées « à mesurer » ; les mesures ffprobe sont dans `docs/data/durations_za.csv`.")
w("")
w("## 0. Point de départ")
w("")
w("Le plugin actuel mappe une seule carte, `[2437]` Zul'Aman, sur le pack Zul'Aman (TBC), sans aucune sous-zone, et livre dix-huit packs (Amani, loa natifs, Sombrelance, Drakkari, Gurubashi, Sandfury, Zandalari, Atal'ai, Troll Mixed). Or Zul'Aman compte une quarantaine de sous-zones réparties en sept familles musicales natives, et l'Île Annelée (12.1, UiMap 2512) en ajoute autant avec cinq familles 12.1, plus les Chambres fortes d'Atal'Utek, qui sont une carte monde ouverte (Map 2916, UiMap 2509) et non une instance.")
w("")
w("Cadre supposé, hérité des décisions Voidstorm et à confirmer :")
w("")
w("- zone monde uniquement (`[2437]`, `[2512]`, `[2509]`, plus les sous-cartes ouvertes 2536 Atal'Aman et 2633 Ring of Glory à vérifier en jeu) ; donjons, raid, lair, gouffres et micro-cartes non mappés ;")
w("- packs « classiques » (Vanilla à BfA) et packs mixés ; les packs natifs Midnight déjà livrés (Zul'Aman Midnight, Zeb'Alar, quatre loa) sont à garder ou à retirer, voir §6 ;")
w("- toute la musique troll est éligible, pas seulement TBC : le raid TBC ne compte que douze fichiers.")
w("")
w("## 1. Midnight — cartes")
w("")
w("| UiMapID | Nom | Type | Parent | Usage |")
w("|---|---|---|---|---|")
w("| 2437 | Zul'Aman | zone | 2537 Quel'Thalas | entrée principale, sous-zones par `GetSubZoneText()` |")
w("| 2536 | Atal'Aman | zone (flags 4) | 2437 | sous-carte ouverte de la cité-temple, comme Slayer's Rise : entrée `[2536]` si `/eoa now` la remonte |")
w("| 2585 | Zul'Aman | zone (flags 524288) | 2437 | carte cachée, nature inconnue : à identifier avec `/eoa now` |")
w("| 2512 | The Coiled Isle | zone | 2537 | entrée principale de l'île |")
w("| 2509 | Vaults of Atal'Utek | zone (flags 4) | 2512 | Map 2916, instanceType 0 : monde ouvert, entrée `[2509]` |")
w("| 2633 | The Ring of Glory | zone | 2512 | arène d'événement ouverte : entrée `[2633]` à confirmer |")
w("| 2580 / 2583 / 2584 / 2639–2645 | tanières et cryptes | micro | 2437 / 2512 | grottes du monde ouvert : le core remonte au parent, pas d'entrée |")
w("| 2501, 2503/2504, 2513/2514/2564, 2535, 2647/2648 | Maisara Caverns, Twilight Crypts, Den of Nalorakk, Atal'Aman (gouffre), Labyrinth of Kindo'jan | donjon / gouffre | 2437 | non mappés |")
w("| 2606–2610, 2632, 2634, 2635 | The Venomous Abyss, Tidebound Grotto, Venomfall Deeps, Gnarldor Isle | raid / lair / gouffres | 2512 | non mappés |")
w("")
w("## 2. Midnight — sous-zones et musique native")
w("")
w("Colonne « natif » = kit ZoneMusic réellement joué (lettres des fichiers). « — » = pas de kit propre, le jeu hérite du parent. Colonne « pack » = proposition (§4).")
w("")
def table(groups):
    for title, ids_ in groups:
        w(f"#### {title}"); w("")
        w("| AreaID | enUS | frFR | Natif | Rôle | Pack |"); w("|---|---|---|---|---|---|")
        for i in ids_:
            it = intro(i)
            w(f"| {i} | {en(i)} | {fr(i)} | {native(i)}{(' ; intro ' + it) if it else ''} | {ROLE.get(i,'')} | `{PROP.get(i,'')}` |")
        w("")
w("### 2.1 Zul'Aman (AreaTable 15947, UiMap 2437)"); w(""); table(ZA_GROUPS)
w("### 2.2 L'Île Annelée (AreaTable 16365, UiMap 2512)"); w(""); table(CI_GROUPS)
w("### 2.3 Chambres fortes d'Atal'Utek (AreaTable 16535, Map 2916, UiMap 2509)"); w(""); table(VA_GROUPS)
w("Remarques :")
w("")
w("- Tokka's Landing et Tokka's Folly jouent nativement un fichier de silence : toute musique y sera un ajout, l'option `NONE` reste possible.")
w("- Les familles 12.1 « Children of Ula'tek », « Soulcoiler Combat », « UlaTek 1–3 », « Zul'jan » et « Naga Lair » ne sont rattachées à aucune aire du monde ouvert (combat, raid, lair, autel des Crocs) : inutiles pour les défauts, utilisables en packs mixés.")
w("- Thresh Cove joue un placeholder Shadowlands (Seat of the Primus), comme Gnawing Reach à Voidstorm.")
w("- Amani Pass, Zeb'Nowa, Tor'Watha et les ruines de Zeb'tela sont dans Eversong (plugin Quel'Thalas), pas ici.")
w("")
w("## 3. Catalogue troll, toutes époques")
w("")
w("Chaque famille avec ses FDID, sa durée (mesurée ou à mesurer) et si elle est déjà déclarée dans le plugin (symbole).")
w("")
for title, note, fl in CATALOG:
    w(f"### {title}"); w(""); w(note); w("")
    w("| FDID | Fichier | Durée (s) | Dans le plugin |"); w("|---|---|---|---|")
    for f in fl:
        w(f"| {f} | {stem(f)} | {dstr(f)} | {inplugin.get(f,'')} |")
    w("")
w("## 4. Rapprochements et packs proposés")
w("")
w("| Lieu Midnight | Musique proposée | Pourquoi |")
w("|---|---|---|")
w("| Forêt de Zul'Aman, lieux sans kit | Amani (TBC) | le set du raid, déjà le défaut |")
w("| Amani'Zar Village, Witherbark Bluffs, Torntusk Overlook | kit natif des Îles de l'Écho (AMB11–15 + set Zul'Farrak) | c'est le « village troll » de Blizzard |")
w("| Temple de Halazzi (lynx) | autel de Har'koa (léopard des neiges, Zul'Drak) | même archétype félin |")
w("| Spiritpaw, Nalorakk (ours) | autel de Rhunok (ours, Zul'Drak) | même loa-ours |")
w("| Temple de Jan'alai (faucon-dragon) | autel de Quetz'lun (serpent-vent) | loa volant |")
w("| Temple d'Akil'zon (aigle) | Paku (ptérrordax, BfA) | loa ailé |")
w("| Speaker's Rest, Broken Throne, Revantusk Sedge | trolls de sang de Nazmir | occupation par un culte sombre ; alternative TBC : catacombes des Terres Fantômes |")
w("| Atal'Aman, terrasses, autel de Malacrass | Atal'Dazar + Cité d'or | cité-temple ↔ cité-temple |")
w("| Atal'Abasi, Leech Bog, Maisara Deeps, Skybridge, Hermit's Mooring | marais de Nazmir | marais troll ; alternative TBC : Zangarmarsh |")
w("| Zeb'Alar Lumberyard, Bitterbark | Gurubashi | jungle exploitée |")
w("| Forêt de l'Île Annelée | jungle de Zuldazar | île-jungle troll ; alternative TBC : Amani |")
w("| Tokka's Landing, Tokka's Folly | côte sombrelance (Durotar) | port troll en bord de mer ; natif = silence |")
w("| Mlurkkr Mire, Ofi's Hut, Cloudlight Beacon, épaves | Zangarmarsh (TBC) | mangrove |")
w("| Queue du serpent, Crocs, portes, Venom Rise, Blistering Terrace, Zail'Zar Span, Path of Whispers | The Coil (Zul'Gurub Cata) | Venoxis le serpent ; Blizzard réutilise ce kit pour le Temple du Croc de Vol'dun ; alternative : Sethrak |")
w("| Altar of Wrath, Whispering Marsh, Ring of Glory, Defiant Ring | Drakkari (Zul'Drak) | zone troll hantée par les esprits ; alternative : loa de Zandalar |")
w("| Cryptes et tombes de l'île | catacombes amani (Terres Fantômes, TBC) | tombes amani |")
w("| Chambres fortes d'Atal'Utek (hors hubs) | Autel du dieu sanglant (Zul'Gurub Cata) + combat TBC | temple-serpent souterrain |")
w("| Hubs des Chambres fortes | Amani (TBC) | camps amani |")
w("")
w("### 4.1 Packs")
w("")
w("| Clé | Label | Contenu | Zones par défaut |"); w("|---|---|---|---|")
for k,lab,cont,zones in PACKS: w(f"| `{k}` | {lab} | {cont} | {zones} |")
w("")
w("Packs mixés : chaque pack ci-dessus + la famille Midnight native des mêmes lieux (Amani + ZulAman, Troll Village + Amanizar Village, chaque Shrine + son loa, Blood Cult + Twilights Blade, City of Gold + AtalAman, Nazmir Swamp + AtalAbasi, Gurubashi + ZebAlar, Zuldazar Jungle + Coiled Isle, Darkspear Coast + Tokkas Landing, Zangarmarsh + Mlurkkr Mire, Serpent Coil + Serpents Tail, Drakkari + Whispering March, Amani Catacombs + Coiled Isle, Blood God + Venomous Abyss).")
w("")
w("### 4.2 Esquisse de `Zones.lua`")
w("")
w("```lua")
def sketch(mapid, namekey, default, ids_):
    w(f'[{mapid}] = Dsl.zone("{namekey}", "{default}", {{')
    seen=set()
    for i in ids_:
        p = PROP.get(i)
        if not p or p == default: continue
        key = re.sub(r"[^A-Z0-9]+", "_", en(i).upper()).strip("_")
        if key in seen: continue
        seen.add(key); w(f'    {key:<24} = "{p}",')
    w("}),")
sketch(2437, "ZULAMAN", "AMANI", [i for _,g in ZA_GROUPS for i in g])
sketch(2512, "THE_COILED_ISLE", "ZULDAZAR_JUNGLE", [i for _,g in CI_GROUPS for i in g])
sketch(2509, "VAULTS_OF_ATAL_UTEK", "BLOOD_GOD", [i for _,g in VA_GROUPS for i in g])
w('[2536] = Dsl.zone("ATAL_AMAN", "CITY_OF_GOLD"),      -- si la sous-carte est remontée en jeu')
w('[2633] = Dsl.zone("THE_RING_OF_GLORY", "DRAKKARI"),  -- idem')
w("```")
w("")
w("## 5. Étapes")
w("")
w("1. Valider §4 (choix des packs, alternatives) et les questions du §6.")
w("2. Mesurer les durées manquantes (script `docs/data/measure.py`), générer `Tracks.lua` (catalogue étendu) et `Locale.lua` (annexe A) depuis les CSV.")
w("3. Réécrire `Packs.lua` et `Zones.lua`, garder les packs existants demandés, corriger Sandfury.")
w("4. Harnais Lua 5.1 (celui de Voidstorm) dans les 11 locales, copie dans AddOns, `/eoa now` sur les cartes 2536, 2585, 2509 et 2633.")
w("5. Release 1.2.0 via `push_addon_release.py za` (bump mineur : nouvelles zones).")
w("")
w("## 6. Questions à trancher")
w("")
w("1. Packs natifs Midnight déjà livrés (Zul'Aman Midnight, Zeb'Alar, Halazzi/Jan'alai/Nalorakk/Akil'zon Loa, Troll Combat) : garder pour compatibilité des profils existants, ou retirer comme pour Voidstorm ?")
w("2. Sandfury : remplacer le substitut Tanaris par le vrai set de Zul'Farrak, ou garder les deux ?")
w("3. Tokka's Landing : musique (côte sombrelance) ou respect du silence natif ?")
w("4. Époque des défauts : pour un plugin « Zul'Aman » les défauts ci-dessus mélangent Vanilla, TBC, Cata, Wrath et BfA selon le meilleur miroir ; préférer un défaut tout-TBC (Amani partout, catacombes pour les cryptes, Zangarmarsh pour la mangrove) et laisser le reste en packs optionnels ?")
w("")
w("## Annexe A — noms localisés (AreaTable 12.1.0)")
w("")
allids = [i for _,g in ZA_GROUPS+CI_GROUPS+VA_GROUPS for i in g]
w("| AreaID | enUS | " + " | ".join(LOCS) + " |"); w("|---|---|" + "---|"*len(LOCS))
for i in allids:
    w(f"| {i} | {en(i)} | " + " | ".join(loc[l].get(i,'?') for l in LOCS) + " |")
w("")
w("## Annexe B — kits natifs, fichier par fichier")
w("")
seen=set()
for i in allids:
    z = int(areas[i]["ZoneMusic"])
    if not z or z in seen: continue
    seen.add(z); r = zm[z]
    users = [f"{j} {en(j)}" for j in allids if int(areas[j]["ZoneMusic"])==z]
    w(f"- **ZoneMusic {z}** « {r['SetName']} » (pauses {int(r['SilenceIntervalMin_0'])//1000}–{int(r['SilenceIntervalMax_0'])//1000} s) — {', '.join(users)}")
    fd=set()
    for k in (int(r["Sounds_0"]), int(r["Sounds_1"])): fd |= set(kits.get(k, []))
    for f in sorted(fd): w(f"  - {f} `{stem(f)}` ({dstr(f)} s)")
w("")
OUT.write_text("\n".join(L)+"\n", encoding="utf-8")
print(OUT, len(L), "lines")
