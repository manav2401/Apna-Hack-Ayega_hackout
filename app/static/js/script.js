function initMap() {
  var point_1 = {
  info: "Pothole",
    lat: 23.187247,
    long: 72.627666,
  }

  var point_2 = {
  info: "Pothole",
    lat: 23.188808,
    long: 72.627243,
  }

  var locations = [
    [point_1.info, point_1.lat, point_1.long, 0],
    [point_2.info, point_2.lat, point_2.long, 1],
  ]

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: new google.maps.LatLng(23.188414, 72.627876),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  })

  var infowindow = new google.maps.InfoWindow({})

  var marker, i

  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      icon: 'dot.png',
      map: map,
    })

    google.maps.event.addListener(
      marker,
      'click',
      (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0])
          infowindow.open(map, marker)
        }
      })(marker, i)
    )
  }
}
