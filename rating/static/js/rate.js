$(document).ready(function() {
    $('.rating').raty({
        number : 8,
        width: false,
        path: '/static/images/',
        starOff : 'rate-hover.png',
        starOn  : 'rate.png',
        iconRange: [
            {range: 1, on: '1.png', off: '0.png' },
            {range: 2, on: '2.png', off: '0.png' },
            {range: 3, on: '3.png', off: '0.png' },
            {range: 4, on: '4.png', off: '0.png' },
            {range: 5, on: '5.png', off: '0.png' },
            {range: 6, on: '1.png', off: '0.png' },
            {range: 7, on: '2.png', off: '0.png' },
            {range: 8, on: '3.png', off: '0.png' },
        ],
        hints: ['Score 1', 'Score 2', 'Score 3', 'Score 4', 'Score 5', 'Score 6', 'Score 7', 'Score 8'],
        click: function(score, evt) {
            $('#rate_score').val(score);
            $('#top_message').show();
            $('#review_text').animate({height: '100px'}).focus();
        },
        score: function() {
            return $(this).attr('data-score');
        },
        readOnly: function() {
            return $(this).is('.readonly');
        }
    });
});