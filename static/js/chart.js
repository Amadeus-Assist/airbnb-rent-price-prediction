const seasonalData = {
    chart: {
        caption: "Seasonal prices of houses from 2019 to 2020",
        yaxisname: "Prices of houses",
        xaxisname: "Date",
        forceaxislimits: "1",
        pixelsperpoint: "0",
        pixelsperlabel: "30",
        compactdatamode: "1",
        dataseparator: "|",
        theme: "candy"
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
        renderAt: "seasonal-chart",
        width: "44%",
        height: "290",
        dataFormat: "json",
        dataSource: seasonalData
    }).render();
});

const availabilityData = {
    chart: {
        caption: "Room availability for 2019-2020",
        lowerlimit: "0",
        upperlimit: "100",
        showvalue: "1",
        numbersuffix: "%",
        theme: "candy",
        showtooltip: "0"
    },
    colorrange: {
        color: [
            {minvalue: "0", maxvalue: "50", code: "#F2726F"},
            {minvalue: "50", maxvalue: "75", code: "#FFC533"},
            {minvalue: "75", maxvalue: "100", code: "#62B58F"}
        ]
    },
    dials: {
        dial: [{ value: availability }]
    }
};

FusionCharts.ready(function() {
    var myChart = new FusionCharts({
        type: "angulargauge",
        renderAt: "availability-chart",
        width: "22%",
        height: "230",
        dataFormat: "json",
        dataSource: availabilityData
    }).render();
});

const distributionData = {
    chart: {
        caption: "Room Type Distribution",
        showpercentvalues: "1",
        defaultcenterlabel: "Room type Distribution",
        aligncaptionwithcanvas: "0",
        captionpadding: "5",
        decimals: "1",
        plottooltext:
        "<b>$percentValue</b> of the rooms are <b>$label</b>",
        theme: "candy"
    },
    data: [
        {label: "Hotel room", value: hotel},
        {label: "Private room", value: private},
        {label: "Entire home", value: entire},
        {label: "Shared room", value: share}
    ]
};

FusionCharts.ready(function() {
    var myChart = new FusionCharts({
        type: "pie2d",
        renderAt: "distribution-chart",
        width: "22%",
        height: "230",
        dataFormat: "json",
        dataSource: distributionData
    }).render();
});

const priceData = {
    chart: {
        caption: "Price data for different types",
        subcaption: "2019-2020",
        xaxisname: "Price range",
        yaxisname: "% Of all listings",
        formatnumberscale: "1",
        plottooltext:
        "<b>$dataValue</b>% of the <b>$seriesName</b>s' prices are in $label",
        theme: "candy",
        drawcrossline: "1"
    },
    categories: [{category: category.split("|").map(x=>({label:x}))}],
    dataset: [
        {seriesname: "Entire room", data: entireList.split("|").map(x=>({value:x}))},
        {seriesname: "Private room", data: privateList.split("|").map(x=>({value:x}))},
        {seriesname: "Hotel room", data: hotelList.split("|").map(x=>({value:x}))},
        {seriesname: "Shared room", data: shareList.split("|").map(x=>({value:x}))},
    ]
};

FusionCharts.ready(function() {
    var myChart = new FusionCharts({
        type: "mscolumn2d",
        renderAt: "price-chart",
        width: "44%",
        height: "260",
        dataFormat: "json",
        dataSource: priceData
    }).render();
});
