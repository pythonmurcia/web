// Initialize and add the map
function initMap() {
	// get the location of Murcia
	var murcia = {lat: -25.344, lng: 131.036};
	// Tcreate the map object, using the google.maps.Map() class
	var map = new google.maps.Map(
    	document.getElementById('google-map'), {zoom: 4, center: murcia});
  	// Create the marker in murcia.
  	var marker = new google.maps.Marker({position: murcia, map: map});
}