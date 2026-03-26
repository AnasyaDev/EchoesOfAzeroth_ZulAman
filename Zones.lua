local _, ns = ...

-- ============================================================
-- Zone -> music-pack mapping
--
-- Wago Tools confirms Zul'Aman music families and legacy zone data,
-- but the in-game Midnight runtime currently resolves Zul'Aman as:
-- - UiMapID 2437
-- - parent chain 2437 -> 2537 -> 13 -> 947 -> 946
--
-- This plugin intentionally only maps the Zul'Aman zone itself.
-- It does not reuse the Amani Pass mapping already owned by the
-- Quel'Thalas plugin.
-- ============================================================

ns.ZoneMusic = {
    -- Zul'Aman (UiMapID 2437 in Midnight runtime)
    [2437] = {
        nameKey = "ZULAMAN",
        pack = "ZULAMAN_MIXED",
    },
}
