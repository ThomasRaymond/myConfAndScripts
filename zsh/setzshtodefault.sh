#! /bin/bash
[ ! $(id -u) == "0" ] || { echo "ERROR: You should't be root"; exit 1; }
chsh -s /bin/zsh
source ~/.zshrc