from tcpgecko import TCPGecko

tcp = TCPGecko(ip)
print("""
unused gear script by Nefarious

1) NoHed, NoClothes, NoShoes (0)
2) MSN001 - Octo Valley armor x1 (27001)
3) MSN002 - Octo Valley armor x2 (27002)
4) MSN003 - Octo Valley armor x3 (27003)
5) RVL001 - Elite Octoling Goggles (28001)
6) SUP000 - testfire preorder gear (29500)
7) SUP001 - testfire SRL gear (29501)
8) reset
""")
option = int(input("Option: "))
if option == 1:
    print("NoHed, NoClothes, NoShoes...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x00000000) #head slot
    tcp.pokemem(0x12CD3DA0+0x1000, 0x00000000) #clothes slot
    tcp.pokemem(0x12CD0DA0+0x1000, 0x00000000) #shoes slot
    tcp.pokemem(0x12CD0D88+0x1000, 0x00000000) #set current head
    tcp.pokemem(0x12CD0D80+0x1000, 0x00000000) #set current clothes
    tcp.pokemem(0x12CD0D84+0x1000, 0x00000000) #set current shoes
    print("Done.")
elif option == 2:
    print("MSN001...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x00006979)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x00006979)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x00006979)
    tcp.pokemem(0x12CD0D88+0x1000, 0x00006979)
    tcp.pokemem(0x12CD0D80+0x1000, 0x00006979)
    tcp.pokemem(0x12CD0D84+0x1000, 0x00006979)
    print("Done.")
elif option == 3:
    print("MSN002...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x0000697A)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x0000697A)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x0000697A)
    tcp.pokemem(0x12CD0D88+0x1000, 0x0000697A)
    tcp.pokemem(0x12CD0D80+0x1000, 0x0000697A)
    tcp.pokemem(0x12CD0D84+0x1000, 0x0000697A)
    print("Done.")
elif option == 4:
    print("MSN003...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x0000697B)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x0000697B)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x0000697B)
    tcp.pokemem(0x12CD0D88+0x1000, 0x0000697B)
    tcp.pokemem(0x12CD0D80+0x1000, 0x0000697B)
    tcp.pokemem(0x12CD0D84+0x1000, 0x0000697B)
    print("Done.")
elif option == 5:
    print("RVL001...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x00006D61)
    tcp.pokemem(0x12CD0D88+0x1000, 0x00006D61)
    print("Done.")
elif option == 6:
    print("SUP000...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x0000733C)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x0000733C)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x0000733C)
    tcp.pokemem(0x12CD0D88+0x1000, 0x0000733C)
    tcp.pokemem(0x12CD0D80+0x1000, 0x0000733C)
    tcp.pokemem(0x12CD0D84+0x1000, 0x0000733C)
    print("Done.")
elif option == 7:
    print("SUP001...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x0000733D)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x0000733D)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x0000733D)
    tcp.pokemem(0x12CD0D88+0x1000, 0x0000733D)
    tcp.pokemem(0x12CD0D80+0x1000, 0x0000733D)
    tcp.pokemem(0x12CD0D84+0x1000, 0x0000733D)
    print("Done.")
elif option == 8:
    print("Resetting...")
    tcp.pokemem(0x12CD6DA0+0x1000, 0x00000001)
    tcp.pokemem(0x12CD3DA0+0x1000, 0x00000001)
    tcp.pokemem(0x12CD0DA0+0x1000, 0x00000001)
    tcp.pokemem(0x12CD0D88+0x1000, 0x00000001)
    tcp.pokemem(0x12CD0D80+0x1000, 0x00000001)
    tcp.pokemem(0x12CD0D84+0x1000, 0x00000001)
    print("Done.")
else:
    print("Invalid option!")
+0x1000
