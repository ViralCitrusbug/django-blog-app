/*global $ */
'use strict';

var tabbed_nav = {

    // ------------------------------------------------------------------------
    // Events
    // ------------------------------------------------------------------------
    event: {

        index: function () {

        },

        details: function () {

            function showHashTargetTab() {
                // Show tab
                $(".nav-tabs a").each(function (index) {
                    $(this).parent().removeClass('active');
                });
                $('a[href="' + window.location.hash + '"]').parent().addClass('active');

                // Show tab content
                $(".tab-content .tab-pane").each(function (index) {
                    $(this).removeClass('active');
                });
                $(window.location.hash).addClass('active');
            }

            // Tabbed nav
            $(".nav-tabs a").click(function (e) {
                e.preventDefault();
                window.location.hash = $(this).attr('href');
            });

            $("a.quick-nav").click(function (e) {
                e.preventDefault();
                window.location.hash = $(this).attr('href');
                showHashTargetTab();
            });

            // Show proper tab on page load
            if (window.location.hash) {
                showHashTargetTab();
            } else {
                window.location.hash = '#tab-event';
                showHashTargetTab();
            }

        },

    }

    // ------------------------------------------------------------------------

};
