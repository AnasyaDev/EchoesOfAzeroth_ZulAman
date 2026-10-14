# Echoes of Azeroth: Zul'Aman

`EchoesOfAzeroth_ZulAman` is a troll-focused content plugin for `EchoesOfAzeroth`.

It replaces the music of Zul'Aman and of The Coiled Isle (Midnight) with classic-era troll music, sub-area by sub-area, and ships the later troll music of the game as optional packs.

## Requires

- `EchoesOfAzeroth`

This plugin depends on the core addon.

## Covered zones

- Zul'Aman (open world), with its villages, loa temples, temple city, swamp and lumber camp
- The Coiled Isle (open world), with the tortollan landing, the mangrove, the serpent cult grounds, the spirit marsh and the crypts
- Vaults of Atal'Utek (the open-world vaults under the isle)

Dungeons, the raid, the lair and the delves keep their native music.

## The mirror

Defaults stay in the classic era (Vanilla, The Burning Crusade, Wrath of the Lich King):

| Midnight place | Music |
|---|---|
| Zul'Aman forest | Zul'Aman raid (TBC), the set Blizzard reuses for every troll place |
| Amani'Zar Village, Witherbark Bluffs, Torntusk Overlook, Tokka's Landing | Blizzard's troll village kit (Echo Isles: Zul'Aman + Vanilla Zul'Farrak) |
| Temple of Halazzi (lynx) | Altar of Har'koa (Zul'Drak) |
| Spiritpaw, Nalorakk (bear) | Altar of Rhunok (Zul'Drak) |
| Temple of Akil'zon (eagle) | Altar of Quetz'lun (Zul'Drak) |
| Temple of Jan'alai (dragonhawk) | Altar of Mam'toth (Zul'Drak) |
| Speaker's Rest, Broken Throne, Revantusk Sedge, the isle's crypts | Amani Catacombs (Ghostlands, TBC) |
| Atal'Aman, Vaults of Atal'Utek | Zul'Aman raid, walking and battle |
| Atal'Abasi swamp | Zangarmarsh (TBC) |
| Zeb'Alar Lumberyard, The Coiled Isle forest | Stranglethorn troll jungle (Vanilla), day and night |
| Mlurkkr Mire | Coilfang marsh (TBC) |
| The Serpent's Tail, the Fangs, the gates | Zul'Gurub (Vanilla) opened by the altar of Sseratus, the serpent loa |
| Whispering Marsh, Altar of Wrath, Ring of Glory | Drakkari (Zul'Drak) |

## Included music packs

Each default pack exists as `(era)` and as `(era + Midnight)`, the latter merging the kit the game natively plays in the same places. There is no pure Midnight pack: that is what you already hear with the addon disabled.

- `Amani`, `Amani Temple`
- `Darkspear`, `Zul'Farrak`
- `Troll Jungle`
- `Shrine of Har'koa`, `Shrine of Rhunok`, `Shrine of Quetz'lun`, `Shrine of Mam'toth`
- `Drakkari`
- `Serpent Altar`
- `Zangarmarsh`, `Coilfang Mire`
- `Amani Catacombs`

Optional packs for manual assignment:

- `Zul'Gurub (Cataclysm)`, `Gurubashi (Cataclysm)`, `Darkspear Strand (Cataclysm)`
- `Zandalari (Pandaria)`
- `Zuldazar (BfA)`, `Atal'Dazar (BfA)`, `Loa of Zandalar (BfA)`, `Nazmir (BfA)`, `Vol'dun / Sethraliss (BfA)`, `Naga Incursion (BfA)`

## Source approach

- FileDataIDs come from the wowdev community listfile (build 12.1.0).
- Sub-area names come from the game's AreaTable in every client locale, so they match `GetSubZoneText()` exactly.
- Track durations were measured from the audio files so pack rotation follows real track length.
- The design notes are in `docs/PLAN.md`.

## How to use it

1. Install `EchoesOfAzeroth`
2. Install this plugin
3. Open `/eoa options`
4. Enable the plugin in `Plugins`
5. Adjust mappings in `Zone Mapping` if desired

## Notes

- The plugin provides content only
- Playback, profiles, custom packs, custom zones, and import/export live in the core addon
- Version 2.0 replaces the whole catalog: pack keys changed, so zone overrides made on version 1.x packs no longer resolve and fall back to the new defaults

## Community profiles

`EchoesOfAzeroth` is meant to grow as a community addon.

If you build a profile that feels especially polished, immersive, or lore-accurate, please share it. Great community profiles can help refine the addon over time, and an especially strong configuration may be adopted as an official default or recommended setup in the future.
