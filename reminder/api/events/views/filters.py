from rest_framework import filters


class EventFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        status = request.query_params.get("status")
        role = request.query_params.get("role")
        kwargs = {"participants__user": request.user}
        if role is not None:
            kwargs.update({"participants__role": role})
        if status is not None:
            kwargs.update({"status": status})
        return queryset.filter(**kwargs)
