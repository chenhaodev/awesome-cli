#brew install youtube-dl
#youtube-dl -F <youtube-url> 
#youtube-dl -f ID <youtube-url>

import os
import sys

url = sys.argv[1]
try:
    cmd = 'youtube-dl -f 18' + url # assume id:18 refers to the mini-mp4 format.
    os.system(cmd)
except:

    cmd = 'youtube-dl -F ' + url + ' > temp.txt'
    os.system(cmd)
    
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if (line.find(' mp4 ') != -1) and (line.find(' 480p ') != -1): #assume most videos shall have mp4 and 480p format. 
        #if (line.find(' '+sys.argv[1]+' ') != -1) and (line.find(' '+ sys.argv[2] +' ') != -1):
            print(line)
            break
    
    id = line.split(' ')[0]; #id = int(id)
    
    cmd = 'youtube-dl -f ' + id + ' ' + url 
    os.system(cmd)
    os.system('rm temp.txt')

