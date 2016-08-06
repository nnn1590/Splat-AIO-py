#Credit to Duckling
#Gives you 999 Super Sea Snails (Splatoon 2.8.0, OVH Gecko)

#tcp = TCPGecko(ip)
#tcp.pokemem(0x12CDB1B4, 999)
#tcp.s.close()
#print("Done.")

level = True
while level:
    absolutely_unused_variable = os.system("cls")
    print("How many snails would you like to have? Max is 999.")
    try:
        level = int(input(">> "))
    except ValueError:
        print("Please use a whole number.")
        time.sleep(2)
        
    if level <= 999:
        if level < 0:
            print("Number too low.")
            time.sleep(2)
            level = True
        else:
            tcp = TCPGecko(ip)
            tcp.pokemem(0x12CDC1B4 + diff, level)
            tcp.s.close()
            level = False
        
    else:
        print("Please use a number from 1 to 999.")
        time.sleep(2)
