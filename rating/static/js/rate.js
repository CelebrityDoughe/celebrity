$(document).ready(function() {
    $('.rating').raty({
        number : 10,
        starOff : '/static/images/rate-hover.png',
        starOn  : '/static/images/rate.png',
        iconRange: [
            {range: 1, on: '/static/images/1.png', off: '/static/images/0.png' },
            {range: 2, on: '/static/images/2.png', off: '/static/images/0.png' },
            {range: 3, on: '/static/images/3.png', off: '/static/images/0.png' },
            {range: 4, on: '/static/images/4.png', off: '/static/images/0.png' },
            {range: 5, on: '/static/images/5.png', off: '/static/images/0.png' },
            {range: 6, on: '/static/images/1.png', off: '/static/images/0.png' },
            {range: 7, on: '/static/images/2.png', off: '/static/images/0.png' },
            {range: 8, on: '/static/images/3.png', off: '/static/images/0.png' },
            {range: 9, on: '/static/images/4.png', off: '/static/images/0.png' },
            {range: 10, on: '/static/images/5.png', off: '/static/images/0.png' }
        ],
        hints: ['Score 1', 'Score 2', 'Score 3', 'Score 4', 'Score 5', 'Score 6', 'Score 7', 'Score 8', 'Score 9', 'Score 10'],
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