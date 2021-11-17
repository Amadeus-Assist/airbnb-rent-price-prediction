const covidData = {
    chart: {
        caption: "Daily New Cases Trend of COVID-19",
        yaxisname: "New Cases",
        xaxisname: "Date",
        forceaxislimits: "1",
        pixelsperpoint: "0",
        pixelsperlabel: "28",
        compactdatamode: "1",
        dataseparator: "|",
        theme: "candy",
        labelDisplay: "rotate",
        slantLabel: "1"
    },
    categories: [
        { category: datelist_covid }
    ],
    dataset: [
        {data: newlist_covid}
    ]
};

FusionCharts.ready(function() {
    var myChart = new FusionCharts({
        type: "zoomline",
        renderAt: "covid-chart",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: covidData
    }).render();
});