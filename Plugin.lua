local _, ns = ...

local api = _G.EchoesOfAzeroth
local Dsl = api and api.PluginDsl
if not Dsl then
    error("EchoesOfAzeroth core must load before EchoesOfAzeroth_ZulAman")
end

Dsl.registerPlugin({
    id = "zulaman",
    title = "Zul'Aman",
    description = "Amani and broader troll music for Zul'Aman.",
    order = 20,
    category = "Eastern Kingdoms",
    tracks = ns.Tracks,
    durations = ns.TrackDurations,
    packs = ns.MusicPacks,
    zones = ns.ZoneMusic,
    locales = ns.L,
    subzoneNames = ns.SubzoneNames,
    subzoneKeys = ns.SubzoneKeys,
})
