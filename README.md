⠀⠀⠀⣤⣄⠀⠀⠀⠀⠀⠀⢀⣤⠶⠒⠚⠛⠒⠲⢦⣄⠀⠀⠀⠀⠀⠀
⣤⡄⠀⠛⡿⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀
⠙⢻⡀⠀⣧⠀⠀⠀⠀⢰⡇⠀⠀⠀⣠⡴⠞⠛⠓⢶⣄⠀⠸⣆⠀⠀⠀
⠀⠈⢳⠶⠛⠛⠶⣄⠀⠸⡇⠀⢀⡾⠁⢀⡴⠶⢶⡄⠙⣧⠀⢻⠀⠀⠀
⠀⠀⣟⠀⠀⠀⠀⠹⣦⡤⠿⠀⢸⡇⢠⡟⢀⡾⠀⣿⠀⣿⠀⣼⠁⠀⠀
⠀⠀⢻⡀⠀⠀⠀⠀⠻⣄⠀⠀⠸⣇⠀⢷⡀⠛⠛⢁⣴⠃⣠⠏⠀⠀⠀
⠀⠀⠀⠻⣆⠀⠀⠀⠀⠈⠳⢦⣄⣙⣷⣄⣉⠛⠛⣋⣠⡴⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢦⣄⡀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠓⠒⠶⠞⣻⠂
⠀⠀⠀⠀⠀⠀⠘⢧⣤⡤⠖⠓⠶⠤⠶⠒⠶⠴⠞⠛⠶⠞⠛⠛⠛⠁⠀

## Snail-Tor :

Snail-Tor is a tool that facilitates the creation and editing of hidden services, attention: You may modify and re-distribute this software as long as the project name "Snail-Tor", credit to the author "Krypton-777". Otherwise, the license agreement will be violated and a takedown notice will be issued.

## License :

You may modify and re-distribute this software as long as the project name "Snail-Tor", credit to the author "Krypton-777". Otherwise, the license agreement will be violated and a takedown notice will be issued.

## Installation (Termux):

apt update && apt upgrade -y

pkg install git -y

pkg install python3 -y

git clone https://github.com/Krypton-777/Snail-Tor

cd Snail-Tor

python Snail-Tor.py

## How to use :

STEP 1 : enter option 01 (Config) and change:

#HiddenServiceDir /data/data/com.termux/files/usr/var/lib/tor/hidden_service/

#HiddenServicePort 80 127.0.0.1:80

To:

HiddenServiceDir /data/data/com.termux/files/usr/var/lib/tor/hidden_service/

HiddenServicePort 80 127.0.0.1:8080

STEP 2 : Create hidden service

STEP 3 : Edit hidden service

###########################################################

A project by Krypton-777