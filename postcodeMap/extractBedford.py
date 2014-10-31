import json
sectors = json.load(open("build/topojsonSectors.json", "rb"))
sectors["objects"]["sectors"]["geometries"] = [x for x in sectors["objects"]["sectors"]["geometries"]
                                                      if x["properties"]["name"].startswith("MK")]
json.dump(sectors, open("output/bedford.json", "wb"))
