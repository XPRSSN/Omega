import time
import requests

print("""

________                       ____              .___                   __           .__   .__                   
\_____  \    _____    ____    / ___\ _____       |   |  ____    _______/  |_ _____   |  |  |  |    ____ _______  
 /   |   \  /     \ _/ __ \  / /_/  >\__  \      |   | /    \  /  ___/\   __\__  \  |  |  |  |  _/ __ \_  __ \ 
/    |    \|  Y Y  \\  ___/  \___  /  / __ \_    |   ||   |  \ \___ \  |  |   / __ \_|  |__|  |__\  ___/ |  | \/ 
\_______  /|__|_|  / \___  >/_____/  (____  /    |___||___|  //____  > |__|  (____  /|____/|____/ \___  >|__|    
        \/       \/      \/               \/               \/      \/             \/                  \/         


Current last build: 5th August 2022
Current last version: 4.55                                                                                                        
""")

yesno=input("\nAre you sure you want to install Omega? [Y/N]: ")

if yesno == "Y" or yesno=="y":
    DLLlink="https://raw.githubusercontent.com/XPRSSN/Omega/main/DLL/Omega5.8.2022.dll"
    Injlink="https://raw.githubusercontent.com/XPRSSN/Omega/main/Injectors/CSGhost-v4.3.1.exe"

    DLLresponse = requests.get(DLLlink)
    open("Omega5.8.2022.dll", "wb").write(DLLresponse.content)

    Injresponse = requests.get(Injlink)
    open("CSGhost-v4.3.1.exe", "wb").write(Injresponse.content)

    print("\nFiles downloaded")
    print("Exiting..")
    time.sleep(2)
    exit()
elif yesno=="N" or yesno=="n":
    print("\nExiting..")
    time.sleep(2)
    exit()
else:
    print("Invalid answer. Exiting...")
    time.sleep(2)
    exit()
