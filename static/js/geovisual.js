const lngList = {
    "nyc": [40.77, -73.97, 11],
}

// initialize the map
var layer = new L.StamenTileLayer("toner");
var map = new L.Map("mapid", {
    center: new L.LatLng(lngList[city][0], lngList[city][1]),
    zoom: lngList[city][2]
});
map.addLayer(layer);

// add neighborhood layer
$.getJSON("../static/data/" + city + "-neighborhoods.geojson", function (hoodData) {
    L.geoJson(hoodData, {
        style: function (feature) {
            var fillColor = "#607d8b";
            return {color: "#3f51b5", weight: 4, fillColor: fillColor, fillOpacity: .6};
        },
        onEachFeature: function (feature, layer) {
            layer.bindPopup("<strong>" + feature.properties.name + "</strong><br/>")
        }
    }).addTo(map);
});

// add marker
$.getJSON("../static/data/" + city + "_pre.geojson", function (data) {
    var roomIcon = L.icon({
        iconUrl: '../static/img/pin.png',
        iconSize: [40, 40]
    });
    var rooms = L.geoJson(data, {
        pointToLayer: function (feature, latlng) {
            var marker = L.marker(latlng, {icon: roomIcon});
            marker.bindPopup(feature.properties.name + '<br/>' + feature.properties.price);
            return marker;
        }
    });
    var clusters = L.markerClusterGroup();
    clusters.addLayer(rooms);
    map.addLayer(clusters);
});