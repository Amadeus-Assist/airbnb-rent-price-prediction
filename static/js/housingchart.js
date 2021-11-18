const housingData = {
    chart: {
        caption: "Seasonal prices of houses from 2020 to 2021",
        yaxisname: "Prices of houses",
        xaxisname: "Date",
        forceaxislimits: "1",
        pixelsperpoint: "0",
        pixelsperlabel: "30",
        compactdatamode: "1",
        dataseparator: "|",
        theme: "fusion"
    },
    categories: [
        { category: dateList }
    ],
    dataset: [
        {seriesname: "Median", data: medianList},
        {seriesname: "Average", data: avgList}
    ]
};

FusionCharts.ready(function() {
    var myChart = new FusionCharts({
        type: "zoomline",
        renderAt: "housing-chart",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: housingData
    }).render();
});