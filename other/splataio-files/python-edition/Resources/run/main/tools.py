tchoice = True
while tchoice:
    absolutely_unused_variable = os.system(clearscreen)
    print("""

Press <1> to decompress a .sarc/.pack/.szs file.
Press <2> to compress a .sarc/.pack/.szs file.
Press <3> to convert .byaml/.xml files.
Press <4> for advanced file tools. (BrawlBox)
Press <5> to convert MP3 to WAV/BRSTM
Press <Enter> to go back.
""")
    tchoice = raw_input(">> ")

    if tchoice == "1":
        print("\nPlace your file in the root folder of the AIO (where Splat-AIO.py is)")
        print("and type in its name with extension.\n")

        sapa = raw_input(">> ")
        os.system(".\\Resources\\run\\tools\\SARCExtract.py %s" %sapa)
        tchoice = True
        
    elif tchoice == "2":
        print("\nPlace the folder to be compressed in the same folder as Splat-AIO.py")
        print("and type in its name.\n")

        sppa = raw_input(">> ")
        os.system(".\\Resources\\run\\tools\\SARCPack.py %s" %sppa)
        tchoice = True

    elif tchoice == "3":
        print("\nPlace the .byaml/.xml to be converted into the same folder as Splat-AIO.py")
        print("and type in its name with extension.\n")

        ymlpa = raw_input(">> ")
        os.system(".\\Resources\\run\\tools\\yamlconv.exe %s" %ymlpa)
        tchoice = True

    elif tchoice == "4":
        subprocess.call("./Resources/run/exe/BrawlBox.exe")

    elif tchoice == "5":
        subprocess.call("./Resources/run/LoopingAudioConverter/LoopingAudioConverter.exe")

    else:
        tchoice = False
