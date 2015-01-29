$.widget("custom.catcomplete", $.ui.autocomplete, {
    _renderMenu : function(ul, items) {
        var that = this, currentCategory = "";
        $.each(items, function(index, item) {
            if (item.category != currentCategory) {
                ul.append("<li class='ui-autocomplete-category'>" + item.category + "</li>");
                currentCategory = item.category;
            }
            that._renderItemData(ul, item);
        });
    }
});

$(document).ready(function() {
    $('#search-input').catcomplete({
        source : function(request, response) {
            $.ajax({
                url : '/search/',
                dataType : 'json',
                data : {
                    keyword : $('#search-input').val()
                },
                success : function(data) {
                    response($.map(data, function(item) {
                        return {
                            label : item.label,
                            category : item.category,
                            url: item.url
                        };
                    }));
                }
            });
        },
        minLength: 2,
        select: function(event, ui) {
            location.href = ui.item.url;
        },
    });

    $('a.confirm').click(function(){
        if(confirm($(this).data('confirm'))) {
            location.href = $(this).data('url');
        }
    });
});
