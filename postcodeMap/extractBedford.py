import json

bedfordPostcodes = set(["MK40 3", "MK45 3", "MK40 2", "MK40 4", "MK41 0", "MK41 6", "MK41 7", "MK41 8", "MK42 0", "MK42 6", "MK42 7", "MK42 8", "MK42 9", "MK43 7", "MK43 8", "MK43 9", "MK44 1", "MK44 2", "MK44 3", "MK41 9", "MK40 1"])

sectors = json.load(open("build/topojsonSectors.json", "rb"))
sectors["objects"]["sectors"]["geometries"] = [x for x in sectors["objects"]["sectors"]["geometries"]
                                                      if x["properties"]["name"] in bedfordPostcodes]

# sectors["objects"]["sectors"]["geometries"] = [x for x in sectors["objects"]["sectors"]["geometries"]
#                                                       if x["properties"]["name"].startswith("MK")]

# Add in the sector data
sectorData = json.load(open("build/sectorData.json","rb"))
for sector in sectors["objects"]["sectors"]["geometries"]:
    postcodeSector = sector["properties"]["name"].replace(" ","")
    if postcodeSector in sectorData:
        sector["properties"].update(sectorData[postcodeSector])

json.dump(sectors, open("output/bedford.json", "wb"))
