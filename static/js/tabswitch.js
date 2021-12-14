var switchState = true;

let shows = []
var preHousingWhole = document.createElement('div');
preHousingWhole.id = "prediction-housing-1";
preHousingWhole.className = "prediction-housing-1";
shows.push(preHousingWhole);
var preHousingDetail = document.createElement('div');
preHousingDetail.id = "prediction-housing-2";
preHousingDetail.className = "prediction-housing-2";
shows.push(preHousingDetail);
var preCovid = document.createElement('div');
preCovid.id = "prediction-covid";
preCovid.className = "prediction-covid";
shows.push(preCovid);
var housingTrend = document.createElement('div');
housingTrend.id = "housing-trend";
housingTrend.className = "housing-trend";
shows.push(housingTrend);
var housingAnalysis = document.createElement('div');
housingAnalysis.id = "housing-analysis";
housingAnalysis.className = "housing-analysis";
shows.push(housingAnalysis);

document.getElementById("history-label").onclick = function(){
    if(!switchState){
        switchContents();
        switchState = !switchState;
    }
}

document.getElementById("prediction-label").onclick = function(){
    if(switchState){
        switchContents();
        switchState = !switchState;
    }
}

function switchContents(){
    var container = document.getElementById("chart-container");
    var alterLength = shows.length;
    while(container.children.length > 0){
        shows.push(container.removeChild(container.children[0]));
    }
    for(var i = 0;i<alterLength;i++){
        container.appendChild(shows.shift());
    }
}