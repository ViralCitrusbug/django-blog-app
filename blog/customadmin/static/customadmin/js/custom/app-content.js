/*global $ */
'use strict';

var app_contents_data = {

    // ------------------------------------------------------------------------
    // APP Content
    // ------------------------------------------------------------------------
    app_contents: {

        index: function () {
            $('#appcontent-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },]
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------


};
