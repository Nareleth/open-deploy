import argparse
import subprocess

def createImage(guestName, size):
    volumeImage =  guestName + ".qcow2"
    volumeSize = size

    print(f"Creating new volume with size: {volumeSize}")

    # Wrapper for qemu-img to create an image
    subprocess.run(["qemu-img", "create", "-f", "qcow2", volumeImage, volumeSize]) 


if __name__ == "__main__":
    # Get args
    parser = argparse.ArgumentParser(description="Deploys quest virtual machines")
    parser.add_argument("-n", "--name", help="Create a new guest VM with given name")
    parser.add_argument("-v", "--volume", help="Create a volume")

    args = parser.parse_args()

    if args.name:
        print(f"Creating new guest: {args.name}")
        guestName = args.name

    if args.volume:
        createImage(guestName, args.volume)