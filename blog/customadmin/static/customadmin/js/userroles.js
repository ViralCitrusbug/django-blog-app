/*global $ */
"use strict";

var userroles = {
  // ------------------------------------------------------------------------
  // Users
  // ------------------------------------------------------------------------
  users: {
    index: function () {
      $("#user-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },
    details: function () {
      $(".groups-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available groups",
        selectedListLabel: "Chosen groups",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // Admin Keywords
  // ------------------------------------------------------------------------
  adminkeywords: {
    index: function () {
      $("#adminkeyword-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // Testimonials
  // ------------------------------------------------------------------------
  testimonials: {
    index: function () {
      $("#testimonial-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  foundationcode: {
    index: function () {
      $("#foundationcode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  groups: {
    index: function () {
      $("#group-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // User
  // ------------------------------------------------------------------------
  user: {
    index: function () {
      $("#user-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // servicecategory
  // ------------------------------------------------------------------------
  servicecategory: {
    index: function () {
      $("#servicecategory-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // inquirytype
  // ------------------------------------------------------------------------
  inquirytype: {
    index: function () {
      $("#inquirytype-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // timeslot
  // ------------------------------------------------------------------------
  timeslot: {
    index: function () {
      $("#timeslot-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // inquiry
  // ------------------------------------------------------------------------
  inquiry: {
    index: function () {
      $("#inquiry-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // phonenumbercode
  // ------------------------------------------------------------------------
  phonenumbercode: {
    index: function () {
      $("#phonenumbercode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // familycode
  // ------------------------------------------------------------------------
  familycode: {
    index: function () {
      $("#familycode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // socialcode
  // ------------------------------------------------------------------------
  socialcode: {
    index: function () {
      $("#socialcode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // othercode
  // ------------------------------------------------------------------------
  othercode: {
    index: function () {
      $("#othercode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // numbercode
  // ------------------------------------------------------------------------
  numbercode: {
    index: function () {
      $("#numbercode-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // shopproduct
  // ------------------------------------------------------------------------
  shopproduct: {
    index: function () {
      $("#shopproduct-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // service
  // ------------------------------------------------------------------------
  service: {
    index: function () {
      $("#service-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
  // ------------------------------------------------------------------------
  // purchasedproduct
  // ------------------------------------------------------------------------
  purchasedproduct: {
    index: function () {
      $("#purchasedproduct-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },

  // ------------------------------------------------------------------------
  // bookedservice
  // ------------------------------------------------------------------------
  bookedservice: {
    index: function () {
      $("#bookedservice-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },

  // ------------------------------------------------------------------------
  // categoryimage
  // ------------------------------------------------------------------------
  categoryimage: {
    index: function () {
      $("#categoryimage-table").DataTable({
        pageLength: 25,
        responsive: true,
        columnDefs: [
          {
            orderable: false,
            targets: -1,
          },
        ],
      });
    },

    details: function () {
      $(".permissions-select").bootstrapDualListbox({
        nonSelectedListLabel: "Available user permissions",
        selectedListLabel: "Chosen user permissions",
        preserveSelectionOnMove: "moved",
        moveOnSelect: false,
      });
    },
  },
};
