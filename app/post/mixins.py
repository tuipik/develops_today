from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response


class NewsViewSetMixin(viewsets.ModelViewSet):
    """Manage objects in the database"""

    serializer_class = None
    queryset = None
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user == instance.author_name:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
