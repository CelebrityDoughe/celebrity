$(document).ready(function() {
    $('.rating').raty({
        number : 10,
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
            {range: 9, on: 'image9-hover.png', off: 'image9.png' },
            {range: 10, on: 'image10-hover.png', off: 'image10.png' },
        ],
        hints: ['Very Nice person', 'Above average nice person', 'Nice person', 'Somewhat nice', 'Somewhat of a Douchebag', 'Douchebag', 'Bigger Douchebag', 'Huge Douchebag', 'Mean and a douchebag', 'Worst person ever'],
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

    // update default tooltip with Bootstrap tooltip
    // $('#rate img').each(function(){
        // var title = $(this).attr('title');
        // $(this).removeAttr('title').data('content', title).data('placement', 'top').data('trigger', 'hover');
    // }).popover();
    $('#rate img').each(function(){
        $(this).data('placement', 'top');
    }).tooltip();
});