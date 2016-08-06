
#Credit to Duckling
#Gives you 9999999 coins (Splatoon 2.8.0, OVH Gecko)

#tcp = TCPGecko(ip)
#tcp.pokemem(0x12CDB1A0,9999999)
#tcp.s.close()
#print("Done.")

level = True
while level:
    absolutely_unused_variable = os.system("cls")
    print("How much money would you like to have? Max is 9,999,999")
    print("(Don't input commas)\n")
    try:
        level = int(input(">> "))
    except ValueError:
        print("Please use a whole number.")
        time.sleep(2)
        
    if level <= 9999999:
        if level < 0:
            print("Number too low.")
            time.sleep(2)
            level = True
        else:
            tcp = TCPGecko(ip)
            tcp.pokemem(0x12CDC1A0 + diff, level)
            tcp.s.close()
            level = False
        
    else:
        print("Number too high.")
        time.sleep(2)
