
$(document).ready(function() {
    $('.panel-footer').click(function() {
        if ($(this).parent().attr('href') == '#') {
            var action = $(this).data('action');
            var that = $(this);
            $.get(action)
             .done(function(data) {
                if (data.status == 'PROGRESS') {
                    that.find('#panel-msg').html('Task Running: ' + data.total_processed + ' processed.');
                    that.children('.progress').removeClass('hide');
                    that.find('.progress-bar').css('width', data.percent + '%').html(data.percent + '%')
                }
                else {
                    that.find('#panel-msg').html(data.message);
                    that.children('.progress').addClass('hide');
                }
             })
             .fail(function(data){
                that.children('.progress').addClass('hide');
                that.find('#panel-msg').html(data.responseJSON.message);
             });
        }
    })
});
