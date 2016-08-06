

sys.argv.append("290")

tcp = TCPGecko(ip)
if sys.argv[1] == "100": #For 1.0.0-?
    tcp.writestr(0x105068F0, b"Tnk_Rvl00")
    tcp.writestr(0x1051A500, b"Tnk_Rvl00")
    tcp.writestr(0x105DBFE0, b"Rival00")
    tcp.writestr(0x105DBFEC, b"Rival00_Hlf")
    tcp.writestr(0x105DBFFC, b"Rival_Squid")
    #tcp.pokemem(0x12CB05A0, 42069)
elif sys.argv[1] == "130": #for 1.3.0
    tcp.writestr(0x105068F0, b"Tnk_Rvl00")
    tcp.writestr(0x105D4000, b"Tnk_Rvl00")
    tcp.writestr(0x105DC118, b"Rival00")
    tcp.writestr(0x105DC124, b"Rival00_Hlf")
    tcp.writestr(0x105DC134, b"Rival_Squid")
    #tcp.pokemem(0x12CB07A0, 42069)
elif sys.argv[1] == "200": #For 2.0.0
    tcp.writestr(0x10506AB0, b"Tnk_Rvl00")
    tcp.writestr(0x105E0278, b"Tnk_Rvl00")
    tcp.writestr(0x105E85B0, b"Rival00")
    tcp.writestr(0x105E85BC, b"Rival00_Hlf")
    tcp.writestr(0x105E85CC, b"Rival_Squid")
    tcp.writestr(0x12BE2350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE239C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE23E8, b"Tnk_Rvl00")
