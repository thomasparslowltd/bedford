import csv

bedfordPostcodes = set(["MK40 3", "MK45 3", "MK40 2", "MK40 4", "MK41 0", "MK41 6", "MK41 7", "MK41 8", "MK42 0", "MK42 6", "MK42 7", "MK42 8", "MK42 9", "MK43 7", "MK43 8", "MK43 9", "MK44 1", "MK44 2", "MK44 3", "MK41 9", "MK40 1"])

postcodes = csv.DictReader(open("data/postcodes.csv", "rb"))
lats = []
lons = []
for pc in postcodes:
    if pc["Postcode"][:-2] in bedfordPostcodes:
        lats.append(pc["Latitude"])
        lons.append(pc["Longitude"])
        
print min(lats), min(lons), max(lats), max(lons)
