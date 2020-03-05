function custom_js() {
    $("#custom_js").append("Of course you can mate!");
}

// Performs GET request from server.
function get_test() {
    var plugin_name = "plugin_debug_example"
    var URL = plugin_name + "/get_test"
    $.get(URL)
    .done(function(data) {
        $("#get_test").text(data);
    })
    .fail(function(data) {
        $("#get_test").text("Yeah that failed chief.");
    });
}

$(document).ready(function() {
    var plugin_name = "plugin_debug_example"

    custom_js();
    // Updates Every Second
    setInterval(get_test, 1000);
});
