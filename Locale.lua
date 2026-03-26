local _, ns = ...

-- ============================================================
-- Localization
--
-- English is the base. Add more subzones later if Zul'Aman
-- exposes stable GetSubZoneText() labels worth mapping.
-- ============================================================

local names = {
    ZULAMAN = "Zul'Aman",
}

local subzones = {}

ns.L = setmetatable(names, {
    __index = function(_, key)
        return key
    end,
})

ns.SubzoneNames = subzones
ns.SubzoneKeys = {}
for key, localizedName in pairs(subzones) do
    ns.SubzoneKeys[localizedName] = key
end
