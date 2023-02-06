from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from globalmessages.models import GlobalMessage
from globalmessages.serializers import GlobalMessageSerializer

@csrf_exempt
def globalmessage_list(request):
    """
    List all code globalmessages, or create a new globalmessage.
    """
    if request.method == 'GET':
        globalmessages = GlobalMessage.objects.all()
        serializer = GlobalMessageSerializer(globalmessages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GlobalMessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def globalmessage_detail(request, pk):
    """
    Retrieve, update or delete a code globalmessage.
    """
    try:
        globalmessage = GlobalMessage.objects.get(pk=pk)
    except GlobalMessage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GlobalMessageSerializer(globalmessage)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GlobalMessageSerializer(globalmessage, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        globalmessage.delete()
        return HttpResponse(status=204)

# from django.http import Http404
# from rest_framework import viewsets
# from rest_framework.response import Response
# from colossus.globalmessages.models import GlobalMessage
# from colossus.globalmessages.serializers import GlobalMessageSerializer


# class GlobalMessageViewSet(viewsets.ModelViewSet):
#     queryset = GlobalMessage.objects.all()
#     serializer_class = GlobalMessageSerializer
#     lookup_field = 'slug'

#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             serializer = self.get_serializer(instance)
#             return Response(serializer.data)
#         except Http404:
#             return Response({ 'detail': 'no content found' })
            