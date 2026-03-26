local _, ns = ...

local register = _G.EchoesOfAzeroth and _G.EchoesOfAzeroth.RegisterPlugin
if not register then
    error("EchoesOfAzeroth core must load before EchoesOfAzeroth_ZulAman")
end

register({
    id = "zulaman",
    title = "Zul'Aman",
    description = "Amani and broader troll music for Zul'Aman.",
    order = 20,
    category = "Eastern Kingdoms",
    tracks = ns.Tracks,
    durations = ns.TrackDurations,
    packs = ns.MusicPacks,
    packOrder = ns.MusicPackOrder,
    zones = ns.ZoneMusic,
    locales = ns.L,
    subzoneNames = ns.SubzoneNames,
    subzoneKeys = ns.SubzoneKeys,
})
