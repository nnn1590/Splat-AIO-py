#Credit to Riru2025
#Gives you rank S+ 99 (Splatoon 2.8.0, OVH Gecko)

#tcp = TCPGecko(ip)
#tcp.pokemem(0x12CD1C24 + diff,0xFFFFFFFF) #progression
#tcp.pokemem(0x12CDC1AC + diff,10) #rank (0 is C-, 1 is C, 2 is C+, and so on to 10 is S+)
#tcp.pokemem(0x12CDB1B0,99) #rank number
#tcp.s.close()

rank = True
while rank:
    absolutely_unused_variable = os.system(clearscreen)
    print("What rank would you like to be? Use lowercase letters.")
    print("Examples, 'c-' 'a' 's+'")
    rank = raw_input(">> ")

    #LETTERS, C
    if rank == "c-":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,0)
        tcp.s.close()

    elif rank == "c":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,1)
        tcp.s.close()

    elif rank == "c+":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,2)
        tcp.s.close()

    #B
    elif rank == "b-":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,3)
        tcp.s.close()

    elif rank == "b":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,4)
        tcp.s.close()

    elif rank == "b+":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,5)
        tcp.s.close()

    #A
    elif rank == "a-":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,6)
        tcp.s.close()

    elif rank == "a":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,7)
        tcp.s.close()

    elif rank == "a+":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,8)
        tcp.s.close()

    #S
    elif rank == "s":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,9)
        tcp.s.close()

    elif rank == "s+":
        tcp = TCPGecko(ip)
        tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
        tcp.pokemem(0x12CDC1AC + diff,10)
        tcp.s.close()

    else:
        rank = True
        break

    #NUMBER

    absolutely_unused_variable = os.system(clearscreen)
    print("How far through %s would you like to be? Max is 99." %rank)
    try:
        number = int(input(">> "))
    except ValueError:
        print("Please use a whole number.")
        time.sleep(2)
        
    if number <= 99:
        if number < 0:
            print("Number too low.")
            time.sleep(2)
        else:
            tcp = TCPGecko(ip)
            tcp.pokemem(0x12CDC1B0 + diff, number)
            tcp.s.close()
            rank = False
        
    else:
        print("Please use a number from 1 to 99.")
        time.sleep(2)
