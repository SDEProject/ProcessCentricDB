import requests
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views import View
from requests import Response
from rest_framework import viewsets, mixins
from travelando import settings
import json

# Create your views here.
class SaveProcessCentricDBView(View):
    def post(self, request):
        body = request.body.decode('utf-8')
        parameters = json.loads(body)

        request_parameters = parameters['request_parameters']

        intent_name = request_parameters['intentName']
        type = request_parameters['type']

        print(parameters)

        if 'type' in request_parameters:
            if intent_name == 'save':
                if type == 'search':
                    response = requests.post(f"http://{settings.MYDB_HOST}:{settings.SERVICE_BUSINESS_LOGIC_DB_PORT}/{settings.SERVICE_BUSINESS_LOGIC_DB}/search/", None, parameters)
                elif type == 'result':
                    response = requests.post(f"http://{settings.MYDB_HOST}:{settings.SERVICE_BUSINESS_LOGIC_DB_PORT}/{settings.SERVICE_BUSINESS_LOGIC_DB}/result/", None, parameters)
                else:
                    response = HttpResponseBadRequest(f"BAD REQUEST: unknown {type} for type parameter. Try search or result.")
                    return HttpResponseBadRequest(response)
        else:
            response = HttpResponseBadRequest(f"BAD REQUEST: type parameter not defined.")
            return HttpResponseBadRequest(response)
        return JsonResponse(response.json(), safe=False)


class RetrieveProcessCentricDBView(View):
    def get(self, request):
        parameters = request.GET
        intent_name = parameters.get('intentName', None)
        type = parameters.get('type', None)

        if type:
            if intent_name == 'retrieve':
                if type == 'search':
                    response = requests.get(
                        f"http://{settings.MYDB_HOST}:{settings.SERVICE_BUSINESS_LOGIC_DB_PORT}/{settings.SERVICE_BUSINESS_LOGIC_DB}/search/", parameters)
                elif type == 'result':
                    response = requests.get(
                        f"http://{settings.MYDB_HOST}:{settings.SERVICE_BUSINESS_LOGIC_DB_PORT}/{settings.SERVICE_BUSINESS_LOGIC_DB}/result/", parameters)
                else:
                    response = HttpResponseBadRequest(
                        f"BAD REQUEST: unknown {type} for type parameter. Try search or result.")
                    return HttpResponseBadRequest(response)
        else:
            response = HttpResponseBadRequest(f"BAD REQUEST: type parameter not defined.")
            return HttpResponseBadRequest(response)

        return JsonResponse(response.json(), safe=False)

class DeleteProcessCentricDBView(View):
    def post(self, request):
        body = request.body.decode('utf-8')
        parameters = json.loads(body)
        intent_name = parameters['intentName']
        type = parameters['type']

        if type:
            if intent_name == 'delete':
                if type == 'search' or type == 'result':
                    response = requests.post(
                        f"http://{settings.MYDB_HOST}:{settings.SERVICE_BUSINESS_LOGIC_DB_PORT}/{settings.SERVICE_BUSINESS_LOGIC_DB}/delete/", None,
                        parameters)
                else:
                    response = HttpResponseBadRequest(
                        f"BAD REQUEST: unknown {type} for type parameter. Try search or result.")
                    return HttpResponseBadRequest(response)
        else:
            response = HttpResponseBadRequest(f"BAD REQUEST: type parameter not defined.")
            return HttpResponseBadRequest(response)

        return JsonResponse(response.json(), safe=False)