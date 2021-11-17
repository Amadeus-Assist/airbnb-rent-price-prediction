const lngList = {
    "nyc": [40.77, -73.97, 11],
}

// initialize the map
var map = L.map('mapid').setView([lngList[city][0], lngList[city][1]], lngList[city][2]);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: '<a href="https://www.mapbox.com/">Mapbox</a> by Liqin Zhang',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ3JhdmVzY243IiwiYSI6ImNrdzFiMmNsbmEyeGwybnFwdzdwdXh3bWgifQ.yrP_vrJ8VRA-1uqTUwkPig'
}).addTo(map);


// add neighborhoods
$.getJSON("../../static/data/" + city + "-neighborhoods.geojson", function (neighborhoods) {
    L.geoJson(neighborhoods, {
        style: function () {
            return {color: "rgba(44,66,194,0.95)", weight: 2, fillColor: "#416272", fillOpacity: .4};
        }
    }).addTo(map);
});

// add houses
$.getJSON("../../static/data/" + city + "_feature.geojson", function (houses) {
    var rooms = L.geoJson(houses, {
        pointToLayer: function (feature, lat_lng) {
            var room = L.marker(lat_lng);
            room.bindPopup(feature.properties.name + '<br/>' + feature.properties.price);
            return room;
        }
    });
    var markers = L.markerClusterGroup();
    markers.addLayer(rooms);
    map.addLayer(markers);
});