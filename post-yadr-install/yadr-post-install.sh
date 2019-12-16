#!/bin/bash
#YADR-POST-INSTALL-SCRIPT
#YADR is awesome but this makes it even beter (for me).

############################
#Install additional plugins#
############################

#Support for Foutnain files
yadr vim-add-plugi -u https://github.com/mcchrish/fountain.vim

#Goyo, the undistracted writing plugin
yadr vim-add-plugin -u https://github.com/junegunn/goyo.vim

#Swiftly comment and uncomment lines
yadr vim-add-plugin -u https://github.com/manasthakur/vim-commentor

############################

echo "YADR post install script was succesfull"
