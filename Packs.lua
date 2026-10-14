local _, ns = ...
local T = ns.Tracks
local api = _G.EchoesOfAzeroth
local Dsl = api and api.PluginDsl
if not Dsl then
    error("EchoesOfAzeroth core must load before EchoesOfAzeroth_ZulAman")
end

local Pack = Dsl.pack
local MixedPack = Dsl.mixedPack
local Merge = Dsl.mergeUnique

-- ============================================================
-- Music Packs
--
-- Defaults stay in the classic era (Vanilla, TBC, Wrath) and pick,
-- for each Midnight place, the closest troll music of that era.
-- Each default pack also exists as a (… + Midnight) mix with the
-- kit the game natively plays there.  No pure Midnight pack is
-- shipped: that is what the player hears with the addon disabled.
-- Later troll music (Cataclysm, MoP, BfA) ships as optional packs
-- for manual assignment.
-- ============================================================

-- T["ZD_GeneralWalkDay01"] style lists built from a prefix and a
-- string of suffixes, so a typo fails at load instead of at play time.
local function Family(prefix, suffixes)
    local out = {}
    for suffix in suffixes:gmatch("%S+") do
        local id = T[prefix .. suffix]
        if not id then
            error("EchoesOfAzeroth_ZulAman: unknown track " .. prefix .. suffix)
        end
        out[#out + 1] = id
    end
    return out
end

-- ------------------------------------------------------------
-- Classic-era groups
-- ------------------------------------------------------------

local ZA_WALK = Family("ZA_AMB", "10 11 12 13 14 15")          -- TBC Zul'Aman, walking
local ZA_BATTLE = Family("ZA_BTL", "11 12 14 15")               -- TBC Zul'Aman, battle (13 is a 40s stinger)
local ZF_SET = Family("ZF_", "Quiet1 Quiet2 Quiet7 QuietShort8") -- Vanilla Zul'Farrak
local ZD_DAY = Family("ZD_GeneralWalkDay", "01 02 03 04")
local ZD_NIGHT = Family("ZD_GeneralWalkNight", "01 02 03 04")
local ZD_EXTRA = Merge(Family("NR_TrollGeneral", "01 02 03 04"), Family("ZD_GeneralIntro", "02 03 04 05 06"))
local ZM_GENERAL = Family("ZM_GeneralWalkUni", "01 02 03 04 05 06")
local GL_DARK = Family("GL_EversongDarkWalkUni", "01 02 03 04")

-- ------------------------------------------------------------
-- Midnight native kits (mixed packs only)
-- ------------------------------------------------------------

local MN_ZULAMAN = Family("MN_ZulAman", "A B C D E F G H")
local MN_VILLAGE = Merge(Family("MN_AmanizarVillage", "A B C D E H"), Family("MN_TokkasLanding", "A B C D H"))
local MN_HALAZZI = Family("MN_HalazziLoa", "A B C D E F G H")
local MN_NALORAKK = Family("MN_NalorakkLoa", "A B C D E F G H I")
local MN_AKILZON = Family("MN_AkilzonLoa", "A B C D H")
local MN_JANALAI = Family("MN_JanalaiLoa", "A B C D E F H")
local MN_TWILIGHT = Family("MN_TwilightsBlade", "A B C D E F G H I")
local MN_TEMPLE = Merge(Family("MN_AtalAman", "A B C D E H"), Family("MN_VenomousAbyss", "A B C D E F G H I J"))
local MN_SWAMP = Family("MN_AtalAbasi", "A B C D E F H")
local MN_MIRE = Family("MN_MlurkkrMire", "A B C D H")
local MN_JUNGLE = Merge(Family("MN_ZebAlar", "A B C D E F H"), Family("MN_CoiledIsle", "A B C D E H"))
local MN_SERPENT = Family("MN_SerpentsTail", "A B C D E F H")
local MN_SPIRITS = Family("MN_WhisperingMarch", "A B C D E F G H I J")

-- ------------------------------------------------------------
-- Default packs (classic era)
-- ------------------------------------------------------------

-- The TBC raid set, which Blizzard reuses as the generic troll sound.
local AMANI = Pack {
    label = "Amani (TBC)",
    any = ZA_WALK,
}

-- Temple districts: the raid's walking set with its battle pieces.
local AMANI_TEMPLE = Pack {
    label = "Amani Temple (TBC)",
    intro = T.ZA_BTL13,
    any = Merge(ZA_WALK, ZA_BATTLE, { T.ZA_VCT10 }),
}

-- Blizzard's own troll village kit (Sen'jin, Echo Isles): the Zul'Aman
-- walking set mixed with the Vanilla Zul'Farrak pieces.
local DARKSPEAR = Pack {
    label = "Darkspear (Vanilla + TBC)",
    any = Merge(Family("ZA_AMB", "11 12 13 14 15"), ZF_SET, { T.ZF_Rally9 }),
}

