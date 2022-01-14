# easyInfra.py

import os
import subprocess

'''




'''

### User Vars ###

fUseDemoFQDN = True  # if True, we will create a demo FQDN; if False, will use value set in variable sFQDNforVoodooLP
sFQDNforVoodooLP = ""  # Point a DNS A Record to the IP Address of the Voodoo LP, e.g. via Route53
sEmailAddressToUseForTLScerts = ""

sLocationAndNameOfVoodooLicenseKey = ".\\voodoo.lic"  # .\\ means the current directory
sLocationAndNameOfVoodooZip = ".\\voodoo.zip"  # .\\ means the current directory
sPasswordToZipFile = ""   # password to the voodoo.zip file

sOutputVerbose = "DEBUG"   # Options include: DEBUG, NORMAL
# sOutputVerbose = "NORMAL"   # Options include: DEBUG, NORMAL

### App Logic ###

def sStatusToString(sVerbose):
    if sVerbose == 'DEBUG':
        return '[~]'
    elif sVerbose == 'NORMAL':
        return '[*]'
    elif sVerbose == 'SUCCESS':
        return '[+]'
    elif sVerbose == 'FAILED':
        return '[-]'
    elif sVerbose == 'ERROR':
        return '[!]'

def sPrint(sString, sStatus = 'DEBUG'):
    print(sStatusToString(sStatus) + " " + sString)

def sVarPrint(sNameOfVar, sVar):
    print(sStatusToString('DEBUG') + " " + sNameOfVar + ": " + str(sVar) + " |-type-| " + str(type(sVar)))

def install_a_dependency(sDependencyName):
    print("TODO")

def check_if_a_file_exists(sLocationAndNameOfFile):
    print("TODO")

def check_if_app_is_installed(sNameOfApp):
    sNameOfAppSafer = sNameOfApp.strip()
    oResultOfsubprocess = subprocess.run(["which", sNameOfAppSafer], stdout=subprocess.PIPE, text=True)
    print("[~] oResultOfsubprocess: " + str(oResultOfsubprocess) + " |-type-| " + str(type(oResultOfsubprocess)))
    print("[~] oResultOfsubprocess.returncode: " + str(oResultOfsubprocess.returncode) + " |-type-| " + str(
        type(oResultOfsubprocess.returncode)))
    print("[~] oResultOfsubprocess.stdout: " + str(oResultOfsubprocess.stdout) + " |-type-| " + str(
        type(oResultOfsubprocess.stdout)))
    if oResultOfsubprocess.returncode == 0:
        return True
    else:
        return False

def install_app(sNameOfApp):
    os.system("apt update")
    os.system("apt install -y " + sNameOfApp)

def install_docker():
    install_app("docker.io")

def check_and_install(sNameOfApp):
    if check_if_app_is_installed(sNameOfApp):
        print("[~] sNameOfApp is already installed: " + sNameOfApp)
    else:
        install_app(sNameOfApp)

def print_banner(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_banner('PyCharm')
    #
    if check_if_app_is_installed("docker"):
        print("[~] Docker is Already Installed")
    else:
        install_docker()
    #
    check_and_install("unzip")
    # check_if_app_is_installed("notdocker")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
