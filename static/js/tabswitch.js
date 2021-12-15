var switchState = 1;

// let shows = []
// var preHousingWhole = document.createElement('div');
// preHousingWhole.id = "prediction-housing-1";
// preHousingWhole.className = "prediction-housing-1";
// shows.push(preHousingWhole);
// var preHousingDetail = document.createElement('div');
// preHousingDetail.id = "prediction-housing-2";
// preHousingDetail.className = "prediction-housing-2";
// shows.push(preHousingDetail);
// var preCovid = document.createElement('div');
// preCovid.id = "prediction-covid";
// preCovid.className = "prediction-covid";
// shows.push(preCovid);
// var housingTrend = document.createElement('div');
// housingTrend.id = "housing-trend";
// housingTrend.className = "housing-trend";
// shows.push(housingTrend);
// var housingAnalysis = document.createElement('div');
// housingAnalysis.id = "housing-analysis";
// housingAnalysis.className = "housing-analysis";
// shows.push(housingAnalysis);

let history = [];
var shownTab = document.getElementById("shown-tab");
var invisibleTab = document.getElementById("invisible-tabs");

document.getElementById("history-label").onclick = function(){
    if(switchState!=1){
        switchContents("history");
        switchState = 1;
    }
}

document.getElementById("analysis-label").onclick = function(){
    if(switchState!=2){
        switchContents("analysis");
        switchState = 2;
    }
}

document.getElementById("prediction-label").onclick = function(){
    if(switchState!=3){
        switchContents("prediction");
        switchState = 3;
    }
}

function switchContents(id){
    invisibleTab.appendChild(shownTab.children[0]);
    shownTab.appendChild(document.getElementById(id));
    console.log(shownTab.children.length);
    // var alterLength = shows.length;
    // while(container.children.length > 0){
    //     shows.push(container.removeChild(container.children[0]));
    // }
    // for(var i = 0;i<alterLength;i++){
    //     container.appendChild(shows.shift());
    // }
}