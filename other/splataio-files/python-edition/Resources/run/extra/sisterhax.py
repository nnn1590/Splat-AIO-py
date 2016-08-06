aori = True
while aori:
    absolutely_unused_variable = os.system(clearscreen)
    print("Press <1> if you dream of Callie.")
    print("Press <2> if you dream of Marie.\n")
    print("...I'm not judging.\n")

    print("Press <3> if you want them to swap places.")
    print("Press <4> if you want everything back to normal.\n")

    print("Press <ENTER> to go back.")

    hotaru = raw_input(">> ")

    if hotaru == "1":
        tcp = TCPGecko(ip)
        tcp.writestr(0x105EB5FC, b"Npc_IdolA")
        tcp.writestr(0x105EB608, b"Npc_IdolA")
        tcp.s.close()

    elif hotaru == "2":
        tcp = TCPGecko(ip)
        tcp.writestr(0x105EB5FC, b"Npc_IdolB")
        tcp.writestr(0x105EB608, b"Npc_IdolB")
        tcp.s.close()

    elif hotaru == "3":
        tcp = TCPGecko(ip)
        tcp.writestr(0x105EB5FC, b"Npc_IdolB")
        tcp.writestr(0x105EB608, b"Npc_IdolA")
        tcp.s.close()

    elif hotaru == "4":
        tcp = TCPGecko(ip)
        tcp.writestr(0x105EB5FC, b"Npc_IdolA")
        tcp.writestr(0x105EB608, b"Npc_IdolB")
        tcp.s.close()

    else:
        aori = False #you monster
