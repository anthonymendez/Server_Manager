// System Info Variables
// CPU Static Info
var cpu_thread_count;
var cpu_physical_count;
// CPU Dynamic Info
var cpu_percent_overall;
var cpu_percent_list;

// Memory Dynamic Info
var mem_total;
var mem_left;

// Replaces element with ID's string with data
function set_element(id, data) {
    $("#" + id).empty();
    $("#" + id).append(data);
}

// Performs GET request from server.
function get_system_info() {
    var plugin_name = "system_monitor"
    var URL = plugin_name + "/system_info/dynamic"
    $.get(URL)
    .done(function(data) {
        var result = JSON.parse(data);
        var cpu_count = result["cpu_physical_count"];
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
    get_static_system_info();
    // setInterval(get_system_info, 1000);
    setInterval(get_dyamic_system_info, 1000);
});

// Gets initial data from server
function get_static_system_info() {
    var plugin_name = "system_monitor"
    var URL = plugin_name + "/system_info/static"
    $.get(URL)
    .done(function(data) {
        var result = JSON.parse(data);
        cpu_thread_count = result["cpu_thread_count"];
        cpu_physical_count = result["cpu_physical_count"];
        set_element("cpu_thread_count", cpu_thread_count);
        set_element("cpu_physical_count", cpu_physical_count);
    })
    .fail(function(data) {
        
    });
}

function get_dyamic_system_info() {
    var plugin_name = "system_monitor"
    var URL = plugin_name + "/system_info/dynamic"
    $.get(URL)
    .done(function(data) {
        var result = JSON.parse(data);
        cpu_percent_overall = result["cpu_percent_overall"];
        cpu_percent_list = result["cpu_percent_list"];
        mem_total = result["mem_total"];
        mem_left = result["mem_left"];
        set_element("cpu_percent_overall", cpu_percent_overall);
        set_element("cpu_percent_list", cpu_percent_list);
        set_element("mem_total", mem_total);
        set_element("mem_left", mem_left);
    })
    .fail(function(data) {
        
    });
}