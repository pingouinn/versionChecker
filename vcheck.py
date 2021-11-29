import requests

version = "v1.0"

def versCheck():
    # Recup
    url = "https://raw.githubusercontent.com/pingouinn/versionChecker/main/version.txt"
    r = requests.get(url)
    currentV = r.text
    
    if currentV.find(version) != -1:
            return True
    return False
