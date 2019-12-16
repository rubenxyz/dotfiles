#!/bin/python

#Change working directory
import os
os.chdir("/Users/admin/dotfiles")
print("CHANGED WORKING DIR TO : %s" % os.getcwd())

# Create target Directory if don't exist
if not os.path.exists("spotylist"):
    os.mkdir("spotylist")
    print("DIRECTORY" , "SPOTYLIST" ,  "CREATED ")
else:
    print("DIRECTORY" , "SPOTYLIST" ,  "ALREADY EXISTS")

os.chdir("/Users/admin/dotfiles/spotylist")
print("CHANGED WORKING DIR TO : %s" % os.getcwd())

#pop-trancilo
#os.system("spotdl --playlist https://open.spotify.com/playlist/3D8OkJpFXcWmzHzoj8FVJb")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/pop-trancilo.txt -f /Volumes/Seagate4TB/spoty/pop-trancilo/")
#print("DOWNLOAD COMPLETE")

#pop-feel-good-downtempo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/2fH0lCSwgwimjVMa8ndZnX")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/pop-feel-good-downtempo.txt -f /Volumes/Seagate4TB/spoty/pop-feel-good-downtempo/")
#print("DOWNLOAD COMPLETE")

#funk
#os.system("spotdl --playlist https://open.spotify.com/playlist/47YJJyhaXIVtCdJwu0OZib")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/funk.txt -f /Volumes/Seagate4TB/spoty/funk/")
#print("DOWNLOAD COMPLETE")

##soul-epic-anthems
#os.system("spotdl --playlist https://open.spotify.com/playlist/3lp9w3k7nzC24JtnkRkcsp")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-epic-anthems.txt -f /Volumes/Seagate4TB/spoty/soul-epic-anthems/")
#print("DOWNLOAD COMPLETE")

#vocal-jazz.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/5iSNw9LGb5Qtt6zJcWBdfn")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/vocal-jazz.txt -f /Volumes/Seagate4TB/spoty/vocal-jazz/")
#print("DOWNLOAD COMPLETE")

#disco-soulful.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/2v6etNkjpP0Kk6ydUTXMZS")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/disco-soulful.txt -f /Volumes/Seagate4TB/spoty/disco-soulful/")
#print("DOWNLOAD COMPLETE")

##jazz-vocal-feel-good.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/0AOXNA8QaV3h00MQo8KbbF")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/jazz-vocal-feel-good.txt -f /Volumes/Seagate4TB/spoty/jazz-vocal-feel-good/")
#print("DOWNLOAD COMPLETE")

##jazz-vocal-trancilo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/7l0FugxAC3wuzskfyAhg2M")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/jazz-vocal-trancilo.txt -f /Volumes/Seagate4TB/spoty/jazz-vocal-trancilo/")
#print("DOWNLOAD COMPLETE")

##jazz-vocal-upptempo-feel-good.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/6Oi0ZAu2iRW8vKPnhgNc29")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/jazz-vocal-upptempo-feel-good.txt -f /Volumes/Seagate4TB/spoty/jazz-vocal-upptempo-feel-good/")
#print("DOWNLOAD COMPLETE")

##soul-50s.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/4XmD6UfugyowyFP95EaeFk")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-50s.txt -f /Volumes/Seagate4TB/spoty/soul-50s/")
#print("DOWNLOAD COMPLETE")

##soul-80s-uptempo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/0Ssr45Xx0fvpshB8BtR3cH")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-80s-uptempo.txt -f /Volumes/Seagate4TB/spoty/soul-80s-uptempo/")
#print("DOWNLOAD COMPLETE")

##soul-power-ballad#
#os.system("spotdl --playlist https://open.spotify.com/playlist/6GJsIbNAJzyqHGLrawP0Dx")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-power-ballad.txt -f /Volumes/Seagate4TB/spoty/soul-power-ballad/")
#print("DOWNLOAD COMPLETE")

##soul.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/2o0osNy726Mqy2pBcBXVex")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul.txt -f /Volumes/Seagate4TB/spoty/soul/")
#print("DOWNLOAD COMPLETE")

##soul-trancilo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/143WqTgnQLZ3yxSQf5iWms")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-trancilo.txt -f /Volumes/Seagate4TB/spoty/soul-trancilo/")
#print("DOWNLOAD COMPLETE")

##soul-procreate.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/5BP4Cd6DfaOcDa6JljiJW0")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-procreate.txt -f /Volumes/Seagate4TB/spoty/soul-procreate/")
#print("DOWNLOAD COMPLETE")

##soul-feel-good-uptempo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/4IEnT8IOwoxTPJ00CbMnHa")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-feel-good-uptempo.txt -f /Volumes/Seagate4TB/spoty/soul-feel-good-uptempo/")
#print("DOWNLOAD COMPLETE")

##soul-feel-good-downtempo.txt
#os.system("spotdl --playlist https://open.spotify.com/playlist/02uLOt3fI0Bz3ul5TTJfMF")
#print("SUCCESFULLY CREATED PLAYLIST FILE")
#print("DOWNLOAD IS INITIATED")
#os.system("spotdl --list ~/dotfiles/spotylist/soul-feel-good-downtempo.txt -f /Volumes/Seagate4TB/spoty/soul-feel-good-downtempo/")
#print("DOWNLOAD COMPLETE")

#/bloomer/core
os.system("spotdl --playlist https://open.spotify.com/playlist/59jbfdlOBCxxqxdXSAEiQK")
print("SUCCESFULLY CREATED PLAYLIST FILE")
print("DOWNLOAD IS INITIATED")
os.system("spotdl --list ~/dotfiles/spotylist/bloomercore.txt -f /Volumes/Seagate4TB/spoty/bloomercore/")
print("DOWNLOAD COMPLETE")
