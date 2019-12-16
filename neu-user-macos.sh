#!/usr/bin/env bash

# WARNING - Do not run this script without reading every line (and understanding it)

# Close any open System Preferences panes, to prevent them from overriding settings we’re about to change
osascript -e 'tell application "System Preferences" to quit'

# Ask for the administrator password upfront
sudo -v

# Keep-alive: update existing `sudo` time stamp until `.macos` has finished
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

################################################################################


# script goes here.


###############################################################################
# Kill affected applications                                                  #
###############################################################################

# Kill affected applications
for app in Finder Dock Mail Safari iTunes iCal Address\ Book SystemUIServer; do killall "$app" > /dev/null 2>&1; done
echo "macOS Hacks Done. Note that some of these changes require a logout/restart to take effect."
