from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from .serializer import IntroduceSerializer
from .models import Introduce

@api_view(['GET'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer])
def default_intro(request):
    article = Introduce.objects.get(id=1)
    if request.accepted_renderer.format == 'json':
        serialized = IntroduceSerializer(article)
        return Response(serialized.data)
    context = {
        'authors': article.authors.split(', '),
        'title': article.title,
        'text': article.text,
    }
    return Response(context, template_name = 'Intro/about.html')