/*global $ */
'use strict';

var group_registration_data = {

    // ------------------------------------------------------------------------
    // Group Registration
    // ------------------------------------------------------------------------
    group_registration: {

        index: function () {
            $('#groupregistration-table').DataTable({
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
