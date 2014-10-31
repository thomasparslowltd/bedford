import csv, json
import heatmap

bedfordPostcodes = set(x.replace(" ", "") for x in ["MK40 3", "MK45 3", "MK40 2", "MK40 4", "MK41 0", "MK41 6", "MK41 7", "MK41 8", "MK42 0", "MK42 6", "MK42 7", "MK42 8", "MK42 9", "MK43 7", "MK43 8", "MK43 9", "MK44 1", "MK44 2", "MK44 3", "MK41 9", "MK40 1"])

print "Getting postcodes"
try:
    postcodes = json.load(open("build/postcodeLookup.json", "rb"))
    print "loaded postcodes from cache file"
except:
    postcodes = {x["Postcode"].replace(" ", ""): (float(x["Latitude"]) , float(x["Longitude"])) for x in csv.DictReader(open("data/postcodes.csv", "rb")) if x["Postcode"].replace(" ", "")[:-2] in bedfordPostcodes}
    json.dump(postcodes, open("build/postcodeLookup.json", "wb"))
# print postcodes
print "Got postcodes"

data = csv.DictReader(open("data/ofcom-broadband-bedform.csv", "rb"))

print bedfordPostcodes
for broadband in data:
    if broadband["Postcode"][:-2] in bedfordPostcodes:
        if broadband["Postcode"] not in postcodes:
            print "Location not found", broadband["Postcode"]
        else:
            print postcodes[broadband["Postcode"]]
