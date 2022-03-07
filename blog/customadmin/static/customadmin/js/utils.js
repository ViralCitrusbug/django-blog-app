/* global $ */
'use strict';

var utils = {

    action_ids: [],


    /**
     * Update Order
     * NOTE: METHOD NOT CURRENTLY IN USE!
     *
     * @param {element} formElem
     * @param {string} orderUrl
     */
    updateOrder: function(formElem, orderUrl) {
        var postData = $(formElem).serializeArray();
        $.ajax({
            url: orderUrl,
            type: 'POST',
            data: postData,
            success: function(data) {
                console.log(data);
            }
        });
    },

    /**
     * Sortable Table
     *
     * Takes a table and a hidden element and makes the table sortable with a
     * callback that updates a hidden element when the table order is changed.
     *
     * @param {element} tableElem
     * @param {element} orderElem
     * @param {function} updateFunc
     */
    sortableTable: function(tableElem, orderElem, updateFunc) {
        console.debug('sortableTable', tableElem, orderElem);
        $(tableElem + ' tbody').sortable({
            cursor: 'move',
            axis: 'y',
            containment: 'parent',
            items: 'tr',
            distance: 10,
            tolerance: 'pointer',
            cancel: 'a',
            helper: function(e, ui) {
                // make sure table columns maintain their widths
                ui.children().each(function() {
                    $(this).width($(this).width());
                });
                return ui;
            },
            update: function() {
                utils.orderTableRows(tableElem, orderElem);
                if (typeof updateFunc !== "undefined") {
                    updateFunc();
                }
            }
        }).disableSelection();

        utils.orderTableRows(tableElem, orderElem);
    },

    sortableTableDragula: function(tableElem, orderElem, updateFunc) {
        console.debug('sortableTableDragula', tableElem, orderElem);

        var drake = dragula({
            containers: [$(tableElem).find('tbody')[0]],
            direction: 'vertical'
        });
        drake.on('drop', function(el, target, source, sibling) {
            utils.orderTableRows(tableElem, orderElem);
            if (typeof updateFunc !== "undefined") {
                updateFunc();
            }
        });
        drake.on('cloned', function(clone, original, type) {
            // TODO: make sure table columns maintain their widths
        });

        utils.orderTableRows(tableElem, orderElem);
    },


    /**
     * Order Table Rows
     *
     * Takes a table and a hidden element and updates the hidden element with
     * the current order of all items.
     *
     * @param {element} tableElem
     * @param {element} orderElem
     */
    orderTableRows: function(tableElem, orderElem) {
        console.debug('orderTableRows', tableElem, orderElem);
        var list_order = [];

        // keep track of tr item order
        $(tableElem + ' tbody tr').each(function() {
            var order = $(this).index() + 1;
            $(this).attr('data-order', order);

            list_order.push({
                'id': $(this).data('id'),
                'order': order
            });
        });

        // update hidden field for use by Django
        $(orderElem).val(JSON.stringify(list_order));
    },

    /**
     * Add Table Row Actions
     *
     * Takes a table and adds generic actions to the table rows.
     *
     * @param {element} tableElem
     */
    addTableRowActions: function(tableElem) {
        console.debug('addTableRowActions');
        // copy thr row actions HTML and then inject it into the data table
        var actions = $('#row-actions').html();
        $('#row-actions').remove();
        var target = $(tableElem + '_wrapper .row .col-sm-6').first();
        target.html(actions);

        // need to use icheck events rather than native events
        $(tableElem + ' tbody tr input[type=checkbox]').on('ifChecked', function() {
            utils.action_ids.push($(this).val());
            //console.log(utils.action_ids);
        });

        $(tableElem + ' tbody tr input[type=checkbox]').on('ifUnchecked', function() {
            var index = utils.action_ids.indexOf($(this).val());
            if (index > -1) {
                utils.action_ids.splice(index, 1);
            }
            //console.log(utils.action_ids);
        });

        $('#select-all').on('ifChecked', function() {
            $("input[name^='action']").iCheck('check');
        });

        $('#select-all').on('ifUnchecked', function() {
            $("input[name^='action']").iCheck('uncheck');
        });

        // Action submit button
        $('#action-submit').click(function() {
            var action = $('#action-select').val();
            $('#action-modal .action-name').html(action);
            console.log(action);
            console.log(utils.action_ids);

            // Make sure there is no click event on this, so unbind it then add it again.
            $('#action-modal .btn-danger').unbind('click').on('click', function() {
                $.ajax({
                    url: window.action_url,
                    type: 'POST',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                        'action': action,
                        'primary_keys': JSON.stringify(utils.action_ids)
                    },
                    success: function(data) {
                        $('#action-modal').modal('hide');
                        if (data.result) {
                            console.debug(data);
                            window.location.reload();
                        } else {
                            console.error(data);
                        }
                    }
                });
            });

            $('#action-modal').modal('show');

        });

    },

    /**
     * inlineFormAdd
     *
     * Sets up inline forms so we can add rows.
     *
     * @param {str} id
     * @param {function} callback
     */
    inlineFormAdd: function(id, callback) {
        $(document).on('click', '#add-inline', function() {
            // console.log('add-form');
            event.preventDefault();
            var template_markup = $('#' + id + '-template').html();
            var count = parseInt($('#id_' + id + '-TOTAL_FORMS').attr('value'), 10);
            var compiled_template = template_markup.replace(/__prefix__/g, count);
            // console.log(compiled_template)
            $('#' + id + '-table tbody').append(compiled_template);
            $('#id_' + id + '-TOTAL_FORMS').attr('value', count + 1);

            if (callback != undefined) {
                callback();
            }
        });
    },

    /**
     * inlineFormRemove
     *
     * Sets up inline forms so we can remove rows.
     */
    inlineFormRemove: function() {
        $(document).on('click', '.inlineform-remove', function() {
            if ($(this).hasClass('btn-default')) {
                $(this).removeClass('btn-default').addClass('btn-danger')
                    .find('i').removeClass('fa-minus').addClass('fa-times');
                $(this).parent().find('input[type=checkbox]').attr("checked", "checked");
            } else if ($(this).hasClass('btn-danger')) {
                $(this).removeClass('btn-danger').addClass('btn-default')
                    .find('i').removeClass('fa-times').addClass('fa-minus');
                $(this).parent().find('input[type=checkbox]').removeAttr('checked');
            }

            if ($(this).attr('data-button') === 'new') {
                $(this).parent().parent().remove();
            }
        });
    }

    /**
     * Add Published Filter
     *
     * Takes a table and adds filtering by published.
     *
     * @param {element} tableElem
     * @param {int} column
     */
    /*addPublishedFilter: function(tableElem, column) {
        console.debug('addPublishedFilter');
        // filter by published/unpublished
        function filterPublished(term) {
            console.log(term);
            var table = $(tableElem).DataTable();
            table.columns(column).search(term).draw();
        }

        $('#btn-all').on('click', function(e) {
            e.preventDefault();
            filterPublished($(this).attr('data-search'));
            //$(this).addClass('active');
            $(this).attr('disabled', 'disabled');
            $('#btn-published').removeAttr('disabled');
            $('#btn-unpublished').removeAttr('disabled');
        });

        $('#btn-published').on('click', function(e) {
            e.preventDefault();
            filterPublished($(this).attr('data-search'));
            //$(this).addClass('active');
            $(this).attr('disabled', 'disabled');
            $('#btn-all').removeAttr('disabled');
            $('#btn-unpublished').removeAttr('disabled');
        });

        $('#btn-unpublished').on('click', function(e) {
            e.preventDefault();
            filterPublished($(this).attr('data-search'));
            //$(this).addClass('active');
            $(this).attr('disabled', 'disabled');
            $('#btn-all').removeAttr('disabled');
            $('#btn-published').removeAttr('disabled');
        });
    }*/


};
