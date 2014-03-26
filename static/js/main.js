$(document).ready(function() {
    $(".item-rate ul li").mouseenter(itemRateHover).mouseleave(function(){return false;});
    $(".item-rate ul li").click(itemRateClick);
});

function itemRateLeave() {
    var targets = $(this).parent().children("li").children("a");
    $(targets).removeClass("active");
}

function itemRateHover() {
    itemRateLeave();

    var rate = parseInt( $(this).children("a").attr("data-rate") );
    
    var targets = $(this).parent().children("li").children("a");
    $(targets).removeClass("active");
    
    for (var i = 1; i < rate; i++) {
        var target = $(this).parent().children("li").children(".rate" + i);
        target.addClass("active");
    }
}

function itemRateClick() {
    RATE = parseInt( $(this).children("a").attr("data-rate") );
    for (var i = 1; i <= RATE; i++) {
        $(".item-rate .rate" + i).addClass("active");
    }
}
