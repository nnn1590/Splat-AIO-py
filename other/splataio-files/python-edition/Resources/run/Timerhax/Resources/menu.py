os.system('cls')

choice = True
while choice:
	os.system("cls")
	print("Versus Timer Changer for Splatoon 2.10.0 -- Wii U IP: %s" % (ip))
	print("Written by Yahya, credits to Seresaa and their Splat AIO")
	
	print("""\nPlease press a button followed by ENTER:""")
	print("""
<1> Adjust timer in Recon
<2> Adjust timer in Battle Dojo
<3> Adjust timer in Amiibo Squid Challenges
<4> Change IP Address
	
<ENTER> Exit\n\n""")
	
	choice = raw_input(">> ")
	
	#Recon
	if choice == "1":
		execfile("./Resources/run/Timerhax/Resources/recon.py")

	#Battle Dojo
	elif choice == "2":
		execfile("./Resources/run/Timerhax/Resources/dojo.py")
		
	#Amiibo Kraken
	elif choice == "3":
		execfile("./Resources/run/Timerhax/Resources/amiibo_squid.py")
	#Change ip
	elif choice == "4":
		execfile("./Resources/run/Timerhax/Resources/change_ip.py")
