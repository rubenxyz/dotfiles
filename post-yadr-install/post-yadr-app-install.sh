#!/bin/bash

#This stupidly simple script that installs my "essential" FOSS apps. 

#Runs a update for good mesure.
brew update

#Runs upgrade for good mesure.
brew upgrade

#Intall CLI apps
brew install mediainfo youtube-dl ffmpeg exiftool python3 buo/cask-upgrade android-platform-tools signify-osx

#Install GUI apps
brew cask install tor-browser audacity gimp dropbox teamviewer filezilla disk-inventory-x karabiner-elements aegisub dropbox veracrypt alfred firefox keepassxc virtualbox android-file-transfer vlc appcleaner mediainfo atom google-backup-and-sync osxfuse wickrme avast-security google-chrome thunderbird calibre handbrake transmission syncthing

#Installs pip apps
pip3 spotdl

echo "Post-yadr-app-install was succesfull."
