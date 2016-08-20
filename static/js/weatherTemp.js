$(document).ready( function() {
    setInterval(function(){
        $.getJSON('/api/v1/weather', function(temp) {
            var apiTemp = temp.weather_data.temperature;
            var apiIcon = temp.weather_data.icon;
            var oldClass = $('#weatherIcon').attr('class');
            var newClass = ("wi wi-owm-" + apiIcon + " fa-5x");

                $("#weatherTemp").html(apiTemp +" F");
                if (oldClass != newClass) {
                    $("#weatherIcon").removeClass(oldClass).addClass(newClass);
                }
        });
    },60000);
});