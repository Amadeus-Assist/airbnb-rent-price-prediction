const seasonalPrediction = {
    chart: {
      caption: "Countries With Most Oil Reserves [2017-18]",
      subcaption: "In MMbbl = One Million barrels",
      xaxisname: "Country",
      yaxisname: "Reserves (MMbbl)",
      numbersuffix: "K",
      theme: "candy"
    },
    data: [
      {
        label: "Venezuela",
        value: "290"
      },
      {
        label: "Saudi",
        value: "260"
      },
      {
        label: "Canada",
        value: "180"
      },
      {
        label: "Iran",
        value: "140"
      },
      {
        label: "Russia",
        value: "115"
      },
      {
        label: "UAE",
        value: "100"
      },
      {
        label: "US",
        value: "30"
      },
      {
        label: "China",
        value: "30"
      }
    ]
  };
  
FusionCharts.ready(function() {
    var myChart = new FusionCharts({
      type: "column2d",
      renderAt: "seasonal-results",
      width: "100%",
      height: "300px",
      dataFormat: "json",
      dataSource: seasonalPrediction
    }).render();
});
  
  

const possibilityPrediction = {
    chart: {
      caption: "Yearly sales of iPhone",
      yaxisname: "Number of units sold",
      subcaption: "2007-2016",
      legendposition: "Right",
      drawanchors: "0",
      showvalues: "0",
      plottooltext: "<b>$dataValue</b> iPhones sold in $label",
      theme: "candy"
    },
    data: [
      {
        label: "2007",
        value: "1380000"
      },
      {
        label: "2008",
        value: "1450000"
      },
      {
        label: "2009",
        value: "1610000"
      },
      {
        label: "2010",
        value: "1540000"
      },
      {
        label: "2011",
        value: "1480000"
      },
      {
        label: "2012",
        value: "1573000"
      },
      {
        label: "2013",
        value: "2232000"
      },
      {
        label: "2014",
        value: "2476000"
      },
      {
        label: "2015",
        value: "2832000"
      },
      {
        label: "2016",
        value: "3808000"
      }
    ]
  };
  
  FusionCharts.ready(function() {
    var myChart = new FusionCharts({
      type: "area2d",
      renderAt: "distribution-results",
      width: "100%",
      height: "300px",
      dataFormat: "json",
      dataSource: possibilityPrediction
    }).render();
  });
  
