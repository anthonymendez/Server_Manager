var cpu_usage_data = {
    labels: [],
    datasets: [{
        label: "",
        data: []
    }]
}

var cpu_usage_options = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                suggestedMin: 0,
                suggestedMax: 100
            }
        }]
    }
}

function get_canvas_ctx(chart_id) {
    return document.getElementById(chart_id).getContext('2d');
}

function chart_init(ctx, data, options) {
    return new Chart(
        ctx,
        {
            type: 'line',
            data: data,
            options: options
        }
    );
}

function cpu_usage_labels(cpu_count) {
    labels = [];
    for (var i = 0; i < cpu_count; i++) {
        labels.push("CPU " + i);
    }
    return labels;
}

function cpu_usage_data_point(cpu_usage) {
    return {
        x: new Date(),
        y: cpu_usage
    }
}