from rest_framework            import viewsets
from rest_framework.generics   import get_object_or_404
from rest_framework.renderers  import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response   import Response

from .serializer import IntroduceSerializer
from .models     import Introduce

class IntroViewSet(viewsets.ViewSet):
    """
        класс представлений для отображения статей
    """
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    def retrieve(self, request):
        """
            выводит статью "о нас"
        """
        article = get_object_or_404(Introduce, id=1)
        if request.accepted_renderer.format == 'json':
            serialized = IntroduceSerializer(article)
            return Response(serialized.data)
        context = {
            'authors': article.authors.split(', '),
            'title': article.title,
            'text': article.text,
            }
        return Response(context, template_name = 'Intro/about.html')
        
    def list (self, request):
        """
            выводит первые 5 статей списком
        """
        query_set = Introduce.objects.all()[:5]
        
        if request.accepted_renderer.format == 'json':
            serialized = IntroduceSerializer(query_set, many=True)
            return Response(serialized.data)
            
        context = { 'articles': query_set }
        return Response(context, template_name = 'Intro/index.html')