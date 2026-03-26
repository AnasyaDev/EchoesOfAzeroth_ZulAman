local _, ns = ...

-- ============================================================
-- Track catalog
--
-- Confirmed sources:
-- - Wago Tools AreaTable / ZoneMusic for Zul'Aman (UiMapID 568)
-- - Wago community listfile for Troll / Zul'Aman / Zul'Drak /
--   Stranglethorn / Durotar / Thunder Isle / Zandalari /
--   Zuldazar music file names and FDIDs
--   music file names and FDIDs
--
-- Fallback local sources:
-- - Existing troll-like Midnight tracks already used in the
--   Quel'Thalas plugin
-- ============================================================

ns.Tracks = {
    -- TBC > Zul'Aman ------------------------------------------
    ZA_WalkUni01 = 53825,
    ZA_WalkUni02 = 53826,
    ZA_WalkUni03 = 53827,
    ZA_WalkUni04 = 53828,
    ZA_WalkUni05 = 53829,
    ZA_WalkUni06 = 53830,
    ZA_Battle01  = 53831,
    ZA_Battle02  = 53832,
    ZA_Battle03  = 53833,
    ZA_Battle04  = 53834,
    ZA_Battle05  = 53835,
    ZA_Victory01 = 53836,

    -- Wrath > Northrend troll general -------------------------
    NR_TrollGeneral01 = 229925,
    NR_TrollGeneral02 = 229926,
    NR_TrollGeneral03 = 229927,
    NR_TrollGeneral04 = 229928,

    -- Wrath > Zul'Drak ----------------------------------------
    ZD_GeneralIntro01 = 230003,
    ZD_GeneralIntro02 = 230004,
    ZD_GeneralIntro03 = 230005,
    ZD_GeneralIntro04 = 230006,
    ZD_GeneralIntro05 = 230007,
    ZD_GeneralIntro06 = 230008,
    ZD_GeneralWalkDay01 = 230009,
    ZD_GeneralWalkDay02 = 230010,
    ZD_GeneralWalkDay03 = 230011,
    ZD_GeneralWalkDay04 = 230012,
    ZD_GeneralWalkNight01 = 230013,
    ZD_GeneralWalkNight02 = 230014,
    ZD_GeneralWalkNight03 = 230015,
    ZD_GeneralWalkNight04 = 230016,
    ZD_HarkoaIntro01 = 230017,
    ZD_HarkoaIntro02 = 230018,
    ZD_MamtothIntro01 = 230019,
    ZD_MamtothIntro02 = 230020,
    ZD_QuetzlunIntro01 = 230021,
    ZD_QuetzlunIntro02 = 230022,
    ZD_RhunokIntro01 = 230023,
    ZD_RhunokIntro02 = 230024,
    ZD_SseratusIntro01 = 230025,
    ZD_SseratusIntro02 = 230026,

    -- Cataclysm > Stranglethorn / Gurubashi -------------------
    STV_GurubashiVale01 = 441768,
    STV_GurubashiVale02 = 441769,
    STV_GurubashiVale03 = 441770,
    STV_GurubashiVale04 = 441771,
    STV_Gurubashi01 = 441772,
    STV_Gurubashi02 = 441773,
    STV_Gurubashi03 = 441774,
    STV_Gurubashi04 = 441775,
    ZG_VoodooMoment = 53254,

    -- Classic / Cataclysm > Tanaris / Sandfury proxy ------------
    TA_General01 = 441776,
    TA_General02 = 441777,
    TA_General03 = 441778,
    TA_General04 = 441779,
    TA_General05 = 441780,
    TA_General06 = 441781,
    TA_General07 = 441782,
    TA_General08 = 441783,
    TA_General09 = 441784,
    TA_General10 = 441785,
    DE_Day01 = 53432,
    DE_Day02 = 53433,
    DE_Day03 = 53434,
    DE_Night01 = 53435,
    DE_Night02 = 53436,
    DE_Night03 = 53437,

    -- Cataclysm > Durotar / Darkspear ---------------------------
    DU_GeneralA01 = 441578,
    DU_GeneralA02 = 441579,
    DU_GeneralA03 = 441580,
    DU_GeneralB01 = 441581,
    DU_GeneralB02 = 441582,
    DU_GeneralB03 = 441583,
    DU_GeneralB04 = 441584,
    DU_GeneralC01 = 441585,
    DU_GeneralC02 = 441586,
    DU_GeneralC03 = 441587,
    DU_GeneralC04 = 441588,
    DU_GeneralD01 = 441589,
    DU_GeneralD02 = 441590,

    -- Pandaria > Zandalari / Thunder Isle -----------------------
    MOP_ZandalariProphecy01 = 840520,
    MOP_Zandalari1A01 = 840521,
    MOP_Zandalari1A02 = 840522,
    MOP_Zandalari1A03 = 840523,
    MOP_Zandalari1B01 = 840524,
    MOP_Zandalari1B02 = 840525,
    MOP_Zandalari1B03 = 840526,
    MOP_Zandalari1C01 = 840527,
    MOP_Zandalari1C02 = 840528,
    MOP_Zandalari2A01 = 840529,
    MOP_Zandalari2A02 = 840530,
    MOP_Zandalari2A03 = 840531,
    MOP_Zandalari2A04 = 840532,
    MOP_Zandalari2A05 = 840533,
    MOP_Zandalari2B01 = 840534,
    MOP_Zandalari2B02 = 840535,
    MOP_Zandalari2B03 = 840536,
    MOP_Zandalari2C01 = 840537,
    MOP_Zandalari2C02 = 840538,
    MOP_Zandalari2C03 = 840539,

    MOP_ThunderIsleA01 = 840469,
    MOP_ThunderIsleA02 = 840470,
    MOP_ThunderIsleA03 = 840471,
    MOP_ThunderIsleA04 = 840472,
    MOP_ThunderIsleA05 = 840473,
    MOP_ThunderIsleA06 = 840474,
    MOP_ThunderIsleA07 = 840475,
    MOP_ThunderIsleB01 = 840481,
    MOP_ThunderIsleB02 = 840482,
    MOP_ThunderIsleB03 = 840483,
    MOP_ThunderIsleB04 = 840484,
    MOP_ThunderIsleB05 = 840485,
    MOP_ThunderIsleC01 = 840487,
    MOP_ThunderIsleC02 = 840488,
    MOP_ThunderIsleC03 = 840489,
    MOP_ThunderIsleC04 = 840490,

    MOP_TrollBattleA01 = 840508,
    MOP_TrollBattleA02 = 840509,
    MOP_TrollBattleA03 = 840510,
    MOP_TrollBattleB01 = 840511,
    MOP_TrollBattleB02 = 840512,
    MOP_TrollBattleB03 = 840513,

    -- Battle for Azeroth > Zandalar / Zuldazar ------------------
    BFA_ZandalariLamentA = 1780948,
    BFA_ZandalariLamentB = 1780949,
    BFA_ZandalariLamentH = 1780950,

    BFA_ZuldazarIntroA = 1780951,
    BFA_ZuldazarIntroB = 1780952,
    BFA_ZuldazarIntroH = 1780953,

    BFA_ZuldazarJungleA = 2143543,
    BFA_ZuldazarJungleB = 2143544,
    BFA_ZuldazarJungleC = 2143545,
    BFA_ZuldazarJungleH = 2143546,
    BFA_ZuldazarJungleD = 2148032,
    BFA_ZuldazarJungleE = 2148033,
    BFA_ZuldazarJungleF = 2148034,
    BFA_ZuldazarJungleG = 2148035,
    BFA_ZuldazarJungleI = 2148036,
    BFA_ZuldazarJungleJ = 2148037,
    BFA_ZuldazarJungleK = 2148038,
    BFA_ZuldazarJungleL = 2148039,
    BFA_ZuldazarJungleM = 2148040,
    BFA_ZuldazarJungleN = 2148041,
    BFA_ZuldazarJungleO = 2148042,
    BFA_ZuldazarJungleP = 2148043,
    BFA_ZuldazarJungleQ = 2148044,
    BFA_ZuldazarJungleR = 2148045,
    BFA_ZuldazarJungleS = 2148046,

    BFA_AtalDazarA = 2146227,
    BFA_AtalDazarB = 2146228,
    BFA_AtalDazarC = 2146229,
    BFA_AtalDazarD = 2146230,
    BFA_AtalDazarH = 2146231,

    BFA_Zuldazar1A = 2146277,
    BFA_Zuldazar1B = 2146278,
    BFA_Zuldazar1H = 2146279,
    BFA_Zuldazar2A = 2146280,
    BFA_Zuldazar2B = 2146281,
    BFA_Zuldazar2C = 2146282,
    BFA_Zuldazar2H = 2146283,
    BFA_ZuldazarDrum = 2179262,

    BFA_ZandalarForeverA = 2564881,
    BFA_ZandalarForeverB = 2564882,
    BFA_ZandalarForeverC = 2564883,
    BFA_ZandalarForeverH = 2564884,
    BFA_ZandalarForeverD = 2575919,
    BFA_ZandalarForeverE = 2575920,
    BFA_ZandalarForeverF = 2575921,
    BFA_ZandalarForeverG = 2575922,
    BFA_ZandalarForeverI = 2575923,
    BFA_ZandalarForeverJ = 2575924,

    BFA_ZandalariTroll1A = 2844629,
    BFA_ZandalariTroll1B = 2844630,
    BFA_ZandalariTroll1C = 2844631,
    BFA_ZandalariTroll2A = 2844632,
    BFA_ZandalariTroll2B = 2844633,
    BFA_ZandalariTroll2C = 2844634,
    BFA_ZandalariTroll3A = 2844635,
    BFA_ZandalariTroll3B = 2844636,
    BFA_ZandalariTroll3C = 2844637,
    BFA_ZandalariTroll4A = 2844638,
    BFA_ZandalariTroll4B = 2844639,
    BFA_ZandalariTroll4C = 2844640,

    -- Midnight > Amani / Zul'Aman -----------------------------
    MN_AmanizarVillageA = 7682264,
    MN_AmanizarVillageB = 7682266,
    MN_AmanizarVillageC = 7682268,
    MN_AmanizarVillageD = 7682270,
    MN_AmanizarVillageE = 7688253,
    MN_AmanizarVillageH = 7688251,

    MN_ZulAmanA = 7682414,
    MN_ZulAmanB = 7682416,
    MN_ZulAmanC = 7682418,
    MN_ZulAmanD = 7682420,
    MN_ZulAmanE = 7682422,
    MN_ZulAmanF = 7682424,
    MN_ZulAmanG = 7682426,
    MN_ZulAmanH = 7682428,

    MN_TrollCombatA = 7693704,
    MN_TrollCombatB = 7693706,
    MN_TrollCombatC = 7693708,
    MN_TrollCombatD = 7693710,
    MN_TrollCombatE = 7693712,
    MN_TrollCombatF = 7693714,
    MN_TrollCombatG = 7693716,
    MN_TrollCombatH = 7693718,
    MN_TrollCombatI = 7693720,
    MN_TrollCombatJ = 7693722,
    MN_TrollCombatK = 7693724,
    MN_TrollCombatL = 7693726,

    -- Midnight > Darkspear / Echo Isles -------------------------
    MN_DenOfEchoesA = 7696410,
    MN_DenOfEchoesB = 7696412,
    MN_DenOfEchoesC = 7696414,
    MN_DenOfEchoesD = 7696416,
    MN_DenOfEchoesH = 7696418,

    -- Local fallback troll-like Midnight tracks ---------------
    MN_AtalAbasiA = 7682280,
    MN_AtalAbasiB = 7682282,
    MN_AtalAbasiC = 7682284,
    MN_AtalAbasiD = 7682286,
    MN_AtalAbasiE = 7682288,
    MN_AtalAbasiF = 7682290,
    MN_AtalAbasiH = 7682292,
    MN_AtalAmanA = 7684176,
    MN_AtalAmanB = 7684178,
    MN_AtalAmanC = 7684180,
    MN_AtalAmanD = 7684182,
    MN_AtalAmanE = 7684184,
    MN_AtalAmanH = 7684186,
    MN_LightbloomTrollC = 7690547,
}

