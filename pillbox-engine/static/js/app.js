
$(document).ready(function() {
    $('.panel-footer').click(function() {
        var action = $(this).data('action');
        var that = $(this);
        if (action == 'products') {
            var progress = setInterval(function() {
                $.get('/spl/sync/products', function(data) {
                    that.html(data.total);
                    if (data.total > 60000) {
                        clearInterval(progress);
                    }
                });
            }, 1000);
        }

    })
});
