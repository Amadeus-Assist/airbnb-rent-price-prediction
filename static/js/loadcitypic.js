console.log(window.location.origin);
const getPicListRequest = new Request("/geovisual/getPicList/" + city);
console.log(getPicListRequest);
fetch(getPicListRequest).then(response => response.json())
    .then(data => {
        console.log("here----------")
        console.log(data)
        var picContainer = document.getElementById("cityScrollTable");
        for (let i = 0; i < cityPicNum; i++) {
            var picLi = document.createElement("li");
            var picpath = "/" + data.pic[i];
            var picImg = new Image();
            picImg.onload = function () {
                console.log(this.width);
                console.log(picheight = this.height);
            }
            picImg.setAttribute("width", 700);
            picImg.setAttribute("height", 400);
            picImg.src = picpath;
            picLi.appendChild(picImg);
            picContainer.appendChild(picLi);
        }
    });

$(function () {
    var scroller = $('#city-discription div.cityScroller');
    var scrollerContent = scroller.children('ul');
    scrollerContent.children().clone().appendTo(scrollerContent);
    var curX = 0;
    scrollerContent.children().each(function () {
        var $this = $(this);
        $this.css('left', curX);
        curX += $this.outerWidth(true);
    });
    var fullW = curX / 2;
    var viewportW = scroller.width();

    scroller.css('overflow-x', 'auto');
});