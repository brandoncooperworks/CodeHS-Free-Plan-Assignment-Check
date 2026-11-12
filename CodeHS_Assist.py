from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

import os


def initGlobals():
    global ID, names, asgnID, classSelect
    classSelect = input("Select a class period: \n"
                        "5 - 5th Period\n"
                        "7 - 7th Period\n"
                        "8 - 8th Period\n"
                        )

    file = open(f"StudentIDs/CSP{classSelect}_CHS_IDs_Names.txt", "r")
    asgnFile = open("AssignmentIDs/CodeHS_Q4W28.txt")
    ID = []
    names = []
    asgnID = []
    x=1
    print(f"\n\n{classSelect}th Period Students:")
    for line in file.readlines():
        if "Period" in line:
            continue
        print(x,line, sep=". ", end="\b")
        # if input("Continue:") == "q": quit()
        x+=1
        ID.append(line[:7])
        names.append(line[10:-1])
    print("\n")
    # [print(el, end=", ") for el in ID]
    # print("\n")
    # [print(name, end=", ") for name in names]

    print("\n\nASSIGNMENTS:")
    for line in asgnFile.readlines():
        print(line, end="\b")
        asgnID.append(line[:9])
    print()
    # [print(id, end=", ") for id in asgnID]
    # print()


def entry():



    email = browser.find_element(by=By.NAME, value="email")
    password = browser.find_element(by=By.NAME, value="password")
    login = browser.find_element(by=By.ID, value="login-submit")

    # Fill in your credentials here if you want the program to automatically fill them.
    email.send_keys("YOUR CREDENTIALS HERE")
    password.send_keys("YOUR CREDENTIALS HERE")
    login.click()

def launchBrowser():
    global browser
    browser = webdriver.Chrome()
    # Need to enter login credentials
    browser.get("https://codehs.com/login")
    print("\n")

    # Uncomment the "entry()" function if you want the program to automatically enter your credentials
    entry()
    input("Logged in?\n") # Enter to continue

def allStudents():
    for i in range(len(ID)):
        site = "https://codehs.com/student/{}/section/439318/assignments".format(ID[i])
        browser.execute_script("window.open('{}','{}');".format(site,i))
        # Unit = browser.find_element(by=By.ID, value="109673007")
        # Unit.click()


    input("Press Enter to Close")

def assignmentList():
    windowNum = 0
    start = 0
    numStudents = len(ID)
    try:
        start = int(input("Enter a roster number from 1-{}\n".format(numStudents)))
        if (start > numStudents or start < 1):
            start = 1
    except:
        start = 1
    for i in range(start - 1, len(ID)):
        print("Student: "+str(i+1)+" - "+names[i])
        main = "https://codehs.com/student/{}/section/439318/assignments".format(ID[i])
        browser.execute_script("window.open('{}','{}');".format(main,windowNum))
        windowNum+=1
        for asgn in asgnID:
            assignment = "https://codehs.com/student/{}/section/439318/assignment/{}".format(ID[i], asgn)
            browser.execute_script("window.open('{}','{}');".format(assignment, windowNum))
            windowNum+=1
        input("Next Student?\n")

    input("Press Enter to Close")

initGlobals()
launchBrowser()
# allStudents()
assignmentList()