# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import urllib2
from bs4 import BeautifulSoup   ## pip install beautifulsoup4

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import (
    UrlFormset,
)

# Create your views here.
def urlView(request):
    template_name = 'freightcrate/index.html'
    heading_message = 'Url Form Demo'
    if request.method == 'GET':
        formset = UrlFormset(request.GET or None)
    elif request.method == 'POST' and request.is_ajax():
        urls = json.loads(request.POST.get('urlslist'))
        response = extract_page_title_from_urls(urls)
        return response

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


def get_data(url):
	soup = BeautifulSoup(urllib2.urlopen(url))
	return soup.title.string
	
def respondWithCollection(statusCode, data):
    response = {}
    response['data'] = data
    
    response['notification'] = {}
    response['notification']['hint'] = "Response Sent"
    response['notification']['message'] = "Success"
    response['notification']['code'] = "200"
    response['notification']['type'] = "Success"
       
    response =  JsonResponse(response, content_type='application/json', status=statusCode)
    return response

def extract_page_title_from_urls(urls):
	result = []
	for url in urls:
		data = {
			'url': url,
			'title': get_data(url)
		}
		result.append(data)
	return respondWithCollection(200, result)