-- The real Zul'Farrak music (also Jintha'Alor and the Frostmane).
local ZULFARRAK = Pack {
    label = "Zul'Farrak (Vanilla)",
    intro = T.ZF_Rally9,
    any = ZF_SET,
}

-- Stranglethorn troll ruins and Witherbark Village, day and night.
local JUNGLE = Pack {
    label = "Troll Jungle (Vanilla)",
    day = Family("CL_DayJungle", "01 02 03"),
    night = Family("CL_NightJungle", "01 02 03"),
}

-- One pack per loa shrine, each with the intro of its Zul'Drak
-- counterpart over the Zul'Drak day/night rotation.
local function Shrine(label, introTrack, extra)
    return Pack {
        label = label,
        intro = introTrack,
        day = ZD_DAY,
        night = ZD_NIGHT,
        any = Merge(ZD_EXTRA, { extra }),
    }
end
local SHRINE_HALAZZI = Shrine("Shrine of Har'koa (Wrath)", T.ZD_HarKoaIntro01, T.ZD_HarKoaIntro02)
local SHRINE_NALORAKK = Shrine("Shrine of Rhunok (Wrath)", T.ZD_RhunokIntro01, T.ZD_RhunokIntro02)
local SHRINE_AKILZON = Shrine("Shrine of Quetz'lun (Wrath)", T.ZD_QuetzLunIntro01, T.ZD_QuetzLunIntro02)
local SHRINE_JANALAI = Shrine("Shrine of Mam'toth (Wrath)", T.ZD_MamTothIntro01, T.ZD_MamTothIntro02)

local DRAKKARI = Pack {
    label = "Drakkari (Wrath)",
    intro = T.ZD_GeneralIntro01,
    day = ZD_DAY,
    night = ZD_NIGHT,
    any = ZD_EXTRA,
}

-- Serpent cult: Vanilla Zul'Gurub over the raid battle set, opened by
-- the altar of Sseratus, the serpent loa of Zul'Drak.
local SERPENT = Pack {
    label = "Serpent Altar (Vanilla + Wrath)",
    intro = T.ZD_SseratusIntro01,
    any = Merge({ T.ZG_VooDoo, T.ZD_SseratusIntro02 }, ZA_BATTLE),
}

local ZANGARMARSH = Pack {
    label = "Zangarmarsh (TBC)",
    any = ZM_GENERAL,
}

local COILFANG_MIRE = Pack {
    label = "Coilfang Mire (TBC)",
    any = Merge(Family("ZM_CoilfangWalkUni", "01 02 03"), Family("ZM_GeneralWalkUni", "01 02")),
}

local AMANI_CATACOMBS = Pack {
    label = "Amani Catacombs (TBC)",
    any = GL_DARK,
}

-- ------------------------------------------------------------
-- Mixed packs (default + the Midnight kit of the same places)
-- ------------------------------------------------------------

local function Native(label, tracks)
    return Pack { label = label, any = tracks }
end

