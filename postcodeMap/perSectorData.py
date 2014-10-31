import csv, json
import heatmap

sectors = {x.replace(" ", ""): {"connections": 0, "people": 0, "households": 0}
             for x in ["MK40 3", "MK45 3", "MK40 2", "MK40 4", "MK41 0", "MK41 6", "MK41 7", "MK41 8", "MK42 0", "MK42 6", "MK42 7", "MK42 8", "MK42 9", "MK43 7", "MK43 8", "MK43 9", "MK44 1", "MK44 2", "MK44 3", "MK41 9", "MK40 1"]}

ofcom = csv.DictReader(open("data/ofcom-broadband-bedford.csv", "rb"))

for d in ofcom:
    sec = d["Postcode"][:-2]
    if sec in sectors:
        sectors[sec]["connections"] += int(2 if d["Number of connections"] == "<3" else d["Number of connections"])
        sectors[sec]["people"] += int(d["Total"])
        sectors[sec]["households"] += int(d["Occupied_Households"])

deprivation = csv.DictReader(open("data/deprivation.csv", "rb"))
for dep in deprivation:
    sec = dep["postcode"][:-2].replace(" ", "")
    if sec in sectors:
        sectors[sec]["IMD"] = int(dep["IMD-rank"])
    else:
        print sec

json.dump(sectors, open("build/sectorData.json", "wb"))
