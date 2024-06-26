from ipyleaflet import basemaps

BASEMAPS = {
    "WorldImagery": basemaps.Esri.WorldImagery,
    "Mapnik": basemaps.OpenStreetMap.Mapnik,
    "Positron": basemaps.CartoDB.Positron,
    "DarkMatter": basemaps.CartoDB.DarkMatter,
    "NatGeoWorldMap": basemaps.Esri.NatGeoWorldMap,
    "France": basemaps.OpenStreetMap.France,
    "DE": basemaps.OpenStreetMap.DE,
}


CITIES = {
    "BUR":{"latitude":34.20061917, "longitude":-118.3584969, "altitude":33},
    "BWI":{"latitude":39.17540167, "longitude":-76.66819833, "altitude":36},
    "CMH":{"latitude":39.99798528, "longitude":-82.89188278, "altitude":35},
    "DEN":{"latitude":39.85840806, "longitude":-104.6670019, "altitude":44},
    "DTW":{"latitude":42.21205889, "longitude":-83.34883583, "altitude":39},
    "FAT":{"latitude":36.77619444, "longitude":-119.7181389, "altitude":71},
    "HSV":{"latitude":34.6404475, "longitude":-86.77310944, "altitude":34},
    "IAH":{"latitude":29.98047222, "longitude":-95.33972222, "altitude":21},
    "MEM":{"latitude":35.04241667, "longitude":-89.97666667, "altitude":44},
    "MFE":{"latitude":26.17583333, "longitude":-98.23861111, "altitude":156},
    "MTJ":{"latitude":38.50886722, "longitude":-107.8938333, "altitude":23},
    "OKC":{"latitude":35.39308833, "longitude":-97.60073389, "altitude":8},
    "OMA":{"latitude":41.30251861, "longitude":-95.89417306, "altitude":76},
    "RIC":{"latitude":37.50516667, "longitude":-77.31966667, "altitude":52},
    "SDF":{"latitude":38.17438889, "longitude":-85.736, "altitude":14},
    "SLC":{"latitude":40.78838778, "longitude":-111.9777731, "altitude":38},
    "XNA":{"latitude":36.28186944, "longitude":-94.30681111, "altitude":667},
    "SEA":{"latitude":47.44898194, "longitude":-122.3093131, "altitude":-2},
    "TPA":{"latitude":27.97547222, "longitude":-82.53325, "altitude":25},
    "BOS":{"latitude":42.3643475, "longitude":-71.00517917, "altitude":14},
    "KOA":{"latitude":19.73876583, "longitude":-156.0456314, "altitude":1634},
    "BDL":{"latitude":41.93887417, "longitude":-72.68322833, "altitude":3650},
    "LAS":{"latitude":36.08036111, "longitude":-115.1523333, "altitude":1400},
    "HDN":{"latitude":40.48118028, "longitude":-107.2176597, "altitude":33},
    "JAC":{"latitude":43.60732417, "longitude":-110.7377389, "altitude":36},
    "RDU":{"latitude":35.87763889, "longitude":-78.78747222, "altitude":35},
    "TUS":{"latitude":32.11608333, "longitude":-110.9410278, "altitude":44},
    "IAD":{"latitude":38.94453194, "longitude":-77.45580972, "altitude":39},
}
