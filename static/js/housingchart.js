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


const housingdates_predict = datelist_housing_predict.split("|");
const housing_predict_data = housing_predict.split("|");
const housingdata_predict = [];
for (let i = 0; i < housingdates_predict.length; i++) {
    housingdata_predict.push({ label: housingdates_predict[i], value: housing_predict_data[i] });
}
const housingData_predict = {
    chart: {
        caption: "Predictions of Housing Prices",
        adjustDiv: "0",
        yAxisMinValue: "0",
        labelFontSize: "10",
        drawAnchors: "0",
        // labelStep: "28",
        theme: "fusion",
        labelDisplay: "rotate",
        slantLabel: "1",
        showvalues: "0",
    },
    data: housingdata_predict
};

FusionCharts.ready(function () {
    var myChart = new FusionCharts({
        type: "line",
        renderAt: "prediction2",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: housingData_predict
    }).render();
});