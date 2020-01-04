from rest_framework            import viewsets
from rest_framework.renderers  import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response   import Response
from .utils      import decoder
from .serializer import RoomSerilizer
from .models     import Room
# Create your views here.

class RoomAPIView(viewsets.ViewSet):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    
    def list(self, request, **kwargs):
        query_set = Room.objects.filter(**kwargs)
        
        if request.accepted_renderer.format == 'json':
            rooms_srlzd = RoomSerilizer(query_set, many = True)
            decoder(query_set, rooms_srlzd)
            return Response (rooms_srlzd.data)
            
        context = {'room_list': query_set}
        return Response(context, template_name = 'SchoolMap/floor.html')
    
    def retrieve(self, request, pk):
        room = get_object_or_404(Room, number = pk)
        
        if request.accepted_renderer == 'json':
            room_srlzd = RoomSerilizer(room)
            room_srlzd.data["number"] = room.decode_number()
            return Response ( room_srlzd.data )
        
        context = {'name':room.name, 'number':room.number}
        return Response( context, template_name = 'SchoolMap/detail.html' )
    