function createColumnChart(config) {
    Highcharts.chart(config.renderTo, {
        chart: {
            type: config.type
        },
        title: {
            text: config.title
        },
        xAxis: {
            categories: config.categories
        },
        yAxis: {
            title: {
                text: config.title
            }
        },
        series: config.series
    });
}

