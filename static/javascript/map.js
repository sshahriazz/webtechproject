// mapboxgl.accessToken = 'pk.eyJ1IjoicG9sYXNoMTk5NCIsImEiOiJjazd0Mm5mcGMwbHR6M2RxcnZ5dW9lMjk5In0.GLK9IKL-X2wmAMdfLRN7Dg';
// const coordinates = document.getElementById('coordinates');
// const lng = document.getElementById('lng');
// const lat = document.getElementById('lat');
// const map = new mapboxgl.Map({
//     container: 'map',
//     style: 'mapbox://styles/mapbox/streets-v11',
//     center: [90.37934213312536, 23.758343482800825],
//     zoom: 13
// });
// const marker = new mapboxgl.Marker({
//     draggable: true,
// });
//
// map.on('click', function (e) {
//     marker.setLngLat(e.lngLat)
//         .addTo(map);
//     coordinates.style.display = 'block';
//     coordinates.innerHTML =
//         'Longitude: ' + e.lngLat.lng + '<br />Latitude: ' + e.lngLat.lat;
//     lng.value = e.lngLat.lng;
//     lat.value = e.lngLat.lat;
//
//     function onDragEnd() {
//         const lngLat = marker.getLngLat();
//         coordinates.style.display = 'block';
//         coordinates.innerHTML =
//             'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
//         lng.value = lngLat.lng;
//         lat.value = lngLat.lat;
//     }
//
//     marker.on('drag', onDragEnd);
// });
//
//
// // Add zoom and rotation controls to the map.
// map.addControl(new MapboxGeocoder({accessToken: mapboxgl.accessToken, mapboxgl: mapboxgl}));
// map.addControl(new mapboxgl.NavigationControl());
// map.addControl(
//     new mapboxgl.GeolocateControl({
//         positionOptions: {
//             enableHighAccuracy: true,
//             maximumAge: 0
//         },
//         trackUserLocation: true,
//
//     })
// );
// // map.addControl(
// //   new MapboxDirections({
// //     accessToken: mapboxgl.accessToken
// //   }),
// //     'top-left'
// // );
mapboxgl.accessToken = 'pk.eyJ1IjoicG9sYXNoMTk5NCIsImEiOiJjazd0Mm5mcGMwbHR6M2RxcnZ5dW9lMjk5In0.GLK9IKL-X2wmAMdfLRN7Dg';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v10',
    center: [-122.662323, 45.523751], // starting position
    zoom: 9
});
// set the bounds of the map

// initialize the map canvas to interact with later
var canvas = map.getCanvasContainer();

// an arbitrary start will always be the same
// only the end or destination will change
var start = [-122.8624, 45.523751];

// this is where the code for the next step will go
// create a function to make a directions request
function getRoute(end) {
    // make a directions request using cycling profile
    // an arbitrary start will always be the same
    // only the end or destination will change
    var start = [-122.8624, 45.523751];
    var url = 'https://api.mapbox.com/directions/v5/mapbox/cycling/' + start[0] + ',' + start[1] + ';' + end[0] + ',' + end[1] + '?steps=true&geometries=geojson&access_token=' + mapboxgl.accessToken;

    // make an XHR request https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
    var req = new XMLHttpRequest();
    req.open('GET', url, true);
    req.onload = function () {
        var json = JSON.parse(req.response);
        var data = json.routes[0];
        var route = data.geometry.coordinates;
        var geojson = {
            type: 'Feature',
            properties: {},
            geometry: {
                type: 'LineString',
                coordinates: route
            }
        };
        // if the route already exists on the map, reset it using setData
        if (map.getSource('route')) {
            map.getSource('route').setData(geojson);
        } else { // otherwise, make a new request
            map.addLayer({
                id: 'route',
                type: 'line',
                source: {
                    type: 'geojson',
                    data: {
                        type: 'Feature',
                        properties: {},
                        geometry: {
                            type: 'LineString',
                            coordinates: geojson
                        }
                    }
                },
                layout: {
                    'line-join': 'round',
                    'line-cap': 'round'
                },
                paint: {
                    'line-color': '#3887be',
                    'line-width': 5,
                    'line-opacity': 0.75
                }
            });
        }
        // add turn instructions here at the end
            // get the sidebar and add the instructions
    var instructions = document.getElementById('instructions');
    var steps = data.legs[0].steps;

    var tripInstructions = [];
    for (var i = 0; i < steps.length; i++) {
        tripInstructions.push('<br><li>' + steps[i].maneuver.instruction) + '</li>';
        instructions.innerHTML = '<br><span class="duration">Trip duration: ' + Math.floor(data.duration / 60) + ' min 🚴 </span>' + tripInstructions;
    }
    };
    req.send();
}

map.on('load', function () {
    // make an initial directions request that
    // starts and ends at the same location
    getRoute(start);

    // Add starting point to the map
    map.addLayer({
        id: 'point',
        type: 'circle',
        source: {
            type: 'geojson',
            data: {
                type: 'FeatureCollection',
                features: [{
                    type: 'Feature',
                    properties: {},
                    geometry: {
                        type: 'Point',
                        coordinates: start
                    }
                }
                ]
            }
        },
        paint: {
            'circle-radius': 10,
            'circle-color': '#3887be'
        }
    });
    // this is where the code from the next step will go
    map.on('click', function (e) {
        var coordsObj = e.lngLat;
        canvas.style.cursor = '';
        var coords = Object.keys(coordsObj).map(function (key) {
            return coordsObj[key];
        });
        var end = {
            type: 'FeatureCollection',
            features: [{
                type: 'Feature',
                properties: {},
                geometry: {
                    type: 'Point',
                    coordinates: coords
                }
            }
            ]
        };
        if (map.getLayer('end')) {
            map.getSource('end').setData(end);
        } else {
            map.addLayer({
                id: 'end',
                type: 'circle',
                source: {
                    type: 'geojson',
                    data: {
                        type: 'FeatureCollection',
                        features: [{
                            type: 'Feature',
                            properties: {},
                            geometry: {
                                type: 'Point',
                                coordinates: coords
                            }
                        }]
                    }
                },
                paint: {
                    'circle-radius': 10,
                    'circle-color': '#f30'
                }
            });
        }
        getRoute(coords);
    });


});
// Getting user current location
// <p>Click the button to get your coordinates.</p>
//
// <button onclick="getLocation()">Try It</button>
//
// <p id="demo"></p>
//
// <script>
// var x = document.getElementById("demo");
//
// function getLocation() {
//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showPosition, showError);
//   } else {
//     x.innerHTML = "Geolocation is not supported by this browser.";
//   }
// }
//
// function showPosition(position) {
//   x.innerHTML = "Latitude: " + position.coords.latitude +
//   "<br>Longitude: " + position.coords.longitude;
// }
//
// function showError(error) {
//   switch(error.code) {
//     case error.PERMISSION_DENIED:
//       x.innerHTML = "User denied the request for Geolocation."
//       break;
//     case error.POSITION_UNAVAILABLE:
//       x.innerHTML = "Location information is unavailable."
//       break;
//     case error.TIMEOUT:
//       x.innerHTML = "The request to get user location timed out."
//       break;
//     case error.UNKNOWN_ERROR:
//       x.innerHTML = "An unknown error occurred."
//       break;
//   }
// }