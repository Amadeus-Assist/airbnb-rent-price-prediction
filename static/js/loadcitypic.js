console.log(window.location.origin);
const getPicListRequest = new Request("/getPicList/" + city);
fetch(getPicListRequest).then(response => response.json())
    .then(data => {
        var picContainer = document.getElementById("city-discription");
        var height = picContainer.offsetHeight;
        var width = picContainer.offsetWidth;
        for (let i = 0; i < cityPicNum; i++) {
            var picLi = document.createElement("li");
            var picImg = document.createElement("img");
            picImg.setAttribute("height", height);
            picImg.setAttribute("width", width);
            picImg.setAttribute("src", data[i]);
            picLi.appendChild(picImg);
            picContainer.appendChild(picLi);
        }
    });