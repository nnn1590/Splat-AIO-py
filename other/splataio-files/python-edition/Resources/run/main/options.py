import urllib2
choice2 = True
while choice2:
    absolutely_unused_variable = os.system(clearscreen)
          

    if diff == 0x0:
        print("""

Press <1> to check for updates.
Press <2> to update your IP address.
Press <3> to view the changelog list.

Press <4> to view the Modding Hub thread.

Press <s> to switch to Homebrew Launcher Gecko mode.

Press <c> to look at the credits.
<ENTER> to go back.\n""")

    if diff == 0x9000:
        print("""

Press <1> to check for updates.
Press <2> to update your IP address.
Press <3> to view the changelog list.

Press <4> to view the Modding Hub thread.
Press <5> to view MCMiners9's Website.

Press <s> to switch to Internet Browser Gecko mode.

Press <c> to look at credits.
Press <ENTER> to go back.\n""")

    choice2 = raw_input(">> ")
    if choice2 == "1":
        execfile("./Resources/setup/update_beta.py")

    elif choice2 == "2":
        absolutely_unused_variable = os.system(clearscreen)
        print("Please type in your new IP address.\n")
        fresh_ip = raw_input(">> ")
        save = open("./Resources/setup/ip.txt", "w")
        save.write(fresh_ip)
        save.close()
        ip = fresh_ip

    elif choice2 == "3":
        execfile("./Resources/run/main/cl.py")

    elif choice2 == "s":
        if diff == 0x0:
            diff = 0x9000
        else:
            diff = 0x0

    elif choice2 == "4":
        os.system("start \"\" http://gbatemp.net/threads/splatoon-modding-hub.425670/")

    elif choice2 == "5":
        os.system("start \"\" http://mcminers9site.weebly.com/")

    elif choice2 == "c":
        absolutely_unused_variable = os.system(clearscreen)
        cr = open("./Resources/run/extra/credits.txt", "r").read()
        print(cr)
        print("\n")
        raw_input("Press ENTER to return.")
