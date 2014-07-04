$(document).ready(function() {
    $('.rating').raty({
        number : 8,
        width: false,
        path: '/static/images/rating/',
        iconRange: [
            {range: 1, on: 'image1-hover.png', off: 'image1.png' },
            {range: 2, on: 'image2-hover.png', off: 'image2.png' },
            {range: 3, on: 'image3-hover.png', off: 'image3.png' },
            {range: 4, on: 'image4-hover.png', off: 'image4.png' },
            {range: 5, on: 'image5-hover.png', off: 'image5.png' },
            {range: 6, on: 'image6-hover.png', off: 'image6.png' },
            {range: 7, on: 'image7-hover.png', off: 'image7.png' },
            {range: 8, on: 'image8-hover.png', off: 'image8.png' },
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