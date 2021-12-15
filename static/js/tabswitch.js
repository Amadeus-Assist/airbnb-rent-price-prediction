var switchState = 1;

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
}