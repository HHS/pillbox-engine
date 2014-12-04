
$(document).ready(function() {

    var addBar = function(elem) {
        elem.children('.progress').removeClass('hide');
    }

    var removeBar = function(elem) {
        elem.children('.progress').addClass('hide');
    }

    var changeButton = function(elem, icon) {
        elem.find('.pull-right>i').attr('class', 'fa fa-' + icon);
    }

    $('#widget-footer').click(function(event) {
        if ($(this).parent().attr('href') == '#') {
            event.preventDefault();
            var action = $(this).data('action');
            var that = $(this);
            changeButton(that, 'refresh');

            $.get(action)
             .done(function(data) {
                if (data.status == 'PROGRESS') {
                    that.find('#panel-msg').html(data.message + ': ' + data.total_processed + ' processed.');
                    addBar(that);

                    that.find('.progress-bar').css('width', data.percent + '%').html(data.percent + '%')
                }
                else {
                    that.find('#panel-msg').html(data.message);
                    removeBar(that);
                }
             })
             .fail(function(data){
                removeBar(that);
                that.find('#panel-msg').html(data.responseJSON.message);
             });
        }
    })

    $('#download-widget-footer').click(function(event) {
        event.preventDefault();
        var action = $(this).data('action');
        var that = $(this);
        changeButton(that, 'refresh');
        $.get(action)
         .done(function(data) {
            if (data.status == 'DOWNLOAD') {
                that.find('#panel-msg').html(data.message);
                addBar(that);

                $('#overall').css('width', data.percent + '%').html(data.percent + '%')
                $('#file-specific').css('width', data.meta.percent + '%').html(data.meta.percent + '%')
            }
            else {
                that.find('#panel-msg').html(data.message);
                removeBar(that);
            }
         });
    });
});