local AMANI_MIXED = MixedPack("Amani (TBC + Midnight)", AMANI, Native("Zul'Aman (Midnight)", MN_ZULAMAN))
local AMANI_TEMPLE_MIXED = MixedPack("Amani Temple (TBC + Midnight)", AMANI_TEMPLE, Native("Atal'Aman (Midnight)", MN_TEMPLE))
local DARKSPEAR_MIXED = MixedPack("Darkspear (Vanilla + TBC + Midnight)", DARKSPEAR, Native("Amani'Zar Village (Midnight)", MN_VILLAGE))
local JUNGLE_MIXED = MixedPack("Troll Jungle (Vanilla + Midnight)", JUNGLE, Native("Zeb'Alar / Coiled Isle (Midnight)", MN_JUNGLE))
local SHRINE_HALAZZI_MIXED = MixedPack("Shrine of Har'koa (Wrath + Midnight)", SHRINE_HALAZZI, Native("Halazzi (Midnight)", MN_HALAZZI))
local SHRINE_NALORAKK_MIXED = MixedPack("Shrine of Rhunok (Wrath + Midnight)", SHRINE_NALORAKK, Native("Nalorakk (Midnight)", MN_NALORAKK))
local SHRINE_AKILZON_MIXED = MixedPack("Shrine of Quetz'lun (Wrath + Midnight)", SHRINE_AKILZON, Native("Akil'zon (Midnight)", MN_AKILZON))
local SHRINE_JANALAI_MIXED = MixedPack("Shrine of Mam'toth (Wrath + Midnight)", SHRINE_JANALAI, Native("Jan'alai (Midnight)", MN_JANALAI))
local DRAKKARI_MIXED = MixedPack("Drakkari (Wrath + Midnight)", DRAKKARI, Native("Whispering Marsh (Midnight)", MN_SPIRITS))
local SERPENT_MIXED = MixedPack("Serpent Altar (Vanilla + Wrath + Midnight)", SERPENT, Native("Serpent's Tail (Midnight)", MN_SERPENT))
local ZANGARMARSH_MIXED = MixedPack("Zangarmarsh (TBC + Midnight)", ZANGARMARSH, Native("Atal'Abasi (Midnight)", MN_SWAMP))
local COILFANG_MIRE_MIXED = MixedPack("Coilfang Mire (TBC + Midnight)", COILFANG_MIRE, Native("Mlurkkr Mire (Midnight)", MN_MIRE))
local AMANI_CATACOMBS_MIXED = MixedPack("Amani Catacombs (TBC + Midnight)", AMANI_CATACOMBS, Native("Twilight's Blade (Midnight)", MN_TWILIGHT))

-- ------------------------------------------------------------
-- Optional packs: later troll music, for manual assignment
-- ------------------------------------------------------------

local ZULGURUB_CATA = Pack {
    label = "Zul'Gurub (Cataclysm)",
    intro = T.CATA_ZG_TheCoilUU01,
    any = Family("CATA_ZG_", "TheCoilUU02 TempleBethekkUU01 TempleBethekkUU02 BethekkUU01 BethekkUU02 AltarBloodGodUU01 AltarBloodGodUU02 AltarBloodGodUU03 CacheOfMadnessUU01 CacheOfMadnessUU02 MandokirUU01 MandokirUU02"),
}

local GURUBASHI_CATA = Pack {
    label = "Gurubashi (Cataclysm)",
    any = Merge(Family("CATA_StranglethornValeGU", "01 02 03 04"), Family("CATA_StranglethornGU", "01 02 03 04")),
}

local DARKSPEAR_STRAND_CATA = Pack {
    label = "Darkspear Strand (Cataclysm)",
    any = Family("CATA_Durotar", "AGU01 AGU02 AGU03 BGU01 BGU02 BGU03 BGU04 CGU01 CGU02 CGU03 CGU04 DGU01 DGU02"),
}

local ZANDALARI_MOP = Pack {
    label = "Zandalari (Pandaria)",
    intro = T.MOP_ZandalariProphecy01,
    any = Merge(
        Family("MOP_Zandalari1", "A01 A02 A03 B01 B02 B03 C01 C02"),
        Family("MOP_Zandalari2", "A01 A02 A03 A04 A05 B01 B02 B03 C01 C02 C03"),
        Family("MOP_ThunderIsle", "A01 A02 A03 A04 A05 A06 A07 B01 B02 B03 B04 B05 C01 C02 C03 C04"),
        Family("MOP_TrollBattle", "A01 A02 A03 B01 B02 B03")
    ),
}

local ZULDAZAR = Pack {
    label = "Zuldazar (BfA)",
    intro = T.BFA_ZuldazarIntroA,
    any = Merge(
        Family("BFA_ZuldazarJungle", "A B C D E F G H I J K L M N O P Q R S"),
        Family("BFA_Zuldazar", "1A 1B 1H 2A 2B 2C 2H"),
        Family("BFA_ZandalariLament", "A B H"),
        Family("BFA_ZuldazarBazaar", "1H 2H"),
        { T.BFA_ZuldazarDrum, T.BFA_ZuldazarIntroB, T.BFA_ZuldazarIntroH },
        Family("BFA_ZandalariTroll", "1A 1B 1C 2A 2B 2C 3A 3B 3C 4A 4B 4C"),
        Family("BFA_ZandalarForever", "A B C D E F G H I J")
    ),
}

