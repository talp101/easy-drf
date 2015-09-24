from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from easy_drf.decorators.etag import etag


class ModelFlatEtagViewSet(NestedViewSetMixin, ModelViewSet):
    flat_serializer_class = None

    @etag
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.flat_serializer_class(instance)
        return Response(serializer.data)

    @etag
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.flat_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.flat_serializer_class(queryset, many=True)
        return Response(serializer.data)
