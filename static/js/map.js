// world map layer
var layer = new L.StamenTileLayer("toner");
var map = new L.Map("mapid", {
    center: new L.LatLng(40.77, -73.97),
    zoom: 3
});
map.addLayer(layer);


var nycMarker = L.marker([41.33, -77],
    {
        icon: L.icon({
            iconUrl: '../static/img/city.png',
            iconSize: [30, 30]
        })
    });
nycMarker.on('click', function (e) {
    window.location.replace('nyc');
});

var clusters = L.markerClusterGroup();
clusters.addLayer(nycMarker);
map.addLayer(clusters);
