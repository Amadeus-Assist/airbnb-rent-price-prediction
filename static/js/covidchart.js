const coviddates = datelist_covid.split("|");
const covidnews = newlist_covid.split("|");
const coviddata = [];
for (let i = 0; i < coviddates.length; i++) {
    coviddata.push({ label: coviddates[i], value: covidnews[i] });
}
const covidData = {
    chart: {
        caption: "Daily New Cases Trend of COVID-19",
        adjustDiv: "0",
        yAxisMinValue: "0",
        labelFontSize: "10",
        drawAnchors: "0",
        labelStep: "28",
        theme: "candy",
        labelDisplay: "rotate",
        slantLabel: "1"
    },
    data: coviddata
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



const coviddates_predict = datelist_covid_predict.split("|");
const covidnews_predict = newlist_covid_predict.split("|");
const coviddata_predict = [];
for (let i = 0; i < coviddates_predict.length; i++) {
    coviddata_predict.push({ label: coviddates_predict[i], value: covidnews_predict[i] });
}
const covidData_predict = {
    chart: {
        caption: "Predictions of COVID-19 Daily New Cases",
        adjustDiv: "0",
        yAxisMinValue: "0",
        labelFontSize: "10",
        drawAnchors: "0",
        // labelStep: "28",
        theme: "candy",
        labelDisplay: "rotate",
        slantLabel: "1"
    },
    data: coviddata_predict
};

FusionCharts.ready(function () {
    var myChart = new FusionCharts({
        type: "line",
        renderAt: "prediction1",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: covidData_predict
    }).render();
});