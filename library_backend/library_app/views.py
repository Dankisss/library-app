import json
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book

class BookCreateView(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body)

            title = body.get('title')
            author = body.get('author')
            description = body.get('description')
            covers = body.get('covers')
            subject_places = body.get('subject_places')
            subject_times = body.get('subject_times')
            subjects = body.get('subjects')
            first_publish_year = body.get('first_publish_year') 
            edition_count = body.get('edition_count')

            book = Book.objects.create(
                title=title,
                author=author,
                description=description,
                covers=covers,
                subject_places=subject_places,
                subject_times=subject_times,
                subjects=subjects,
                first_publish_year=first_publish_year,
                edition_count=edition_count
            )

            return JsonResponse({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'covers': book.covers,
                'subject_places': book.subject_places,
                'subject_times': book.subject_times,
                'subjects': book.subjects,
                'first_publish_year': book.first_publish_year,
                'edition_count': edition_count
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

from .serializers import BookSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all() 
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)  
            book.delete() 
            return Response({"message": "Book deleted successfully!"}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
        
class BookSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None) 
        if query:
            books = Book.objects.filter(title__icontains=query)
        else:
            books = Book.objects.all() 
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookSearchViewId(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk) 
            serializer = BookSerializer(book)  
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)