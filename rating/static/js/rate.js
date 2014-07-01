$(document).ready(function() {
    $('.rating').raty({
        number : 10,
        starOff : '/static/images/rate-hover.png',
        starOn  : '/static/images/rate.png',
        click: function(score, evt) {
            $('#rate_score').val(score);
            $('#top_message').show();
            $('#review_text').slideDown().focus();
        },
        score: function() {
            return $(this).attr('data-score');
        },
        readOnly: function() {
            return $(this).is('.readonly');
        }
    });
});