from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from .models import Message, MessageSerializer
from django.http import JsonResponse


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

def get_data(request):
    json_object = {'key': "value"}
    return JsonResponse(json_object)

#
# class MessageViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
