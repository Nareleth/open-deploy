import argparse
import json
import os
import subprocess
import sys


# Boot existing guest VM
def bootGuest(guestName):
    print(f"Booting guest: {guestName}")

    bootConfig = f"{guestName}.json"

    # Validate input
    if not os.path.exists(bootConfig):
        print(f"Error: File not exists")
        sys.exit(1)

    
    # Read config file
    with open(bootConfig, 'r') as f:
        config = json.load(f)

    subprocess.run([
        "qemu-system-x86_64",
        "-m", config["memory"],
        "-smp", config["cores"],
        config["kvm"],
        "-cdrom", config["cdrom"],
        "-hda", config["volume"],
        "-boot", config["boot"],
        "-net", config["net1"], 
        "-net", config["net2"], 
    ])


# Create a new image for the guest VM
def createImage(guestName, size):
    volumeImage =  guestName + ".qcow2"
    volumeSize = size

    print(f"Creating new volume with size: {volumeSize}")

    # Wrapper for qemu-img to create an image
    subprocess.run(["qemu-img", "create", "-f", "qcow2", volumeImage, volumeSize]) 


# Create the guest VM
def createGuest(guestName, guestMemory, guestCores, guestISO, guestVolume):
    guestConfig = guestName + ".json"

    config = {
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
    with open(guestConfig, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"Config {guestConfig} created")


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


    # Boots an existing VM
    if args.boot:
        bootGuest(args.boot)

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
            createImage(guestName, args.volume)
        else:
            print("Error: No volume given to guest machine")
            sys.exit(1)
        
        # Create Guest VM
        createGuest(guestName, guestMemory, guestCores, guestISO, guestName + ".qcow2")
    