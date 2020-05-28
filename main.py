from colorama import init, Fore
import os
import re
import io

emailList = []
emailExtracted = []
totalLines = 0
totalExtracted = 0


def inHandler(file):
    try:
        data = io.open(file, "r", encoding="utf-8", errors="ignore")
        checkExtension = re.search(r"[.]+txt", file)
        if (data):
            if(checkExtension):
                extractEmail(data)
            else:
                print("invalid extension")
    except PermissionError:
        print("permission denied")
    except (FileNotFoundError, OSError):
        print("file not found")


def extractEmail(checkedFile):
    global totalLines, totalExtracted
    emailList = checkedFile.readlines()
    for email in emailList:
        totalLines += 1
        getEmail = re.search(
            r"([a-z0-9_.+-]+[@]+[a-z0-9-]+[.]+[a-z.]+)", email, re.I)
        if (getEmail):
            emailExtracted.append(getEmail.group())
            totalExtracted += 1
    outFile(emailExtracted)


def outFile(emailExtracted):
    out = open("out.txt", "w")
    numIndex = 0
    for email in emailExtracted:
        out.write(email+"\n")
        numIndex += 1
        print("[{}] {}".format(numIndex, email))
    out.close()
    print("\nTotal lines: {}". format(totalLines))
    print("Extracted email: {}\n". format(totalExtracted))


def main():
    try:
        os.system("clear")
        appTitle = (Fore.RED+r"""
                             _   _
   ___   _ __ ___     __ _  (_) | |          _ __     __ _   _ __   ___    ___   _ __
  / _ \ | '_ ` _ \   / _` | | | | |  _____  | '_ \   / _` | | '__| / __|  / _ \ | '__|
 |  __/ | | | | | | | (_| | | | | | |_____| | |_) | | (_| | | |    \__ \ |  __/ | |
  \___| |_| |_| |_|  \__,_| |_| |_|         | .__/   \__,_| |_|    |___/  \___| |_|
                                            |_|
    | Author  : vt92i
    | Version : 0.7
    """)
        print(appTitle)

        inFile = input(
            "{}Input file (*.txt) : {}".format(Fore.GREEN, Fore.WHITE))
        if(inFile):
            inHandler(inFile)

    except KeyboardInterrupt:
        print("\nCTRL + C")
    except EOFError as e:
        print(e)


main()
