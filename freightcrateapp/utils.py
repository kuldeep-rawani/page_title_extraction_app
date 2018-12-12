
""" libray """
import urllib2
from bs4 import BeautifulSoup

""" django """
from django.http import JsonResponse


""" get page title from url
@param url
@return title string
 """
def get_data(url):
	soup = BeautifulSoup(urllib2.urlopen(url))
	return soup.title.string
	

"""
@param urls
@return json response of url, title    
"""
def extract_page_title_from_urls(urls):
    result = []
    for url in urls:
        try:
            url = make_valid_url(url)
            data = {
                'url': url,
                'title': get_data(url)
            }
        except Exception as e:
            print e
            data = {
                'url': url,
                'title': 'Name or service not known'
            }
        result.append(data)
    return respondWithCollection(200, result)

""" make the url valid with https
"""
def make_valid_url(url):
    if url.startswith('https://www.'):
        return 'https://' + url[len('https://www.'):]
    if url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    if not url.startswith('http://'):
        return 'https://www.' + url
    return url

""" for returning data
@param http status code
@param data
@return json response
"""
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