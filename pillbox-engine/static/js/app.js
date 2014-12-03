
$(document).ready(function() {
    $('.panel-footer').click(function(event) {
        if ($(this).parent().attr('href') == '#') {
            event.preventDefault();
            var action = $(this).data('action');
            var that = $(this);

            var addBar = function() {
                that.children('.progress').removeClass('hide');
            }

            var removeBar = function() {
                that.children('.progress').addClass('hide');
            }

            var changeButton = function(icon) {
                that.find('.pull-right>i').attr('class', 'fa fa-' + icon);
            }

            changeButton('refresh');

            $.get(action)
             .done(function(data) {
                if (data.status == 'PROGRESS') {
                    that.find('#panel-msg').html(data.message + ': ' + data.total_processed + ' processed.');
                    addBar();

                    that.find('.progress-bar').css('width', data.percent + '%').html(data.percent + '%')
                }
                else {
                    that.find('#panel-msg').html(data.message);
                    removeBar();
                }
             })
             .fail(function(data){
                removeBar();
                that.find('#panel-msg').html(data.responseJSON.message);
             });
        }
    })
});
