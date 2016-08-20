$(document).ready( function() {
    setInterval(function(){
        $.getJSON('/api/v1/server/status', function(status_code) {
            var api_status = status_code.server_status.statusC;

            var curr_icon = $('#server_statusico').attr('class');
            var up_icon = "fa fa-thumbs-o-up fa-5x";
            var down_icon = "fa fa-thumbs-down fa-5x";

            var curr_bg = $('#server_statusbg').attr('class');
            var up_bg = "panel panel-green";
            var down_bg = "panel panel-red";

            if (api_status == 1){
                $('#server_status').html("OK");
                if (curr_icon != up_icon) {
                    $('#server_statusico').removeClass(curr_icon).addClass(up_icon);
                    $('#server_statusbg').removeClass(curr_bg).addClass(up_bg);
                }
            } else {
                $('#server_status').html("DOWN");
                if (curr_icon != down_icon) {
                    $('#server_statusico').removeClass(curr_icon).addClass(down_icon);
                    $('#server_statusbg').removeClass(curr_bg).addClass(down_bg);
                }
                console.log("down");
            }
        });
    },3000);
});