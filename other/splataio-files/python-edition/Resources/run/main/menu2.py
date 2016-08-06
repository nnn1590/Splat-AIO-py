#Menu, in hopes that os.system() will function properly.
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
    print("Original AIO by iAqua, rewritten by Resa, now owned by Deck of Noobs and MCMiners9")
    print("Splat AIO v%d (for Splatoon 2.11) -- Wii U IP: %s" % (cver, ip))
    print("""
Please don't just blindly use these hacks. Your chances of getting banned
vary depending on which of these hacks you use and how you use them.
""")
    print("Please press a button followed by ENTER:")
    print("""
<1> View the Splat AIO GitHub repository.
<2> View the SplatAIO help page
<3> Report a issue with the SplatAIO.
<r> Return to the main menu.


                                      <ENTER> Exit\n\n""")

    choice = raw_input(">>")

    #View the SplatAIO 2 GitHub repository.
    if choice == "1":
        os.system("start \"\" https://github.com/MCMiners9/Splat-AIO")

    #View the SplatAIO help page
    elif choice == "2":
        os.system("start \"\" https://github.com/MCMiners9/Splat-AIO/tree/master/help")
        
    #Report an issue with the SplatAIO
    elif choice == "3":
        os.system("start \"\" https://github.com/MCMiners9/Splat-AIO/issues")

    #Return to the main menu
    elif choice == "r":
        execfile("./Resources/run/main/menu.py")
        
