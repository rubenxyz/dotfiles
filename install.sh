#!/usr/bin/env bash

# WARNING - Do not run this script without reading every line (and understanding it)

# Close any open System Preferences panes, to prevent them from overriding settings we’re about to change
osascript -e 'tell application "System Preferences" to quit'

# Ask for the administrator password upfront
sudo -v

# Keep-alive: update existing `sudo` time stamp until `.macos` has finished
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

################################################################################

#INSTALL YADR
sh -c "`curl -fsSL https://raw.githubusercontent.com/skwp/dotfiles/master/install.sh`"

#Run post-yadr-install script
sh -c "`curl -fsSL https://raw.githubusercontent.com/rubensz/dotfiles/master/post-yadr-install/yadr-post-install.sh`"

#Run post-yadr-app-install script
sh -c "`curl -fsSL https://raw.githubusercontent.com/rubensz/dotfiles/master/post-yadr-install/post-yadr-app-install.sh`"

#Run sensible-macos-settings
sh -c "`curl -fsSL https://raw.githubusercontent.com/rubensz/dotfiles/master/post-yadr-install/sensible-macos-settings.sh`"

echo "Rubensz dotfiles installtion is done. Note that some of these changes require a logout/restart to take effect."
