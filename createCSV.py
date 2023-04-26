import csv
import glob
"""by rene Avila,Luis Robledo and Diego iñigez"""

Graffiti =glob.glob(".\\Graffiti\\*")
Graffiti = list(map(lambda line: line.replace(".\\Graffiti\\",""),Graffiti))
GraffitiPath = "./Gaffiti/"

PopArt = glob.glob(".\\PopArt\\*")
PopArt = list(map(lambda line: line.replace(".\\PopArt\\",""),PopArt))
PopArtPath = "./PopArt/"

Cubism = glob.glob(".\\Cubism\\*")
Cubism = list(map(lambda line: line.replace(".\\Cubism\\",""),Cubism))
CubismPath = "./Cubism/"
# ./Gaffiti/Graffiti_1.png
with open('ImagesData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Path", "tag"])
    for image in Graffiti:
        writer.writerow([GraffitiPath+image,"Graffiti"])

    for image in PopArt:
        writer.writerow([PopArtPath+image,"PopArt"])

    for image in Cubism:
        writer.writerow([CubismPath+image,"Cubism"])
