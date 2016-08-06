import time
#Separated; rank hack is in MaxStats2
#Credit to Riru2025
#Gives you level 50 (Splatoon 2.8.0, HBL Gecko)
 
#tcp = TCPGecko(ip)
#tcp.pokemem(0x12CD8C24, 0xFFFFFFFF) #progression
#tcp.pokemem(0x12CE31A8, 49) #level (+1 in-game)
#tcp.pokemem(0x12CE31A4, 0) #level points
#tcp.s.close()
#print("Done.")
level = True
while level:
    absolutely_unused_variable = os.system("cls")
    print("What level would you like to be? Max is 50.")
    try:
        level = int(input(">> "))
    except ValueError:
        print("Please use a whole number.")
        time.sleep(2)
        
    if level <= 50:
        if level <= 0:
            print("Please use a number higher than 0.")
            time.sleep(2)
            level = True
        else:
            tcp = TCPGecko(ip)
            tcp.pokemem(0x12CD1C24 + diff, 0xFFFFFFFF)
            tcp.pokemem(0x12CDC1A8 + diff, level - 1)
            tcp.pokemem(0x12CDC1A4 + diff, 0)
            tcp.s.close()
            level = False
        
    else:
        print("Please use a number from 1 to 50.")
        time.sleep(2)
