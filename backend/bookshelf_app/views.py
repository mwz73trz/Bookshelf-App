from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from bookshelf_app.models import Book
from bookshelf_app.serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def filter_book(self, finished):
        book_list = Book.objects.filter(finished=finished)
        serializer = self.get_serializer(book_list, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def finished(self):
        return self.filter_book(finished=True)

    @action
    def unfinished(self):
        return self.filter_book(finished=False)

