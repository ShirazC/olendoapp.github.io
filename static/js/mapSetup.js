/**
 * AmCharts.ready function handler is executed when the page loads
 * We are going to create both maps then. We'll store references to
 * all maps we create in the global maps variable so that we can
 * come back and get info from them later.
 */
var maps = {};
AmCharts.ready(function() {
  createMap('unRegions');
  // createMap('canada');
});

/**
 * Creates a country map
 * $param country A map and container id
 */

 var currentCountry = 0
function createMap (country) {
    var map = new AmCharts.AmMap();
    maps[country] = map;
    map.panEventsEnabled = true;
    map.backgroundColor = "transparent";
    map.backgroundAlpha = 1;

    map.zoomControl.panControlEnabled = false;
    map.zoomControl.zoomControlEnabled = true;

    var dataProvider = {
    map: country + "High",
        getAreasFromMap: true
    };

    map.dataProvider = dataProvider;

    map.areasSettings = {
        autoZoom: false,
        color: "#CDCDCD",
        colorSolid: "#68B0AB",
        selectedColor: "#68B0AB",
        outlineColor: "#666666",
        rollOverColor: "#88CAE7",
        rollOverOutlineColor: "#FFFFFF",
        selectable: true,
        showAsSelected: false
    };

    map.addListener('clickMapObject', function (event) {
        // deselect the area by assigning all of the dataProvider as selected object
        // map.selectedObject = map.dataProvider;

        // event.mapObject.showAsSelected = true
        document.getElementById("region_field").value = event.mapObject.enTitle;
        console.log(document.getElementById("region_field").value);
        // debugger;



    });

    map.write(country);
}
