#Menu, in hopes that os.system() will function properly
diff = 0x0
cver = int(open("./Resources/setup/ver.txt", "r").read())
opsys = os.name

if opsys == "nt":
    clearscreen = "cls"
else:
    clearscreen = "clear"

choice = True
while choice:
    absolutely_unsigned_variable = os.system(clearscreen)
    print("Original AIO by iAqua, rewritten by Resa, now owned by Deck Of Noobs and MCMiners9")
    print("Splat AIO v%d (for Splatoon 2.11) -- Wii U IP: %s" % (cver, ip))
    print("""
Please don't just blindly use these hacks. Your chances of getting banned
vary depending on which of these hacks you use and how you use them.
""")
    print("Please press a button followed by ENTER:")
    print("""
<1> Octohax+, with Squid Form       <g> GeckoMapTester
<2> Octohax+, with  Octo Form       <a> Amiibohax
<u> Unused Gear                     <r> Timerhax (change timer)
<3> Set Money                       <c> Splathax
<4> Set Snails                      <s> Sisterhax
<5> Set Level                       <e> SplatAIO 2
<6> Set Rank                        <m> Cafiine Music Randomizer (buggy)
<0> Editable DojoHax                <t> TCPGecko.NET
<7> All (Safely) Obtainable Gear    <i> Scan for IP         
<8> All Obtainable Weapons          <v> Options
<9> Unlock All Minigames            <n> Tools
<x> More Menu options               

                                    <ENTER> Exit\n\n""")
    
    choice = raw_input(">> ")

    #Squidform Octohax
    if choice == "1":
        execfile("./Resources/run/OVH/octohax+.py")

    #Octoform Octohax so people stop saying it doesn't work.
    elif choice == "2":
        execfile("./Resources/run/OVH/octocto+.py")

    #Max Money.
    elif choice == "3":
        execfile("./Resources/run/OVH/money.py")

    #Max Snails.
    elif choice == "4":
        execfile("./Resources/run/OVH/Snails.py")

    #Level 50.
    elif choice == "5":
        execfile("./Resources/run/OVH/MaxStats1.py")

    #S+ 99
    elif choice == "6":
        execfile("./Resources/run/OVH/MaxStats2.py")

    #All Gear.
    elif choice == "7":
        execfile("./Resources/run/OVH/AllGear.py")

    #All Weapons.
    elif choice == "8":
            execfile("./Resources/run/OVH/Weapons.py")

    #All Minigames.
    elif choice == "9":
        execfile("./Resources/run/OVH/AllMinigames.py")

    #amiibohax
    elif choice == "a":
        subprocess.call("./Resources/run/exe/amiibohax.exe")
        

    #Colorizer -- Instaban. Don't use this, you'll get banned.  (<-- actually nowhere near instant, or I'd be banned too -Resa)
    #elif choice == "b":
        #os.system(r".\Resources\run\exe\gudWrapper.jar .\Resources\run\exe\SplatoonColorizer.28.gud")

    #Timerhax - Change the time left in Recon and Battle Dojo mode.
    elif choice == "r":
       execfile("./Resources/run/Timerhax/timer_changer.py")
                 
    #SplatHax
    elif choice == "c":
        subprocess.call("./Resources/run/exe/Splathax.exe")

    #TCPGecko
    elif choice == "t":
        subprocess.call("./Resources/run/Gecko/Gecko_dNet.exe")

    #IP Scanner
    elif choice == "i":
        subprocess.call("./Resources/run/exe/ipscan24.exe")

    #Options
    elif choice == "v":
        execfile("./Resources/run/main/options.py")

    #Tools
    elif choice == "n":
        execfile("./Resources/run/main/tools.py")

    #Sisterhax
    elif choice == "s":
        execfile("./Resources/run/extra/sisterhax.py")

    #GeckoMapTester
    elif choice == "g":
        subprocess.call("./Resources/run/exe/GeckoMapTester.exe")

    #BETA TEST the new SplatAIO 2
    elif choice == "e":
        subprocess.call("./Resources/run/exe/SplatAIO.exe")

    #Cafiine Music Randomizer
    elif choice == "m":
        subprocess.call("./Resources/run/exe/MusicRandomizer.exe")

    #Editable DojoHax
    elif choice == "0":
        subprocess.call("./Resources/run/exe/DojoHax.exe")

    #Unused Gear, somewhat unsafe
    elif choice == "u":
        execfile("./Resources/run/OVH/unusedgear.py")

    #View more menu options
    elif choice == "x":
        execfile("./Resources/run/main/menu2.py")
