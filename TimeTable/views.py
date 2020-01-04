from rest_framework.renderers  import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response   import Response
from .utils       import decode_serialized_data, decode_query_data
from .serializers import LessonSerializer 
from .models      import Lesson
# Create your views here.    

@api_view(['GET'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer])
def table(request, **kwargs):
    """
    
    """
    kwargs['is_extra'] = request.GET["type"]=='extra'
    query_set = Lesson.objects.filter(**kwargs)
    if request.accepted_renderer.format == 'json':
        serialized = LessonSerializer(query_set, many = True)
        decode_serialized_data(query_set, serialized) 
        return Response( serialized.data )    
    
    tmp = 'TimeTable/'
    tmp += 'coursestable' if 'course' in kwargs else 'table.html'
    content = decode_query_data(query_set)
    return Response(content, template_name = tmp)