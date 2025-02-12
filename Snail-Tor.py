#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os
import time
import os as sistema

os.system("cd ~;pkg install tor nginx")

os.system("cd banner;python Bann3r.py")
print
print ("\033[49m                   Welcome To Snail-Tor              \033[0m")
print ("\033[48m                   Author: Krypton-777                 \033[0m")

os.system("cd banner;python Table.py")

def creator_program():
    print("Snail-Tor by Krypton-777:")

def edit_hidden_service():
    os.system("cd ~;cd ../usr/share/nginx;cd html;nano index.html")

def create_hidden_service():
    os.system("cd ~; cd ../usr/var/lib;mkdir tor;cd tor;mkdir hidden_service;cd;cat ../usr/var/lib/tor/hidden_service/hostname")

def config_config():
    os.system("cd ~;nano ../usr/etc/tor/torrc")
    
def main():
    while True:
        creator_program()
        
        option = input("Choose an option: ")
        
        if option == "03":
            edit_hidden_service()
        elif option == "02":
            create_hidden_service()
        elif option == "01":
            config_config()
        elif option == "00":
            sys.exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()