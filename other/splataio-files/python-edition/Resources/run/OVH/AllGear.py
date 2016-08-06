"""
Credit to H0neyBadger
Gives you all gear except for level-exclusive/amiibo-exclusive gear and the Splatfest Tee (Splatoon 2.8.0, OVH Gecko)
Uncomment those lines if you want them but be careful
Splatfest Tee will probably ban you outside of Splatfest

Damage Up               0x00000000
Defense Up              0x00000001
Ink Saver Main          0x00000002
Ink Saver Sub           0x00000003
Ink Recovery Up         0x00000004
Run Speed Up            0x00000005
Swim Speed Up           0x00000006
Special Charge Up       0x00000007
Special Duration Up     0x00000008
Quick Respawn           0x00000009
Special Saver           0x0000000A
Quick Super Jump        0x0000000B
Bomb Range Up           0x0000000C
"""

hats = {    
    #object ID : sub 1        sub 2       sub 3      ,   Brand          Main Ability        en_NA                   en_EU
    0x00000001 : [0x00000000, 0x00000000, 0x00000000], # SquidForce        Ink Recovery Up     White Headband          White Headband
    0x000003e8 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Bomb Range Up       Urchins Cap             Urchins Cap
    0x000003e9 : [0x00000001, 0x00000001, 0x00000001], # Inkline   Swim Speed Up       Lightweight Cap         Lightweight Cap
    0x000003ea : [0x00000007, 0x00000007, 0x00000007], # Takoroka  Defense Up          Takoroka Mesh           Takoroka Mesh
    0x000003eb : [0x00000009, 0x00000009, 0x00000009], # Skalop            Ink Saver (Sub)     Streetstyle Cap         Fashion Cap
    0x000003ec : [0x00000009, 0x00000009, 0x00000009], # Skalop            Opening Gambit      Squid-Stitch Cap        Squid-Stitch Cap
    0x000003ed : [0x00000009, 0x00000009, 0x00000009], # Skalop            Special Charge Up   Squidvader Cap          Squidvader Cap
    0x000003ee : [0x00000003, 0x00000003, 0x00000003], # Firefin   Swim Speed Up       Camo Mesh               Camo Mesh Cap
    0x000003ef : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Comeback            Five-Panel Cap          5-Panel Cap
    0x000003f0 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Quick Super Jump    Zekko Mesh              Zekko Mesh
    0x000003f1 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Quick Respawn       Backwards Cap           Backwards Cap
    0x000003f2 : [0x00000006, 0x00000006, 0x00000006], # Krak-On   Special Saver       Two-Stripe Mesh         2-Stripe Mesh Cap
    0x000003f3 : [0x00000003, 0x00000003, 0x00000003], # Firefin   Special Saver       Jet Cap                 Jet Cap
    0x000003f4 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink              Bomb Range Up       Cycling Cap             Cycling Cap
    0x000003f6 : [0x00000004, 0x00000004, 0x00000004], # Tentatek  Defense Up          Cycle King Cap          Cycle King Cap
    0x000007d0 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob        Quick Super Jump    Bobble Hat              Bobble Hat
    0x000007d1 : [0x00000001, 0x00000001, 0x00000001], # Inkline   Ink Saver (Main)    Short Beanie            Short Beanie
    0x000007d2 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob        Opening Gambit      Striped Beanie          Striped Beanie
    0x000007d3 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Tenacity            Sporty Bobble Hat       Sporty Bobble Hat
    0x000007d4 : [0x00000008, 0x00000008, 0x00000008], # Forge             Opening Gambit      Special Forces Beret    Special Forces Beret
    0x000007d5 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Comeback            Squid Nordic            Squid Nordic
    0x00000bb8 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob        Quick Respawn       Retro Specs             Retro Specs
    0x00000bb9 : [0x00000008, 0x00000008, 0x00000008], # Forge             Defense Up          Splash Goggles          Splash Goggles
    0x00000bba : [0x00000008, 0x00000008, 0x00000008], # Forge             Bomb Range Up       Pilot Goggles           Pilot Goggles
    0x00000bbb : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Last-Ditch Effort   Tinted Shades           Coloured Shades
    0x00000bbc : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Tenacity            Black Arrowbands        Black Arrowbands
    0x00000bbd : [0x00000008, 0x00000008, 0x00000008], # Forge             Damage Up           Snorkel Mask            Snorkel
    0x00000bbe : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Special Duration Up White Arrowbands        White Arrowbands
    0x00000bbf : [0x00000004, 0x00000004, 0x00000004], # Tentatek  Special Charge Up   Fake Contacts           Fake Contacts
    0x00000bc0 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg        Last-Ditch Effort   18K Aviators            18K Aviators
    0x00000bc1 : [0x00000006, 0x00000006, 0x00000006], # Krak-On   Quick Super Jump    Full Moon Glasses       Full Moon Glasses
    0x00000bc2 : [0x00000003, 0x00000003, 0x00000003], # Firefin   Last-Ditch Effort   Octoglasses             Octoglasses
    0x00000fa0 : [0x00000008, 0x00000008, 0x00000008], # Forge             Last-Ditch Effort   Safari Hat              Jungle Hat
    0x00000fa1 : [0x00000003, 0x00000003, 0x00000003], # Firefin   Ink Saver (Main)    Jungle Hat              Safari Hat
    0x00000fa2 : [0x00000001, 0x00000001, 0x00000001], # Inkline   Special Duration Up Camping Hat             Camping Hat
    0x00000fa3 : [0x00000003, 0x00000003, 0x00000003], # Firefin   Ink Recovery Up     Blowfish Bell Hat       Fugu Bell Hat
    0x00000fa4 : [0x00000001, 0x00000001, 0x00000001], # Inkline   Ink Saver (Main)    Bamboo Hat              Bamboo Hat
    0x00000fa5 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Quick Super Jump    Straw Boater            Straw Boater
    0x00000fa6 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Special Duration Up Classic Straw Boater    Classic Straw Boater
    0x00000fa7 : [0x00000008, 0x00000008, 0x00000008], # Forge             Ink Recovery Up     Treasure Hunter         Treasure Hunter
    0x00001388 : [0x00000008, 0x00000008, 0x00000008], # Forge             Ink Saver (Main)    Studio Headphones       Studio Headphones
    0x00001389 : [0x00000008, 0x00000008, 0x00000008], # Forge             Ink Saver (Sub)     Designer Headphones     Colourful Headphones
    0x0000138a : [0x00000008, 0x00000008, 0x00000008], # Forge             Quick Respawn       Noise Cancelers         Noise Cancellers
    0x00001770 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink              Run Speed Up        Golf Visor              Golf Visor
    0x00001771 : [0x00000003, 0x00000003, 0x00000003], # Firefin   Special Charge Up   FishFry Visor           FishFry Visor
    0x00001772 : [0x00000004, 0x00000004, 0x00000004], # Tentatek  Bomb Range Up       Sun Visor               Sun Visor
    0x00001b58 : [0x00000009, 0x00000009, 0x00000009], # Skalop            Ink Recovery Up     Bike Helmet             Cycle Helmet
    0x00001b5a : [0x00000008, 0x00000008, 0x00000008], # Forge             Swim Speed Up       Stealth Goggles         Stealth Goggles
    0x00001b5b : [0x00000008, 0x00000008, 0x00000008], # Forge             Run Speed Up        Tentacles Helmet        Tentacles Helmet
    0x00001b5c : [0x00000009, 0x00000009, 0x00000009], # Skalop            Special Saver       Skate Helmet            Skate Helmet
    0x00001b5d : [0x00000009, 0x00000009, 0x00000009], # Skalop            Last-Ditch Effort   Visor Skate Helmet      Visor Skate Helmet
    0x00001f40 : [0x00000008, 0x00000008, 0x00000008], # Forge             Tenacity            Gas Mask                Gas Mask
    0x00001f41 : [0x00000008, 0x00000008, 0x00000008], # Forge             Comeback            Paintball Mask          Paintball Mask
    0x00001f42 : [0x00000006, 0x00000006, 0x00000006], # Krak-On   Ink Saver (Sub)     Paisley Bandana         Paisley Bandana
    0x00001f43 : [0x00000008, 0x00000008, 0x00000008], # Forge             Special Saver       Skull Bandana           Skull Bandana
    0x00002329 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink              Opening Gambit      B-ball Headband         B-Ball Headband
    0x0000232a : [0x0000000B, 0x0000000B, 0x0000000B], # Zink              Damage Up           Squash Headband         Squash Headband
    0x0000232b : [0x00000004, 0x00000004, 0x00000004], # Tentatek  Comeback            Tennis Headband         Tennis Headband
    0x0000232c : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko             Ink Saver (Sub)     Jogging Headband        Jogging Headband
    0x0000232d : [0x00000004, 0x00000004, 0x00000004], # Tentatek  Tenacity            Soccer Headband         Football Headband
    0x000003f5 : [0x00000005, 0x00000006, 0x0000000C], # The SQUID GIRL    Opening Gambit      SQUID GIRL Hat          SQUID GIRL Hat
    0x0000232e : [0x0000000A, 0x0000000C, 0x00000003], # Famitsu   Comeback            Traditional Headband    Traditional Headband
    0x000061a8 : [0x00000006, 0x00000004, 0x00000005], # amiibo            Swim Speed Up       Squid Hairclip          Squid Hairclip
    0x000061a9 : [0x00000000, 0x00000001, 0x00000005], # amiibo            Damage Up           Samurai Helmet          Samurai Helmet
    0x000061aa : [0x00000001, 0x00000001, 0x0000000B], # amiibo            Defense Up          Power Mask              Power Mask
    0x00006978 : [0x00000002, 0x00000005, 0x00000006], # Cuttlegear        Run Speed Up        Hero Headset Replica    Hero Headset Replica
    #0x0000697c : [0x00000007, 0x00000007, 0x00000008], # Cuttlegear        Tenacity            Armor Helmet Replica    Armour Helmet Replica
    0x00006d60 : [0x0000000C, 0x0000000C, 0x00000003], # Cuttlegear        Bomb Range Up       Octoling Goggles        Octoling Scope
    #0x000003f7 : [0x00000000, 0x00000001, 0x00000005], # Cuttlegear        Damage Up           Legendary Cap           Legendary Cap
    0x000003f8 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Damage Up           CoroCoro Cap            CoroCoro Cap
}
clothes = {
    0x00000001 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Quick Respawn       Basic Tee             Basic Tee    
    0x000003e8 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Ink Saver (Sub)     White Tee             White Tee    
    0x000003e9 : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Run Speed Up        Black Squideye        Black Squideye    
    0x000003eb : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Cold Blooded        Sky-Blue Squideye     Sky Blue Squideye    
    0x000003ec : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Ink Recovery Up     Rockenberg White      Rockenberg White    
    0x000003ed : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Damage Up           Rockenberg Black      Rockenberg Black    
    0x000003ee : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Special Duration Up Black Tee             Black Tee    
    0x000003ef : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Special Charge Up   Sunny-Day Tee         Sunny Day Tee    
    0x000003f0 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Ink Saver (Main)    Rainy-Day Tee         Rainy Day Tee    
    0x000003f1 : [0x00000009, 0x00000009, 0x00000009], # Skalop         Special Saver       Reggae Tee            Reggae Tee    
    0x000003f2 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Swim Speed Up       Fugu Tee              Fugu Tee    
    0x000003f3 : [0x00000009, 0x00000009, 0x00000009], # Skalop         Defense Up          Mint Tee              Mint Tee    
    0x000003f4 : [0x00000009, 0x00000009, 0x00000009], # Skalop         Ink Recovery Up     Grape Tee             Grape Tee    
    0x000003f5 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Ink Saver (Main)    Red Vector Tee        Red Vector Tee    
    0x000003f6 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Quick Super Jump    Gray Vector Tee       Grey Vector Tee    
    0x000003f7 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Ink Saver (Sub)     Blue Peaks Tee        Blue Peaks Tee    
    0x000003f8 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Haunt               Ivory Peaks Tee       Ivory Peaks Tee    
    0x000003f9 : [0x00000009, 0x00000009, 0x00000009], # Skalop         Swim Speed Up       Squid-Stitch Tee      Squid-Stitch Tee    
    0x000003fa : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Special Duration Up Pirate-Stripe Tee     Pirate Stripes Tee    
    0x000003fb : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Run Speed Up        Sailor-Stripe Tee     Sailor Stripes Tee    
    0x000003fc : [0x00000003, 0x00000003, 0x00000003], # Firefin        Recon               White 8-Bit FishFry   White 8-Bit FishFry    
    0x000003fd : [0x00000003, 0x00000003, 0x00000003], # Firefin        Defense Up          Black 8-Bit FishFry   Black 8-Bit FishFry    
    0x000003fe : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Ninja Squid         White Anchor Tee      White Anchor Tee    
    0x000003ff : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Recon               Black Anchor Tee      Black Anchor Tee    
    0x00000402 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Defense Up          Carnivore Tee         Carnivore Tee    
    0x00000403 : [0x00000009, 0x00000009, 0x00000009], # Skalop         Ink Saver (Sub)     Pearl Tee             Pearl Tee    
    0x00000405 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Ninja Squid         Herbivore Tee         Herbivore Tee    
    0x000007d0 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Quick Respawn       White Striped LS      White Striped LS    
    0x000007d1 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Quick Super Jump    Black LS              Black LS    
    0x000007d2 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Bomb Range Up       Purple Camo LS        Purple Camo LS    
    0x000007d3 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Damage Up           Navy Striped LS       Navy Striped LS    
    0x000007d4 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Defense Up          Zekko Baseball LS     Zekko Baseball LS    
    0x000007d5 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Recon               Varsity Baseball LS   Varsity Baseball LS    
    0x000007d6 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Swim Speed Up       Black Baseball LS     Black Baseball LS    
    0x000007d7 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Quick Super Jump    White Baseball LS     White Baseball LS    
    0x000007d8 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Ink Recovery Up     White LS              White LS    
    0x000007d9 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Ninja Squid         Green Striped LS      Green Striped LS    
    0x000007da : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Haunt               Squidmark LS          Squidmark LS    
    0x000007db : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Special Duration Up Zink LS               Zink LS    
    0x000007dc : [0x00000001, 0x00000001, 0x00000001], # Inkline        Quick Super Jump    Striped Peaks LS      Striped Peaks LS    
    0x00000bb8 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Special Saver       White Layered LS      White Layered LS    
    0x00000bb9 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Quick Super Jump    Yellow Layered LS     Yellow Layered LS    
    0x00000bba : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Special Charge Up   Camo Layered LS       Layered Camo LS    
    0x00000bbb : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Ink Saver (Main)    Black Layered LS      Black Layered LS    
    0x00000bbc : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Damage Up           Zink Layered LS       Zink Layered LS    
    0x00000bbd : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Run Speed Up        Layered Anchor LS     Layered Anchor LS    
    0x00000bbe : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Ink Saver (Sub)     Choco Layered LS      Choco Layered LS    
    0x00000bbf : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Damage Up           Part-Time Pirate      Part-Time Pirate    
    0x00000bc0 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Special Saver       Layered Vector LS     Layered Vector LS    
    0x00000bc1 : [0x00000008, 0x00000008, 0x00000008], # Forge          Special Saver       Green Tee             Green Tee    
    0x00000fa0 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Ninja Squid         Shrimp-Pink Polo      Pink Shrimp Polo    
    0x00000fa1 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Run Speed Up        Striped Rugby         Striped Rugby    
    0x00000fa2 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Quick Respawn       Tricolor Rugby        Tricolour Rugby    
    0x00000fa3 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Cold Blooded        Sage Polo             Sage Green Polo    
    0x00000fa4 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Recon               Black Polo            Black Polo    
    0x00000fa5 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Cold Blooded        Cycling Shirt         Cycling Shirt    
    0x00000fa6 : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Defense Up          Cycle King Jersey     Cycle King Jersey    
    0x00000fa7 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Defense Up          Slipstream United     Slipstream United    
    0x00000fa8 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Damage Up           FC Albacore           FC Albacore    
    0x00001388 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Recon               Olive Ski Jacket      Olive Ski Jacket    
    0x0000138a : [0x00000001, 0x00000001, 0x00000001], # Inkline        Special Duration Up Berry Ski Jacket      Berry Ski Jacket    
    0x0000138b : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Damage Up           Varsity Jacket        Varsity Jacket    
    0x0000138c : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Ninja Squid         School Jersey         School Jersey    
    0x0000138d : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Recon               Green Cardigan        Green Cardigan    
    0x0000138e : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Bomb Range Up       Black Inky Rider      Black Inky Rider    
    0x0000138f : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Special Duration Up White Inky Rider      White Inky Rider    
    0x00001390 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Quick Respawn       Retro Gamer Jersey    Retro Gamer Jersey    
    0x00001391 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Special Charge Up   Orange Cardigan       Orange Cardigan    
    0x00001392 : [0x00000008, 0x00000008, 0x00000008], # Forge          Run Speed Up        Forge Inkling Parka   Forge Inkling Parka    
    0x00001393 : [0x00000008, 0x00000008, 0x00000008], # Forge          Haunt               Forge Octarian Jacket Forge Octarian Jacket    
    0x00001394 : [0x00000008, 0x00000008, 0x00000008], # Forge          Bomb Range Up       Blue Sailor Suit      Blue Sailor Suit    
    0x00001395 : [0x00000008, 0x00000008, 0x00000008], # Forge          Ink Saver (Main)    White Sailor Suit     White Sailor Suit    
    0x00001396 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Quick Respawn       Squid Satin Jacket    Squid Satin Jacket    
    0x00001397 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Special Charge Up   Zapfish Satin Jacket  Zapfish Satin Jacket    
    0x00001398 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Run Speed Up        Krak-On 528           Krak-On 528    
    0x00001770 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Special Saver       B-ball Jersey (Home)  B-Ball Vest (Home)    
    0x00001771 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Ink Saver (Sub)     B-ball Jersey (Away)  B-Ball Vest (Away)    
    0x00001b58 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Swim Speed Up       Gray College Sweat    Grey College Sweat    
    0x00001b59 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Bomb Range Up       Squidmark Sweat       Squidmark Sweat    
    0x00001b5a : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Defense Up          Retro Sweat           Retro Sweat    
    0x00001b5b : [0x00000003, 0x00000003, 0x00000003], # Firefin        Bomb Range Up       Firefin Navy Sweat    Firefin Sweat Navy    
    0x00001b5c : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Damage Up           Navy College Sweat    Navy College Sweat    
    0x00001b5d : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Special Duration Up Reel Sweat            Reel Sweat    
    0x00001b5e : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Cold Blooded        Anchor Sweat          Anchor Sweat    
    0x00001f40 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Ink Saver (Main)    Lumberjack Shirt      Lumberjack Shirt    
    0x00001f41 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Quick Super Jump    Rodeo Shirt           Rodeo Shirt    
    0x00001f42 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Bomb Range Up       Green-Check Shirt     Green Check Shirt    
    0x00001f43 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Ink Recovery Up     White Shirt           White Shirt    
    0x00001f44 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Run Speed Up        Urchins Jersey        Urchins Jersey    
    0x00001f45 : [0x00000008, 0x00000008, 0x00000008], # Forge          Ink Recovery Up     Aloha Shirt           Aloha Shirt    
    0x00001f46 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Ink Saver (Main)    Red-Check Shirt       Red Check Shirt    
    0x00001f47 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Defense Up          Baby-Jelly Shirt      Baby Jelly Shirt    
    0x00001f48 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Special Charge Up   Baseball Jersey       Baseball Jersey    
    0x00001f49 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Quick Super Jump    Gray Mixed Shirt      Grey Mixed Shirt    
    0x00001f4a : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Haunt               Vintage Check Shirt   Vintage Check    
    0x00001f4b : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Ink Saver (Sub)     Round-Collar Shirt    Round Collar Shirt    
    0x00001f4c : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Ink Recovery Up     Logo Aloha Shirt      Logo Aloha Shirt    
    0x00001f4d : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Quick Super Jump    Striped Shirt         Striped Shirt    
    0x00001f4e : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Bomb Range Up       Linen Shirt           Linen Shirt    
    0x00001f4f : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Special Saver       Shirt & Tie           Shirt and Tie    
    0x00002328 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Swim Speed Up       Mountain Vest         Mountain Gilet    
    0x00002329 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Ink Recovery Up     Forest Vest           Forest Gilet    
    0x0000232a : [0x00000003, 0x00000003, 0x00000003], # Firefin        Cold Blooded        Dark Urban Vest       Dark Urban Gilet    
    0x0000232b : [0x00000003, 0x00000003, 0x00000003], # Firefin        Haunt               Yellow Urban Vest     Yellow Urban Gilet    
    0x0000232c : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Special Duration Up Squid-Pattern WaistcoaSquid Pattern Waistcoat    
    0x0000232d : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Cold Blooded        Squidstar Waistcoat   Squidstar Waistcoat
    0x00002710 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Quick Respawn       Camo Zip Hoodie       Camo Zip Hoodie    
    0x00002711 : [0x00000003, 0x00000003, 0x00000003], # Firefin        Special Duration Up Green Zip Hoodie      Green Zip Hoodie    
    0x00002712 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Ninja Squid         Zekko Hoodie          Zekko Hoodie    
    0x00000400 : [0x00000006, 0x00000005, 0x00000005], # KOG            Swim Speed Up       White Line Tee        White Line Tee    
    0x00000401 : [0x0000000A, 0x0000000C, 0x00000001], # KOG            Special Saver       Black Pipe Tee        Black Pipe Tee    
    0x00001772 : [0x00000000, 0x00000005, 0x00000001], # The SQUID GIRL Damage Up           SQUID GIRL Tunic      SQUID GIRL Tunic    
    0x00001f50 : [0x00000004, 0x0000000C, 0x0000000B], # Famitsu        Quick Respawn       Traditional Apron     Traditional Apron    
    0x000061a8 : [0x0000000B, 0x0000000A, 0x0000000C], # amiibo         Ink Recovery Up     School Uniform        School Uniform    
    0x000061a9 : [0x00000007, 0x00000008, 0x00000008], # amiibo         Special Charge Up   Samurai Jacket        Samurai Jacket    
    0x000061aa : [0x00000009, 0x00000001, 0x0000000C], # amiibo         Quick Respawn       Power Armor           Power Armour    
    #0x00006590 : [0x00000000, 0x00000000, 0x00000000], # SquidForce     Special Saver       Splatfest Tee         Splatfest Tee    
    #0x00000404 : [0x0000000C, 0x0000000C, 0x00000009], # Cuttlegear     Haunt               Octo Tee              Octo Tee    
    0x00006978 : [0x0000000B, 0x0000000C, 0x0000000A], # Cuttlegear     Swim Speed Up       Hero Jacket Replica   Hero Jacket Replica    
    #0x0000697c : [0x00000008, 0x00000003, 0x00000006], # Cuttlegear     Special Charge Up   Armor Jacket Replica  Armour Jacket Replica    
    0x00006d60 : [0x0000000C, 0x00000003, 0x0000000C], # Cuttlegear     Ink Saver (Sub)     Octoling Armor        Octoling Armour
    0x00002713 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Cold Blooded        CoroCoro Hoodie         CoroCoro Hoodie
}
shoes = {
    0x00000001 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Special Saver       Cream Basics          Cream Basics
    0x000003e8 : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Defense Up          Blue Lo-Tops          Blue Lo-Tops
    0x000003e9 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Bomb Sniffer        Banana Basics         Banana Basics
    0x000003ea : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Ink Saver (Sub)     LE Lo-Tops            Ltd Edition Lo-Tops
    0x000003eb : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Ink Recovery Up     White Seahorses       White Seahorses
    0x000003ec : [0x0000000A, 0x0000000A, 0x0000000A], # Zekko          Swim Speed Up       Orange Lo-Tops        Orange Lo-Tops
    0x000003ed : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Swim Speed Up       Black Seahorses       Black Seahorses
    0x000003ee : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Special Charge Up   Clownfish Basics      Clownfish Basics
    0x000003ef : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Bomb Sniffer        Yellow Seahorses      Yellow Seahorses
    0x000003f0 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Ink Saver (Sub)     Strapping Whites      Strapping Whites
    0x000003f1 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Ink Resistance Up   Strapping Reds        Strapping Reds
    0x000003f2 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Bomb Sniffer        Soccer Cleats         Football Studs
    0x000003f3 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Ink Resistance Up   LE Soccer Cleats      LE Football Studs
    0x000007d0 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Ink Saver (Main)    Red Hi-Horses         Red Hi-Horses
    0x000007d1 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Special Charge Up   Zombie Hi-Horses      Zombie Hi-Horses
    0x000007d2 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Stealth Jump        Cream Hi-Tops         Cream Hi-Tops
    0x000007d3 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Special Duration Up Purple Hi-Horses      Purple Hi-Horses
    0x000007d4 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Ink Recovery Up     Hunter Hi-Tops        Dark Green Hi-Tops
    0x000007d5 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Ink Resistance Up   Red Hi-Tops           Red Hi-Tops
    0x000007d6 : [0x0000000B, 0x0000000B, 0x0000000B], # Zink           Run Speed Up        Gold Hi-Horses        Gold Hi-Horses
    0x000007d8 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Bomb Range Up       Shark Moccasins       Shark Moccasins
    0x000007d9 : [0x00000002, 0x00000002, 0x00000002], # Splash Mob     Ink Recovery Up     Mawcasins             Mawcasins
    0x00000bb8 : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Bomb Range Up       Pink Trainers         Pink Trainers
    0x00000bb9 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Ink Saver (Main)    Orange Arrows         Orange Arrows
    0x00000bba : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Ink Resistance Up   Neon Sea Slugs        Neon Green Sea Slugs
    0x00000bbb : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Special Duration Up White Arrows          White Arrows
    0x00000bbc : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Damage Up           Cyan Trainers         Cyan Trainers
    0x00000bbd : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Special Charge Up   Blue Sea Slugs        Blue Sea Slugs
    0x00000bbe : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Special Saver       Red Sea Slugs         Red Sea Slugs
    0x00000bbf : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Run Speed Up        Purple Sea Slugs      Purple Sea Slugs
    0x00000bc0 : [0x00000007, 0x00000007, 0x00000007], # Takoroka       Stealth Jump        Crazy Arrows          Crazy Arrows
    0x00000bc1 : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Quick Respawn       Black Trainers        Black Trainers
    0x00000fa0 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Run Speed Up        Oyster Clogs          Oyster Clogs
    0x00000fa1 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Quick Respawn       Choco Clogs           Choco Clogs
    0x00000fa2 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Ink Saver (Sub)     Blueberry Casuals     Blueberry Casuals
    0x00000fa3 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Damage Up           Plum Casuals          Plum Casuals
    0x00001388 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Ink Recovery Up     Trail Boots           Trail Boots
    0x00001389 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Special Duration Up Custom Trail Boots    Custom Trail Boots
    0x0000138a : [0x00000001, 0x00000001, 0x00000001], # Inkline        Bomb Sniffer        Pro Trail Boots       Pro Trail Boots
    0x00001770 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Quick Respawn       Moto Boots            Biker Boots
    0x00001771 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Bomb Range Up       Tan Work Boots        Tan Work Boots
    0x00001772 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Quick Super Jump    Red Work Boots        Red Work Boots
    0x00001773 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Ink Resistance Up   Blue Moto Boots       Blue Biker Boots
    0x00001774 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Stealth Jump        Green Rain Boots      Moss-Green Wellies
    0x00001775 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Run Speed Up        Acerola Rain Boots    Acerola Wellies
    0x00001776 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Special Charge Up   Punk Whites           Punk Whites
    0x00001777 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Bomb Sniffer        Punk Cherries         Punk Cherries
    0x00001778 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Special Saver       Punk Yellows          Punk Yellows
    0x00001779 : [0x00000001, 0x00000001, 0x00000001], # Inkline        Damage Up           Bubble Rain Boots     Bubble Rain Boots
    0x0000177a : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Quick Super Jump    Snowy Down Boots      Snowy Down Boots
    0x0000177b : [0x00000004, 0x00000004, 0x00000004], # Tentatek       Stealth Jump        Icy Down Boots        Icy Down Boots
    0x00001b58 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Bomb Range Up       Blue Slip-Ons         Blue Plimsolls
    0x00001b59 : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Quick Super Jump    Red Slip-Ons          Red Plimsolls
    0x00001b5a : [0x00000006, 0x00000006, 0x00000006], # Krak-On        Defense Up          Squid-Stitch Slip-Ons Squid-Stitch Plimsolls
    0x00001f40 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Swim Speed Up       White Kicks           White Kicks
    0x00001f41 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Stealth Jump        Cherry Kicks          Cherry Kicks
    0x00001f42 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Special Charge Up   Turquoise Kicks       Turquoise Kicks
    0x00001f43 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Quick Respawn       Squink Wingtips       Squid Ink Brogues
    0x00001f44 : [0x00000005, 0x00000005, 0x00000005], # Rockenberg     Defense Up          Roasted Brogues       Roasted Brogues
    0x00000fa6 : [0x00000000, 0x00000001, 0x00000007], # Famitsu        Run Speed Up        Traditional Sandals   Traditional Sandals
    0x000007d7 : [0x0000000A, 0x00000008, 0x00000007], # The SQUID GIRL Swim Speed Up       SQUID GIRL Shoes      SQUID GIRL Shoes
    0x000061a8 : [0x0000000B, 0x0000000C, 0x0000000C], # amiibo         Ink Saver (Sub)     School Shoes          School Shoes
    0x000061a9 : [0x00000007, 0x00000004, 0x00000002], # amiibo         Special Duration Up Samurai Shoes         Samurai Shoes
    0x000061aa : [0x0000000C, 0x00000007, 0x00000009], # amiibo         Ink Saver (Main)    Power Boots           Power Boots
    0x00006978 : [0x00000002, 0x00000004, 0x00000009], # Cuttlegear     Quick Super Jump    Hero Runner Replicas  Hero Runner Replicas
    #0x0000697c : [0x00000005, 0x00000003, 0x00000006], # Cuttlegear     Ink Saver (Main)    Armor Boot Replicas   Armour Boot Replicas
    0x00006d60 : [0x0000000C, 0x00000009, 0x00000007], # Cuttlegear     Special Saver       Octoling Boots        Octoling Boots
}

