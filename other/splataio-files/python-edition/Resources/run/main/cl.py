import urllib, urllib2, os

clc = True
while clc:
    absolutely_unused_variable = os.system(clearscreen)

    print("""Press a number/letter given to view update changes/the Splatoon Modding Hub, or anything else to go back.

    <1> v2
    <2> v3
    <3> v4
    <4> v5
    <5> v6
    <6> v7
    <7> v8
    <8> v9
    <9> v10
    <10> v11
    <11> v12
    <12> v13
    <13> v14
    <14> v15
    <15> v16
    <16> v17
    <17> v18
    <18> v19
    <19> v20
    <20> v21
    <21> v22
    <22> v23
    <23> v24
    <24> v25
    <25> v26
    <26> v27
    <27> v28
    <28> v29
    <29> v30
    <30> v31
    <31> v32
    <32> v33
    <33> v34

    """)

    clc = raw_input(">> ")

    if clc == "1":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch2.txt").read()

    elif clc == "2":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch3.txt").read()

    elif clc == "3":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch4.txt").read()

    elif clc == "4":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch5.txt").read()
        
    elif clc == "5":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch6.txt").read()

    elif clc == "6":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch7.txt").read()

    elif clc == "7":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch8.txt").read()

    elif clc == "8":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch9.txt").read()

    elif clc == "9":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch10.txt").read()

    elif clc == "10":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch11.txt").read()

    elif clc == "11":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch12.txt").read()

    elif clc == "12":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch13.txt").read()

    elif clc == "13":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch14.txt").read()

    elif clc == "14":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch15.txt").read()

    elif clc == "15":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch16.txt").read()

    elif clc == "16":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch17.txt").read()

    elif clc == "17":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch18.txt").read()

    elif clc == "18":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch19.txt").read()

    elif clc == "19":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch20.txt").read()

    elif clc == "20":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch21.txt").read()

    elif clc == "21":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch22.txt").read()

    elif clc == "22":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch23.txt").read()

    elif clc == "23":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch24.txt").read()

    elif clc == "24":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch25.txt").read()

    elif clc == "25":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch26.txt").read()

    elif clc == "26":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch27.txt").read()

    elif clc == "27":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch28.txt").read()

    elif clc == "28":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch29.txt").read()

    elif clc == "29":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch30.txt").read()

    elif clc == "30":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch31.txt").read()

    elif clc == "31":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch32.txt"),read()

    elif clc == "32":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch33.txt").read()

    elif clc == "33":
        info = urllib2.urlopen("https://raw.githubusercontent.com/MCMiners9/Splat-AIO/master/cl/ch34.txt").read()
        
    else:
        break

    absolutely_unused_variable = os.system(clearscreen)
    print(info)
    print("")
    print("Use any button to return.\n")
    raw_input()

    clc = True
