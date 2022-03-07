/* global $ */
'use strict';

var customadmin = {

    init: function () {
        console.info('init');

        // custom checkboxes
        $('.i-checks').iCheck({
            checkboxClass: 'icheckbox_square-green',
            radioClass: 'iradio_square-green'
        });

    },

    fileBrowse: function (element) {
        var fullPath = $(element).val();
        if (fullPath) {
            var startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
            var filename = fullPath.substring(startIndex);
            if (filename.indexOf('\\') === 0 || filename.indexOf('/') === 0) {
                filename = filename.substring(1);
            }
            var renamed = '' + filename;
            $(element).parent().find('.faker').val(renamed);
        }
    },

};

$(function () {

    // customadmin.init();

    // Datatables defaults
    try {
        $.extend(true, $.fn.DataTable.defaults, {
            pageLength: 25,
            stateSave: true,
            info: true,
            responsive: true,
        });
    } catch(err) {
        console.warn("Unable to extend DataTable defaults.")
    }

    // ------------------------------------------------------------------------
    // Events
    // ------------------------------------------------------------------------

    $(document).on('change', '.file-browse', function () {
        console.debug('file browse change');
        customadmin.fileBrowse(this);
    });

    // AJAX delete object from a list
    /*$('.list .btn-delete').on('click', function(event) {
        console.info('customadmin - AJAX list delete');
        event.preventDefault();

        var targ_elem = $(this);
        // var id = $(this).parent().parent().data('id');
        var obj_title = $(this).data('title');
        var delete_url = $(this).attr('href');

        swal({
            title: 'Are you sure?',
            text: '"' + obj_title + '" will be deleted! This action cannot be undone.',
            icon: 'warning',
            dangerMode: true,
            buttons: ['Cancel', 'Yes, delete it!'],
            closeOnEsc: true,
            closeOnClickOutside: true
        }).then((value) => {
            if (value) {
                $.ajax({
                    url: delete_url,
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $(document).find('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function(data) {
                        if (data.result) {
                            var item = targ_elem.parent().parent();
                            item.empty();
                            // swal('Deleted!', 'Successfully deleted.', 'success');
                        }
                    },
                    error:function() {
                        swal('Uh oh!', 'Something went wrong!.', 'error');
                    }
                });
            } else {
                // swal('Crisis averted!', 'No action taken.', 'success');
            }

        });

    });*/

    // Toggle expand/collapse labels on iboxes
    $('.collapse-link').on('click', function (event) {
        var label = $(this).find('span').html();
        if (label === 'Expand') {
            $(this).find("span").html('Collapse');
        } else {
            $(this).find("span").html('Expand');
        }
    });

    // ------------------------------------------------------------------------
});
