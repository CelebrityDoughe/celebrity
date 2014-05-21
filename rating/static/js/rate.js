$(document).ready(function() {
    $('.rating').raty({
        number : 10,
        starOff : '/static/raty/img/star-off.png',
        starOn  : '/static/raty/img/star-on.png',
        click: function(score, evt) {
            $('#rate_score').val(score);
        },
        score: function() {
            return $(this).attr('data-score');
        },
        readOnly: function() {
            return $(this).is('.readonly');
        }
    });
});