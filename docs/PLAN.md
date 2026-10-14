# EchoesOfAzeroth_ZulAman — plan de refonte : Zul'Aman et l'Île Annelée

Rédigé le 16/09/2026 à partir des tables de jeu 12.1.0.69814 (wago.tools : AreaTable en 11 langues, ZoneMusic, SoundKitEntry, ZoneIntroMusicTable, UiMap, Map) et du listfile wowdev. Même méthode que le plan Voidstorm. Les durées non encore mesurées sont marquées « à mesurer » ; les mesures ffprobe sont dans `docs/data/durations_za.csv`.

## Décisions (16/09/2026)

1. Packs natifs Midnight purs : **retirés**. Seuls restent les packs d'époque et leurs versions mixées (époque + kit natif du lieu).
2. Sandfury : **remplacé** par le vrai set de Zul'Farrak (Vanilla) ; le substitut Tanaris disparaît. Le catalogue est entièrement réécrit, rien de l'ancien n'est conservé (clés de packs nouvelles, voir README).
3. Tokka's Landing : **Sombrelance** (kit des Îles de l'Écho, ère classique).
4. Défauts **multi-époques mais ère classique** (Vanilla à Wrath) : Cataclysm, Pandaria et BfA passent en packs optionnels (Zul'Gurub Cata, Gurubashi, côte sombrelance, Zandalari MoP, Zuldazar, Atal'Dazar, loa de Zandalar, Nazmir, Vol'dun, naga). Conséquences sur le §4 : Lame du Crépuscule → catacombes amani (TBC), Atal'Aman et Chambres fortes → temple amani (marche + combat TBC), marais → Zangarmarsh, mangrove → Coilfang, scierie et forêt de l'île → jungle Vanilla, venin → Zul'Gurub Vanilla ouvert par l'autel de Sseratus, Akil'zon → Quetz'lun et Jan'alai → Mam'toth (Paku est BfA).

État : implémenté (Tracks/Locale générés par `docs/data/gen_plugin_za.py`, Packs/Zones réécrits), validé par le harnais Lua 5.1 dans les 11 locales, déployé dans AddOns pour test en jeu. Version cible 2.0.0.

## 0. Point de départ

Le plugin actuel mappe une seule carte, `[2437]` Zul'Aman, sur le pack Zul'Aman (TBC), sans aucune sous-zone, et livre dix-huit packs (Amani, loa natifs, Sombrelance, Drakkari, Gurubashi, Sandfury, Zandalari, Atal'ai, Troll Mixed). Or Zul'Aman compte une quarantaine de sous-zones réparties en sept familles musicales natives, et l'Île Annelée (12.1, UiMap 2512) en ajoute autant avec cinq familles 12.1, plus les Chambres fortes d'Atal'Utek, qui sont une carte monde ouverte (Map 2916, UiMap 2509) et non une instance.

Cadre supposé, hérité des décisions Voidstorm et à confirmer :

- zone monde uniquement (`[2437]`, `[2512]`, `[2509]`, plus les sous-cartes ouvertes 2536 Atal'Aman et 2633 Ring of Glory à vérifier en jeu) ; donjons, raid, lair, gouffres et micro-cartes non mappés ;
- packs « classiques » (Vanilla à BfA) et packs mixés ; les packs natifs Midnight déjà livrés (Zul'Aman Midnight, Zeb'Alar, quatre loa) sont à garder ou à retirer, voir §6 ;
- toute la musique troll est éligible, pas seulement TBC : le raid TBC ne compte que douze fichiers.

## 1. Midnight — cartes

| UiMapID | Nom | Type | Parent | Usage |
|---|---|---|---|---|
| 2437 | Zul'Aman | zone | 2537 Quel'Thalas | entrée principale, sous-zones par `GetSubZoneText()` |
| 2536 | Atal'Aman | zone (flags 4) | 2437 | sous-carte ouverte de la cité-temple, comme Slayer's Rise : entrée `[2536]` si `/eoa now` la remonte |
| 2585 | Zul'Aman | zone (flags 524288) | 2437 | carte cachée, nature inconnue : à identifier avec `/eoa now` |
| 2512 | The Coiled Isle | zone | 2537 | entrée principale de l'île |
| 2509 | Vaults of Atal'Utek | zone (flags 4) | 2512 | Map 2916, instanceType 0 : monde ouvert, entrée `[2509]` |
| 2633 | The Ring of Glory | zone | 2512 | arène d'événement ouverte : entrée `[2633]` à confirmer |
| 2580 / 2583 / 2584 / 2639–2645 | tanières et cryptes | micro | 2437 / 2512 | grottes du monde ouvert : le core remonte au parent, pas d'entrée |
| 2501, 2503/2504, 2513/2514/2564, 2535, 2647/2648 | Maisara Caverns, Twilight Crypts, Den of Nalorakk, Atal'Aman (gouffre), Labyrinth of Kindo'jan | donjon / gouffre | 2437 | non mappés |
| 2606–2610, 2632, 2634, 2635 | The Venomous Abyss, Tidebound Grotto, Venomfall Deeps, Gnarldor Isle | raid / lair / gouffres | 2512 | non mappés |

## 2. Midnight — sous-zones et musique native

Colonne « natif » = kit ZoneMusic réellement joué (lettres des fichiers). « — » = pas de kit propre, le jeu hérite du parent. Colonne « pack » = proposition (§4).

### 2.1 Zul'Aman (AreaTable 15947, UiMap 2437)

#### A. Forêt et lieux sans musique propre (héritent de la racine)

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 15947 | Zul'Aman | Zul’Aman | ZulAman A/B/C/D/F/H | Racine : forêt amani (« Forest General ») | `AMANI` |
| 16730 | Thresh Cove | Crique du Requin | mus_mx_cov_seatoftheprimus_01 | Anse de chasse (« Forest Prey »), kit natif = placeholder Shadowlands | `AMANI` |
| 16196 | Funerary Coast | Côte Funéraire | — | Côte funéraire (zm = 0) | `AMANI` |
| 16198 | Shrine of Kulzi | Sanctuaire de Kulzi | — | Sanctuaire de Kulzi (zm = 0) | `AMANI` |
| 16203 | Camp Stonewash | Camp Rochembruns | — | Camp (zm = 0) | `AMANI` |
| 16204 | Shrine of Filo | Sanctuaire de Filo | — | Sanctuaire de Filo (zm = 0) | `AMANI` |
| 16348 | Zul'Aman Depths | Profondeurs de Zul’Aman | — | Profondeurs (zm = 0) | `AMANI` |
| 16352 | Numazon Crypts | Cryptes de Numazon | — | Cryptes (zm = 0) | `AMANI` |
| 16367 | Solemn Valley | Vallée Solennelle | — | Vallée (zm = 0) | `AMANI` |
| 16375 | Loaknit Den | Tanière de Tisse-Loa | — | Tanière, micro-carte 2580 (zm = 0) | `AMANI` |
| 16379 | Strait of Hexx'alor | Détroit de Hexx’alor | — | Détroit (zm = 0) | `AMANI` |
| 16418 | Shadebasin Watch | Guet d’Ombre-Bassin | — | Guet (zm = 0) | `AMANI` |
| 16567 | Wit'Kalar Crypt | Crypte de Wit’Kalar | — | Crypte, micro-carte 2583 (zm = 0) | `AMANI` |
| 16568 | Miststone Wells | Puits de Brume-Roche | — | Puits (zm = 0) | `AMANI` |
| 16598 | The Stump | La Souche | — | La Souche (zm = 0) | `AMANI` |
| 16841 | Tomb of Mun'jin | Tombe de Mun’jin | — | Tombe de Mun'jin (« SpeakersRestMicro », zm = 0) | `AMANI` |
| 16860 | The Great Sea | Grande mer | — | Mer (zm = 0) | `AMANI` |
| 17720 | The Forbidding Sea | Mer Interdite | — | Mer (zm = 0) | `AMANI` |

#### B. Villages (hubs)

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16183 | Amani'Zar Village | Amani’Zar | Amanizar Village A/B/C/D/H/E | Hub principal amani (« Hub AmaniZar ») | `TROLL_VILLAGE` |
| 16202 | Witherbark Bluffs | Pitons de Fanécorce | Amanizar Village A/B/C/H/E | Village Witherbark (« Hub General ») | `TROLL_VILLAGE` |
| 16586 | Torntusk Overlook | Surplomb des Brocherompue | Amanizar Village A/B/C/H/E | Belvédère Torntusk (« Hub General ») | `TROLL_VILLAGE` |

#### C. Temples des loa

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16184 | Temple of Akil'zon | Temple d’Akil’zon | Akilzon Loa A/B/C | Temple du loa aigle Akil'zon | `SHRINE_AKILZON` |
| 16187 | Akil'zon's Reach | Confins d’Akil’zon | Akilzon Loa A/B/C | Domaine d'Akil'zon | `SHRINE_AKILZON` |
| 16185 | Temple of Jan'alai | Temple de Jan’alai | Janalai Loa A/B/C | Temple du loa faucon-dragon Jan'alai | `SHRINE_JANALAI` |
| 16186 | Temple of Halazzi | Temple d’Halazzi | Halazzi Loa A/B/C/H | Temple du loa lynx Halazzi | `SHRINE_HALAZZI` |
| 16188 | Spiritpaw Borough | Quartier des Pattes-Spirituelles | Nalorakk Loa C/D/E/H | Bourg des Spiritpaw, tribu de l'ours (« Nalorakk Temple ») | `SHRINE_NALORAKK` |
| 16189 | Nalorakk's Prowl | Maraude de Nalorakk | Nalorakk Loa C/D/E/H | Rôderie de Nalorakk | `SHRINE_NALORAKK` |
| 16190 | Spiritpaw Backwoods | Arrière pays Patte-Spirituelle | Nalorakk Loa C/D/E/H | Bois des Spiritpaw | `SHRINE_NALORAKK` |

#### D. Occupation de la Lame du Crépuscule

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16191 | Speaker's Rest | Repos de l’orateur | Twilights Blade B/C/E/F/G/I | Repos de l'Orateur, occupé par la Lame du Crépuscule | `BLOOD_CULT` |
| 16192 | Broken Throne | Trône brisé | Twilights Blade B/C/E/F/G/I | Trône brisé (Atal'Kaldan), base de la Lame du Crépuscule | `BLOOD_CULT` |
| 16193 | Revantusk Sedge | Carex des Vengebroches | Twilights Blade B/C/E/F/G/I | Sedge des Revantusk, même kit | `BLOOD_CULT` |

#### E. Atal'Aman, la cité-temple

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16194 | Atal'Aman | Atal’Aman | AtalAman A/B/C/D/E ; intro MUS_120_AtalAman_H | Cité-temple, autel de Malacrass (intro AtalAman_H) | `CITY_OF_GOLD` |
| 16382 | Talonstrike Terrace | Terrasse des Frappe-Serres | — | Terrasse (hérite d'Atal'Aman) | `CITY_OF_GOLD` |
| 16383 | Swiftclaw Terrace | Terrasse des Vivegriffes | — | Terrasse | `CITY_OF_GOLD` |
| 16384 | Ragemaw Terrace | Terrasse des Rage-Gueules | — | Terrasse | `CITY_OF_GOLD` |
| 16385 | Firewing Terrace | Terrasse des Ailes-de-Feu | — | Terrasse | `CITY_OF_GOLD` |
| 16386 | Warlord's Stair | Escalier du Seigneur de guerre | — | Escalier du seigneur de guerre | `CITY_OF_GOLD` |
| 16670 | Altar of Malacrass | Autel de Malacrass | — | Autel de Malacrass | `CITY_OF_GOLD` |

#### F. Marais

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16195 | Atal'Abasi | Atal’Abasi | AtalAbasi A/B/C/D/E/F/H | Marais d'Atal'Abasi (« Swamp ») | `NAZMIR_SWAMP` |
| 16197 | Leech Bog | Marais aux Sangsues | AtalAbasi A/B/C/D/E/F/H | Tourbière | `NAZMIR_SWAMP` |
| 16199 | Maisara Deeps | Tréfonds de Maisara | AtalAbasi A/B/C/D/E/F/H | Profondeurs de Maisara | `NAZMIR_SWAMP` |
| 16380 | The Skybridge | Le pont Céleste | AtalAbasi A/B/C/D/E/F/H | Pont du ciel | `NAZMIR_SWAMP` |
| 16721 | Hermit's Mooring | Amarrage de l’ermite | AtalAbasi A/B/C/D/E/F/H | Mouillage de l'ermite | `NAZMIR_SWAMP` |

#### G. Scierie

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16200 | Zeb'Alar Lumberyard | Scierie de Zeb’Alar | ZebAlar A/B/H/C/D/E/F | Scierie de Zeb'Alar (« Lumber ») | `GURUBASHI` |
| 16201 | Bitterbark | Amerécorce | ZebAlar A/B/H/C/D/E/F | Bitterbark, même kit | `GURUBASHI` |

### 2.2 L'Île Annelée (AreaTable 16365, UiMap 2512)

#### A. Forêt et lieux sans musique propre

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16365 | The Coiled Isle | Île Annelée | Coiled Isle A/B/C/H/D/E | Racine : forêt de l'île (« Forest General ») | `ZULDAZAR_JUNGLE` |
| 16783 | Wreck of Gral's Belly | Épave de la Panse de Gral | — | Épave (zm = 0) | `ZULDAZAR_JUNGLE` |
| 16784 | Gnarldor Isle | Île Torsadine | — | Entrée du gouffre Gnarldor (zm = 0) | `ZULDAZAR_JUNGLE` |
| 16786 | Gate of the Western Fang | Porte du Crochet occidental | — | Porte ouest (zm = 0) | `ZULDAZAR_JUNGLE` |
| 16787 | The Forum | Forum | — | Le Forum (intro Coiled_Isle_H, zm = 0) | `ZULDAZAR_JUNGLE` |
| 16788 | Wreck of Sethraliss's Scale | Épave de l’Écaille de Sephraliss | — | Épave (zm = 0) | `ZULDAZAR_JUNGLE` |
| 16824 | Tooth of Sargoth | Dent de Sargoth | — | Dent de Sargoth (zm = 0) | `ZULDAZAR_JUNGLE` |
| 16897 | Diver's Arch | Arche du plongeon | — | Arche du plongeur (zm = 0) | `ZULDAZAR_JUNGLE` |
| 17718 | The Great Sea | Grande mer | — | Mer (zm = 0) | `ZULDAZAR_JUNGLE` |
| 17719 | The Forbidding Sea | Mer Interdite | — | Mer (zm = 0) | `ZULDAZAR_JUNGLE` |

#### B. Hub tortollan (silence natif)

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16774 | Tokka's Landing | Débarcadère de Tokka | Silent_310 | Hub tortollan du capitaine Tokka : kit natif = SILENCE (Silent_310) | `DARKSPEAR_COAST` |
| 16830 | Tokka's Folly | Folie de Tokka | Silent_310 | Folie de Tokka, même silence | `DARKSPEAR_COAST` |

#### C. Mangrove

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16775 | Ofi's Hut | Hutte d’Ofi | Mlurkkr Mire A/B/C/D/H | Hutte d'Ofi (« Mire ») | `ZANGARMARSH` |
| 16776 | Mlurkkr Mire | Le Mrrglécage | Mlurkkr Mire A/B/C/D/H | Mangrove aux murlocs et gnarldins | `ZANGARMARSH` |
| 16777 | Cloudlight Beacon | Balise Luminuée | Mlurkkr Mire A/B/C/D/H | Balise (« Mire ») | `ZANGARMARSH` |
| 16778 | Wreck of Paku's Talon | Épave de la Serre de Paku | Mlurkkr Mire A/B/C/D/H | Épave de la Serre de Paku (« Mire ») | `ZANGARMARSH` |
| 16779 | Wreck of Torga's Beak | Épave du Bec de Torga | Mlurkkr Mire A/B/C/D/H | Épave du Bec de Torga (« Mire ») | `ZANGARMARSH` |

#### D. Venin : les Enfants d'Ula'tek

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16769 | Zail'Zar Span | Travée de Zail’Zar | Serpents Tail A/H/B/C/D/F ; intro MUS_121_Serpents_Tail_E | Passerelle de Zail'Zar (« Venom Exterior ») | `SERPENT_COIL` |
| 16785 | Gate of the Eastern Fang | Porte du Crochet oriental | Serpents Tail A/H/B/C/D/F | Porte du Croc est | `SERPENT_COIL` |
| 16789 | The Fangs | Les Crocs | Serpents Tail A/H/B/C/D/F | Les Crocs | `SERPENT_COIL` |
| 16790 | Path of Whispers | Sente des Murmures | Serpents Tail A/H/B/C/D/F | Chemin des murmures | `SERPENT_COIL` |
| 16791 | Gate of the Serpent's Eye | Porte de l’Œil du serpent | Serpents Tail A/H/B/C/D/F ; intro MUS_121_Serpents_Tail_E | Porte de l'Œil du serpent (intro Serpents_Tail_E) | `SERPENT_COIL` |
| 16792 | Venom Rise | Cime Venimeuse | Serpents Tail A/H/B/C/D/F | Montée du venin | `SERPENT_COIL` |
| 16793 | Blistering Terrace | Terrasse Infestée | Serpents Tail A/H/B/C/D/F ; intro MUS_121_Serpents_Tail_E | Terrasse cloquante (intro) | `SERPENT_COIL` |
| 16795 | The Serpent's Tail | La Serpentine | Serpents Tail A/H/B/C/D/F ; intro MUS_121_Serpents_Tail_E | Queue du serpent (intro), fief des Enfants d'Ula'tek | `SERPENT_COIL` |

#### E. Esprits

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16771 | The Altar of Wrath | Autel du Courroux | Whispering March A/B/C/D/E/H | Autel de la colère (« Spirit ») | `DRAKKARI` |
| 16780 | The Whispering Marsh | Marais Murmurant | Whispering March A/B/C/D/E/H | Marais murmurant (« Spirit ») | `DRAKKARI` |
| 16781 | The Ring of Glory | Arène de la Gloire | Whispering March A/B/C/D/E/H | Anneau de gloire, arène d'événement (carte 2633) | `DRAKKARI` |
| 16782 | Defiant Ring | Cercle de la Défiance | Whispering March A/B/C/D/E/H | Anneau défiant | `DRAKKARI` |

#### F. Cryptes et tombes

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16755 | Crypt of the Denied | Crypte des Bannis | — | Crypte (zm = 0, micro-carte 2639) | `AMANI_CATACOMBS` |
| 16992 | Crypt of the Lost Mason | Crypte des Architectes perdus | — | Crypte (zm = 0, 2643) | `AMANI_CATACOMBS` |
| 16993 | Kin's Rest | Repos des Ancêtres | — | Repos des proches (zm = 0, 2645) | `AMANI_CATACOMBS` |
| 16994 | Blistering Vault | Caveau Infesté | — | Caveau (zm = 0) | `AMANI_CATACOMBS` |
| 16995 | Tomb of the Lost Priest | Tombe du Clergé perdu | — | Tombe (zm = 0, 2642) | `AMANI_CATACOMBS` |
| 16996 | Crypt of The Lost Warrior | Crypte de l’Armée perdue | — | Crypte (zm = 0, 2641) | `AMANI_CATACOMBS` |
| 16997 | Crypt of the Disgraced | Crypte de la Disgrâce | — | Crypte (zm = 0, 2644) | `AMANI_CATACOMBS` |

#### G. Chambres fortes d'Atal'Utek, entrée extérieure

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 17316 | Vaults of Atal'Utek | Caveaux d’Atal’Utek | Venomous Abyss C/H/F/G/I/J | Entrée extérieure des Chambres fortes (« Venom Vaults ») | `BLOOD_GOD` |

### 2.3 Chambres fortes d'Atal'Utek (AreaTable 16535, Map 2916, UiMap 2509)

#### Chambres fortes d'Atal'Utek (Map 2916, monde ouvert, UiMap 2509)

| AreaID | enUS | frFR | Natif | Rôle | Pack |
|---|---|---|---|---|---|
| 16535 | Vaults of Atal'Utek | Caveaux d’Atal’Utek | Venomous Abyss C/H/F/G/I/J | Racine des Chambres fortes (carte monde 2916 / UiMap 2509) | `BLOOD_GOD` |
| 17650 | Amani Foothold | Tête de pont amani | Venomous Abyss A/B/D/E | Hub amani (« Vaults Hub ») | `AMANI` |
| 17729 | Northern Amani Bulwark | Rempart amani septentrional | Venomous Abyss A/B/D/E | Hub amani nord | `AMANI` |
| 17730 | Eastern Amani Outpost | Avant-poste amani oriental | Venomous Abyss A/B/D/E | Hub amani est | `AMANI` |
| 16977 | Ruuk'Jar's Clutch | Couvée de Ruuk’Jar | — | Couvée de Ruuk'Jar (zm = 0) | `BLOOD_GOD` |
| 16978 | Vault of Restless Bones | Caveau des Ossements tourmentés | — | Caveau des os agités (zm = 0) | `BLOOD_GOD` |
| 16979 | Profaned Mausoleum | Mausolée profané | — | Mausolée profané (zm = 0) | `BLOOD_GOD` |
| 16990 | The Underbelly | Entrailles | — | Le Bas-Ventre (« BigMicro », zm = 0) | `BLOOD_GOD` |
| 17022 | Cursed Depths | Profondeurs Maudites | — | Profondeurs maudites (zm = 0) | `BLOOD_GOD` |
| 17023 | The Seal of Wrath | Sceau du Courroux | — | Sceau de la colère (zm = 0) | `BLOOD_GOD` |

Remarques :

- Tokka's Landing et Tokka's Folly jouent nativement un fichier de silence : toute musique y sera un ajout, l'option `NONE` reste possible.
- Les familles 12.1 « Children of Ula'tek », « Soulcoiler Combat », « UlaTek 1–3 », « Zul'jan » et « Naga Lair » ne sont rattachées à aucune aire du monde ouvert (combat, raid, lair, autel des Crocs) : inutiles pour les défauts, utilisables en packs mixés.
- Thresh Cove joue un placeholder Shadowlands (Seat of the Primus), comme Gnawing Reach à Voidstorm.
- Amani Pass, Zeb'Nowa, Tor'Watha et les ruines de Zeb'tela sont dans Eversong (plugin Quel'Thalas), pas ici.

## 3. Catalogue troll, toutes époques

Chaque famille avec ses FDID, sa durée (mesurée ou à mesurer) et si elle est déjà déclarée dans le plugin (symbole).

### Amani, raid Zul'Aman (TBC)

Le set de marche AMB10–15 est réutilisé par Blizzard pour Strangleronce, Hinterlands, Îles de l'Écho, Zul'Farrak, Temple englouti, Zul'Gurub Cata : c'est le « son troll universel ». BTL = combat, VCT = victoire.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 53825 | ZA_zulaman_AMB10 | 113.8 | ZA_WalkUni01 |
| 53826 | ZA_zulaman_AMB11 | 74.5 | ZA_WalkUni02 |
| 53827 | ZA_zulaman_AMB12 | 108.6 | ZA_WalkUni03 |
| 53828 | ZA_zulaman_AMB13 | 70.5 | ZA_WalkUni04 |
| 53829 | ZA_zulaman_AMB14 | 90.5 | ZA_WalkUni05 |
| 53830 | ZA_zulaman_AMB15 | 113.9 | ZA_WalkUni06 |
| 53831 | ZA_zulaman_BTL11 | 136.2 | ZA_Battle01 |
| 53832 | ZA_zulaman_BTL12 | 117.1 | ZA_Battle02 |
| 53833 | ZA_zulaman_BTL13 | 40.7 | ZA_Battle03 |
| 53834 | ZA_zulaman_BTL14 | 92.4 | ZA_Battle04 |
| 53835 | ZA_zulaman_BTL15 | 79.8 | ZA_Battle05 |
| 53836 | ZA_zulaman_VCT10 | 80.0 | ZA_Victory01 |

### Zul'Farrak, Sombrelance et Jintha'Alor (Vanilla)

Le vrai set des trolls de Zul'Farrak, joué aussi à Jintha'Alor, Bal'lal/Ziata'jai, aux Îles de l'Écho et chez les Frostmane. Absent du plugin, qui utilise Tanaris en substitut pour « Sandfury ».

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 371374 | ZFQuiet1 | 79.4 |  |
| 371375 | ZFQuiet2 | 87.4 |  |
| 371376 | ZFQuiet7 | 53.1 |  |
| 371377 | ZFQuietShort8 | 17.7 |  |
| 371378 | ZFRally9 | 67.0 |  |

### Jungle (Vanilla)

Set générique des ruines trolls de Strangleronce (Zul'Mamwe, Kal'ai, Mizjah) et de Witherbark Village.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 53541 | DayJungle01 | 46.1 |  |
| 53542 | DayJungle02 | 98.7 |  |
| 53543 | DayJungle03 | 48.3 |  |
| 53544 | NightJungle01 | 54.7 |  |
| 53545 | NightJungle02 | 53.4 |  |
| 53546 | NightJungle03 | 89.1 |  |

### Sombrelance, côte de Durotar (Cataclysm)

Darkspear Strand ; dans le plugin (pack Darkspear).

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 441578 | MUS_DurotarA_GU01 | 124.7 | DU_GeneralA01 |
| 441579 | MUS_DurotarA_GU02 | 101.6 | DU_GeneralA02 |
| 441580 | MUS_DurotarA_GU03 | 101.6 | DU_GeneralA03 |
| 441581 | MUS_DurotarB_GU01 | 72.8 | DU_GeneralB01 |
| 441582 | MUS_DurotarB_GU02 | 72.1 | DU_GeneralB02 |
| 441583 | MUS_DurotarB_GU03 | 95.2 | DU_GeneralB03 |
| 441584 | MUS_DurotarB_GU04 | 95.2 | DU_GeneralB04 |
| 441585 | MUS_DurotarC_GU01 | 85.4 | DU_GeneralC01 |
| 441586 | MUS_DurotarC_GU02 | 85.4 | DU_GeneralC02 |
| 441587 | MUS_DurotarC_GU03 | 61.3 | DU_GeneralC03 |
| 441588 | MUS_DurotarC_GU04 | 61.2 | DU_GeneralC04 |
| 441589 | MUS_DurotarD_GU01 | 84.8 | DU_GeneralD01 |
| 441590 | MUS_DurotarD_GU02 | 84.9 | DU_GeneralD02 |

### Gurubashi, Strangleronce (Cataclysm)

Arène des Gurubashi et vallée ; dans le plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 441768 | MUS_StranglethornVale_GU01 | 78.0 | STV_GurubashiVale01 |
| 441769 | MUS_StranglethornVale_GU02 | 92.9 | STV_GurubashiVale02 |
| 441770 | MUS_StranglethornVale_GU03 | 91.0 | STV_GurubashiVale03 |
| 441771 | MUS_StranglethornVale_GU04 | 102.1 | STV_GurubashiVale04 |
| 441772 | MUS_Stranglethorn_GU01 | 64.4 | STV_Gurubashi01 |
| 441773 | MUS_Stranglethorn_GU02 | 90.5 | STV_Gurubashi02 |
| 441774 | MUS_Stranglethorn_GU03 | 84.9 | STV_Gurubashi03 |
| 441775 | MUS_Stranglethorn_GU04 | 89.8 | STV_Gurubashi04 |

### Zul'Gurub (Cataclysm)

La Spirale (The Coil, Venoxis le serpent), Temple de Bethekk, Autel du dieu sanglant, Cache de la folie, Domaine de Mandokir, Terrasse du Diable. Blizzard réutilise thecoil/templebethek pour le Temple du Croc de Vol'dun (serpents). Absent du plugin, sauf ZulGurubVooDoo.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 520983 | MUS_41_ZA_altarbloodgod_UU01 | 68.7 |  |
| 520984 | MUS_41_ZA_altarbloodgod_UU02 | 68.7 |  |
| 520985 | MUS_41_ZA_altarbloodgod_UU03 | 68.7 |  |
| 520986 | MUS_41_ZA_bethekk_UU01 | 26.4 |  |
| 520987 | MUS_41_ZA_bethekk_UU02 | 26.4 |  |
| 520988 | MUS_41_ZA_cacheofmadness_UU01 | 34.1 |  |
| 520989 | MUS_41_ZA_cacheofmadness_UU02 | 34.1 |  |
| 520990 | MUS_41_ZA_devilsterrace_UU01 | 15.7 |  |
| 520991 | MUS_41_ZA_devilsterrace_UU02 | 15.7 |  |
| 520992 | MUS_41_ZA_mandokir_UU01 | 100.1 |  |
| 520993 | MUS_41_ZA_mandokir_UU02 | 100.1 |  |
| 520994 | MUS_41_ZA_templebethek_UU01 | 60.7 |  |
| 520995 | MUS_41_ZA_templebethek_UU02 | 60.7 |  |
| 520996 | MUS_41_ZA_terracedevils_UU01 | 16.4 |  |
| 520997 | MUS_41_ZA_terracedevils_UU02 | 16.4 |  |
| 520998 | MUS_41_ZA_thecoil_UU01 | 119.1 |  |
| 520999 | MUS_41_ZA_thecoil_UU02 | 119.1 |  |
| 53254 | ZulGurubVooDoo | 84.4 | ZG_VoodooMoment |

### Drakkari, Zul'Drak et Drak'Tharon (Wrath)

Marche jour/nuit, intros des autels de loa (Har'koa le léopard, Rhunok l'ours, Quetz'lun, Mam'toth, Sseratus le serpent) ; dans le plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 230003 | ZD_GeneralIntro_01 | 98.3 | ZD_GeneralIntro01 |
| 230004 | ZD_GeneralIntro_02 | 98.3 | ZD_GeneralIntro02 |
| 230005 | ZD_GeneralIntro_03 | 128.6 | ZD_GeneralIntro03 |
| 230006 | ZD_GeneralIntro_04 | 125.9 | ZD_GeneralIntro04 |
| 230007 | ZD_GeneralIntro_05 | 129.5 | ZD_GeneralIntro05 |
| 230008 | ZD_GeneralIntro_06 | 125.9 | ZD_GeneralIntro06 |
| 230009 | ZD_GeneralWalk_Day01 | 89.8 | ZD_GeneralWalkDay01 |
| 230010 | ZD_GeneralWalk_Day02 | 90.8 | ZD_GeneralWalkDay02 |
| 230011 | ZD_GeneralWalk_Day03 | 101.7 | ZD_GeneralWalkDay03 |
| 230012 | ZD_GeneralWalk_Day04 | 92.7 | ZD_GeneralWalkDay04 |
| 230013 | ZD_GeneralWalk_Night01 | 90.3 | ZD_GeneralWalkNight01 |
| 230014 | ZD_GeneralWalk_Night02 | 90.2 | ZD_GeneralWalkNight02 |
| 230015 | ZD_GeneralWalk_Night03 | 101.4 | ZD_GeneralWalkNight03 |
| 230016 | ZD_GeneralWalk_Night04 | 93.0 | ZD_GeneralWalkNight04 |
| 230017 | ZD_HarKoa_Intro01 | 28.2 | ZD_HarkoaIntro01 |
| 230018 | ZD_HarKoa_Intro02 | 27.9 | ZD_HarkoaIntro02 |
| 230019 | ZD_MamToth_Intro01 | 30.9 | ZD_MamtothIntro01 |
| 230020 | ZD_MamToth_Intro02 | 27.9 | ZD_MamtothIntro02 |
| 230021 | ZD_QuetzLun_Intro01 | 32.3 | ZD_QuetzlunIntro01 |
| 230022 | ZD_QuetzLun_Intro02 | 27.9 | ZD_QuetzlunIntro02 |
| 230023 | ZD_Rhunok_Intro01 | 30.0 | ZD_RhunokIntro01 |
| 230024 | ZD_Rhunok_Intro02 | 27.9 | ZD_RhunokIntro02 |
| 230025 | ZD_Sseratus_Intro01 | 28.3 | ZD_SseratusIntro01 |
| 230026 | ZD_Sseratus_Intro02 | 27.9 | ZD_SseratusIntro02 |
| 229925 | NR_Troll_General01 | 46.2 | NR_TrollGeneral01 |
| 229926 | NR_Troll_General02 | 55.7 | NR_TrollGeneral02 |
| 229927 | NR_Troll_General03 | 38.4 | NR_TrollGeneral03 |
| 229928 | NR_Troll_General04 | 44.2 | NR_TrollGeneral04 |

### Zandalari, Île du Tonnerre (MoP)

Dans le plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 840469 | MUS_52_ThunderIsle_A_01 | 86.9 | MOP_ThunderIsleA01 |
| 840470 | MUS_52_ThunderIsle_A_02 | 87.4 | MOP_ThunderIsleA02 |
| 840471 | MUS_52_ThunderIsle_A_03 | 66.4 | MOP_ThunderIsleA03 |
| 840472 | MUS_52_ThunderIsle_A_04 | 22.5 | MOP_ThunderIsleA04 |
| 840473 | MUS_52_ThunderIsle_A_05 | 124.5 | MOP_ThunderIsleA05 |
| 840474 | MUS_52_ThunderIsle_A_06 | 60.2 | MOP_ThunderIsleA06 |
| 840475 | MUS_52_ThunderIsle_A_07 | 71.3 | MOP_ThunderIsleA07 |
| 840481 | MUS_52_ThunderIsle_B_01 | 66.5 | MOP_ThunderIsleB01 |
| 840482 | MUS_52_ThunderIsle_B_02 | 73.1 | MOP_ThunderIsleB02 |
| 840483 | MUS_52_ThunderIsle_B_03 | 94.5 | MOP_ThunderIsleB03 |
| 840484 | MUS_52_ThunderIsle_B_04 | 106.5 | MOP_ThunderIsleB04 |
| 840485 | MUS_52_ThunderIsle_B_05 | 97.1 | MOP_ThunderIsleB05 |
| 840487 | MUS_52_ThunderIsle_C_01 | 95.4 | MOP_ThunderIsleC01 |
| 840488 | MUS_52_ThunderIsle_C_02 | 98.3 | MOP_ThunderIsleC02 |
| 840489 | MUS_52_ThunderIsle_C_03 | 119.6 | MOP_ThunderIsleC03 |
| 840490 | MUS_52_ThunderIsle_C_04 | 48.6 | MOP_ThunderIsleC04 |
| 840508 | MUS_52_TrollBattle_A_01 | 40.1 | MOP_TrollBattleA01 |
| 840509 | MUS_52_TrollBattle_A_02 | 84.6 | MOP_TrollBattleA02 |
| 840510 | MUS_52_TrollBattle_A_03 | 56.5 | MOP_TrollBattleA03 |
| 840511 | MUS_52_TrollBattle_B_01 | 41.1 | MOP_TrollBattleB01 |
| 840512 | MUS_52_TrollBattle_B_02 | 80.5 | MOP_TrollBattleB02 |
| 840513 | MUS_52_TrollBattle_B_03 | 54.8 | MOP_TrollBattleB03 |
| 840520 | MUS_52_ZandalariProphecy_01 | 170.6 | MOP_ZandalariProphecy01 |
| 840521 | MUS_52_Zandalari_1_A_01 | 72.4 | MOP_Zandalari1A01 |
| 840522 | MUS_52_Zandalari_1_A_02 | 80.1 | MOP_Zandalari1A02 |
| 840523 | MUS_52_Zandalari_1_A_03 | 75.0 | MOP_Zandalari1A03 |
| 840524 | MUS_52_Zandalari_1_B_01 | 72.4 | MOP_Zandalari1B01 |
| 840525 | MUS_52_Zandalari_1_B_02 | 80.1 | MOP_Zandalari1B02 |
| 840526 | MUS_52_Zandalari_1_B_03 | 74.0 | MOP_Zandalari1B03 |
| 840527 | MUS_52_Zandalari_1_C_01 | 64.3 | MOP_Zandalari1C01 |
| 840528 | MUS_52_Zandalari_1_C_02 | 78.9 | MOP_Zandalari1C02 |
| 840529 | MUS_52_Zandalari_2_A_01 | 77.6 | MOP_Zandalari2A01 |
| 840530 | MUS_52_Zandalari_2_A_02 | 50.2 | MOP_Zandalari2A02 |
| 840531 | MUS_52_Zandalari_2_A_03 | 38.4 | MOP_Zandalari2A03 |
| 840532 | MUS_52_Zandalari_2_A_04 | 49.2 | MOP_Zandalari2A04 |
| 840533 | MUS_52_Zandalari_2_A_05 | 64.2 | MOP_Zandalari2A05 |
| 840534 | MUS_52_Zandalari_2_B_01 | 118.1 | MOP_Zandalari2B01 |
| 840535 | MUS_52_Zandalari_2_B_02 | 46.5 | MOP_Zandalari2B02 |
| 840536 | MUS_52_Zandalari_2_B_03 | 64.2 | MOP_Zandalari2B03 |
| 840537 | MUS_52_Zandalari_2_C_01 | 77.1 | MOP_Zandalari2C01 |
| 840538 | MUS_52_Zandalari_2_C_02 | 50.5 | MOP_Zandalari2C02 |
| 840539 | MUS_52_Zandalari_2_C_03 | 33.3 | MOP_Zandalari2C03 |

### Zandalari, Zuldazar et Atal'Dazar (BfA)

Jungle, ville d'or, temples, lamentation, Zandalar Forever ; dans le plugin sauf cityofgold et bazaar.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 1780948 | mus_80_zandalarilament_a | 82.8 | BFA_ZandalariLamentA |
| 1780949 | mus_80_zandalarilament_b | 82.8 | BFA_ZandalariLamentB |
| 1780950 | mus_80_zandalarilament_h | 82.8 | BFA_ZandalariLamentH |
| 1780951 | mus_80_zuldazarintro_a | 72.5 | BFA_ZuldazarIntroA |
| 1780952 | mus_80_zuldazarintro_b | 72.5 | BFA_ZuldazarIntroB |
| 1780953 | mus_80_zuldazarintro_h | 72.5 | BFA_ZuldazarIntroH |
| 2143541 | mus_80_zuldazarbazaar_1_h | 148.4 |  |
| 2143542 | mus_80_zuldazarbazaar_2_h | 140.2 |  |
| 2143543 | mus_80_zuldazarjungle_a | 159.9 | BFA_ZuldazarJungleA |
| 2143544 | mus_80_zuldazarjungle_b | 159.9 | BFA_ZuldazarJungleB |
| 2143545 | mus_80_zuldazarjungle_c | 167.0 | BFA_ZuldazarJungleC |
| 2143546 | mus_80_zuldazarjungle_h | 162.3 | BFA_ZuldazarJungleH |
| 2146227 | mus_80_ataldazar_a | 93.5 | BFA_AtalDazarA |
| 2146228 | mus_80_ataldazar_b | 93.5 | BFA_AtalDazarB |
| 2146229 | mus_80_ataldazar_c | 93.5 | BFA_AtalDazarC |
| 2146230 | mus_80_ataldazar_d | 93.5 | BFA_AtalDazarD |
| 2146231 | mus_80_ataldazar_h | 93.5 | BFA_AtalDazarH |
| 2146234 | mus_80_cityofgold_a | 81.1 |  |
| 2146235 | mus_80_cityofgold_b | 81.1 |  |
| 2146236 | mus_80_cityofgold_h | 81.1 |  |
| 2146277 | mus_80_zuldazar_1_a | 72.1 | BFA_Zuldazar1A |
| 2146278 | mus_80_zuldazar_1_b | 72.1 | BFA_Zuldazar1B |
| 2146279 | mus_80_zuldazar_1_h | 72.1 | BFA_Zuldazar1H |
| 2146280 | mus_80_zuldazar_2_a | 85.8 | BFA_Zuldazar2A |
| 2146281 | mus_80_zuldazar_2_b | 85.8 | BFA_Zuldazar2B |
| 2146282 | mus_80_zuldazar_2_c | 85.8 | BFA_Zuldazar2C |
| 2146283 | mus_80_zuldazar_2_h | 85.8 | BFA_Zuldazar2H |
| 2148032 | mus_80_zuldazarjungle_d | 115.9 | BFA_ZuldazarJungleD |
| 2148033 | mus_80_zuldazarjungle_e | 111.9 | BFA_ZuldazarJungleE |
| 2148034 | mus_80_zuldazarjungle_f | 117.8 | BFA_ZuldazarJungleF |
| 2148035 | mus_80_zuldazarjungle_g | 118.0 | BFA_ZuldazarJungleG |
| 2148036 | mus_80_zuldazarjungle_i | 122.7 | BFA_ZuldazarJungleI |
| 2148037 | mus_80_zuldazarjungle_j | 121.1 | BFA_ZuldazarJungleJ |
| 2148038 | mus_80_zuldazarjungle_k | 122.5 | BFA_ZuldazarJungleK |
| 2148039 | mus_80_zuldazarjungle_l | 101.2 | BFA_ZuldazarJungleL |
| 2148040 | mus_80_zuldazarjungle_m | 92.0 | BFA_ZuldazarJungleM |
| 2148041 | mus_80_zuldazarjungle_n | 92.0 | BFA_ZuldazarJungleN |
| 2148042 | mus_80_zuldazarjungle_o | 92.7 | BFA_ZuldazarJungleO |
| 2148043 | mus_80_zuldazarjungle_p | 89.7 | BFA_ZuldazarJungleP |
| 2148044 | mus_80_zuldazarjungle_q | 92.2 | BFA_ZuldazarJungleQ |
| 2148045 | mus_80_zuldazarjungle_r | 92.1 | BFA_ZuldazarJungleR |
| 2148046 | mus_80_zuldazarjungle_s | 91.9 | BFA_ZuldazarJungleS |
| 2179262 | mus_80_zuldazar_drum | 71.9 | BFA_ZuldazarDrum |
| 2844629 | mus_815_zandalaritroll_1_a | 121.1 | BFA_ZandalariTroll1A |
| 2844630 | mus_815_zandalaritroll_1_b | 122.1 | BFA_ZandalariTroll1B |
| 2844631 | mus_815_zandalaritroll_1_c | 93.6 | BFA_ZandalariTroll1C |
| 2844632 | mus_815_zandalaritroll_2_a | 116.9 | BFA_ZandalariTroll2A |
| 2844633 | mus_815_zandalaritroll_2_b | 121.7 | BFA_ZandalariTroll2B |
| 2844634 | mus_815_zandalaritroll_2_c | 101.5 | BFA_ZandalariTroll2C |
| 2844635 | mus_815_zandalaritroll_3_a | 139.3 | BFA_ZandalariTroll3A |
| 2844636 | mus_815_zandalaritroll_3_b | 108.2 | BFA_ZandalariTroll3B |
| 2844637 | mus_815_zandalaritroll_3_c | 110.3 | BFA_ZandalariTroll3C |
| 2844638 | mus_815_zandalaritroll_4_a | 127.4 | BFA_ZandalariTroll4A |
| 2844639 | mus_815_zandalaritroll_4_b | 127.7 | BFA_ZandalariTroll4B |
| 2844640 | mus_815_zandalaritroll_4_c | 102.3 | BFA_ZandalariTroll4C |
| 2564881 | mus_81_zandalarforever_a | 121.6 | BFA_ZandalarForeverA |
| 2564882 | mus_81_zandalarforever_b | 112.9 | BFA_ZandalarForeverB |
| 2564883 | mus_81_zandalarforever_c | 115.9 | BFA_ZandalarForeverC |
| 2564884 | mus_81_zandalarforever_h | 145.5 | BFA_ZandalarForeverH |
| 2575919 | mus_81_zandalarforever_d | 101.0 | BFA_ZandalarForeverD |
| 2575920 | mus_81_zandalarforever_e | 105.7 | BFA_ZandalarForeverE |
| 2575921 | mus_81_zandalarforever_f | 102.9 | BFA_ZandalarForeverF |
| 2575922 | mus_81_zandalarforever_g | 94.9 | BFA_ZandalarForeverG |
| 2575923 | mus_81_zandalarforever_i | 130.8 | BFA_ZandalarForeverI |
| 2575924 | mus_81_zandalarforever_j | 125.8 | BFA_ZandalarForeverJ |

### Loa de Zandalar (BfA)

Thèmes d'Akunda, Bwonsamdi, Paku, Shadra et thème principal des loa. Absent du plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 2146244 | mus_80_loa_akunda_a | 36.7 |  |
| 2146245 | mus_80_loa_akunda_b | 36.7 |  |
| 2146246 | mus_80_loa_akunda_c | 36.7 |  |
| 2146247 | mus_80_loa_akunda_h | 36.7 |  |
| 2146250 | mus_80_loa_bwonsamdi_c | 36.5 |  |
| 2146251 | mus_80_loa_bwonsamdi_d | 36.6 |  |
| 2146252 | mus_80_loa_bwonsamdi_h | 38.0 |  |
| 2146253 | mus_80_loa_maintheme_a | 46.1 |  |
| 2146256 | mus_80_loa_maintheme_d | 46.1 |  |
| 2146257 | mus_80_loa_maintheme_h | 46.1 |  |
| 2146258 | mus_80_loa_paku_a | 41.7 |  |
| 2146261 | mus_80_loa_paku_d | 41.8 |  |
| 2146267 | mus_80_loa_shadra_d | 55.6 |  |
| 2146268 | mus_80_loa_shadra_h | 55.6 |  |
| 2146263 | Intro_80_Zuldazar_Paku_2146263 | à mesurer |  |

### Nazmir (BfA)

Marais des trolls de sang, magie du sang, Nazwatha (Vide). Absent du plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 1780904 | mus_80_bloodmagic_b | 89.2 |  |
| 1780905 | mus_80_bloodmagic_c | 89.2 |  |
| 1780906 | mus_80_bloodmagic_d | 86.5 |  |
| 1780907 | mus_80_bloodmagic_e | 86.5 |  |
| 1780908 | mus_80_bloodmagic_h | 89.2 |  |
| 1780909 | mus_80_bloodsacrifice_a | 99.3 |  |
| 1780910 | mus_80_bloodsacrifice_b | 99.3 |  |
| 1780911 | mus_80_bloodsacrifice_h | 99.3 |  |
| 1780944 | mus_80_nazmirvoid_a | 84.0 |  |
| 1780945 | mus_80_nazmirvoid_b | 101.0 |  |
| 1780946 | mus_80_nazmirvoid_c | 84.0 |  |
| 1780947 | mus_80_nazmirvoid_h | 84.9 |  |
| 2143526 | mus_80_nazmirswamp_a | 156.8 |  |
| 2143527 | mus_80_nazmirswamp_b | 103.8 |  |
| 2143528 | mus_80_nazmirswamp_c | 102.4 |  |
| 2143529 | mus_80_nazmirswamp_d | 93.8 |  |
| 2143530 | mus_80_nazmirswamp_e | 97.8 |  |
| 2143531 | mus_80_nazmirswamp_f | 126.9 |  |
| 2143532 | mus_80_nazmirswamp_h | 155.0 |  |
| 2146232 | mus_80_bloodsacrifice_c | 99.3 |  |
| 2146233 | mus_80_bloodsacrifice_d | 99.3 |  |
| 2150454 | mus_80_bloodmagic_a | 89.2 |  |

### Vol'dun et Sethraliss (BfA)

Désert des Sethrak, Sanctuaire des Dévoués, Cœur de Sethraliss (loa serpent). Absent du plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 2146275 | mus_80_voldun_a | 151.1 |  |
| 2146276 | mus_80_voldun_h | 151.1 |  |
| 2146597 | mus_80_heartofsethraliss_1_a | 56.4 |  |
| 2146598 | mus_80_heartofsethraliss_1_h | 56.4 |  |
| 2146599 | mus_80_heartofsethraliss_2_a | 64.7 |  |
| 2146600 | mus_80_heartofsethraliss_2_h | 64.7 |  |
| 2146636 | mus_80_sethrak_1_a | 70.7 |  |
| 2146638 | mus_80_sethrak_2_a | 74.3 |  |
| 2146639 | mus_80_sethrak_2_h | 76.7 |  |
| 2150465 | mus_80_voldun_b | 150.3 |  |
| 2150466 | mus_80_voldun_c | 72.7 |  |
| 2150467 | mus_80_voldun_d | 92.9 |  |
| 2150468 | mus_80_voldun_e | 149.8 |  |
| 2151743 | mus_80_sethrak_1_h | 73.9 |  |

### Naga (BfA)

Incursions naga d'Atal'Gral et de la Grève de Krag'wa ; l'île a des naga.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 2146631 | mus_80_nagaincursion_a | 154.2 |  |
| 2146632 | mus_80_nagaincursion_b | 154.2 |  |
| 2146633 | mus_80_nagaincursion_c | 69.1 |  |
| 2146634 | mus_80_nagaincursion_h | 154.2 |  |

### Zangarmarsh (TBC)

Mangrove : marche générale et Coilfang.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 53816 | ZA_CoilfangWalkUni01 | 133.1 |  |
| 53817 | ZA_CoilfangWalkUni02 | 99.4 |  |
| 53818 | ZA_CoilfangWalkUni03 | 109.8 |  |
| 53819 | ZA_GeneralWalkUni01 | 81.6 |  |
| 53820 | ZA_GeneralWalkUni02 | 120.1 |  |
| 53821 | ZA_GeneralWalkUni03 | 59.9 |  |
| 53822 | ZA_GeneralWalkUni04 | 103.0 |  |
| 53823 | ZA_GeneralWalkUni05 | 71.7 |  |
| 53824 | ZA_GeneralWalkUni06 | 89.7 |  |

### Terres Fantômes, set sombre (TBC)

Catacombes amani, An'daroth, ziggourats ; dans le plugin Quel'Thalas.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 53499 | GL_EversongDarkWalkUni01 | 62.4 |  |
| 53500 | GL_EversongDarkWalkUni02 | 62.2 |  |
| 53501 | GL_EversongDarkWalkUni03 | 63.9 |  |
| 53502 | GL_EversongDarkWalkUni04 | 60.8 |  |

### Zul'Aman (Midnight 12.0)

Familles natives, dans le plugin.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 7681066 | MUS_120_Halazzi_Loa_A | 83.6 | MN_HalazziLoaA |
| 7681068 | MUS_120_Halazzi_Loa_B | 81.3 | MN_HalazziLoaB |
| 7681070 | MUS_120_Halazzi_Loa_C | 89.2 | MN_HalazziLoaC |
| 7681072 | MUS_120_Halazzi_Loa_D | 75.9 | MN_HalazziLoaD |
| 7681074 | MUS_120_Halazzi_Loa_H | 132.9 | MN_HalazziLoaH |
| 7682264 | MUS_120_Amanizar_Village_A | 158.2 | MN_AmanizarVillageA |
| 7682266 | MUS_120_Amanizar_Village_B | 146.8 | MN_AmanizarVillageB |
| 7682268 | MUS_120_Amanizar_Village_C | 129.1 | MN_AmanizarVillageC |
| 7682270 | MUS_120_Amanizar_Village_D | 212.1 | MN_AmanizarVillageD |
| 7682280 | MUS_120_AtalAbasi_A | 107.3 | MN_AtalAbasiA |
| 7682282 | MUS_120_AtalAbasi_B | 110.3 | MN_AtalAbasiB |
| 7682284 | MUS_120_AtalAbasi_C | 147.0 | MN_AtalAbasiC |
| 7682286 | MUS_120_AtalAbasi_D | 135.9 | MN_AtalAbasiD |
| 7682288 | MUS_120_AtalAbasi_E | 127.9 | MN_AtalAbasiE |
| 7682290 | MUS_120_AtalAbasi_F | 74.6 | MN_AtalAbasiF |
| 7682292 | MUS_120_AtalAbasi_H | 158.3 | MN_AtalAbasiH |
| 7682366 | MUS_120_Nalorakk_Loa_A | 135.2 | MN_NalorakkLoaA |
| 7682368 | MUS_120_Nalorakk_Loa_B | 139.4 | MN_NalorakkLoaB |
| 7682370 | MUS_120_Nalorakk_Loa_C | 140.4 | MN_NalorakkLoaC |
| 7682372 | MUS_120_Nalorakk_Loa_D | 134.3 | MN_NalorakkLoaD |
| 7682374 | MUS_120_Nalorakk_Loa_E | 130.5 | MN_NalorakkLoaE |
| 7682376 | MUS_120_Nalorakk_Loa_F | 132.0 | MN_NalorakkLoaF |
| 7682378 | MUS_120_Nalorakk_Loa_H | 178.0 | MN_NalorakkLoaH |
| 7682400 | MUS_120_ZebAlar_A | 143.3 | MN_ZebAlarA |
| 7682402 | MUS_120_ZebAlar_B | 163.1 | MN_ZebAlarB |
| 7682404 | MUS_120_ZebAlar_H | 202.7 | MN_ZebAlarH |
| 7682406 | MUS_120_ZebAlar_C | 184.1 | MN_ZebAlarC |
| 7682408 | MUS_120_ZebAlar_D | 121.6 | MN_ZebAlarD |
| 7682410 | MUS_120_ZebAlar_E | 135.2 | MN_ZebAlarE |
| 7682412 | MUS_120_ZebAlar_F | 202.7 | MN_ZebAlarF |
| 7682414 | MUS_120_ZulAman_A | 220.6 | MN_ZulAmanA |
| 7682416 | MUS_120_ZulAman_B | 221.9 | MN_ZulAmanB |
| 7682418 | MUS_120_ZulAman_C | 221.0 | MN_ZulAmanC |
| 7682420 | MUS_120_ZulAman_D | 76.8 | MN_ZulAmanD |
| 7682422 | MUS_120_ZulAman_E | 76.2 | MN_ZulAmanE |
| 7682424 | MUS_120_ZulAman_F | 75.7 | MN_ZulAmanF |
| 7682426 | MUS_120_ZulAman_G | 106.9 | MN_ZulAmanG |
| 7682428 | MUS_120_ZulAman_H | 222.2 | MN_ZulAmanH |
| 7684176 | MUS_120_AtalAman_A | 177.6 | MN_AtalAmanA |
| 7684178 | MUS_120_AtalAman_B | 162.8 | MN_AtalAmanB |
| 7684180 | MUS_120_AtalAman_C | 132.4 | MN_AtalAmanC |
| 7684182 | MUS_120_AtalAman_D | 189.8 | MN_AtalAmanD |
| 7684184 | MUS_120_AtalAman_E | 129.7 | MN_AtalAmanE |
| 7684186 | MUS_120_AtalAman_H | 177.8 | MN_AtalAmanH |
| 7688241 | MUS_120_Akilzon_Loa_A | 95.7 | MN_AkilzonLoaA |
| 7688243 | MUS_120_Akilzon_Loa_B | 98.5 | MN_AkilzonLoaB |
| 7688245 | MUS_120_Akilzon_Loa_C | 127.9 | MN_AkilzonLoaC |
| 7688247 | MUS_120_Akilzon_Loa_D | 128.6 | MN_AkilzonLoaD |
| 7688249 | MUS_120_Akilzon_Loa_H | 149.6 | MN_AkilzonLoaH |
| 7688251 | MUS_120_Amanizar_Village_H | 212.4 | MN_AmanizarVillageH |
| 7688253 | MUS_120_Amanizar_Village_E | 212.4 | MN_AmanizarVillageE |
| 7689597 | MUS_120_Janalai_Loa_A | 126.6 | MN_JanalaiLoaA |
| 7689599 | MUS_120_Janalai_Loa_B | 121.0 | MN_JanalaiLoaB |
| 7689601 | MUS_120_Janalai_Loa_C | 149.3 | MN_JanalaiLoaC |
| 7689603 | MUS_120_Janalai_Loa_D | 103.5 | MN_JanalaiLoaD |
| 7689605 | MUS_120_Janalai_Loa_E | 87.9 | MN_JanalaiLoaE |
| 7689607 | MUS_120_Janalai_Loa_F | 100.9 | MN_JanalaiLoaF |
| 7689609 | MUS_120_Janalai_Loa_H | 230.0 | MN_JanalaiLoaH |
| 7698288 | MUS_120_Halazzi_Loa_E | 58.4 | MN_HalazziLoaE |
| 7698290 | MUS_120_Halazzi_Loa_F | 55.9 | MN_HalazziLoaF |
| 7698292 | MUS_120_Halazzi_Loa_G | 68.8 | MN_HalazziLoaG |
| 7713422 | MUS_120_Nalorakk_Loa_G | 121.7 | MN_NalorakkLoaG |
| 7713424 | MUS_120_Nalorakk_Loa_I | 100.0 | MN_NalorakkLoaI |

### Lame du Crépuscule (Midnight 12.0)

Dans le plugin Quel'Thalas.

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 7681218 | MUS_120_Twilights_Blade_A | 92.3 |  |
| 7681220 | MUS_120_Twilights_Blade_B | 103.4 |  |
| 7681222 | MUS_120_Twilights_Blade_C | 95.1 |  |
| 7681224 | MUS_120_Twilights_Blade_D | 61.6 |  |
| 7681226 | MUS_120_Twilights_Blade_E | 75.6 |  |
| 7681228 | MUS_120_Twilights_Blade_H | 159.4 |  |
| 7713458 | MUS_120_Twilights_Blade_F | 77.8 |  |
| 7713460 | MUS_120_Twilights_Blade_G | 75.3 |  |
| 7713462 | MUS_120_Twilights_Blade_I | 76.9 |  |

### Île Annelée (Midnight 12.1)

Familles natives 12.1 : forêt, Queue du serpent, Marais murmurant, Mangrove, Abîme venimeux, hub Tokka (joué au gouffre Gnarldor, le hub lui-même est silencieux), Enfants d'Ula'tek et Soulcoiler (combat), UlaTek 1–3 (raid), Zul'jan (Autel des Crocs), Naga Lair (Grotte).

| FDID | Fichier | Durée (s) | Dans le plugin |
|---|---|---|---|
| 8218530 | MUS_121_Children_Of_Ulatek_A | 72.0 |  |
| 8218532 | MUS_121_Children_Of_Ulatek_B | 107.6 |  |
| 8218534 | MUS_121_Children_Of_Ulatek_C | 102.2 |  |
| 8218536 | MUS_121_Children_Of_Ulatek_D | 154.4 |  |
| 8218538 | MUS_121_Children_Of_Ulatek_E | 148.0 |  |
| 8218540 | MUS_121_Children_Of_Ulatek_F | 104.0 |  |
| 8218542 | MUS_121_Children_Of_Ulatek_G | 114.4 |  |
| 8218544 | MUS_121_Children_Of_Ulatek_H | 190.5 |  |
| 8218546 | MUS_121_Children_Of_Ulatek_Stinger | 19.7 |  |
| 8218548 | MUS_121_Mlurkkr_Mire_A | 106.4 |  |
| 8218551 | MUS_121_Mlurkkr_Mire_B | 109.5 |  |
| 8218554 | MUS_121_Mlurkkr_Mire_C | 102.0 |  |
| 8218556 | MUS_121_Mlurkkr_Mire_D | 123.0 |  |
| 8218558 | MUS_121_Mlurkkr_Mire_H | 111.2 |  |
| 8218560 | MUS_121_Naga_Lair_A | 111.4 |  |
| 8218562 | MUS_121_Naga_Lair_H | 176.4 |  |
| 8218578 | MUS_121_Serpents_Tail_A | 124.2 |  |
| 8218580 | MUS_121_Serpents_Tail_H | 190.2 |  |
| 8218582 | MUS_121_Soulcoiler_Combat_A | 127.6 |  |
| 8218584 | MUS_121_Soulcoiler_Combat_B | 164.1 |  |
| 8218586 | MUS_121_Soulcoiler_Combat_C | 156.8 |  |
| 8218588 | MUS_121_Soulcoiler_Combat_D | 142.0 |  |
| 8218590 | MUS_121_Soulcoiler_Combat_E | 157.5 |  |
| 8218592 | MUS_121_Soulcoiler_Combat_G | 178.9 |  |
| 8218594 | MUS_121_Soulcoiler_Combat_H1 | 133.7 |  |
| 8218596 | MUS_121_Soulcoiler_Combat_H2 | 93.8 |  |
| 8218598 | MUS_121_Tokkas_Landing_A | 179.5 |  |
| 8218600 | MUS_121_Tokkas_Landing_H | 184.3 |  |
| 8218602 | MUS_121_UlaTek_1_A | 140.1 |  |
| 8218604 | MUS_121_UlaTek_1_B | 161.1 |  |
| 8218606 | MUS_121_UlaTek_1_C | 118.7 |  |
| 8218608 | MUS_121_UlaTek_1_H | 89.3 |  |
| 8218610 | MUS_121_UlaTek_2_A | 123.8 |  |
| 8218612 | MUS_121_UlaTek_2_B | 117.4 |  |
| 8218614 | MUS_121_UlaTek_2_C | 138.7 |  |
| 8218616 | MUS_121_UlaTek_2_H | 67.9 |  |
| 8218618 | MUS_121_UlaTek_3_A | 130.7 |  |
| 8218620 | MUS_121_UlaTek_3_B | 146.5 |  |
| 8218622 | MUS_121_UlaTek_3_H | 106.9 |  |
| 8218624 | MUS_121_Venomous_Abyss_A | 203.0 |  |
| 8218626 | MUS_121_Venomous_Abyss_B | 198.4 |  |
| 8218628 | MUS_121_Venomous_Abyss_C | 196.7 |  |
| 8218630 | MUS_121_Venomous_Abyss_D | 160.8 |  |
| 8218632 | MUS_121_Venomous_Abyss_E | 167.5 |  |
| 8218634 | MUS_121_Venomous_Abyss_H | 205.1 |  |
| 8218636 | MUS_121_Whispering_March_A | 137.6 |  |
| 8218638 | MUS_121_Whispering_March_B | 145.5 |  |
| 8218640 | MUS_121_Whispering_March_C | 121.6 |  |
| 8218642 | MUS_121_Whispering_March_D | 131.7 |  |
| 8218644 | MUS_121_Whispering_March_E | 94.0 |  |
| 8218646 | MUS_121_Whispering_March_F | 132.2 |  |
| 8218648 | MUS_121_Whispering_March_G | 121.7 |  |
| 8218650 | MUS_121_Whispering_March_H | 241.1 |  |
| 8218652 | MUS_121_Whispering_March_I | 131.3 |  |
| 8218654 | MUS_121_Zuljan_A | 104.9 |  |
| 8218656 | MUS_121_Zuljan_B | 185.7 |  |
| 8218658 | MUS_121_Zuljan_C | 97.0 |  |
| 8218660 | MUS_121_Zuljan_H | 191.1 |  |
| 8221021 | MUS_121_Naga_Lair_B | 107.3 |  |
| 8221023 | MUS_121_Serpents_Tail_B | 122.2 |  |
| 8221025 | MUS_121_Serpents_Tail_C | 114.4 |  |
| 8221027 | MUS_121_Serpents_Tail_D | 123.2 |  |
| 8221029 | MUS_121_Soulcoiler_Combat_I | 126.0 |  |
| 8221031 | MUS_121_Tokkas_Landing_B | 118.0 |  |
| 8221033 | MUS_121_Venomous_Abyss_F | 208.4 |  |
| 8242911 | MUS_121_Coiled_Isle_A | 127.7 |  |
| 8242913 | MUS_121_Coiled_Isle_B | 143.5 |  |
| 8242915 | MUS_121_Coiled_Isle_C | 142.7 |  |
| 8242917 | MUS_121_Coiled_Isle_H | 205.8 |  |
| 8242919 | MUS_121_Tokkas_Landing_C | 141.9 |  |
| 8242921 | MUS_121_Tokkas_Landing_D | 153.7 |  |
| 8242923 | MUS_121_UlaTek_3_C | 128.9 |  |
| 8242925 | MUS_121_UlaTek_3_D | 34.1 |  |
| 8242927 | MUS_121_UlaTek_3_E | 44.6 |  |
| 8244825 | MUS_121_Naga_Lair_C | 105.0 |  |
| 8244827 | MUS_121_Naga_Lair_D | 138.4 |  |
| 8244829 | MUS_121_Serpents_Tail_E | 135.4 |  |
| 8244831 | MUS_121_Venomous_Abyss_G | 143.5 |  |
| 8244833 | MUS_121_Venomous_Abyss_I | 149.7 |  |
| 8245059 | MUS_121_Coiled_Isle_D | 133.8 |  |
| 8245061 | MUS_121_Coiled_Isle_E | 134.8 |  |
| 8245063 | MUS_121_Venomous_Abyss_J | 135.4 |  |
| 8245306 | MUS_121_Serpents_Tail_F | 133.9 |  |
| 8246372 | MUS_121_Whispering_March_J | 140.7 |  |

## 4. Rapprochements et packs proposés

| Lieu Midnight | Musique proposée | Pourquoi |
|---|---|---|
| Forêt de Zul'Aman, lieux sans kit | Amani (TBC) | le set du raid, déjà le défaut |
| Amani'Zar Village, Witherbark Bluffs, Torntusk Overlook | kit natif des Îles de l'Écho (AMB11–15 + set Zul'Farrak) | c'est le « village troll » de Blizzard |
| Temple de Halazzi (lynx) | autel de Har'koa (léopard des neiges, Zul'Drak) | même archétype félin |
| Spiritpaw, Nalorakk (ours) | autel de Rhunok (ours, Zul'Drak) | même loa-ours |
| Temple de Jan'alai (faucon-dragon) | autel de Quetz'lun (serpent-vent) | loa volant |
| Temple d'Akil'zon (aigle) | Paku (ptérrordax, BfA) | loa ailé |
| Speaker's Rest, Broken Throne, Revantusk Sedge | trolls de sang de Nazmir | occupation par un culte sombre ; alternative TBC : catacombes des Terres Fantômes |
| Atal'Aman, terrasses, autel de Malacrass | Atal'Dazar + Cité d'or | cité-temple ↔ cité-temple |
| Atal'Abasi, Leech Bog, Maisara Deeps, Skybridge, Hermit's Mooring | marais de Nazmir | marais troll ; alternative TBC : Zangarmarsh |
| Zeb'Alar Lumberyard, Bitterbark | Gurubashi | jungle exploitée |
| Forêt de l'Île Annelée | jungle de Zuldazar | île-jungle troll ; alternative TBC : Amani |
| Tokka's Landing, Tokka's Folly | côte sombrelance (Durotar) | port troll en bord de mer ; natif = silence |
| Mlurkkr Mire, Ofi's Hut, Cloudlight Beacon, épaves | Zangarmarsh (TBC) | mangrove |
| Queue du serpent, Crocs, portes, Venom Rise, Blistering Terrace, Zail'Zar Span, Path of Whispers | The Coil (Zul'Gurub Cata) | Venoxis le serpent ; Blizzard réutilise ce kit pour le Temple du Croc de Vol'dun ; alternative : Sethrak |
| Altar of Wrath, Whispering Marsh, Ring of Glory, Defiant Ring | Drakkari (Zul'Drak) | zone troll hantée par les esprits ; alternative : loa de Zandalar |
| Cryptes et tombes de l'île | catacombes amani (Terres Fantômes, TBC) | tombes amani |
| Chambres fortes d'Atal'Utek (hors hubs) | Autel du dieu sanglant (Zul'Gurub Cata) + combat TBC | temple-serpent souterrain |
| Hubs des Chambres fortes | Amani (TBC) | camps amani |

### 4.1 Packs

| Clé | Label | Contenu | Zones par défaut |
|---|---|---|---|
| `AMANI` | Amani (TBC) | ZA_zulaman_AMB10–15 (existe : ZULAMAN) | racine de Zul'Aman, lieux sans musique, hubs des Chambres fortes |
| `TROLL_VILLAGE` | Troll Village (Vanilla + TBC) | kit natif des Îles de l'Écho : ZA_zulaman_AMB11–15 + ZFQuiet1/2/7, ZFQuietShort8, ZFRally9 | Amani'Zar Village, Witherbark Bluffs, Torntusk Overlook |
| `SANDFURY` | Zul'Farrak (Vanilla) | ZFQuiet1/2/7, ZFQuietShort8, intro ZFRally9 ; remplace le substitut Tanaris du pack actuel (ou s'y ajoute) | pack utilitaire |
| `SHRINE_HALAZZI` | Shrine of Har'koa (Wrath) | intro ZD_HarKoa_Intro01, any ZD_GeneralWalk jour/nuit + NR_Troll_General | Temple de Halazzi (lynx ↔ Har'koa le léopard des neiges) |
| `SHRINE_NALORAKK` | Shrine of Rhunok (Wrath) | intro ZD_Rhunok_Intro01, même rotation | Spiritpaw, Nalorakk's Prowl (ours ↔ Rhunok) |
| `SHRINE_JANALAI` | Shrine of Quetz'lun (Wrath) | intro ZD_QuetzLun_Intro01, même rotation | Temple de Jan'alai (faucon-dragon ↔ Quetz'lun le serpent-vent) |
| `SHRINE_AKILZON` | Shrine of Paku (BfA) | intro mus_80_loa_paku_a, any mus_80_loa_paku_d + ZD rotation | Temple d'Akil'zon, Akil'zon's Reach (aigle ↔ Paku le ptérrordax) |
| `BLOOD_CULT` | Blood Trolls (BfA) | mus_80_bloodmagic_a–e/h + mus_80_bloodsacrifice_a–d/h + mus_80_nazmirvoid_a–c/h | Speaker's Rest, Broken Throne, Revantusk Sedge (Lame du Crépuscule) ; alternative TBC : set sombre des Terres Fantômes |
| `CITY_OF_GOLD` | Atal'Dazar (BfA) | mus_80_ataldazar_a–d/h (existe) + mus_80_cityofgold_a/b/h | Atal'Aman et ses terrasses (Atal ↔ Atal) |
| `NAZMIR_SWAMP` | Nazmir (BfA) | mus_80_nazmirswamp_a–f/h | Atal'Abasi, Leech Bog, Maisara Deeps, Skybridge, Hermit's Mooring ; alternative TBC : Zangarmarsh |
| `GURUBASHI` | Gurubashi (Cataclysm) | existe | Zeb'Alar Lumberyard, Bitterbark |
| `ZULDAZAR_JUNGLE` | Zuldazar Jungle (BfA) | mus_80_zuldazarjungle_a–s (existe dans Zandalari BFA, à isoler) | racine de l'Île Annelée et lieux sans musique ; alternative TBC : Amani |
| `DARKSPEAR_COAST` | Darkspear Strand (Cataclysm) | MUS_DurotarA_GU01, B_GU03/04, C_GU01/02 (kit natif de la côte sombrelance) | Tokka's Landing, Tokka's Folly (natif = silence : autre option NONE) |
| `ZANGARMARSH` | Zangarmarsh (TBC) | ZA_GeneralWalkUni01–06 + ZA_CoilfangWalkUni01–03 | Mlurkkr Mire, Ofi's Hut, Cloudlight Beacon, épaves |
| `SERPENT_COIL` | The Coil (Cataclysm) | intro MUS_41_ZA_thecoil_UU01, any thecoil_UU02 + templebethek_UU01/02 + bethekk_UU01/02 + ZulGurubVooDoo (kit que Blizzard réutilise au Temple du Croc) | Zail'Zar Span, Gates, The Fangs, Path of Whispers, Venom Rise, Blistering Terrace, The Serpent's Tail ; alternative : Sethrak (BfA) |
| `SETHRAK` | Sethraliss (BfA) | mus_80_sethrak_1_a/h, 2_a/h + heartofsethraliss_1/2_a/h + voldun_c/e | alternative pour les lieux du venin |
| `DRAKKARI` | Drakkari (Wrath) | existe | Altar of Wrath, Whispering Marsh, Ring of Glory, Defiant Ring (esprits) ; alternative : Loa de Zandalar |
| `LOA_SPIRITS` | Loa of Zandalar (BfA) | mus_80_loa_maintheme_a/d/h + bwonsamdi_c/d/h + shadra_d/h + akunda_a/b/c/h | alternative pour les lieux des esprits |
| `AMANI_CATACOMBS` | Amani Catacombs (TBC) | GL_EversongDarkWalkUni01–04 | les sept cryptes et tombes de l'île |
| `BLOOD_GOD` | Altar of the Blood God (Cataclysm) | intro MUS_41_ZA_altarbloodgod_UU01, any altarbloodgod_UU02/03 + mandokir_UU01/02 + cacheofmadness_UU01/02 + ZA_zulaman_BTL11–15 | Chambres fortes d'Atal'Utek (extérieur et intérieur, hors hubs) ; alternative : Temple englouti = Amani |

Packs mixés : chaque pack ci-dessus + la famille Midnight native des mêmes lieux (Amani + ZulAman, Troll Village + Amanizar Village, chaque Shrine + son loa, Blood Cult + Twilights Blade, City of Gold + AtalAman, Nazmir Swamp + AtalAbasi, Gurubashi + ZebAlar, Zuldazar Jungle + Coiled Isle, Darkspear Coast + Tokkas Landing, Zangarmarsh + Mlurkkr Mire, Serpent Coil + Serpents Tail, Drakkari + Whispering March, Amani Catacombs + Coiled Isle, Blood God + Venomous Abyss).

### 4.2 Esquisse de `Zones.lua`

```lua
[2437] = Dsl.zone("ZULAMAN", "AMANI", {
    AMANI_ZAR_VILLAGE        = "TROLL_VILLAGE",
    WITHERBARK_BLUFFS        = "TROLL_VILLAGE",
    TORNTUSK_OVERLOOK        = "TROLL_VILLAGE",
    TEMPLE_OF_AKIL_ZON       = "SHRINE_AKILZON",
    AKIL_ZON_S_REACH         = "SHRINE_AKILZON",
    TEMPLE_OF_JAN_ALAI       = "SHRINE_JANALAI",
    TEMPLE_OF_HALAZZI        = "SHRINE_HALAZZI",
    SPIRITPAW_BOROUGH        = "SHRINE_NALORAKK",
    NALORAKK_S_PROWL         = "SHRINE_NALORAKK",
    SPIRITPAW_BACKWOODS      = "SHRINE_NALORAKK",
    SPEAKER_S_REST           = "BLOOD_CULT",
    BROKEN_THRONE            = "BLOOD_CULT",
    REVANTUSK_SEDGE          = "BLOOD_CULT",
    ATAL_AMAN                = "CITY_OF_GOLD",
    TALONSTRIKE_TERRACE      = "CITY_OF_GOLD",
    SWIFTCLAW_TERRACE        = "CITY_OF_GOLD",
    RAGEMAW_TERRACE          = "CITY_OF_GOLD",
    FIREWING_TERRACE         = "CITY_OF_GOLD",
    WARLORD_S_STAIR          = "CITY_OF_GOLD",
    ALTAR_OF_MALACRASS       = "CITY_OF_GOLD",
    ATAL_ABASI               = "NAZMIR_SWAMP",
    LEECH_BOG                = "NAZMIR_SWAMP",
    MAISARA_DEEPS            = "NAZMIR_SWAMP",
    THE_SKYBRIDGE            = "NAZMIR_SWAMP",
    HERMIT_S_MOORING         = "NAZMIR_SWAMP",
    ZEB_ALAR_LUMBERYARD      = "GURUBASHI",
    BITTERBARK               = "GURUBASHI",
}),
[2512] = Dsl.zone("THE_COILED_ISLE", "ZULDAZAR_JUNGLE", {
    TOKKA_S_LANDING          = "DARKSPEAR_COAST",
    TOKKA_S_FOLLY            = "DARKSPEAR_COAST",
    OFI_S_HUT                = "ZANGARMARSH",
    MLURKKR_MIRE             = "ZANGARMARSH",
    CLOUDLIGHT_BEACON        = "ZANGARMARSH",
    WRECK_OF_PAKU_S_TALON    = "ZANGARMARSH",
    WRECK_OF_TORGA_S_BEAK    = "ZANGARMARSH",
    ZAIL_ZAR_SPAN            = "SERPENT_COIL",
    GATE_OF_THE_EASTERN_FANG = "SERPENT_COIL",
    THE_FANGS                = "SERPENT_COIL",
    PATH_OF_WHISPERS         = "SERPENT_COIL",
    GATE_OF_THE_SERPENT_S_EYE = "SERPENT_COIL",
    VENOM_RISE               = "SERPENT_COIL",
    BLISTERING_TERRACE       = "SERPENT_COIL",
    THE_SERPENT_S_TAIL       = "SERPENT_COIL",
    THE_ALTAR_OF_WRATH       = "DRAKKARI",
    THE_WHISPERING_MARSH     = "DRAKKARI",
    THE_RING_OF_GLORY        = "DRAKKARI",
    DEFIANT_RING             = "DRAKKARI",
    CRYPT_OF_THE_DENIED      = "AMANI_CATACOMBS",
    CRYPT_OF_THE_LOST_MASON  = "AMANI_CATACOMBS",
    KIN_S_REST               = "AMANI_CATACOMBS",
    BLISTERING_VAULT         = "AMANI_CATACOMBS",
    TOMB_OF_THE_LOST_PRIEST  = "AMANI_CATACOMBS",
    CRYPT_OF_THE_LOST_WARRIOR = "AMANI_CATACOMBS",
    CRYPT_OF_THE_DISGRACED   = "AMANI_CATACOMBS",
    VAULTS_OF_ATAL_UTEK      = "BLOOD_GOD",
}),
[2509] = Dsl.zone("VAULTS_OF_ATAL_UTEK", "BLOOD_GOD", {
    AMANI_FOOTHOLD           = "AMANI",
    NORTHERN_AMANI_BULWARK   = "AMANI",
    EASTERN_AMANI_OUTPOST    = "AMANI",
}),
[2536] = Dsl.zone("ATAL_AMAN", "CITY_OF_GOLD"),      -- si la sous-carte est remontée en jeu
[2633] = Dsl.zone("THE_RING_OF_GLORY", "DRAKKARI"),  -- idem
```

## 5. Étapes

1. Valider §4 (choix des packs, alternatives) et les questions du §6.
2. Mesurer les durées manquantes (script `docs/data/measure.py`), générer `Tracks.lua` (catalogue étendu) et `Locale.lua` (annexe A) depuis les CSV.
3. Réécrire `Packs.lua` et `Zones.lua`, garder les packs existants demandés, corriger Sandfury.
4. Harnais Lua 5.1 (celui de Voidstorm) dans les 11 locales, copie dans AddOns, `/eoa now` sur les cartes 2536, 2585, 2509 et 2633.
5. Release 1.2.0 via `push_addon_release.py za` (bump mineur : nouvelles zones).

## 6. Questions à trancher

1. Packs natifs Midnight déjà livrés (Zul'Aman Midnight, Zeb'Alar, Halazzi/Jan'alai/Nalorakk/Akil'zon Loa, Troll Combat) : garder pour compatibilité des profils existants, ou retirer comme pour Voidstorm ?
2. Sandfury : remplacer le substitut Tanaris par le vrai set de Zul'Farrak, ou garder les deux ?
3. Tokka's Landing : musique (côte sombrelance) ou respect du silence natif ?
4. Époque des défauts : pour un plugin « Zul'Aman » les défauts ci-dessus mélangent Vanilla, TBC, Cata, Wrath et BfA selon le meilleur miroir ; préférer un défaut tout-TBC (Amani partout, catacombes pour les cryptes, Zangarmarsh pour la mangrove) et laisser le reste en packs optionnels ?

## Annexe A — noms localisés (AreaTable 12.1.0)

| AreaID | enUS | frFR | deDE | esES | esMX | ptBR | ruRU | itIT | koKR | zhCN | zhTW |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 15947 | Zul'Aman | Zul’Aman | Zul'Aman | Zul'Aman | Zul'Aman | Zul'Aman | Зул'Аман | Zul'aman | 줄아만 | 祖阿曼 | 祖阿曼 |
| 16730 | Thresh Cove | Crique du Requin | Die Dreschbucht | Cala Trillada | Cala de Trilladores | Enseada Sumanta | Бухта молотильщиков | Baia di Thresh | 타작 만 | 特雷什海湾 | 瑟雷西灣 |
| 16196 | Funerary Coast | Côte Funéraire | Begräbnisküste | Costa Funeraria | Costa Funeraria | Costa Funérea | Погребальный берег | Costa Funebre | 장송의 해안 | 礼葬海岸 | 葬儀海岸 |
| 16198 | Shrine of Kulzi | Sanctuaire de Kulzi | Schrein von Kulzi | Santuario de Kulzi | Santuario de Kulzi | Santuário de Kurzi | Святилище Кулзи | Santuario di Kulzi | 쿨지의 제단 | 库尔吉神殿 | 庫爾吉聖壇 |
| 16203 | Camp Stonewash | Camp Rochembruns | Reinsteinlager | Campo Piedralimpia | Campamento Pedregoso | Acampamento Lavapedra | Галечный лагерь | Accampamento Acquapetra | 돌연마 야영지 | 石洗营地 | 石洗營地 |
| 16204 | Shrine of Filo | Sanctuaire de Filo | Der Schrein von Filo | Santuario de Filo | Santuario de Filo | Santuário de Filo | Святилище Фило | Santuario di Filo | 필로의 제단 | 费洛神殿 | 菲洛聖壇 |
| 16348 | Zul'Aman Depths | Profondeurs de Zul’Aman | Tiefen von Zul'Aman | Profundidades de Zul'Aman | Profundidades de Zul'Aman | Profundezas de Zul'Aman | Глубины Зул'Амана | Abissi di Zul'aman | 줄아만 심연 | 祖阿曼深渊 | 祖阿曼地底 |
| 16352 | Numazon Crypts | Cryptes de Numazon | Numazongruften | Criptas de Numazon | Criptas Numazon | Criptas Numazon | Склепы Нумазона | Cripte di Numazon | 누마존 납골당 | 努马松墓穴 | 努曼佐墓穴 |
| 16367 | Solemn Valley | Vallée Solennelle | Solenne Senke | Valle Solemne | Valle Solemne | Vale Solene | Скорбная долина | Valle Solenne | 경건한 계곡 | 庄严谷 | 莊嚴谷地 |
| 16375 | Loaknit Den | Tanière de Tisse-Loa | Loagewirkter Bau | Cubil Forjaloa | Cubil de Loatejido | Toca Urdiloa | Логово зверей лоа | Covo Intrecciato ai Loa | 로아니트 소굴 | 神愈兽穴 | 羅亞尼特之穴 |
| 16379 | Strait of Hexx'alor | Détroit de Hexx’alor | Straße von Hexx'alor | Estrecho de Hexx'alor | Estrecho de Hexx'alor | Estreito de Hexx'alor | Пролив Клят'алора | Stretto di Mal'alor | 헥살로어의 해협 | 赫克萨罗海峡 | 黑薩洛海峽 |
| 16418 | Shadebasin Watch | Guet d’Ombre-Bassin | Schattenbeckenwacht | Atalaya Cuencasombra | Avanzada Umbracuenca | Vigília da Bacia Sombria | Тенепрудный дозор | Presidio del Bacino Ombroso | 그늘분지 감시터 | 影盆岗哨 | 影盆守望 |
| 16567 | Wit'Kalar Crypt | Crypte de Wit’Kalar | Gruft Wit'Kalar | Cripta de Wit'Kalar | Cripta Wit'Kalar | Cripta Wit'Kalar | Вит'Каларский склеп | Cripta di Wit'kalar | 위트칼라르 납골당 | 维特卡拉尔墓穴 | 溫卡拉墓穴 |
| 16568 | Miststone Wells | Puits de Brume-Roche | Nebelsteinquellen | Pozas Piedrabruma | Pozos de Petrabruma | Poços de Pedrabruma | Колодцы туманного камня | Pozzi di Pietranebbia | 안개돌 우물 | 雾石深井 | 霧石之井 |
| 16598 | The Stump | La Souche | Der Stumpf | El Tocón | El Tocón | O Toco | Пень | Troncone | 그루터기 | 大树桩 | 大樹樁 |
| 16841 | Tomb of Mun'jin | Tombe de Mun’jin | Mun'jins Grab | Tumba de Mun'jin | Tumba de Mun'jin | Tumba de Mun'jin | Гробница Мун'джина | Tomba di Mun'jin | 문진의 무덤 | 穆金之墓 | 穆恩金之墓 |
| 16860 | The Great Sea | Grande mer | Das Große Meer | Mare Magnum | Mare Magnum | O Grande Oceano | Великое море | Grande Mare | 대해 | 无尽之海 | 無盡之海 |
| 17720 | The Forbidding Sea | Mer Interdite | Das Verbotene Meer | Mar Adusto | Mar Adusto | O Mar Proibido | Зловещее море | Mar delle Insidie | 성난 바다 | 禁忌之海 | 禁忌之海 |
| 16183 | Amani'Zar Village | Amani’Zar | Amani'zar | Aldea Amani'Zar | Aldea Amani'Zar | Aldeia Amani'Zar | Деревня Амани'Зар | Amani'zar | 아마니자르 마을 | 阿曼尼扎村 | 阿曼尼扎村 |
| 16202 | Witherbark Bluffs | Pitons de Fanécorce | Klippen der Bleichborken | Cimas Secacorteza | Cima Secacorteza | Penhascos Cascasseca | Деревня Сухокожих | Picchi degli Scorzasecca | 마른나무껍질 절벽 | 枯木山崖 | 枯木崖 |
| 16586 | Torntusk Overlook | Surplomb des Brocherompue | Warte der Stumpfhauer | Mirador Colmillopartido | Mirador Colmillopartido | Mirante Presa-arrancada | Пост Сломанного Клыка | Altura degli Zannaculea | 톤터스크 전망대 | 断齿瞭望台 | 斷齒瞰臺 |
| 16184 | Temple of Akil'zon | Temple d’Akil’zon | Der Tempel von Akil'zon | Templo de Akil'zon | Templo de Akil'zon | Templo de Akil'zon | Храм Акил'зон | Tempio di Akil'zon | 아킬존의 사원 | 埃基尔松神庙 | 阿奇爾森神廟 |
| 16187 | Akil'zon's Reach | Confins d’Akil’zon | Weiten von Akil'zon | Confín de Akil'zon | Confín de Akil'zon | Fronte de Akil'zon | Предел Акил'зон | Foresta di Akil'zon | 아킬존의 외연 | 埃基尔松的领地 | 阿奇爾森之境 |
| 16185 | Temple of Jan'alai | Temple de Jan’alai | Der Tempel von Jan'alai | Templo de Jan'alai | Templo de Jan'alai | Templo de Jan'alai | Храм Джан'алай | Tempio di Jan'alai | 잔알라이의 사원 | 加亚莱的神庙 | 賈納雷神廟 |
| 16186 | Temple of Halazzi | Temple d’Halazzi | Der Tempel von Halazzi | Templo de Halazzi | Templo de Halazzi | Templo de Halazzi | Храм Халаззи | Tempio di Halazzi | 할라지의 사원 | 哈尔拉兹神庙 | 哈拉齊神廟 |
| 16188 | Spiritpaw Borough | Quartier des Pattes-Spirituelles | Gemeinde der Geisterpfoten | Distrito de los Pataespíritu | Distrito Zarpánima | Distrito Espiriturso | Селение Призрачной Лапы | Borgo degli Zampaspirito | 영혼발바닥 거주지 | 灵爪密区 | 靈爪鎮 |
| 16189 | Nalorakk's Prowl | Maraude de Nalorakk | Nalorakks Pirsch | Acecho de Nalorakk | Merodeo de Nalorakk | Espreita de Nalorakk | Угодья Налоракка | Ronda di Nalorakk | 날로라크의 배회지 | 纳洛拉克之匿 | 納羅拉克之匿 |
| 16190 | Spiritpaw Backwoods | Arrière pays Patte-Spirituelle | Hinterwald der Geisterpfoten | Bosque Remoto Pataespíritu | Bosque Remoto Zarpánima | Ermo Espiriturso | Чаща Призрачной Лапы | Entroterre degli Zampaspirito | 영혼발바닥 산골 | 灵爪边林 | 靈爪荒林 |
| 16191 | Speaker's Rest | Repos de l’orateur | Rednerruh | Reposo del Portavoz | Reposo del Portavoz | Repouso do Mensageiro | Вещий покой | Riposo dell'Oratore | 예언자의 휴식처 | 代言人的梦乡 | 語者之憩 |
| 16192 | Broken Throne | Trône brisé | Der Zerschlagene Thron | Trono Destrozado | Trono Quebrado | Trono Partido | Разрушенный трон | Trono Distrutto | 부서진 왕좌 | 残破神庙 | 破碎王座 |
| 16193 | Revantusk Sedge | Carex des Vengebroches | Die Bruchhauersegge | Juncos Sañadiente | Juncia Sañadiente | Junco Revatusco | Тростинник Сломанного Клыка | Palude degli Zannatorta | 깨진엄니 부락 | 恶齿莎台 | 惡齒莎草 |
| 16194 | Atal'Aman | Atal’Aman | Atal'Aman | Atal'Aman | Atal'Aman | Atal'Aman | Атал'Аман | Atal'aman | 아탈아만 | 阿塔阿曼 | 阿塔阿曼 |
| 16382 | Talonstrike Terrace | Terrasse des Frappe-Serres | Krallenschlagterrasse | Bancal Golpegarfa | Bancal Golpegarra | Terraço Lançagarra | Терраса Удара Когтя | Terrazza degli Zannartiglio | 갈퀴쐐기의 정원 | 鹰击台 | 爪擊露臺 |
| 16383 | Swiftclaw Terrace | Terrasse des Vivegriffes | Flinkklauenterrasse | Bancal Garrapresta | Bancal Zarpapresta | Terraço Garrápida | Терраса Стремительного Когтя | Terrazza degli Zannalesta | 날쌘발톱의 정원 | 迅爪台 | 迅爪露臺 |
| 16384 | Ragemaw Terrace | Terrasse des Rage-Gueules | Zornschlundterrasse | Bancal Faucerrabia | Bancal Faucefuria | Terraço Rosnafúria | Терраса Яростной Пасти | Terrazza dei Faucirabbiose | 분노아귀 정원 | 怒喉台 | 怒顎露臺 |
| 16385 | Firewing Terrace | Terrasse des Ailes-de-Feu | Feuerschwingenterrasse | Bancal Alafuego | Bancal Alafuego | Terraço Asardente | Терраса Огнекрылов | Terrazza degli Alardente | 불꽃날개의 정원 | 火翼台 | 火翼露臺 |
| 16386 | Warlord's Stair | Escalier du Seigneur de guerre | Treppe des Kriegsfürsten | Escalera del Señor de la Guerra | Escalera del Señor de la Guerra | Escadaria do Senhor da Guerra | Спуск вождя | Scalinata del Signore della Guerra | 전쟁군주의 계단 | 督军之阶 | 督軍階梯 |
| 16670 | Altar of Malacrass | Autel de Malacrass | Der Altar von Malacrass | Altar de Malacrass | Altar de Malacrass | Altar de Malacrass | Алтарь Малакрасса | Altare di Malacrass | 말라크라스의 제단 | 玛拉卡斯的祭坛 | 瑪拉克雷斯祭壇 |
| 16195 | Atal'Abasi | Atal’Abasi | Atal'Abasi | Atal'Abasi | Atal'Abasi | Atal'Abasi | Атал'Абаси | Atal'abasi | 아탈아바시 | 阿塔阿巴希 | 阿塔阿巴斯 |
| 16197 | Leech Bog | Marais aux Sangsues | Egelsumpf | Ciénaga Sanguijuela | Ciénaga Sanguijuela | Brejo das Sanguessugas | Болото пиявок | Pantano delle Sanguisughe | 거머리 수렁 | 水蛭沼泽 | 汲血泥沼 |
| 16199 | Maisara Deeps | Tréfonds de Maisara | Maisaratiefen | Profundidades de Maisara | Profundidades de Maisara | Abismo de Maisara | Глубины Маисара | Abissi di Maisara | 마이사라 심연 | 迈萨拉深渊 | 梅薩拉深淵 |
| 16380 | The Skybridge | Le pont Céleste | Die Himmelsbrücke | El Puente Celestial | El Puente Celestial | Ponte Celeste | Небесный Мост | Ponte Celeste | 하늘다리 | 天空之桥 | 天空之橋 |
| 16721 | Hermit's Mooring | Amarrage de l’ermite | Die Anlegestelle des Einsiedlers | Embarcadero del Ermitaño | Embarcadero del Ermitaño | Ancoradouro do Ermitão | Укромная стоянка | Ormeggio dell'Eremita | 은둔자의 계류장 | 赫米特的避风港 | 隱士泊地 |
| 16200 | Zeb'Alar Lumberyard | Scierie de Zeb’Alar | Holzlager Zeb'Alar | Aserradero Zeb'Alar | Aserradero Zeb'Alar | Madeireira de Zeb'Alar | Лесопилка Зеб'Алара | Deposito di Legname di Zeb'alar | 제브알라르 벌목장 | 泽布阿拉尔伐木场 | 桀阿拉木材場 |
| 16201 | Bitterbark | Amerécorce | Bitterborke | Cortezamarga | Cortezamarga | Cascamarga | Корогнилье | Cortamara | 비통껍질 | 苦皮 | 苦木 |
| 16365 | The Coiled Isle | Île Annelée | Die Gewundene Insel | Isla Serpenteante | La Isla Serpenteante | A Ilha Enrolada | Спиральный остров | Isola Serpeggiante | 똬리의 섬 | 盘卷蛇岛 | 盤蛇島 |
| 16783 | Wreck of Gral's Belly | Épave de la Panse de Gral | Wrack von Grals Bauch | Restos de la Barriga de Gral | Naufragio de Vientre de Gral | Destroços da Barriga de Gral | Обломки "Живота Грала" | Relitto della Ventre di Gral | 그랄의 위장호 잔해 | 格罗尔之腹号残骸 | 格拉爾之腹殘骸 |
| 16784 | Gnarldor Isle | Île Torsadine | Die Knardorinsel | Isla Gnarldor | Isla Gnarldor | Ilha Dendronor | Остров Дряздор | Isola di Nodor | 날도르 섬 | 纳拉多尔岛 | 納爾多島 |
| 16786 | Gate of the Western Fang | Porte du Crochet occidental | Tor des Westlichen Fangzahns | Puerta del Colmillo Occidental | Puerta del Colmillo Occidental | Portão da Presa Ocidental | Врата Западного Клыка | Cancello della Zanna Occidentale | 서쪽 송곳니의 관문 | 西牙侧门 | 西牙之門 |
| 16787 | The Forum | Forum | Das Forum | Foro | El Foro | Fórum | Форум | Foro | 광장 | 广场 | 廣場 |
| 16788 | Wreck of Sethraliss's Scale | Épave de l’Écaille de Sephraliss | Wrack von Sethraliss' Schuppe | Restos del Escama de Sethraliss | Naufragio de Escama de Sethraliss | Destroços da Escama de Sethraliss | Обломки "Чешуи Сетралисс" | Relitto della Scaglia di Sethralis | 세스랄리스의 비늘호 잔해 | 塞塔里斯之鳞号残骸 | 瑟沙利斯之鱗殘骸 |
| 16824 | Tooth of Sargoth | Dent de Sargoth | Zahn von Sargoth | Diente de Sargoth | Colmillo de Sargoth | Dente de Sargoth | Клык Саргота | Dente di Sargoth | 사르고스의 이빨 | 萨戈斯之牙 | 薩戈斯之齒 |
| 16897 | Diver's Arch | Arche du plongeon | Der Bogen des Tauchers | Arco del Buzo | Arco del Salto | Arco do Mergulhador | Арка ныряльщика | Arco del Sommozzatore | 잠수부의 아치 | 跳潜者石拱 | 潛者拱礁 |
| 17718 | The Great Sea | Grande mer | Das Große Meer | Mare Magnum | Mare Magnum | O Grande Oceano | Великое море | Grande Mare | 대해 | 无尽之海 | 無盡之海 |
| 17719 | The Forbidding Sea | Mer Interdite | Das Verbotene Meer | Mar Adusto | Mar Adusto | O Mar Proibido | Зловещее море | Mar delle Insidie | 성난 바다 | 禁忌之海 | 禁忌之海 |
| 16774 | Tokka's Landing | Débarcadère de Tokka | Tokkas Landung | Desembarco de Tokka | Desembarco de Tokka | Pouso de Tokka | Лагерь Токки | Crocevia di Tokka | 토카의 상륙지 | 托卡的登陆点 | 托卡臺地 |
| 16830 | Tokka's Folly | Folie de Tokka | Tokkas Torheit | Capricho de Tokka | Imprudencia de Tokka | Desatino de Tokka | Ошибка Токки | Follia di Tokka | 토카의 우행 | 托卡的愚行 | 托卡的愚行 |
| 16775 | Ofi's Hut | Hutte d’Ofi | Ofis Hütte | Cabaña de Ofi | Choza de Ofi | Cabana da Oufi | Хижина Офи | Rifugio di Ofi | 오피의 오두막 | 奥菲的小屋 | 歐菲的小屋 |
| 16776 | Mlurkkr Mire | Le Mrrglécage | Der Mlurkkrmorast | Fangal de Mlurkkr | Marisma Mlurkkr | Charco Mlurkkr | Трясина Млурккр | Pantano Mlurkkr | 멀록잠복 수렁 | 姆噜咕尔泥沼 | 姆嚕咕沼地 |
| 16777 | Cloudlight Beacon | Balise Luminuée | Das Wolkenlichtleuchtfeuer | Faro Luzlunar | Faro de Nubeluz | Farol Lumenimbus | Маяк Светлого Облака | Segnalatore Nubechiara | 구름불빛 봉화 | 云光道标 | 雲光信標 |
| 16778 | Wreck of Paku's Talon | Épave de la Serre de Paku | Wrack von Pakus Kralle | Restos de Garfa de Paku | Naufragio de Garfa de Paku | Destroços da Garra de Paco | Обломки "Когтя Паку" | Relitto dell'Artiglio di Paku | 파쿠의 갈퀴발톱호 잔해 | 帕库之爪号残骸 | 帕骷之爪殘骸 |
| 16779 | Wreck of Torga's Beak | Épave du Bec de Torga | Wrack von Torgas Schnabel | Restos del Pico de Torga | Naufragio de Pico de Torga | Destroços do Bico de Torga | Обломки "Клюва Торги" | Relitto della Becco di Torga | 토르가의 부리호 잔해 | 托加之喙号残骸 | 托加之喙殘骸 |
| 16769 | Zail'Zar Span | Travée de Zail’Zar | Die Spanne von Zail'Zar | Tramo de Zail'Zar | El Paso de Zail'Zar | Vastidão de Zail'Zar | Мост Заил'Зар | Passo di Zail'zar | 잘리자르 교각 | 扎尔扎之桥 | 札爾札大橋 |
| 16785 | Gate of the Eastern Fang | Porte du Crochet oriental | Tor des Östlichen Fangzahns | Puerta del Colmillo Oriental | Puerta del Colmillo Oriental | Portão da Presa Oriental | Врата Восточного Клыка | Cancello della Zanna Orientale | 동쪽 송곳니의 관문 | 东牙侧门 | 東牙之門 |
| 16789 | The Fangs | Les Crocs | Die Fänge | Los Colmillos | Los Colmillos | As Presas | Клыки | Zanne | 송곳니 | 毒牙区 | 尖牙之地 |
| 16790 | Path of Whispers | Sente des Murmures | Pfad des Flüsterns | Senda de los Susurros | Sendero de Susurros | Caminho dos Sussurros | Путь голосов | Sentiero dei Sussurri | 속삭임의 길 | 低语小径 | 低語之徑 |
| 16791 | Gate of the Serpent's Eye | Porte de l’Œil du serpent | Tor des Schlangenauges | Puerta del Ojo de la Serpiente | Puerta del Ojo Viperino | Portão do Olho-de-serpente | Врата Змеиного ока | Cancello dell'Occhio della Serpe | 뱀의 눈 관문 | 蛇眼之门 | 蛇眼之門 |
| 16792 | Venom Rise | Cime Venimeuse | Die Giftanhöhen | Alto del Veneno | Ascenso Venenoso | Alto da Peçonha | Ядовитый холм | Altura del Veleno | 맹독 오름길 | 毒液高地 | 毒液高地 |
| 16793 | Blistering Terrace | Terrasse Infestée | Die Befallene Terrasse | Bancal Virulento | Bancal Virulento | Terraço Pustulento | Обжигающая терраса | Terrazza Rovente | 끓어오르는 정원 | 毒疱平台 | 灼蝕露臺 |
| 16795 | The Serpent's Tail | La Serpentine | Der Schlangenschwanz | Cola de la Sierpe | La Cola Viperina | Cauda da Serpente | Змеиный Хвост | Coda del Serpente | 뱀의 꼬리 | 毒蛇之尾 | 蛇尾之地 |
| 16771 | The Altar of Wrath | Autel du Courroux | Der Altar des Zorns | Altar de la Cólera | El Altar de la Cólera | Altar da Ira | Алтарь гнева | Altare della Collera | 분노의 제단 | 愤怒祭坛 | 憤怒祭壇 |
| 16780 | The Whispering Marsh | Marais Murmurant | Die Flüsternde Marsch | Marisma Susurrante | El Pantano Susurrante | Charco Sussurrante | Шепчущее болото | Palude Sussurrante | 속삭이는 습지 | 低语沼泽 | 低語沼澤 |
| 16781 | The Ring of Glory | Arène de la Gloire | Der Ring des Ruhms | Círculo de la Gloria | El Círculo de la Gloria | O Ringue da Glória | Арена Славы | Anello della Gloria | 영광의 투기장 | 荣耀之环 | 榮耀競技場 |
| 16782 | Defiant Ring | Cercle de la Défiance | Der Ring der Unbeugsamen | Anillo Desafiante | Arena Desafiante | Círculo Desafiante | Круг непокорных | Circolo Sprezzante | 저항의 장 | 抗命者之环 | 不屈競技場 |
| 16755 | Crypt of the Denied | Crypte des Bannis | Die Krypta der Verschmähten | Cripta de los Rechazados | Cripta de los Rechazados | Cripta dos Renegados | Склеп отвергнутых | Cripta dei Rinnegati | 부정당한 자의 납골당 | 弃民墓穴 | 受拒者墓穴 |
| 16992 | Crypt of the Lost Mason | Crypte des Architectes perdus | Gruft des verlorenen Steinmetzes | Cripta del Mampostero Perdido | Cripta del Albañil Perdido | Cripta do Alvanel Perdido | Склеп потерянного каменщика | Cripta del Costruttore Perduto | 방황하는 석공의 납골당 | 迷失石匠之墓 | 失落石匠墓穴 |
| 16993 | Kin's Rest | Repos des Ancêtres | Ruhestätte der Ahnen | Reposo de los Parientes | Reposo Fraterno | Repouso da Tribo | Покой сородичей | Riposo della Prole | 혈족의 안식처 | 亲族之眠 | 同胞之眠 |
| 16994 | Blistering Vault | Caveau Infesté | Die Befallene Kammer | Cámara Virulenta | Bóveda Virulenta | Câmara Pustulante | Обжигающее хранилище | Cripta Rovente | 끓어오르는 금고 | 毒疱地窟 | 灼蝕寶庫 |
| 16995 | Tomb of the Lost Priest | Tombe du Clergé perdu | Grabstätte des verlorenen Priesters | Tumba del Sacerdote Perdido | Tumba del Sacerdote Perdido | Tumba do Sacerdote Perdido | Гробница потерянного жреца | Tomba del Sacerdote Perduto | 방황하는 사제의 무덤 | 迷失祭司之墓 | 失落牧師之墓 |
| 16996 | Crypt of The Lost Warrior | Crypte de l’Armée perdue | Gruft des verlorenen Kriegers | Cripta del Guerrero Perdido | Cripta del Guerrero Perdido | Cripta do Guerreiro Perdido | Склеп потерянного воина | Cripta del Guerriero Perduto | 방황하는 전사의 납골당 | 迷失战士之墓 | 失落戰士墓穴 |
| 16997 | Crypt of the Disgraced | Crypte de la Disgrâce | Gruft der Entehrten | Cripta de los Deshonrados | Cripta de los Desgraciados | Cripta dos Desonrados | Склеп опозоренных | Cripta dei Disonorati | 명예를 잃은 자의 납골당 | 蒙羞者之墓 | 失寵者墓穴 |
| 17316 | Vaults of Atal'Utek | Caveaux d’Atal’Utek | Die Kammern von Atal'Utek | Cámaras de Atal'Utek | Bóvedas de Atal'Utek | Câmaras de Atal'Utek | Хранилища Атал'Утека | Segrete di Atal'utek | 아탈우텍 금고 | 阿塔乌特克地窟 | 阿塔烏特克寶庫 |
| 16535 | Vaults of Atal'Utek | Caveaux d’Atal’Utek | Die Kammern von Atal'Utek | Cámaras de Atal'Utek | Bóvedas de Atal'Utek | Câmaras de Atal'Utek | Хранилища Атал'Утека | Segrete di Atal'utek | 아탈우텍 금고 | 阿塔乌特克地窟 | 阿塔烏特克寶庫 |
| 17650 | Amani Foothold | Tête de pont amani | Der Stützpunkt der Amani | Base Amani | Asentamiento Amani | Ponto de Apoio dos Amani | Плацдарм Амани | Avamposto degli Amani | 아마니 거점 | 阿曼尼据点 | 阿曼尼據點 |
| 17729 | Northern Amani Bulwark | Rempart amani septentrional | Nördliches Amani-Bollwerk | Baluarte Norte Amani | Baluarte Amani del Norte | Baluarte Amani Setentrional | Северный аманийский бастион | Barricata Settentrionale degli Amani | 북부 아마니 보루 | 北阿曼尼堡垒 | 北部阿曼尼壁壘 |
| 17730 | Eastern Amani Outpost | Avant-poste amani oriental | Östlicher Amani-Außenposten | Avanzada Este Amani | Puesto de Avanzada Amani del Este | Posto Avançado Amani Oriental | Восточная аманийская застава | Avamposto Orientale degli Amani | 동부 아마니 전초기지 | 东阿曼尼岗哨 | 東部阿曼尼哨站 |
| 16977 | Ruuk'Jar's Clutch | Couvée de Ruuk’Jar | Ruuk'Jars Gelege | Nidada de Ruuk'Jar | Nidada de Ruuk'Jar | Ninhada de Ruuk'Jar | Кладка Руук'джар | Cumulo di Ruuk'jar | 루크자르의 부화장 | 鲁克贾尔的孵化巢 | 魯克賈窩巢 |
| 16978 | Vault of Restless Bones | Caveau des Ossements tourmentés | Kammer der Ruhelosen Knochen | Cámara de los Huesos sin Sosiego | Bóveda de los Huesos sin Sosiego | Câmara dos Ossos Inquietos | Хранилище костей неупокоенных | Segrete delle Ossa Irrequiete | 안식 없는 유골의 금고 | 无眠骸骨地窟 | 無法安息的骸骨寶庫 |
| 16979 | Profaned Mausoleum | Mausolée profané | Das Entweihte Mausoleum | Mausoleo Profanado | Mausoleo Profanado | Mausoléu Profanado | Оскверненный мавзолей | Mausoleo Profanato | 불경한 영묘 | 被亵渎的陵墓 | 瀆神墓塚 |
| 16990 | The Underbelly | Entrailles | Die Schattenseite | Bajos Fondos | Bajos Fondos | Os Esgotos | Клоака | Sotterranei | 뒤안길 | 地下坟茔 | 墓窖 |
| 17022 | Cursed Depths | Profondeurs Maudites | Die Verfluchten Tiefen | Zonas Profundas Malditas | Profundidades Malditas | Profundezas Amaldiçoadas | Проклятые глубины | Profondità Maledette | 저주받은 나락 | 诅咒深渊 | 詛咒深淵 |
| 17023 | The Seal of Wrath | Sceau du Courroux | Das Siegel des Zorns | Sello de la Cólera | El Sello de la Cólera | Selo da Ira | Печать гнева | Sigillo della Collera | 분노의 봉인 | 愤怒封印 | 憤怒之印 |

## Annexe B — kits natifs, fichier par fichier

- **ZoneMusic 3254** « Zone 12.0 - Zul'Aman - Forest - General - Walk » (pauses 180–300 s) — 15947 Zul'Aman
  - 7682414 `MUS_120_ZulAman_A` (220.6 s)
  - 7682416 `MUS_120_ZulAman_B` (221.9 s)
  - 7682418 `MUS_120_ZulAman_C` (221.0 s)
  - 7682420 `MUS_120_ZulAman_D` (76.8 s)
  - 7682424 `MUS_120_ZulAman_F` (75.7 s)
  - 7682428 `MUS_120_ZulAman_H` (222.2 s)
- **ZoneMusic 3441** « Zone 12.0 - Zul'Aman - Forest - Prey - Walk » (pauses 180–300 s) — 16730 Thresh Cove
  - 3931650 `mus_mx_cov_seatoftheprimus_01` (à mesurer s)
- **ZoneMusic 3249** « Zone 12.0 - Zul'Aman - Hub - AmaniZar - Walk » (pauses 180–300 s) — 16183 Amani'Zar Village
  - 7682264 `MUS_120_Amanizar_Village_A` (158.2 s)
  - 7682266 `MUS_120_Amanizar_Village_B` (146.8 s)
  - 7682268 `MUS_120_Amanizar_Village_C` (129.1 s)
  - 7682270 `MUS_120_Amanizar_Village_D` (212.1 s)
  - 7688251 `MUS_120_Amanizar_Village_H` (212.4 s)
  - 7688253 `MUS_120_Amanizar_Village_E` (212.4 s)
- **ZoneMusic 3250** « Zone 12.0 - Zul'Aman - Hub - General - Walk » (pauses 180–300 s) — 16202 Witherbark Bluffs, 16586 Torntusk Overlook
  - 7682264 `MUS_120_Amanizar_Village_A` (158.2 s)
  - 7682266 `MUS_120_Amanizar_Village_B` (146.8 s)
  - 7682268 `MUS_120_Amanizar_Village_C` (129.1 s)
  - 7688251 `MUS_120_Amanizar_Village_H` (212.4 s)
  - 7688253 `MUS_120_Amanizar_Village_E` (212.4 s)
- **ZoneMusic 3353** « Zone 12.0 - Zul'Aman - Akil'zon - General - Walk » (pauses 180–300 s) — 16184 Temple of Akil'zon, 16187 Akil'zon's Reach
  - 7688241 `MUS_120_Akilzon_Loa_A` (95.7 s)
  - 7688243 `MUS_120_Akilzon_Loa_B` (98.5 s)
  - 7688245 `MUS_120_Akilzon_Loa_C` (127.9 s)
- **ZoneMusic 3282** « Zone 12.0 - Zul'Aman - Jan'alai - Temple - Pre-Campaign - Walk » (pauses 180–300 s) — 16185 Temple of Jan'alai
  - 7689597 `MUS_120_Janalai_Loa_A` (126.6 s)
  - 7689599 `MUS_120_Janalai_Loa_B` (121.0 s)
  - 7689601 `MUS_120_Janalai_Loa_C` (149.3 s)
- **ZoneMusic 3246** « Zone 12.0 - Zul'Aman - Halazzi - Temple - Walk » (pauses 100–220 s) — 16186 Temple of Halazzi
  - 7681066 `MUS_120_Halazzi_Loa_A` (83.6 s)
  - 7681068 `MUS_120_Halazzi_Loa_B` (81.3 s)
  - 7681070 `MUS_120_Halazzi_Loa_C` (89.2 s)
  - 7681074 `MUS_120_Halazzi_Loa_H` (132.9 s)
- **ZoneMusic 3252** « Zone 12.0 - Zul'Aman - Nalorakk - Temple - Walk » (pauses 180–300 s) — 16188 Spiritpaw Borough, 16189 Nalorakk's Prowl, 16190 Spiritpaw Backwoods
  - 7682370 `MUS_120_Nalorakk_Loa_C` (140.4 s)
  - 7682372 `MUS_120_Nalorakk_Loa_D` (134.3 s)
  - 7682374 `MUS_120_Nalorakk_Loa_E` (130.5 s)
  - 7682378 `MUS_120_Nalorakk_Loa_H` (178.0 s)
- **ZoneMusic 3248** « Zone 12.0 - Zul'Aman - Twilights Blade - General - Walk » (pauses 180–300 s) — 16191 Speaker's Rest, 16192 Broken Throne, 16193 Revantusk Sedge
  - 7681220 `MUS_120_Twilights_Blade_B` (103.4 s)
  - 7681222 `MUS_120_Twilights_Blade_C` (95.1 s)
  - 7681226 `MUS_120_Twilights_Blade_E` (75.6 s)
  - 7713458 `MUS_120_Twilights_Blade_F` (77.8 s)
  - 7713460 `MUS_120_Twilights_Blade_G` (75.3 s)
  - 7713462 `MUS_120_Twilights_Blade_I` (76.9 s)
- **ZoneMusic 3271** « Zone 12.0 - Zul'Aman - Atal'Aman - General - Walk » (pauses 180–300 s) — 16194 Atal'Aman
  - 7684176 `MUS_120_AtalAman_A` (177.6 s)
  - 7684178 `MUS_120_AtalAman_B` (162.8 s)
  - 7684180 `MUS_120_AtalAman_C` (132.4 s)
  - 7684182 `MUS_120_AtalAman_D` (189.8 s)
  - 7684184 `MUS_120_AtalAman_E` (129.7 s)
- **ZoneMusic 3251** « Zone 12.0 - Zul'Aman - Swamp - General - Walk » (pauses 180–300 s) — 16195 Atal'Abasi, 16197 Leech Bog, 16199 Maisara Deeps, 16380 The Skybridge, 16721 Hermit's Mooring
  - 7682280 `MUS_120_AtalAbasi_A` (107.3 s)
  - 7682282 `MUS_120_AtalAbasi_B` (110.3 s)
  - 7682284 `MUS_120_AtalAbasi_C` (147.0 s)
  - 7682286 `MUS_120_AtalAbasi_D` (135.9 s)
  - 7682288 `MUS_120_AtalAbasi_E` (127.9 s)
  - 7682290 `MUS_120_AtalAbasi_F` (74.6 s)
  - 7682292 `MUS_120_AtalAbasi_H` (158.3 s)
- **ZoneMusic 3253** « Zone 12.0 - Zul'Aman - Lumber - General - Walk » (pauses 180–300 s) — 16200 Zeb'Alar Lumberyard, 16201 Bitterbark
  - 7682400 `MUS_120_ZebAlar_A` (143.3 s)
  - 7682402 `MUS_120_ZebAlar_B` (163.1 s)
  - 7682404 `MUS_120_ZebAlar_H` (202.7 s)
  - 7682406 `MUS_120_ZebAlar_C` (184.1 s)
  - 7682408 `MUS_120_ZebAlar_D` (121.6 s)
  - 7682410 `MUS_120_ZebAlar_E` (135.2 s)
  - 7682412 `MUS_120_ZebAlar_F` (202.7 s)
- **ZoneMusic 3624** « Zone 12.1 - The Coiled Isle - Forest - General - Walk » (pauses 180–300 s) — 16365 The Coiled Isle
  - 8242911 `MUS_121_Coiled_Isle_A` (127.7 s)
  - 8242913 `MUS_121_Coiled_Isle_B` (143.5 s)
  - 8242915 `MUS_121_Coiled_Isle_C` (142.7 s)
  - 8242917 `MUS_121_Coiled_Isle_H` (205.8 s)
  - 8245059 `MUS_121_Coiled_Isle_D` (133.8 s)
  - 8245061 `MUS_121_Coiled_Isle_E` (134.8 s)
- **ZoneMusic 3656** « Zone 12.1 - The Coiled Isle - Hub - Tokka's Landing - Master » (pauses 120–240 s) — 16774 Tokka's Landing, 16830 Tokka's Folly
  - 7713995 `Silent_310` (à mesurer s)
- **ZoneMusic 3576** « Zone 12.1 - The Coiled Isle - Mire - General - Walk » (pauses 180–300 s) — 16775 Ofi's Hut, 16776 Mlurkkr Mire, 16777 Cloudlight Beacon, 16778 Wreck of Paku's Talon, 16779 Wreck of Torga's Beak
  - 8218548 `MUS_121_Mlurkkr_Mire_A` (106.4 s)
  - 8218551 `MUS_121_Mlurkkr_Mire_B` (109.5 s)
  - 8218554 `MUS_121_Mlurkkr_Mire_C` (102.0 s)
  - 8218556 `MUS_121_Mlurkkr_Mire_D` (123.0 s)
  - 8218558 `MUS_121_Mlurkkr_Mire_H` (111.2 s)
- **ZoneMusic 3577** « Zone 12.1 - The Coiled Isle - Venom - Exterior - Walk » (pauses 180–300 s) — 16769 Zail'Zar Span, 16785 Gate of the Eastern Fang, 16789 The Fangs, 16790 Path of Whispers, 16791 Gate of the Serpent's Eye, 16792 Venom Rise, 16793 Blistering Terrace, 16795 The Serpent's Tail
  - 8218578 `MUS_121_Serpents_Tail_A` (124.2 s)
  - 8218580 `MUS_121_Serpents_Tail_H` (190.2 s)
  - 8221023 `MUS_121_Serpents_Tail_B` (122.2 s)
  - 8221025 `MUS_121_Serpents_Tail_C` (114.4 s)
  - 8221027 `MUS_121_Serpents_Tail_D` (123.2 s)
  - 8245306 `MUS_121_Serpents_Tail_F` (133.9 s)
- **ZoneMusic 3575** « Zone 12.1 - The Coiled Isle - Spirit - General - Walk » (pauses 180–300 s) — 16771 The Altar of Wrath, 16780 The Whispering Marsh, 16781 The Ring of Glory, 16782 Defiant Ring
  - 8218636 `MUS_121_Whispering_March_A` (137.6 s)
  - 8218638 `MUS_121_Whispering_March_B` (145.5 s)
  - 8218640 `MUS_121_Whispering_March_C` (121.6 s)
  - 8218642 `MUS_121_Whispering_March_D` (131.7 s)
  - 8218644 `MUS_121_Whispering_March_E` (94.0 s)
  - 8218650 `MUS_121_Whispering_March_H` (241.1 s)
- **ZoneMusic 3579** « Zone 12.1 - The Coiled Isle - Venom - Vaults - Walk » (pauses 180–300 s) — 17316 Vaults of Atal'Utek, 16535 Vaults of Atal'Utek
  - 8218628 `MUS_121_Venomous_Abyss_C` (196.7 s)
  - 8218634 `MUS_121_Venomous_Abyss_H` (205.1 s)
  - 8221033 `MUS_121_Venomous_Abyss_F` (208.4 s)
  - 8244831 `MUS_121_Venomous_Abyss_G` (143.5 s)
  - 8244833 `MUS_121_Venomous_Abyss_I` (149.7 s)
  - 8245063 `MUS_121_Venomous_Abyss_J` (135.4 s)
- **ZoneMusic 3635** « Zone 12.1 - The Coiled Isle - Venom - Vaults - Hub » (pauses 180–300 s) — 17650 Amani Foothold, 17729 Northern Amani Bulwark, 17730 Eastern Amani Outpost
  - 8218624 `MUS_121_Venomous_Abyss_A` (203.0 s)
  - 8218626 `MUS_121_Venomous_Abyss_B` (198.4 s)
  - 8218630 `MUS_121_Venomous_Abyss_D` (160.8 s)
  - 8218632 `MUS_121_Venomous_Abyss_E` (167.5 s)

