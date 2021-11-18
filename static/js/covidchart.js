const coviddates = datelist_covid.split("|");
const covidnews = newlist_covid.split("|");
const coviddata = [];
for (let i = 0; i < coviddates.length; i++) {
    coviddata.push({ label: coviddates[i], value: covidnews[i] });
}
const covidData = {
    chart: {
        caption: "Daily New Cases Trend of COVID-19",
        // yaxisname: "New Cases",
        // xaxisname: "Date",
        // forceaxislimits: "1",
        // xAxisValueFontSize: "5",
        // yAxisValueFontSize: "5",
        // setAdaptiveYMin:"1",
        adjustDiv: "0",
        yAxisMinValue: "0",
        labelFontSize: "10",
        drawAnchors: "0",
        // pixelsperpoint: "0",
        // pixelsperlabel: "50",
        labelStep: "28",
        // compactdatamode: "1",
        // dataseparator: "|",
        theme: "candy",
        labelDisplay: "rotate",
        slantLabel: "1"
    },
    data: coviddata
    // categories: [
    //     { category: datelist_covid }
    // ],
    // dataset: [
    //     {data: newlist_covid}
    // ]
};

FusionCharts.ready(function () {
    var myChart = new FusionCharts({
        type: "line",
        renderAt: "covid-chart",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: covidData
    }).render();
});