ns.TrackDurations = {
    [53825] =  113.8,  -- ZA_WalkUni01
    [53826] =   74.5,  -- ZA_WalkUni02
    [53827] =  108.6,  -- ZA_WalkUni03
    [53828] =   70.5,  -- ZA_WalkUni04
    [53829] =   90.5,  -- ZA_WalkUni05
    [53830] =  113.9,  -- ZA_WalkUni06
    [53831] =  136.2,  -- ZA_Battle01
    [53832] =  117.1,  -- ZA_Battle02
    [53833] =   40.7,  -- ZA_Battle03
    [53834] =   92.4,  -- ZA_Battle04
    [53835] =   79.8,  -- ZA_Battle05
    [53836] =   80.0,  -- ZA_Victory01
    [229925] =   46.2,  -- NR_TrollGeneral01
    [229926] =   55.7,  -- NR_TrollGeneral02
    [229927] =   38.4,  -- NR_TrollGeneral03
    [229928] =   44.2,  -- NR_TrollGeneral04
    [230003] =   98.3,  -- ZD_GeneralIntro01
    [230004] =   98.3,  -- ZD_GeneralIntro02
    [230005] =  128.6,  -- ZD_GeneralIntro03
    [230006] =  125.9,  -- ZD_GeneralIntro04
    [230007] =  129.5,  -- ZD_GeneralIntro05
    [230008] =  125.9,  -- ZD_GeneralIntro06
    [230009] =   89.8,  -- ZD_GeneralWalkDay01
    [230010] =   90.8,  -- ZD_GeneralWalkDay02
    [230011] =  101.7,  -- ZD_GeneralWalkDay03
    [230012] =   92.7,  -- ZD_GeneralWalkDay04
    [230013] =   90.3,  -- ZD_GeneralWalkNight01
    [230014] =   90.2,  -- ZD_GeneralWalkNight02
    [230015] =  101.4,  -- ZD_GeneralWalkNight03
    [230016] =   93.0,  -- ZD_GeneralWalkNight04
    [230017] =   28.2,  -- ZD_HarkoaIntro01
    [230018] =   27.9,  -- ZD_HarkoaIntro02
    [230019] =   30.9,  -- ZD_MamtothIntro01
    [230020] =   27.9,  -- ZD_MamtothIntro02
    [230021] =   32.3,  -- ZD_QuetzlunIntro01
    [230022] =   27.9,  -- ZD_QuetzlunIntro02
    [230023] =   30.0,  -- ZD_RhunokIntro01
    [230024] =   27.9,  -- ZD_RhunokIntro02
    [230025] =   28.3,  -- ZD_SseratusIntro01
    [230026] =   27.9,  -- ZD_SseratusIntro02
    [441768] =   78.0,  -- STV_GurubashiVale01
    [441769] =   92.9,  -- STV_GurubashiVale02
    [441770] =   91.0,  -- STV_GurubashiVale03
    [441771] =  102.1,  -- STV_GurubashiVale04
    [441772] =   64.4,  -- STV_Gurubashi01
    [441773] =   90.5,  -- STV_Gurubashi02
    [441774] =   84.9,  -- STV_Gurubashi03
    [441775] =   89.8,  -- STV_Gurubashi04
    [53254] =   84.4,  -- ZG_VoodooMoment
    [441776] =   87.5,  -- TA_General01
    [441777] =   87.9,  -- TA_General02
    [441778] =   84.3,  -- TA_General03
    [441779] =   66.4,  -- TA_General04
    [441780] =   82.1,  -- TA_General05
    [441781] =   72.1,  -- TA_General06
    [441782] =   72.1,  -- TA_General07
    [441783] =   61.5,  -- TA_General08
    [441784] =   34.4,  -- TA_General09
    [441785] =   84.2,  -- TA_General10
    [53432] =   65.7,  -- DE_Day01
    [53433] =   81.0,  -- DE_Day02
    [53434] =   54.2,  -- DE_Day03
    [53435] =   77.7,  -- DE_Night01
    [53436] =   62.5,  -- DE_Night02
    [53437] =   57.7,  -- DE_Night03
    [441578] =  124.7,  -- DU_GeneralA01
    [441579] =  101.6,  -- DU_GeneralA02
    [441580] =  101.6,  -- DU_GeneralA03
    [441581] =   72.8,  -- DU_GeneralB01
    [441582] =   72.1,  -- DU_GeneralB02
    [441583] =   95.2,  -- DU_GeneralB03
    [441584] =   95.2,  -- DU_GeneralB04
    [441585] =   85.4,  -- DU_GeneralC01
    [441586] =   85.4,  -- DU_GeneralC02
    [441587] =   61.3,  -- DU_GeneralC03
    [441588] =   61.2,  -- DU_GeneralC04
    [441589] =   84.8,  -- DU_GeneralD01
    [441590] =   84.9,  -- DU_GeneralD02
    [840520] =  170.6,  -- MOP_ZandalariProphecy01
    [840521] =   72.4,  -- MOP_Zandalari1A01
    [840522] =   80.1,  -- MOP_Zandalari1A02
    [840523] =   75.0,  -- MOP_Zandalari1A03
    [840524] =   72.4,  -- MOP_Zandalari1B01
    [840525] =   80.1,  -- MOP_Zandalari1B02
    [840526] =   74.0,  -- MOP_Zandalari1B03
    [840527] =   64.3,  -- MOP_Zandalari1C01
    [840528] =   78.9,  -- MOP_Zandalari1C02
    [840529] =   77.6,  -- MOP_Zandalari2A01
    [840530] =   50.2,  -- MOP_Zandalari2A02
    [840531] =   38.4,  -- MOP_Zandalari2A03
    [840532] =   49.2,  -- MOP_Zandalari2A04
    [840533] =   64.2,  -- MOP_Zandalari2A05
    [840534] =  118.1,  -- MOP_Zandalari2B01
    [840535] =   46.5,  -- MOP_Zandalari2B02
    [840536] =   64.2,  -- MOP_Zandalari2B03
    [840537] =   77.1,  -- MOP_Zandalari2C01
    [840538] =   50.5,  -- MOP_Zandalari2C02
    [840539] =   33.3,  -- MOP_Zandalari2C03
    [840469] =   86.9,  -- MOP_ThunderIsleA01
    [840470] =   87.4,  -- MOP_ThunderIsleA02
    [840471] =   66.4,  -- MOP_ThunderIsleA03
    [840472] =   22.5,  -- MOP_ThunderIsleA04
    [840473] =  124.5,  -- MOP_ThunderIsleA05
    [840474] =   60.2,  -- MOP_ThunderIsleA06
    [840475] =   71.3,  -- MOP_ThunderIsleA07
    [840481] =   66.5,  -- MOP_ThunderIsleB01
    [840482] =   73.1,  -- MOP_ThunderIsleB02
    [840483] =   94.5,  -- MOP_ThunderIsleB03
    [840484] =  106.5,  -- MOP_ThunderIsleB04
    [840485] =   97.1,  -- MOP_ThunderIsleB05
    [840487] =   95.4,  -- MOP_ThunderIsleC01
    [840488] =   98.3,  -- MOP_ThunderIsleC02
    [840489] =  119.6,  -- MOP_ThunderIsleC03
    [840490] =   48.6,  -- MOP_ThunderIsleC04
    [840508] =   40.1,  -- MOP_TrollBattleA01
    [840509] =   84.6,  -- MOP_TrollBattleA02
    [840510] =   56.5,  -- MOP_TrollBattleA03
    [840511] =   41.1,  -- MOP_TrollBattleB01
    [840512] =   80.5,  -- MOP_TrollBattleB02
    [840513] =   54.8,  -- MOP_TrollBattleB03
    [1780948] =   82.8,  -- BFA_ZandalariLamentA
    [1780949] =   82.8,  -- BFA_ZandalariLamentB
    [1780950] =   82.8,  -- BFA_ZandalariLamentH
    [1780951] =   72.5,  -- BFA_ZuldazarIntroA
    [1780952] =   72.5,  -- BFA_ZuldazarIntroB
    [1780953] =   72.5,  -- BFA_ZuldazarIntroH
    [2143543] =  159.9,  -- BFA_ZuldazarJungleA
    [2143544] =  159.9,  -- BFA_ZuldazarJungleB
    [2143545] =  167.0,  -- BFA_ZuldazarJungleC
    [2143546] =  162.3,  -- BFA_ZuldazarJungleH
    [2148032] =  115.9,  -- BFA_ZuldazarJungleD
    [2148033] =  111.9,  -- BFA_ZuldazarJungleE
    [2148034] =  117.8,  -- BFA_ZuldazarJungleF
    [2148035] =  118.0,  -- BFA_ZuldazarJungleG
    [2148036] =  122.7,  -- BFA_ZuldazarJungleI
    [2148037] =  121.1,  -- BFA_ZuldazarJungleJ
    [2148038] =  122.5,  -- BFA_ZuldazarJungleK
    [2148039] =  101.2,  -- BFA_ZuldazarJungleL
    [2148040] =   92.0,  -- BFA_ZuldazarJungleM
    [2148041] =   92.0,  -- BFA_ZuldazarJungleN
    [2148042] =   92.7,  -- BFA_ZuldazarJungleO
    [2148043] =   89.7,  -- BFA_ZuldazarJungleP
    [2148044] =   92.2,  -- BFA_ZuldazarJungleQ
    [2148045] =   92.1,  -- BFA_ZuldazarJungleR
    [2148046] =   91.9,  -- BFA_ZuldazarJungleS
    [2146227] =   93.5,  -- BFA_AtalDazarA
    [2146228] =   93.5,  -- BFA_AtalDazarB
    [2146229] =   93.5,  -- BFA_AtalDazarC
    [2146230] =   93.5,  -- BFA_AtalDazarD
    [2146231] =   93.5,  -- BFA_AtalDazarH
    [2146277] =   72.1,  -- BFA_Zuldazar1A
    [2146278] =   72.1,  -- BFA_Zuldazar1B
    [2146279] =   72.1,  -- BFA_Zuldazar1H
    [2146280] =   85.8,  -- BFA_Zuldazar2A
    [2146281] =   85.8,  -- BFA_Zuldazar2B
    [2146282] =   85.8,  -- BFA_Zuldazar2C
    [2146283] =   85.8,  -- BFA_Zuldazar2H
    [2179262] =   71.9,  -- BFA_ZuldazarDrum
    [2564881] =  121.6,  -- BFA_ZandalarForeverA
    [2564882] =  112.9,  -- BFA_ZandalarForeverB
    [2564883] =  115.9,  -- BFA_ZandalarForeverC
    [2564884] =  145.5,  -- BFA_ZandalarForeverH
    [2575919] =  101.0,  -- BFA_ZandalarForeverD
    [2575920] =  105.7,  -- BFA_ZandalarForeverE
    [2575921] =  102.9,  -- BFA_ZandalarForeverF
    [2575922] =   94.9,  -- BFA_ZandalarForeverG
    [2575923] =  130.8,  -- BFA_ZandalarForeverI
    [2575924] =  125.8,  -- BFA_ZandalarForeverJ
    [2844629] =  121.1,  -- BFA_ZandalariTroll1A
    [2844630] =  122.1,  -- BFA_ZandalariTroll1B
    [2844631] =   93.6,  -- BFA_ZandalariTroll1C
    [2844632] =  116.9,  -- BFA_ZandalariTroll2A
    [2844633] =  121.7,  -- BFA_ZandalariTroll2B
    [2844634] =  101.5,  -- BFA_ZandalariTroll2C
    [2844635] =  139.3,  -- BFA_ZandalariTroll3A
    [2844636] =  108.2,  -- BFA_ZandalariTroll3B
    [2844637] =  110.3,  -- BFA_ZandalariTroll3C
    [2844638] =  127.4,  -- BFA_ZandalariTroll4A
    [2844639] =  127.7,  -- BFA_ZandalariTroll4B
    [2844640] =  102.3,  -- BFA_ZandalariTroll4C
    [7682264] =  158.2,  -- MN_AmanizarVillageA
    [7682266] =  146.8,  -- MN_AmanizarVillageB
    [7682268] =  129.1,  -- MN_AmanizarVillageC
    [7682270] =  212.1,  -- MN_AmanizarVillageD
    [7688253] =  212.4,  -- MN_AmanizarVillageE
    [7688251] =  212.4,  -- MN_AmanizarVillageH
    [7682414] =  220.6,  -- MN_ZulAmanA
    [7682416] =  221.9,  -- MN_ZulAmanB
    [7682418] =  221.0,  -- MN_ZulAmanC
    [7682420] =   76.8,  -- MN_ZulAmanD
    [7682422] =   76.2,  -- MN_ZulAmanE
    [7682424] =   75.7,  -- MN_ZulAmanF
    [7682426] =  106.9,  -- MN_ZulAmanG
    [7682428] =  222.2,  -- MN_ZulAmanH
    [7693704] =   72.1,  -- MN_TrollCombatA
    [7693706] =   59.7,  -- MN_TrollCombatB
    [7693708] =  120.5,  -- MN_TrollCombatC
    [7693710] =   63.8,  -- MN_TrollCombatD
    [7693712] =   59.1,  -- MN_TrollCombatE
    [7693714] =   87.1,  -- MN_TrollCombatF
    [7693716] =   26.6,  -- MN_TrollCombatG
    [7693718] =  203.4,  -- MN_TrollCombatH
    [7693720] =  139.3,  -- MN_TrollCombatI
    [7693722] =  159.0,  -- MN_TrollCombatJ
    [7693724] =  131.1,  -- MN_TrollCombatK
    [7693726] =  129.8,  -- MN_TrollCombatL
    [7696410] =  180.8,  -- MN_DenOfEchoesA
    [7696412] =  130.9,  -- MN_DenOfEchoesB
    [7696414] =  156.3,  -- MN_DenOfEchoesC
    [7696416] =  180.9,  -- MN_DenOfEchoesD
    [7696418] =  178.8,  -- MN_DenOfEchoesH
    [7682280] =  107.3,  -- MN_AtalAbasiA
    [7682282] =  110.3,  -- MN_AtalAbasiB
    [7682284] =  147.0,  -- MN_AtalAbasiC
    [7682286] =  135.9,  -- MN_AtalAbasiD
    [7682288] =  127.9,  -- MN_AtalAbasiE
    [7682290] =   74.6,  -- MN_AtalAbasiF
    [7682292] =  158.3,  -- MN_AtalAbasiH
    [7684176] =  177.6,  -- MN_AtalAmanA
    [7684178] =  162.8,  -- MN_AtalAmanB
    [7684180] =  132.4,  -- MN_AtalAmanC
    [7684182] =  189.8,  -- MN_AtalAmanD
    [7684184] =  129.7,  -- MN_AtalAmanE
    [7684186] =  177.8,  -- MN_AtalAmanH
    [7690547] =  157.4,  -- MN_LightbloomTrollC
}
