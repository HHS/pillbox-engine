
$(document).ready(function() {

    $('[data-toggle="tooltip"]').tooltip()

    var addBar = function(elem) {
        elem.children('.widget-progress').removeClass('hide');
        elem.children('.widget-progress').addClass('active-task');
    }

    var removeBar = function(elem) {
        elem.children('.widget-progress').addClass('hide');
        elem.children('.widget-progress').removeClass('active-task');
        $('#timer').remove();
    }

    var changeButton = function(elem, icon) {
      var pullRight = elem.find('.pull-right>i');
      pullRight.attr('class', 'fa fa-' + icon);

    }

    var status_update = function(obj, data) {
        if (typeof data.meta !== 'undefined' && data.meta != null) {
            obj.find('#panel-msg').html(data.status);
            addBar(obj);

           if (data.meta.action && data.meta.added !== 'undefined' && data.meta.updated !== 'undefined') {
               $(`#${data.meta.action}`).html(parseInt(data.meta.added) + parseInt(data.meta.updated));
            }

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

            if ($('#timer').length === 0) {
              $('<span id="timer"></span>').insertBefore(obj.find('.pull-right>i'));
            }
        }
        else {
            removeBar(obj);
            obj.find('#panel-msg').html(data.message);
        }
    }

    var seconds = 10;

    // Update the count down every 1 second
    var x = setInterval(function() {
        // Time calculations for days, hours, minutes and seconds
        seconds = seconds - 1;
        // Output the result in an element with id="demo"
        $('#timer').html(seconds + "s ");

        // If the count down is over, write some text
        if (seconds < 1) {
            seconds = 15;
            var that = $('.active-task:first');
            $.get('/spl/download/').done(function(data) {
              status_update(that, data);
            });
        }
    }, 1000);

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
