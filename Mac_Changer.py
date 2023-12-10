#! /usr/bin/env python

import subprocess
import optparse


def mac_changer(interface, New_Mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + New_Mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    print("Your new Mac Address is: " + New_Mac)
def get_argumets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change Mac Adresss")
    parser.add_option("-m", "--mac", dest="New_Mac", help="new Mac Address to use")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter an network interface")
    elif not options.New_Mac:
        parser.error("Please enter a Mac address")
    return options


options = get_argumets()
mac_changer(options.interface, options.New_Mac)
