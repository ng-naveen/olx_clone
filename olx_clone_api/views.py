from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from olx_clone_api.serializers import BikeSerializer
from olx_clone_api.models import BikeModel

class BikeView(APIView):
    def get(self, request, *args, **kwargs):
        bikes_objs = BikeModel.objects.all()

        if 'limit' in request.query_params:
            bike_limit = request.query_params.get('limit')
            bikes_objs = bikes_objs[:int(bike_limit)]


        deserialized_data = BikeSerializer(bikes_objs, many=True)
        return Response(data=deserialized_data.data)

    def post(self, request, *args, **kwargs):
        bike_data = request.data
        serialized_data = BikeSerializer(data=bike_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        else:
            return Response(data=serialized_data.errors)


class BikeDetailView(APIView):
    def get(self, request, *args, **kwargs):
        bike_id = kwargs.get('id')
        bike_obj = BikeModel.objects.get(id=bike_id)
        deserialized_data = BikeSerializer(bike_obj, many=False)
        return Response(data=deserialized_data.data)

    def put(self, request, *args, **kwargs):
        bike_id = kwargs.get('id')
        bike_obj = BikeModel.objects.get(id=bike_id)
        serialized_data = BikeSerializer(data=request.data, instance=bike_obj)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        else:
            return Response(data=serialized_data.errors)

    def delete(self, request, *args, **kwargs):
        bike_id = kwargs.get('id')
        BikeModel.objects.get(id=bike_id).delete()
        return Response(data='Deleted')
