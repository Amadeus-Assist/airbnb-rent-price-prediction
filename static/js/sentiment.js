const sentiment_datesdsds = sentiment_date.split("|");
const sentiment_datadfsdf = sentiment_data.split("|");

console.log(sentiment_data)

const sentiment__data = [];
for (let i = 0; i < sentiment_datesdsds.length; i++) {
    sentiment__data.push({ label: sentiment_datesdsds[i], value: sentiment_datadfsdf[i] });
}
console.log(sentiment__data)

const sentimentData = {
    chart: {
        caption: "Daily Sentiment Trend on Twitter",
        adjustDiv: "0",
        yAxisMinValue: "0",
        labelFontSize: "10",
        drawAnchors: "0",
        labelStep: "28",
        theme: "candy",
        labelDisplay: "rotate",
        slantLabel: "1"
    },
    data: sentiment__data
};

FusionCharts.ready(function () {
    var myChart = new FusionCharts({
        type: "line",
        renderAt: "emotion-display",
        width: "100%",
        height: "100%",
        dataFormat: "json",
        dataSource: sentimentData
    }).render();
});