local ATALDAZAR = Pack {
    label = "Atal'Dazar (BfA)",
    any = Merge(Family("BFA_AtalDazar", "A B C D H"), Family("BFA_CityOfGold", "A B H")),
}

local LOA_OF_ZANDALAR = Pack {
    label = "Loa of Zandalar (BfA)",
    intro = T.BFA_LoaMainThemeA,
    any = Merge(
        Family("BFA_LoaMainTheme", "D H"),
        Family("BFA_LoaAkunda", "A B C H"),
        Family("BFA_LoaBwonsamdi", "C D H"),
        Family("BFA_LoaPaku", "A D"),
        Family("BFA_LoaShadra", "D H")
    ),
}

local NAZMIR = Pack {
    label = "Nazmir (BfA)",
    any = Merge(
        Family("BFA_NazmirSwamp", "A B C D E F H"),
        Family("BFA_BloodMagic", "A B C D E H"),
        Family("BFA_BloodSacrifice", "A B C D H"),
        Family("BFA_NazmirVoid", "A B C H")
    ),
}

local VOLDUN = Pack {
    label = "Vol'dun / Sethraliss (BfA)",
    any = Merge(
        Family("BFA_Voldun", "A B C D E H"),
        Family("BFA_Sethrak", "1A 1H 2A 2H"),
        Family("BFA_HeartOfSethraliss", "1A 1H 2A 2H")
    ),
}

local NAGA = Pack {
    label = "Naga Incursion (BfA)",
    any = Family("BFA_NagaIncursion", "A B C H"),
}

ns.MusicPacks = {
    AMANI = AMANI,
    AMANI_MIXED = AMANI_MIXED,
    AMANI_TEMPLE = AMANI_TEMPLE,
    AMANI_TEMPLE_MIXED = AMANI_TEMPLE_MIXED,
    DARKSPEAR = DARKSPEAR,
    DARKSPEAR_MIXED = DARKSPEAR_MIXED,
    ZULFARRAK = ZULFARRAK,
    JUNGLE = JUNGLE,
    JUNGLE_MIXED = JUNGLE_MIXED,
    SHRINE_HALAZZI = SHRINE_HALAZZI,
    SHRINE_HALAZZI_MIXED = SHRINE_HALAZZI_MIXED,
    SHRINE_NALORAKK = SHRINE_NALORAKK,
    SHRINE_NALORAKK_MIXED = SHRINE_NALORAKK_MIXED,
    SHRINE_AKILZON = SHRINE_AKILZON,
    SHRINE_AKILZON_MIXED = SHRINE_AKILZON_MIXED,
    SHRINE_JANALAI = SHRINE_JANALAI,
    SHRINE_JANALAI_MIXED = SHRINE_JANALAI_MIXED,
    DRAKKARI = DRAKKARI,
    DRAKKARI_MIXED = DRAKKARI_MIXED,
    SERPENT = SERPENT,
    SERPENT_MIXED = SERPENT_MIXED,
    ZANGARMARSH = ZANGARMARSH,
    ZANGARMARSH_MIXED = ZANGARMARSH_MIXED,
    COILFANG_MIRE = COILFANG_MIRE,
    COILFANG_MIRE_MIXED = COILFANG_MIRE_MIXED,
    AMANI_CATACOMBS = AMANI_CATACOMBS,
    AMANI_CATACOMBS_MIXED = AMANI_CATACOMBS_MIXED,
    ZULGURUB_CATA = ZULGURUB_CATA,
    GURUBASHI_CATA = GURUBASHI_CATA,
    DARKSPEAR_STRAND_CATA = DARKSPEAR_STRAND_CATA,
    ZANDALARI_MOP = ZANDALARI_MOP,
    ZULDAZAR = ZULDAZAR,
    ATALDAZAR = ATALDAZAR,
    LOA_OF_ZANDALAR = LOA_OF_ZANDALAR,
    NAZMIR = NAZMIR,
    VOLDUN = VOLDUN,
    NAGA = NAGA,
}
