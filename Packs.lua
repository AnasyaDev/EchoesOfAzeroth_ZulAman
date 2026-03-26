local _, ns = ...
local T = ns.Tracks

local function MergeUnique(...)
    local out = {}
    local seen = {}
    for i = 1, select("#", ...) do
        local list = select(i, ...)
        if list then
            for _, track in ipairs(list) do
                if track and not seen[track] then
                    seen[track] = true
                    out[#out + 1] = track
                end
            end
        end
    end
    return out
end

local ZULAMAN_TBC_TRACKS = {
    T.ZA_WalkUni01,
    T.ZA_WalkUni02,
    T.ZA_WalkUni03,
    T.ZA_WalkUni04,
    T.ZA_WalkUni05,
    T.ZA_WalkUni06,
}

local ZULAMAN_MIDNIGHT_TRACKS = {
    T.MN_ZulAmanA,
    T.MN_ZulAmanB,
    T.MN_ZulAmanC,
    T.MN_ZulAmanD,
    T.MN_ZulAmanE,
    T.MN_ZulAmanF,
    T.MN_ZulAmanG,
    T.MN_ZulAmanH,
    T.MN_AmanizarVillageA,
    T.MN_AmanizarVillageB,
    T.MN_AmanizarVillageC,
    T.MN_AmanizarVillageD,
    T.MN_AmanizarVillageE,
    T.MN_AmanizarVillageH,
}

local AMANI_TRACKS = MergeUnique(
    ZULAMAN_TBC_TRACKS,
    ZULAMAN_MIDNIGHT_TRACKS,
    {
        T.MN_AtalAmanA,
        T.MN_AtalAmanB,
        T.MN_AtalAmanC,
        T.MN_AtalAmanD,
        T.MN_AtalAmanE,
        T.MN_AtalAmanH,
    }
)

local DARKSPEAR_TRACKS = {
    T.DU_GeneralA01,
    T.DU_GeneralA02,
    T.DU_GeneralA03,
    T.DU_GeneralB01,
    T.DU_GeneralB02,
    T.DU_GeneralB03,
    T.DU_GeneralB04,
    T.DU_GeneralC01,
    T.DU_GeneralC02,
    T.DU_GeneralC03,
    T.DU_GeneralC04,
    T.DU_GeneralD01,
    T.DU_GeneralD02,
    T.MN_DenOfEchoesA,
    T.MN_DenOfEchoesB,
    T.MN_DenOfEchoesC,
    T.MN_DenOfEchoesD,
    T.MN_DenOfEchoesH,
}

local GURUBASHI_TRACKS = {
    T.STV_GurubashiVale01,
    T.STV_GurubashiVale02,
    T.STV_GurubashiVale03,
    T.STV_GurubashiVale04,
    T.STV_Gurubashi01,
    T.STV_Gurubashi02,
    T.STV_Gurubashi03,
    T.STV_Gurubashi04,
}

local SANDFURY_TRACKS = {
    T.TA_General01,
    T.TA_General02,
    T.TA_General03,
    T.TA_General04,
    T.TA_General05,
    T.TA_General06,
    T.TA_General07,
    T.TA_General08,
    T.TA_General09,
    T.TA_General10,
    T.DE_Day01,
    T.DE_Day02,
    T.DE_Day03,
    T.DE_Night01,
    T.DE_Night02,
    T.DE_Night03,
}

local DRAKKARI_DAY_TRACKS = {
    T.ZD_GeneralWalkDay01,
    T.ZD_GeneralWalkDay02,
    T.ZD_GeneralWalkDay03,
    T.ZD_GeneralWalkDay04,
}

local DRAKKARI_NIGHT_TRACKS = {
    T.ZD_GeneralWalkNight01,
    T.ZD_GeneralWalkNight02,
    T.ZD_GeneralWalkNight03,
    T.ZD_GeneralWalkNight04,
}

local DRAKKARI_ANY_TRACKS = {
    T.NR_TrollGeneral01,
    T.NR_TrollGeneral02,
    T.NR_TrollGeneral03,
    T.NR_TrollGeneral04,
    T.ZD_HarkoaIntro01,
    T.ZD_MamtothIntro01,
    T.ZD_QuetzlunIntro01,
    T.ZD_RhunokIntro01,
    T.ZD_SseratusIntro01,
}

local DRAKKARI_TRACKS = MergeUnique(
    DRAKKARI_DAY_TRACKS,
    DRAKKARI_NIGHT_TRACKS,
    DRAKKARI_ANY_TRACKS
)

local ZANDALARI_TRACKS = {
    T.MOP_Zandalari1A01,
    T.MOP_Zandalari1A02,
    T.MOP_Zandalari1A03,
    T.MOP_Zandalari1B01,
    T.MOP_Zandalari1B02,
    T.MOP_Zandalari1B03,
    T.MOP_Zandalari1C01,
    T.MOP_Zandalari1C02,
    T.MOP_Zandalari2A01,
    T.MOP_Zandalari2A02,
    T.MOP_Zandalari2A03,
    T.MOP_Zandalari2A04,
    T.MOP_Zandalari2A05,
    T.MOP_Zandalari2B01,
    T.MOP_Zandalari2B02,
    T.MOP_Zandalari2B03,
    T.MOP_Zandalari2C01,
    T.MOP_Zandalari2C02,
    T.MOP_Zandalari2C03,
    T.MOP_ThunderIsleA01,
    T.MOP_ThunderIsleA02,
    T.MOP_ThunderIsleA03,
    T.MOP_ThunderIsleA04,
    T.MOP_ThunderIsleA05,
    T.MOP_ThunderIsleA06,
    T.MOP_ThunderIsleA07,
    T.MOP_ThunderIsleB01,
    T.MOP_ThunderIsleB02,
    T.MOP_ThunderIsleB03,
    T.MOP_ThunderIsleB04,
    T.MOP_ThunderIsleB05,
    T.MOP_ThunderIsleC01,
    T.MOP_ThunderIsleC02,
    T.MOP_ThunderIsleC03,
    T.MOP_ThunderIsleC04,
}

local ZANDALARI_BFA_TRACKS = {
    T.BFA_ZandalariLamentA,
    T.BFA_ZandalariLamentB,
    T.BFA_ZandalariLamentH,
    T.BFA_ZuldazarIntroA,
    T.BFA_ZuldazarIntroB,
    T.BFA_ZuldazarIntroH,
    T.BFA_Zuldazar1A,
    T.BFA_Zuldazar1B,
    T.BFA_Zuldazar1H,
    T.BFA_Zuldazar2A,
    T.BFA_Zuldazar2B,
    T.BFA_Zuldazar2C,
    T.BFA_Zuldazar2H,
    T.BFA_ZuldazarDrum,
    T.BFA_ZuldazarJungleA,
    T.BFA_ZuldazarJungleB,
    T.BFA_ZuldazarJungleC,
    T.BFA_ZuldazarJungleD,
    T.BFA_ZuldazarJungleE,
    T.BFA_ZuldazarJungleF,
    T.BFA_ZuldazarJungleG,
    T.BFA_ZuldazarJungleH,
    T.BFA_ZuldazarJungleI,
    T.BFA_ZuldazarJungleJ,
    T.BFA_ZuldazarJungleK,
    T.BFA_ZuldazarJungleL,
    T.BFA_ZuldazarJungleM,
    T.BFA_ZuldazarJungleN,
    T.BFA_ZuldazarJungleO,
    T.BFA_ZuldazarJungleP,
    T.BFA_ZuldazarJungleQ,
    T.BFA_ZuldazarJungleR,
    T.BFA_ZuldazarJungleS,
    T.BFA_AtalDazarA,
    T.BFA_AtalDazarB,
    T.BFA_AtalDazarC,
    T.BFA_AtalDazarD,
    T.BFA_AtalDazarH,
    T.BFA_ZandalarForeverA,
    T.BFA_ZandalarForeverB,
    T.BFA_ZandalarForeverC,
    T.BFA_ZandalarForeverD,
    T.BFA_ZandalarForeverE,
    T.BFA_ZandalarForeverF,
    T.BFA_ZandalarForeverG,
    T.BFA_ZandalarForeverH,
    T.BFA_ZandalarForeverI,
    T.BFA_ZandalarForeverJ,
    T.BFA_ZandalariTroll1A,
    T.BFA_ZandalariTroll1B,
    T.BFA_ZandalariTroll1C,
    T.BFA_ZandalariTroll2A,
    T.BFA_ZandalariTroll2B,
    T.BFA_ZandalariTroll2C,
    T.BFA_ZandalariTroll3A,
    T.BFA_ZandalariTroll3B,
    T.BFA_ZandalariTroll3C,
    T.BFA_ZandalariTroll4A,
    T.BFA_ZandalariTroll4B,
    T.BFA_ZandalariTroll4C,
}

local ATALAI_TRACKS = {
    T.MN_AtalAbasiA,
    T.MN_AtalAbasiB,
    T.MN_AtalAbasiC,
    T.MN_AtalAbasiD,
    T.MN_AtalAbasiE,
    T.MN_AtalAbasiF,
    T.MN_AtalAbasiH,
}

-- ============================================================
-- Music Packs
--
-- This plugin stays centered on Zul'Aman, but also ships
-- additional troll-flavored packs the player can assign manually.
-- ============================================================

ns.MusicPacks = {
    ZULAMAN = {
        label = "Zul'Aman (TBC)",
        any = ZULAMAN_TBC_TRACKS,
    },

    ZULAMAN_MIDNIGHT = {
        label = "Zul'Aman (Midnight)",
        any = ZULAMAN_MIDNIGHT_TRACKS,
    },

    ZULAMAN_MIXED = {
        label = "Zul'Aman (TBC + Midnight)",
        any = MergeUnique(ZULAMAN_TBC_TRACKS, ZULAMAN_MIDNIGHT_TRACKS),
    },

    AMANI = {
        label = "Amani",
        any = AMANI_TRACKS,
    },

    DARKSPEAR = {
        label = "Darkspear",
        any = DARKSPEAR_TRACKS,
    },

    DRAKKARI = {
        label = "Drakkari (Northrend)",
        intro = T.ZD_GeneralIntro01,
        day = DRAKKARI_DAY_TRACKS,
        night = DRAKKARI_NIGHT_TRACKS,
        any = DRAKKARI_ANY_TRACKS,
    },

    GURUBASHI = {
        label = "Gurubashi (Stranglethorn)",
        intro = T.ZG_VoodooMoment,
        any = GURUBASHI_TRACKS,
    },

    SANDFURY = {
        label = "Sandfury (Tanaris / Zul'Farrak)",
        any = SANDFURY_TRACKS,
    },

    ZANDALARI = {
        label = "Zandalari (Pandaria)",
        intro = T.MOP_ZandalariProphecy01,
        any = ZANDALARI_TRACKS,
    },

    ZANDALARI_BFA = {
        label = "Zandalari (BFA)",
        intro = T.BFA_ZuldazarIntroA,
        any = ZANDALARI_BFA_TRACKS,
    },

    ATALAI = {
        label = "Atal'ai",
        any = ATALAI_TRACKS,
    },

    TROLL_MIXED = {
        label = "Troll Mixed",
        any = MergeUnique(
            AMANI_TRACKS,
            DARKSPEAR_TRACKS,
            GURUBASHI_TRACKS,
            SANDFURY_TRACKS,
            DRAKKARI_TRACKS,
            ZANDALARI_TRACKS,
            ZANDALARI_BFA_TRACKS,
            ATALAI_TRACKS,
            {
                T.MN_AtalAmanA,
                T.MN_AtalAmanB,
                T.MN_AtalAmanC,
                T.MN_AtalAmanD,
                T.MN_AtalAmanE,
                T.MN_AtalAmanH,
            }
        ),
    },
}

ns.MusicPackOrder = {
    "ZULAMAN",
    "ZULAMAN_MIDNIGHT",
    "ZULAMAN_MIXED",
    "AMANI",
    "DARKSPEAR",
    "DRAKKARI",
    "GURUBASHI",
    "SANDFURY",
    "ZANDALARI",
    "ZANDALARI_BFA",
    "ATALAI",
    "TROLL_MIXED",
}
