import subprocess
import argparse
import re


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


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


args = get_arguments()
current_mac = get_current_mac(args.interface)
print("current_mac: ", current_mac)

change_mac(args.interface, args.new_mac)

current_mac = get_current_mac(args.interface)
if current_mac == args.new_mac:
    print("[+] MAC address was successfully changed to: ", current_mac)
else:
    print("[-] MAC address did not get changed.")
