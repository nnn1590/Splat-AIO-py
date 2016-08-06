import urllib, urllib2, zipfile, shutil

#Check to see if there is even any update to begin with
hver = int(open("./Resources/setup/ver.txt", "r").read())
wver = int(urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/ver.txt").read())
if wver > hver:
    upc = True
    while upc:
        absolutely_unused_variable = os.system("cls")
        print("There is an update available. Changes:\n")
        changes = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/changes.txt").read()
        print(changes)
        print("\n Do you want to update? (<y> for Yes, anything else for no..)")

        upc = raw_input(">> ")
        if upc == "y":

            if os.path.isdir("./Resources/run") == True:
                shutil.rmtree("./Resources/run")

                absolutely_unused_variable = os.system("cls")
                print("Downloading your hax...")
                urllib.urlretrieve("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/update.zip", "./Resources/update.zip")

                with zipfile.ZipFile("./Resources/update.zip", "r") as z:
                    z.extractall("./Resources/run")

                os.remove("./Resources/update.zip")
                
                os.remove("./Resources/setup/ver.txt")
                urllib.urlretrieve("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/ver.txt", "./Resources/setup/ver.txt")
                del hver
                del wver
                os.execl(sys.executable, sys.executable, *sys.argv)
        elif upc == "n":
            execfile("./Resources/run/main/menu.py")

        else:
            os.execl(sys.executable, sys.executable, *sys.argv)

else:
    print("There are currently no updates.")
    time.sleep(0)
    del hver
    del wver
    pass
