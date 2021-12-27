import subprocess
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='Changes the informed network interface MAC address.')
    parser.add_argument('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC address')
    options = parser.parse_args()
    if not options.interface or not options.new_mac:
        parser.error("[-] Please specify an interface and a new_mac address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


args = get_arguments()
change_mac(args.interface, args.new_mac)

