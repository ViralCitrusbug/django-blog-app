# -*- coding: utf-8 -*-

import logging
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

logger = logging.getLogger(__name__)


class DataTableMixin(object):
    """
    Create JSON response suitable for datatables ajax pagination.
    https://datatables.net/manual/server-side
    """

    model = None
    queryset = None

    @property
    def _querydict(self):
        """Return the request method query dict."""
        if self.request.method == "POST":
            return self.request.POST
        else:
            return self.request.GET

    @property
    def draw(self):
        """Draw counter. This is used by DataTables to ensure that the Ajax
        returns from server-side processing requests are drawn in sequence by
        DataTables (Ajax requests are asynchronous and thus can return out of
        sequence)."""
        return int(self._querydict.get("draw"))

    @property
    def start(self):
        """Paging first record indicator. This is the start point in the
        current data set (0 index based - i.e. 0 is the first record)."""
        return int(self._querydict.get("start"))

    @property
    def length(self):
        """Number of records that the table can display in the current draw."""
        return int(self._querydict.get("length"))

    @property
    def order_col(self):
        """Column to which ordering should be applied."""
        return int(self._querydict.get("order[0][column]"))

    @property
    def order_dir(self):
        """Ordering direction for this column. It will be asc or desc to
        indicate ascending ordering or descending ordering, respectively."""
        return self._querydict.get("order[0][dir]")

    @property
    def search(self):
        """Global search value. To be applied to all columns which have
        searchable as true."""
        return self._querydict.get("search[value]")

    @property
    def field(self):
        """Order by field."""
        return self._querydict.get(f"columns[{self.order_col}][name]")

    @property
    def page(self):
        """Current page."""
        return int(self.start / self.length + 1) if self.start > 1 else 1

    def get_ordering(self, qs):
        """Return the field or fields to use for ordering the queryset."""
        if not self.is_orderable():
            return qs
        # Determine sort order
        direction = "" if self.order_dir == "asc" else "-"
        ordering = f"{direction}{self.field}"
        # print(ordering)
        return qs.order_by(ordering)

    def is_orderable(self):
        if self._querydict.get("order"):
            return True
        return False

    def filter_queryset(self, qs):
        """
        Override with custom search logic.

        Example:
        ```
        if self.search:
            return qs.filter(
                Q(field1__icontains=self.search) |
                Q(field2__icontains=self.search) |
                Q(field3__icontains=self.search) |
                Q(field4__icontains=self.search)
            )
        return qs
        ```
        """
        return qs

    def get_queryset(self):
        """Get queryset."""
        if not self.queryset:
            return self.model.objects.all()
        return self.queryset

    def get_paging(self, qs):
        """Get paging."""
        paginator = Paginator(qs, self.length)
        try:
            object_list = paginator.page(self.page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)

        return object_list

    def prepare_results(self, qs):
        """Override this method."""
        return []

    def handle_exception(self, e):
        """Handle exceptions."""
        logger.exception(str(e))
        raise e

    def get_context_data(self, request):
        """Get object list."""
        try:
            self.request = request

            # Get queryset
            qs = self.get_queryset()

            # Number of records (before filtering)
            records_total = qs.count()

            # Apply filters
            qs = self.filter_queryset(qs)

            # Number of records (after filtering)
            records_filtered = qs.count()

            # Apply ordering
            qs = self.get_ordering(qs)

            # Apply pagintion
            qs = self.get_paging(qs)

            # Prepare output data
            data = self.prepare_results(qs)

            return {
                "draw": self.draw,
                "recordsTotal": records_total,
                "recordsFiltered": records_filtered,
                "data": data,
            }
        except Exception as e:
            return self.handle_exception(e)

    def get(self, request, *args, **kwargs):
        """Handle GET request."""
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)

    def post(self, request, *args, **kwargs):
        """Handle POST request."""
        return self.get(request, *args, **kwargs)
