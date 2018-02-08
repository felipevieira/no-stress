# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.http import JsonResponse



def get_nonstress_song(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'

    return JsonResponse(response_data)


# Create your views here.
