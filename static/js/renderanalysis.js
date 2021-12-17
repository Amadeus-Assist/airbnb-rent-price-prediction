for(var i = 1;i<=4;i++){
    var analysischart = document.getElementById("analysis-img"+i);
    analysischart.src = "./../../static/img/analysis/analysis_"+city+"_"+i+".png";
    analysischart.style.maxWidth="100%";
    analysischart.style.maxHeight="100%";
    analysischart.style.margin="auto";
    analysischart.style.display="block";
}