elif sys.argv[1] == "210": #For 2.1.0
    tcp.writestr(0x10506AF8, b"Tnk_Rvl00")
    tcp.writestr(0x105E0350, b"Tnk_Rvl00")
    tcp.writestr(0x105E8698, b"Rival00")
    tcp.writestr(0x105E86A4, b"Rival00_Hlf")
    tcp.writestr(0x105E86B4, b"Rival_Squid")
    tcp.writestr(0x12BE2350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE239C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE23E8, b"Tnk_Rvl00")
    tcp.pokemem(0x12CC7C80, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "220": #For 2.2.0
    tcp.writestr(0x10506AF8, b"Tnk_Rvl00")
    tcp.writestr(0x105E0350, b"Tnk_Rvl00")
    tcp.writestr(0x105EB040, b"Rival00")
    tcp.writestr(0x105EB04C, b"Rival00_Hlf")
    tcp.writestr(0x105EB05C, b"Rival_Squid")
    tcp.writestr(0x12BE5350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE539C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE53E8, b"Tnk_Rvl00")
    tcp.pokemem(0x12CCAC80, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "230": #For 2.3.0
    tcp.writestr(0x10506AF8, b"Tnk_Rvl00")
    tcp.writestr(0x105E3BB8, b"Tnk_Rvl00")
    tcp.writestr(0x105EBF98, b"Rival00")
    tcp.writestr(0x105EBFA4, b"Rival00_Hlf")
    tcp.writestr(0x105EBFB4, b"Rival_Squid")
    tcp.writestr(0x12BE6350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE639C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE63E8, b"Tnk_Rvl00")
    tcp.pokemem(0x12CCBB90, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "240": #For 2.4.0
    tcp.writestr(0x10506AF8, b"Tnk_Rvl00")
    tcp.writestr(0x105E4EA0, b"Tnk_Rvl00")
    tcp.writestr(0x105ED7B8, b"Rival00")
    tcp.writestr(0x105ED7C4, b"Rival00_Hlf")
    tcp.writestr(0x105ED7D4, b"Rival_Squid")
    tcp.writestr(0x12BE8350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE839C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE83E8, b"Tnk_Rvl00")
    tcp.pokemem(0x12CCDB90, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "250": #For 2.5.0
    tcp.writestr(0x10506AF8, b"Tnk_Rvl00")
    tcp.writestr(0x105E4EB8, b"Tnk_Rvl00")
    tcp.writestr(0x105ED7D0, b"Rival00")
    tcp.writestr(0x105ED7DC, b"Rival00_Hlf")
    #Don't really need squid, looks bad without proper bone offsets
    #tcp.writestr(0x105ED7D4, b"Rival_Squid")
    tcp.writestr(0x12BE8350, b"Tnk_Rvl00")
    tcp.writestr(0x12BE839C, b"Tnk_Rvl00")
    tcp.writestr(0x12BE83E8, b"Tnk_Rvl00")
    tcp.pokemem(0x12CCDB90, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "260": #For 2.6.0
    tcp.writestr(0x10506B28, b"Tnk_Rvl00")
    tcp.writestr(0x105E59B8, b"Tnk_Rvl00")
    tcp.writestr(0x105EE350, b"Rival00")
    tcp.writestr(0x105EE35C, b"Rival00_Hlf")
    #Don't really need squid, looks bad without proper bone offsets
    #tcp.writestr(0x105EE36C, b"Rival_Squid")
    tcp.writestr(0x12BE9354, b"Tnk_Rvl00")
    tcp.writestr(0x12BE93A0, b"Tnk_Rvl00")
    tcp.writestr(0x12BE93EC, b"Tnk_Rvl00")
    tcp.pokemem(0x12CCF990, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "270": #For 2.7.0
    tcp.writestr(0x10506B58, b"Tnk_Rvl00")
    tcp.writestr(0x105E5F40, b"Tnk_Rvl00")
    tcp.writestr(0x105EE968, b"Rival00")
    tcp.writestr(0x105EE974, b"Rival00_Hlf")
    #Don't really need squid, looks bad without proper bone offsets
    #tcp.writestr(0x105EE984, b"Rival_Squid")
    tcp.writestr(0x12BEA354, b"Tnk_Rvl00")
    tcp.writestr(0x12BEA3A0, b"Tnk_Rvl00")
    tcp.writestr(0x12BEA3EC, b"Tnk_Rvl00")
    tcp.pokemem(0x12CD0D90, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "280": #For 2.8.0
    tcp.writestr(0x10506B58, b"Tnk_Rvl00")
    tcp.writestr(0x105E6000, b"Tnk_Rvl00")
    tcp.writestr(0x105EEA28, b"Rival00")
    tcp.writestr(0x105EEA34, b"Rival00_Hlf")
    #Don't really need squid, looks bad without proper bone offsets
    #tcp.writestr(0x105EEA44, b"Rival_Squid")
    tcp.writestr(0x12C1F354, b"Tnk_Rvl00")
    tcp.writestr(0x12C1F3A0, b"Tnk_Rvl00")
    tcp.writestr(0x12C1F3EC, b"Tnk_Rvl00")
    tcp.pokemem(0x12CD0D90, 0x00000000) #Enforce Female Inkling
elif sys.argv[1] == "290": #For 2.9.0

    #Tnk_Rvl00 1
    tcp.pokemem(0x10506BC0, 0x546E6B5F)
    tcp.pokemem(0x10506BC4, 0x53696D70)
    tcp.pokemem(0x10506BC8, 0x6C650000)

    #Tnk_Rvl00 2
    tcp.pokemem(0x105E62C0, 0x546E6B5F)
    tcp.pokemem(0x105E62C4, 0x53696D70)
    tcp.pokemem(0x105E62C8, 0x6C650000)

    #Rival00
    tcp.pokemem(0x105EF3C0, 0x52697661)
    tcp.pokemem(0x105EF3C4, 0x6C303000)

    #Rival00_Hlf
    tcp.pokemem(0x105EF3CC, 0x52697661)
    tcp.pokemem(0x105EF3D0, 0x6C30305F)
    tcp.pokemem(0x105EF3D4, 0x486C6600)


    #Rival_Squid
    #tcp.pokemem(0x105EF3DC, 0x52697661)
    #tcp.pokemem(0x105EF3E0, 0x6C5F5371)
    #tcp.pokemem(0x105EF3E4, 0x75696400)

    #Tnk_Rvl00 3
    tcp.pokemem(0x12BF3354, 0x546E6B5F)
    tcp.pokemem(0x12BF3358, 0x53696D70)
    tcp.pokemem(0x12BF335C, 0x6C650000)

    #Tnk_Rvl00 4
    tcp.pokemem(0x12BF33A0, 0x546E6B5F)
    tcp.pokemem(0x12BF33A4, 0x53696D70)
    tcp.pokemem(0x12BF33A8, 0x6C650000)

    #Tnk_Rvl00 5
    tcp.pokemem(0x12BF33EC, 0x546E6B5F)
    tcp.pokemem(0x12BF33D0, 0x53696D70)
    tcp.pokemem(0x12BF33D4, 0x6C650000)

#poke female
    tcp.pokemem(0x12CD1D90, 0x00000000)
tcp.s.close()
print("Done.")
