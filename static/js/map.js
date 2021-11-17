// world map layer
var mymap = L.map('worldmapid').setView([40.77, -73.97], 3.5);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: '<a href="https://www.mapbox.com/">Mapbox</a> by Liqin Zhang',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZ3JhdmVzY243IiwiYSI6ImNrdzFiMmNsbmEyeGwybnFwdzdwdXh3bWgifQ.yrP_vrJ8VRA-1uqTUwkPig'
}).addTo(mymap);

var nyc_marker = L.marker([40.77, -73.97]).addTo(mymap);
nyc_marker.on('click', function (e) {
    window.location.replace('cityview/nyc');
});