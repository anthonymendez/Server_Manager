// Performs GET request from server.
function get_system_info() {
    var plugin_name = "system_monitor"
    var URL = plugin_name + "/system_info"
    $.get(URL)
    .done(function(data) {
        var result = JSON.parse(data);
        var cpu_count = result["cpu_count"];
        var cpu_percent = result["cpu_percent_list"];
        var cpu_percent_str = ""
        for (var i = 0; i < cpu_count; i++) {
            cpu_percent_str += `<p class="col">`;
            cpu_percent_str += "Core " + i + ": ";
            cpu_percent_str += cpu_percent[i].toFixed(1);
            cpu_percent_str += "%";
            cpu_percent_str += "</p>";
        }
        var cpu_stats = result["cpu_stats"];
        var mem_total = result["mem_total"]/1024/1024/1024;
        var mem_left = result["mem_left"]/1024/1024/1024;
        $("#cpu_percent").empty();
        $("#cpu_percent").append(cpu_percent_str);
        $("#cpu_stats").empty();
        $("#cpu_stats").append(cpu_stats);
        $("#mem_total").text(mem_total.toFixed(4) + " Gigabytes");
        $("#mem_left").text(mem_left.toFixed(4) + " Gigabytes");
    })
    .fail(function(data) {
        $("#cpu_count").text("Yeah that failed chief.");
    });
}

$(document).ready(function() {
    // Updates Every Second
    setInterval(get_system_info, 1000);
});
