from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from book.models import Book, Author
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializers = BookSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        book = BookCreateSerializer(data=request.data)
        book.is_valid()
        book.save()
        return Response("Book saved successfully")


# @api_view(['GET', 'DELETE'])
# def book_detail(request, pk):
#         book = Book.objects.get(pk=pk)
#         if request.method == 'GET':
#             serializer = BookCreateSerializer(book)
#             return Response(serializer.data)
#         if request.method == 'DELETE':
#             book.delete()
#             return Response('Book deleted successfully')

# getById
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(Book)
        return Response(serializer.data)


# getAll author
# @api_view(['GET', 'PUT', 'PATCH'])
# def book_author(request):
#     if request.method == 'GET':
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class based view
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# @api_view(['DELETE'])
# def book_delete(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response("Book not found", status=status.HTTP_404_NOT_FOUND)
#     book.delete()
#     return Response("Book deleted successfully", status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT'])
# def book_update(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response("Book not found", status=status.HTTP_404_NOT_FOUND)
#     serializer = BookCreateSerializer(book, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# classBasedViews
class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


# get all authors
# class AuthorsApiView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# get one author
class AuthorsApiView(generics.ListAPIView):
    def get(self, request, id):
        try:
            queryset = Author.objects.get(pk=id)
            serializer = AuthorSerializer(queryset)
            return Response(serializer.data)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

