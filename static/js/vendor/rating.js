$(function() {

	// Initialize interaction buttons tooltips
	$('.person-status-rating [data-toggle="tooltip"]').tooltip()

	// Init rate buttons
	$(".person-status-rating").each(function() {
		var rate = parseRate($(this).data("ratevalue"));

		setStars($(this), rate);
	});

	// Rate
	$(".rate-smile").hover(function(){
		var rate = parseRate($(this).data("rate"));
		setStars($(this).closest(".person-status-rating"), rate);

	},function(){
		var rate = parseRate($(this).closest(".person-status-rating").data("ratevalue"));
		setStars($(this).closest(".person-status-rating"), rate);
	});

	$(".rate-smile").on("click", function() {
		var rate = parseRate($(this).data("rate"));
		$(this).closest(".person-status-rating").data("ratevalue", rate);
		return false;
	});

});

function setStars($btn, starsNum) {
	$btn.find(".rate-smile").removeClass("active");
	$btn.find(".rate-smile:lt("+starsNum+")").addClass("active");
}

function parseRate(rate) {
	var rate = parseInt(rate);
		rate = Math.max(rate,0);
		rate = Math.min(rate,10);

	return rate;
}