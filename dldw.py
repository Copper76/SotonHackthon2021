import bs4
import urllib.request
import re

MAX_SEASONS = 24
MAX_EPISODES = 30

base = "http://www.chakoteya.net/DoctorWho/"

scripts = ""

for i in range(1, MAX_SEASONS + 1):
    for j in range(1, MAX_EPISODES + 1):

        print("Processing season {} episode {}".format(i, j))

        # Construct link address
        suffix = "{}-{}.htm".format(i, j)
        link = base + suffix

        # Open page and extract body text
        try:
            webpage = str(urllib.request.urlopen(link).read())
            soup = bs4.BeautifulSoup(webpage, features="html.parser")
            soup = soup.tbody.text

        except:
            # Skip to next if season doesn't exist
            break

        # Strip carriage returns and shit
        text = soup.replace("\\r\\n", "\n").replace("\\n","\n").replace("\\","")

        scripts += text

# Write scripts to file
f = open("dwscripts.txt", "w")
f.write(scripts)
f.close()

print("Finished writing scripts")
