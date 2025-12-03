import os
import time
import requests


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
    print("\nSafe Guard Main Menu")
    
    while True:
        print("1.) Check Password Strength")
        print("2.) Check Password Similarity")
        print("3.) Check Password Expiration")
        print("4.) Generate Password")
        print("5.) Exit")

        userInput = input("\nSelect an Option: ")

        if userInput == "1":
            checkStrength()
        elif userInput == "2":
            checkSimilarity()
        elif userInput == "3":
            checkExpiration()
        elif userInput == "4":
            generatePassword()
        elif userInput == "5":
            print("\nGoodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid Option. Try Again...\n")
            time.sleep(1)


def checkStrength():
    """
    Checks Password Strength via Microservice
    """
    clear()

    # Password Input to be Evaluated
    password = input("\nEnter Password to Check: ")
    print()

    try:
        response = requests.post("http://localhost:5001/strength", json={"password": password})
        if response.status_code == 200:
            result = response.json()

            # Print Score Rating
            print(f"Strength Score: {result['score']}/5")

            # Loop Through Feedback List
            for fb in result['feedback']:
                print(f"  - {fb}")
        else:
            print("❌ Error Checking Password Strength.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Could Not Connect to Strength Service: {e}")

    time.sleep(2)
    print()


def checkSimilarity():
    """
    Checks Password Similarity via Microservice
    """
    clear()

    print("\nChoose Similarity Check:")
    print("1.) Check Similarity to Old Password")
    print("2.) Check Similarity to Username")

    choice = input("\nSelect an Option: ")

    if choice == "1":
        new_password = input("Enter New Password: ")
        old_password = input("Enter Old Password: ")
        try:
            response = requests.post("http://localhost:5002/check_password_similarity", json={"new_password": new_password, "old_password": old_password})
            if response.status_code == 200:
                result = response.json()
                print(f"Similarity to Old Password: {result['Similarity']:.2f}")
                print(f"  - {result['Feedback']}")
            else:
                print("❌ Error Checking Password Similarity.")
        except requests.exceptions.RequestException as e:
            print(f"❌ Could Not Connect to Similarity Service: {e}")
    elif choice == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            response = requests.post("http://localhost:5002/check_username_similarity", json={"username": username, "password": password})
            if response.status_code == 200:
                result = response.json()
                print(f"Similarity to Username: {result['Similarity']:.2f}")
                print(f"  - {result['Feedback']}")
            else:
                print("❌ Error checking username similarity.")
        except requests.exceptions.RequestException as e:
            print(f"❌ Could Not Connect to Similarity Service: {e}")
    else:
        print("Invalid Option.")

    time.sleep(2)
    print()


def checkExpiration():
    """
    Checks Password Expiration via Microservice
    """
    clear()

    last_changed = input("\nEnter Last Password Change Date (YYYY-MM-DD): ")
    print()

    try:
        response = requests.post("http://localhost:5003/check_password_age", json={"last_changed": last_changed})
        if response.status_code == 200:
            result = response.json()
            print(f"Password Age: {result['days_old']} days")
            print(f"Status: {result['status']}")
            print(f"  - {result['message']}")
        else:
            print("❌ Error Checking Password Age.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Could Not Connect to Expiration Service: {e}")

    time.sleep(2)
    print()


def generatePassword():
    """
    Generates a Password via Microservice
    """
    clear()

    length = input("\nEnter Desired Password Length (Minimum 8): ")

    try:
        response = requests.get(f"http://localhost:5004/generate?length={length}")
        if response.status_code == 200:
            result = response.json()
            print(f"Generated Password: {result['password']}")
            print("(Password Copied to Clipboard)")
        else:
            print("❌ Error Cenerating Password.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Could Not Connect to Generator Service: {e}")

    time.sleep(2)
    print()


if __name__ == "__main__":
    splashScreenMenu()
    mainMenu()
