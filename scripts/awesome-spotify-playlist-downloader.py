#!/bin/python

import os
print("Welcome to Ruben's Spotify Playlist Downloader")

#################################
#       Setting variables       #
#################################

print("Setting variables to memory")

#Path to the txt-files with the song URLs 
txtPath = "~/dotfiles/spotylist/"

#Path for the mp3s to be downloaded
downloadPath = "/Volumes/Seagate4TB/spoty/"

#Commands array
systemCommand = "brew update && brew upgrade && brew cleanup",
                "brew install ffmpeg",
                "pip3 install --upgrade spotdl",
                "pip3 install --upgrade youtube_dl"]

spotdlCommand = "spotdl --playlist",
                "spotdl --list"]

#Array with the names of playlists
playlistNames = ["pop-trancilo",
                 "pop-feel-good-downtempo",
                 "funk",
                 "soul-epic-anthems",
                 "vocal-jazz",
                 "disco-soulful",
                 "jazz-vocal-feel-good",
                 "jazz-vocal-trancilo",
                 "jazz-vocal-upptempo-feel-good",
                 "soul-50s",
                 "soul-80s-uptempo",
                 "soul-power-ballad",
                 "soul",
                 "soul-trancilo",
                 "soul-procreate",
                 "soul-feel-good-uptempo",
                 "soul-feel-good-downtempo",
                 "bloomer",
                 "boomer",
                 "aurora"]

#platlist array with the spotify URLs
playlists = ["https://open.spotify.com/playlist/3D8OkJpFXcWmzHzoj8FVJb",
             "https://open.spotify.com/playlist/2fH0lCSwgwimjVMa8ndZnX",
             "https://open.spotify.com/playlist/47YJJyhaXIVtCdJwu0OZib",
             "https://open.spotify.com/playlist/3lp9w3k7nzC24JtnkRkcsp",
             "https://open.spotify.com/playlist/5iSNw9LGb5Qtt6zJcWBdfn",
             "https://open.spotify.com/playlist/2v6etNkjpP0Kk6ydUTXMZS",
             "https://open.spotify.com/playlist/0AOXNA8QaV3h00MQo8KbbF",
             "https://open.spotify.com/playlist/7l0FugxAC3wuzskfyAhg2M",
             "https://open.spotify.com/playlist/6Oi0ZAu2iRW8vKPnhgNc29",
             "https://open.spotify.com/playlist/4XmD6UfugyowyFP95EaeFk",
             "https://open.spotify.com/playlist/0Ssr45Xx0fvpshB8BtR3cH",
             "https://open.spotify.com/playlist/6GJsIbNAJzyqHGLrawP0Dx",
             "https://open.spotify.com/playlist/2o0osNy726Mqy2pBcBXVex",
             "https://open.spotify.com/playlist/143WqTgnQLZ3yxSQf5iWms",
             "https://open.spotify.com/playlist/5BP4Cd6DfaOcDa6JljiJW0",
             "https://open.spotify.com/playlist/4IEnT8IOwoxTPJ00CbMnHa",
             "https://open.spotify.com/playlist/02uLOt3fI0Bz3ul5TTJfMF",
             "https://open.spotify.com/playlist/5Kpa0rttkF2AMuDdeqNNSw",
             "https://open.spotify.com/playlist/1IaJAL6La4fmSuvTdrD3z5",
             "https://open.spotify.com/playlist/2QUS9543nzCPjilCmps60Y"]

#################################
#       DEPENDENCIES            #
#################################

print("Running dependencies")
os.system("brew update && brew upgrade && brew cleanup")
os.system("brew install ffmpeg")
os.system("pip3 install --upgrade spotdl")
os.system("pip3 install --upgrade youtube_dl")

##################################
#Setting and creating directories#
##################################


#Change working directory
os.chdir("/Users/admin/dotfiles")
print("CHANGED WORKING DIR TO : %s" % os.getcwd())

# Create target Directory if don't exist
if not os.path.exists("spotylist"):
    os.mkdir("spotylist")
    print("DIRECTORY" , "SPOTYLIST" ,  "CREATED ")
else:
    print("DIRECTORY" , "SPOTYLIST" ,  "ALREADY EXISTS")

os.chdir("/Users/admin/dotfiles/spotylist/")

print("CHANGED WORKING DIR TO : %s" % os.getcwd())

#################################
#       DOWNLOAD LOOP           #
#################################

i = 0
while i < len(playlists):
    os.system(spotdl --playlist {}".format(playlists[i]))
    print("SUCCESFULLY CREATED TXT-FILE FOR: {}".format(playlistNames[i]))
    print("DOWNLOAD IS INITIATED FOR: {}".format(playlistNames[i]))
    os.system("spotdl --list {0}{2}.txt -f {1}{2}/".format(txtPath, downloadPath,playlistNames[i]))
    print("DOWNLOAD OF '{}' COMPLETE".format(playlistNames[i]))
    i += 1

print("The download-loop is done. 'i' should be 20. It is = {}".format(i))