def poke_gear(base, oid, lvl=0x00000004, slots=0x00000004, slot1=0x000000000, slot2=0x000000001, slot3=0x000000005):
    print("{0} {1} {2} {3} {4} {5} {6}".format(base, oid, lvl, slots, slot1, slot2, slot3))
    lvl_addr = base + 0x00000004
    slots_addr = base + 0x00000008
    slot1_addr = base + 0x0000000C
    slot2_addr = base + 0x00000010
    slot3_addr = base + 0x00000014
    date_addr = base + 0x00000024
    new_addr = base + 0x00000028
    tcp.pokemem(base, oid)
    tcp.pokemem(lvl_addr, lvl)
    tcp.pokemem(slots_addr, slots)
    tcp.pokemem(slot1_addr, slot1)
    tcp.pokemem(slot2_addr, slot2)
    tcp.pokemem(slot3_addr, slot3)
    tcp.pokemem(date_addr, 0x00000000)
    tcp.pokemem(new_addr, 0x00010000)

addresses = (
    {'base':0x12CD1DA0 + diff, 'object_ids': shoes},
    {'base':0x12CD4DA0 + diff, 'object_ids': clothes},
    {'base':0x12CD7DA0 + diff, 'object_ids': hats},
)


tcp = TCPGecko(ip)

# money_addr = 0x12CDB1A0
# tcp.pokemem(money_addr, 0x005D1420)
# snails_addr = 0x12CDB1B4
# tcp.pokemem(snails_addr, 0x00000000)

for obj in addresses:
    base = obj['base']
    oids = obj['object_ids'].keys()
    # Sort the keys so that the starter gear appears in first slot
    oids.sort()
    for oid in oids:
        abilities = obj['object_ids'][oid]
        poke_gear(base, oid, 4, 4, abilities[0], abilities[1], abilities[2])
        base = base + 0x00000030
    
tcp.s.close()
print("Done.")
