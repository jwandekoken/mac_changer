import subprocess
import argparse

parser = argparse.ArgumentParser(description='Changes the informed network interface MAC address.')
parser.add_argument('-i', '--interface', dest='interface', help='Interface to change its MAC address')
parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC address')

args = parser.parse_args()

interface = args.interface
new_mac = args.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.run(["ifconfig", interface, "down"])
subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.run(["ifconfig", interface, "up"])

