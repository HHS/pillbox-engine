
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

    var status_update = function(obj, data) {
        if (typeof data.meta !== 'undefined' && data.meta != null) {
            obj.find('#panel-msg').html(data.status);
            addBar(obj);
            if (typeof data.meta.percent === 'undefined') {
                var percent = 0;
            }
            else {
                var percent = data.meta.percent;
            }
            if (! typeof data.meta.file !== 'undefined') {
                obj.find('.task-name').html(data.meta.file);
            }
            obj.find('.progress-bar').css('width', percent + '%').html(parseFloat(percent).toFixed(2) + '%')
        }
        else {
            removeBar(obj);
            obj.find('#panel-msg').html(data.message);
        }
    }

    $('.widget-footer').click(function(event) {
        var action = $(this).data('action');
        var that = $(this);
        changeButton(that, 'refresh');
        $.get(action)
         .done(function(data) {
            status_update(that, data);
         });
    });

});
