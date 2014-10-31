all: output/bedford.json

build/Reconstructed-UK-postcode-polygons-March-2014.zip: 
	cd build && wget http://www.opendoorlogistics.com/wp-content/uploads/2014/04/Reconstructed-UK-postcode-polygons-March-2014.zip

# The folder the uk postcode polygons extract to
build/Distribution/Sectors.shp: build/Reconstructed-UK-postcode-polygons-March-2014.zip
	cd build && unzip Reconstructed-UK-postcode-polygons-March-2014.zip
	touch build/Distribution/Sectors.shp

build/geojson/sectors.json: build/Distribution/Sectors.shp
	cd build/geojson && ogr2ogr -f GeoJSON sectors.json ../Distribution/Sectors.shp

build/topojsonSectors.json: build/geojson/sectors.json
	topojson -o build/topojsonSectors.json --properties name=name build/geojson/sectors.json

build/sectorData.json: perSectorData.py data/ofcom-broadband-bedford.csv
	python perSectorData.py

output/bedford.json: build/topojsonSectors.json extractBedford.py build/sectorData.json
	python extractBedford.py
