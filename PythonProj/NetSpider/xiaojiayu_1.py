import urllib.request as ur
import os
print(os.getcwd())
reponse = ur.urlopen("http://placekitten.com/500/600")
cat_img = reponse.read()
with open('cat_500_600.jpg') as f:
    f.write(cat_img)
print(cat_img)