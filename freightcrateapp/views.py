# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
  
""" django """   
from django.shortcuts import render, redirect
from django.views import generic

""" local django """
from .forms import (
    UrlFormset,
)
from utils import extract_page_title_from_urls

""" main fucntion url
@param request
"""
def urlView(request):
    """ template name """
    template_name = 'freightcrate/index.html'
    
    """ heading message """
    heading_message = 'FreightCrate Page Title Extraction'

    """ Basesd on http method """
    if request.method == 'GET':
        formset = UrlFormset(request.GET or None)
    elif request.method == 'POST' and request.is_ajax():
        urls = json.loads(request.POST.get('urlslist'))
        response = extract_page_title_from_urls(urls)
        return response

    """ rendering data to template """
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


