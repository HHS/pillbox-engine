
$(document).ready(function() {

    $('[data-toggle="tooltip"]').tooltip()

    var addBar = function(elem) {
        elem.children('.widget-progress').removeClass('hide');
    }

    var removeBar = function(elem) {
        elem.children('.widget-progress').addClass('hide');
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
                    that.find('#panel-msg').html(data.message + ': ' + data.status);
                    removeBar(that);
                }
             })
             .fail(function(data){
                removeBar(that);
                that.find('#panel-msg').html(data.responseJSON.message);
             });
        }
    })

    $('.download-widget-footer').click(function(event) {
        event.preventDefault();
        var action = $(this).data('action');
        var that = $(this);
        changeButton(that, 'refresh');
        $.get(action)
         .done(function(data) {
            if (typeof data.meta !== 'undefined' && data.meta != null) {
                that.find('#panel-msg').html(data.status);
                addBar(that);
                if (typeof data.meta.percent === 'undefined') {
                    var percent = 0;
                }
                else {
                    var percent = data.meta.percent;
                }
                if (! typeof data.meta.file !== 'undefined') {
                    // console.log(data.meta.file);
                    that.find('.task-name').html(data.meta.file);
                }
                that.find('.progress-bar').css('width', percent + '%').html(percent.toFixed(2) + '%')
            }
            else {
                removeBar(that);
                that.find('#panel-msg').html(data.message);
            }

         });
    });
});
