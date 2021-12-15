let chartlist = ["covid-chart", "housing-chart",
    "analysis1", "analysis2", "analysis3", "analysis4",
    "prediction1", "prediction2"];

let storedElements = []
var expandcontainer = document.getElementById("tab-container");
var parentdiv;
isExpand = false;

for (var i = 0; i < chartlist.length; i++) {
    // $("#"+chartlist[i]).click(function(){
    //     var prop = {}
    //     var speed = 1;
    //     if (!isExpand) {
    //         while (expandcontainer.children.length > 0) {
    //             storedElements.push(expandcontainer.removeChild(expandcontainer.children[0]));
    //         }
    //         parentdiv = this.parentNode;
    //         expandcontainer.appendChild(this);
    //         isExpand = !isExpand;
    //         // prop.width = "100%";
    //         // prop.height = "100%";
    //         $("#"+this.id).animate(prop, speed);
    //         // setTimeout(function() { 
    //         //     $("#"+this.id).css("position","absolute");
    //         //   }, 920);
    //     } else {
    //         parentdiv.appendChild(this);
    //         while (storedElements.length > 0) {
    //             expandcontainer.appendChild(storedElements.shift());
    //         }
    //         isExpand = !isExpand;
    //     }
    // });
    document.getElementById(chartlist[i]).onclick = function () {
        if (!isExpand) {
            while (expandcontainer.children.length > 0) {
                storedElements.push(expandcontainer.removeChild(expandcontainer.children[0]));
            }
            parentdiv = this.parentNode;
            expandcontainer.appendChild(this);
            isExpand = !isExpand;
        }else{
            parentdiv.appendChild(this);
            while(storedElements.length>0){
                expandcontainer.appendChild(storedElements.shift());
            }
            isExpand = !isExpand;
        }
    }
}

// var expandWindow = document.createElement('div');
// expandWindow.className = "full-chart";

// let historylist = [document.getElementById("covid-chart"),
// document.getElementById("emotion-display"),
// document.getElementById("housing-chart")];

// let predictionlist = []

// for (var i = 0; i < chartlist.length; i++) {
//     chartlist[i].onclick = function () {
//         var container = document.getElementById("tab-container");
//         if (!isExpand) {
//             // while(container.children.length>0){
//             //     storedElements.push(container.removeChild(container.children[0]));
//             // }
//             // container.appendChild(expandWindow);
//             // this.style.width = "100%";
//             // this.style.height = "100%";
//             console.log(this.id);
//             this.id = "111";
//             console.log(this.id);
//             // expandWindow.id = this.id;
//             // console.log(expandWindow.id);
//             isExpand = !isExpand;
//         } else {
//             this.id = "covid-chart";
//         }
//         // }else{
//         //     this.style.width = "50%";
//         //     this.style.height = "50%";
//         //     while(container.children.length>0){
//         //         container.removeChild(this);
//         //     }
//         //     while(storedElements.length > 0){
//         //         container.appendChild(storedElements.shift());
//         //     }
//         //     isExpand = !isExpand;
//         // }
//     }
// }

// expandWindow.onclick = function(){
//     if(isExpand){
//         var container = document.getElementById("tab-container");
//         while(container.children.length>0){
//             container.removeChild(container.children[0]);
//         }
//         while(storedElements.length > 0){
//             container.appendChild(storedElements.shift());
//         }
//         isExpand = !isExpand;
//     }
// }