// initialize the map
var layer = new L.StamenTileLayer("toner");
var map = new L.Map("mapid", {
    center: new L.LatLng(30, 25),
    zoom: 3
});
map.addLayer(layer);


var nycMarker = L.marker([41.33, -77], {icon: L.icon({iconUrl: '../static/img/nyc.png', iconSize: [55, 55]})});
nycMarker.on('click', function (e) {
    window.location.replace('nyc');
});

var londonMarker = L.marker([56.3, -3], {icon: L.icon({iconUrl: '../static/img/london.png', iconSize: [50, 50]})});
londonMarker.on('click', function (e) {
    window.location.replace('london');
});

var parisMarker = L.marker([47.52, 2.2], {icon: L.icon({iconUrl: '../static/img/paris.png', iconSize: [45, 45]})});
parisMarker.on('click', function (e) {
    window.location.replace('paris');
});

var beijingMarker = L.marker([38.92, 116.46], {
    icon: L.icon({
        iconUrl: '../static/img/beijing.png',
        iconSize: [55, 55]
    })
});
beijingMarker.on('click', function (e) {
    window.location.replace('beijing');
});

var tokyoMarker = L.marker([35.42, 139.46], {icon: L.icon({iconUrl: '../static/img/tokyo.png', iconSize: [45, 45]})});
tokyoMarker.on('click', function (e) {
    window.location.replace('tokyo');
});

var clusters = L.markerClusterGroup();
clusters.addLayer(nycMarker);
clusters.addLayer(londonMarker);
clusters.addLayer(parisMarker);
clusters.addLayer(beijingMarker);
clusters.addLayer(tokyoMarker);
map.addLayer(clusters);
