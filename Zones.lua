local _, ns = ...
local api = _G.EchoesOfAzeroth
local Dsl = api and api.PluginDsl
if not Dsl then
    error("EchoesOfAzeroth core must load before EchoesOfAzeroth_ZulAman")
end

-- ============================================================
-- Zone -> music-pack mapping (Midnight UiMapIDs)
--
-- Open world only: Zul'Aman (2437), The Coiled Isle (2512) and the
-- Vaults of Atal'Utek (2509, an open-world map), plus two open
-- sub-maps to confirm in-game (2536 Atal'Aman, 2633 The Ring of
-- Glory).  Dungeons, the raid, the lair and the delves keep their
-- native music.  Sub-areas without a ZoneMusic of their own in the
-- game data inherit the zone pack and are not listed.
--
-- Discover zone / subzone info in-game:  /eoa now
-- ============================================================

ns.ZoneMusic = {
    -- Zul'Aman (2437), child of Quel'Thalas (2537)
    [2437] = Dsl.zone("ZULAMAN", "AMANI", {
        -- villages
        AMANI_ZAR_VILLAGE   = "DARKSPEAR",
        WITHERBARK_BLUFFS   = "DARKSPEAR",
        TORNTUSK_OVERLOOK   = "DARKSPEAR",
        -- loa shrines <-> Zul'Drak altars
        TEMPLE_OF_AKILZON   = "SHRINE_AKILZON",
        AKILZONS_REACH      = "SHRINE_AKILZON",
        TEMPLE_OF_JANALAI   = "SHRINE_JANALAI",
        TEMPLE_OF_HALAZZI   = "SHRINE_HALAZZI",
        SPIRITPAW_BOROUGH   = "SHRINE_NALORAKK",
        NALORAKKS_PROWL     = "SHRINE_NALORAKK",
        SPIRITPAW_BACKWOODS = "SHRINE_NALORAKK",
        -- Twilight's Blade occupation
        SPEAKERS_REST       = "AMANI_CATACOMBS",
        BROKEN_THRONE       = "AMANI_CATACOMBS",
        REVANTUSK_SEDGE     = "AMANI_CATACOMBS",
        -- Atal'Aman, the temple city
        ATAL_AMAN           = "AMANI_TEMPLE",
        TALONSTRIKE_TERRACE = "AMANI_TEMPLE",
        SWIFTCLAW_TERRACE   = "AMANI_TEMPLE",
        RAGEMAW_TERRACE     = "AMANI_TEMPLE",
        FIREWING_TERRACE    = "AMANI_TEMPLE",
        WARLORDS_STAIR      = "AMANI_TEMPLE",
        ALTAR_OF_MALACRASS  = "AMANI_TEMPLE",
        -- swamp
        ATAL_ABASI          = "ZANGARMARSH",
        LEECH_BOG           = "ZANGARMARSH",
        MAISARA_DEEPS       = "ZANGARMARSH",
        THE_SKYBRIDGE       = "ZANGARMARSH",
        HERMITS_MOORING     = "ZANGARMARSH",
        -- lumber camp
        ZEB_ALAR_LUMBERYARD = "JUNGLE",
        BITTERBARK          = "JUNGLE",
    }),

    -- Atal'Aman open sub-map (2536): confirm with /eoa now
    [2536] = Dsl.zone("ATAL_AMAN", "AMANI_TEMPLE"),

    -- The Coiled Isle (2512), child of Quel'Thalas (2537)
    [2512] = Dsl.zone("THE_COILED_ISLE", "JUNGLE", {
        -- tortollan hub (natively silent)
        TOKKAS_LANDING            = "DARKSPEAR",
        TOKKAS_FOLLY              = "DARKSPEAR",
        -- mangrove
        OFIS_HUT                  = "COILFANG_MIRE",
        MLURKKR_MIRE              = "COILFANG_MIRE",
        CLOUDLIGHT_BEACON         = "COILFANG_MIRE",
        WRECK_OF_PAKUS_TALON      = "COILFANG_MIRE",
        WRECK_OF_TORGAS_BEAK      = "COILFANG_MIRE",
        -- venom: the Children of Ula'tek
        ZAIL_ZAR_SPAN             = "SERPENT",
        GATE_OF_THE_EASTERN_FANG  = "SERPENT",
        THE_FANGS                 = "SERPENT",
        PATH_OF_WHISPERS          = "SERPENT",
        GATE_OF_THE_SERPENTS_EYE  = "SERPENT",
        VENOM_RISE                = "SERPENT",
        BLISTERING_TERRACE        = "SERPENT",
        THE_SERPENTS_TAIL         = "SERPENT",
        -- spirits
        THE_ALTAR_OF_WRATH        = "DRAKKARI",
        THE_WHISPERING_MARSH      = "DRAKKARI",
        THE_RING_OF_GLORY         = "DRAKKARI",
        DEFIANT_RING              = "DRAKKARI",
        -- crypts and tombs
        CRYPT_OF_THE_DENIED       = "AMANI_CATACOMBS",
        CRYPT_OF_THE_LOST_MASON   = "AMANI_CATACOMBS",
        KINS_REST                 = "AMANI_CATACOMBS",
        BLISTERING_VAULT          = "AMANI_CATACOMBS",
        TOMB_OF_THE_LOST_PRIEST   = "AMANI_CATACOMBS",
        CRYPT_OF_THE_LOST_WARRIOR = "AMANI_CATACOMBS",
        CRYPT_OF_THE_DISGRACED    = "AMANI_CATACOMBS",
        -- vaults entrance
        VAULTS_OF_ATAL_UTEK       = "AMANI_TEMPLE",
    }),

    -- The Ring of Glory open sub-map (2633): confirm with /eoa now
    [2633] = Dsl.zone("THE_RING_OF_GLORY", "DRAKKARI"),

    -- Vaults of Atal'Utek (2509): open-world map 2916 under the isle
    [2509] = Dsl.zone("VAULTS_OF_ATAL_UTEK", "AMANI_TEMPLE", {
        AMANI_FOOTHOLD         = "AMANI",
        NORTHERN_AMANI_BULWARK = "AMANI",
        EASTERN_AMANI_OUTPOST  = "AMANI",
    }),
}
