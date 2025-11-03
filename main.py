import os
import time


def clear():
   """
   Clear Terminal
   """ 
   os.system('cls' if os.name == 'nt' else 'clear')

def ASCII_Art():
    """
    ASCII Art Function
    """
    return r"""
 ____                  ___                  
/\  _`\              /'___\                 
\ \,\L\_\      __   /\ \__/    __           
 \/_\__ \    /'__`\ \ \ ,__\ /'__`\         
   /\ \L\ \ /\ \L\.\_\ \ \_//\  __/         
   \ `\____\\ \__/.\_\\ \_\ \ \____\        
    \/_____/ \/__/\/_/ \/_/  \/____/        
 ____                                __     
/\  _`\                             /\ \    
\ \ \L\_\   __  __     __     _ __  \_\ \   
 \ \ \L_L  /\ \/\ \  /'__`\  /\`'__\/'_` \  
  \ \ \/, \\ \ \_\ \/\ \L\.\_\ \ \//\ \L\ \ 
   \ \____/ \ \____/\ \__/.\_\\ \_\\ \___,_\
    \/___/   \/___/  \/__/\/_/ \/_/ \/__,_ /
"""


def splashScreenMenu():
    """
    Splash Screen
    """
    print(ASCII_Art())
    time.sleep(0.5)

    print("\nWelcome to Safe Guard!")
    time.sleep(0.5)

    input("Press ENTER to Continue...")


def mainMenu():
    """
    Main Menu
    """
    clear()
    print("\nMAIN MENU")
    
    while True:
        print("1.) Start Password Check")
        print("2.) Exit")

        userInput = input("\nSelect an Option: ")

        if userInput == "1":
            passwordChecker()
        elif userInput == "2":
            print("\nGoodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid Option. Try Again...\n")
            time.sleep(1)

def passwordLengthCheck(password, min_length = 8):
    """
    Password Length Check
    """
    if len(password) >= 8:
        print(f"✅ Password Length is Sufficient ({len(password)} characters).")
    else:
        print(f"❌ Password is too Short ({len(password)} characters). Minimum is {min_length}.")



def passwordChecker():
    """
    Checks Password Strength
    """
    clear()

    # Enter Input
    password = input("\nEnter Password to Check: ")
    time.sleep(0.5)
    
    print()
    passwordLengthCheck(password)

    time.sleep(2)

    input("\nPress ENTER to Return to Main Menu...")


if __name__ == "__main__":
    splashScreenMenu()
    mainMenu()