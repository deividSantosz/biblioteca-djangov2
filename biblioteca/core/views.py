from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Para Filtros
class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']

# Para Livro
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

# Para Categoria
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

# Para Autor
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

# Home View
class HomeView(APIView):
    def get(self, request):
        # Buscando dados
        livros = Livro.objects.all()
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        # Serializando dados
        livros_serializados = LivroSerializer(livros, many=True).data
        categorias_serializadas = CategoriaSerializer(categorias, many=True).data
        autores_serializados = AutorSerializer(autores, many=True).data

        # Retornando a resposta
        return Response({
            "livros": livros_serializados,
            "categorias": categorias_serializadas,
            "autores": autores_serializados
        })

