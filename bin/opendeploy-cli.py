import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def loadConfig():
    with open ('conf/config.json', 'r') as f:
        return json.load(f)

# Boot existing guest VM
def bootGuest(config, guestName):

    ROOT_PATH = Path(config['vm_root']).expanduser()
    bootConfig = f"{ROOT_PATH}/{guestName}/{guestName}.json"

    
    print(f"Booting guest: {guestName}")

    # Validate input
    if not os.path.exists(bootConfig):
        print(f"Error: File not exists")
        sys.exit(1)

    
    # Read config file
    with open(bootConfig, 'r') as f:
        guestConfig = json.load(f)

    subprocess.run([
        "qemu-system-x86_64",
        "-m", guestConfig["memory"],
        "-smp", guestConfig["cores"],
        guestConfig["kvm"],
        "-cdrom", guestConfig["cdrom"],
        "-hda", guestConfig["volume"],
        "-boot", guestConfig["boot"],
        "-net", guestConfig["net1"], 
        "-net", guestConfig["net2"], 
    ])


# Create a new image for the guest VM
def createImage(config, guestName, volumeSize):
    ROOT_PATH = Path(config['vm_root']).expanduser()
    volumeImage =  f"{ROOT_PATH}/{guestName}/{guestName}.qcow2"

    print(f"Creating new volume with size: {volumeSize}")

    # Create dir if not exists
    if not os.path.exists(f"{ROOT_PATH}/{guestName}/"):
        os.makedirs(f"{ROOT_PATH}/{guestName}/")


    # Wrapper for qemu-img to create an image
    subprocess.run(["qemu-img", "create", "-f", "qcow2", volumeImage, volumeSize]) 


# Create the guest VM
def createGuest(config, guestName, guestMemory, guestCores, guestISO, guestVolume):
    ROOT_PATH = Path(config['vm_root']).expanduser()
    guestConfigPath = f"{ROOT_PATH}/{guestName}/{guestName}.json"

    # Create dir if not exists
    if not os.path.exists(f"{ROOT_PATH}/{guestName}/"):
        os.makedirs(f"{ROOT_PATH}/{guestName}/")

        
    # Define the config for guest parameters
    guestConfig = {
        "name":     guestName,
        "memory":   guestMemory,
        "cores":    guestCores,
        "kvm":      "-enable-kvm",
        "cdrom":    guestISO,
        "volume":   guestVolume,
        "boot":     "d",
        "net1":     "nic",
        "net2":     "user"
    }

    # Create boot instructions
    with open(guestConfigPath, 'w') as f:
        json.dump(guestConfig, f, indent=2)

    print(f"Config {guestConfigPath} created")


# Main
if __name__ == "__main__":
    # Get args: $0 -c -n name -m 1024 -v 20G
    parser = argparse.ArgumentParser(description="Deploys quest virtual machines")
    parser.add_argument("-b", "--boot", help="Boots an existing virtual machine")
    parser.add_argument("-c", "--create", action="store_true", help="Creates a new virtual machine")
    parser.add_argument("-cpu", "--cpu", help="Sets cpu cores")
    parser.add_argument("-i", "--cdrom", help="Sets ISO for cdrom")
    parser.add_argument("-m", "--memory", help="Sets the memory of the deployed VM")
    parser.add_argument("-n", "--name", help="Create a new guest VM with given name")
    parser.add_argument("-v", "--volume", help="Create a volume")
    args = parser.parse_args()

    config = loadConfig()


    # Boots an existing VM
    if args.boot:
        bootGuest(config, args.boot)

    # Create new VM
    if args.create:
        # Name
        if args.name:
            guestName = args.name
        else:
            print("Error: No name given to guest machine")
            sys.exit(1)

        # Memory
        if args.memory:
            guestMemory = args.memory
        else:
            print("Error: No memory allocated to guest machine")
            sys.exit(1)

        # CPU Cores
        if args.cpu:
            guestCores = args.cpu
        else:
            print("Error: No cores allocated to guest machine")
            sys.exit(1)

        # CDROM
        if args.cdrom:
            guestISO = args.cdrom
        else:
            print("Error: No ISO is allocated to guest machine")
            sys.exit(1)

        # Volume
        if args.volume:
            createImage(config, guestName, args.volume)
        else:
            print("Error: No volume given to guest machine")
            sys.exit(1)
        
        # Create Guest VM
        createGuest(config, guestName, guestMemory, guestCores, guestISO, guestName + ".qcow2")
    