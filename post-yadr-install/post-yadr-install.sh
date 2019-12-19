#!/bin/bash
#POST-YADR-INSTALL-SCRIPT
#YADR is awesome but this makes it even beter (for me).


######################################
# Uninstall selection of vim plugins #
######################################


######################################
#    Install additional plugins      #
######################################

#Support for Foutnain files
yadr vim-add-plugi -u https://github.com/mcchrish/fountain.vim

#Goyo, the undistracted writing plugin
yadr vim-add-plugin -u https://github.com/junegunn/goyo.vim

#Swiftly comment and uncomment lines
yadr vim-add-plugin -u https://github.com/manasthakur/vim-commentor

######################################
#       Append alias list            #
######################################
wget https://raw.githubusercontent.com/rubensz/dotfiles/master/post-yadr-install/ruben-alias.txt -O ~/.ruben/ruben-alias.txt 
cat ~/.ruben/ruben-alias.txt  >> ~/.yadr/zsh/aliases.zsh
rm ~/.ruben/ruben-alias.txt


############################

echo "Ruben's YADR post install script was succesfull"
