import json
from urllib.request import urlopen

import requests
from django.shortcuts import render

# Create your views here.

class GetWeather(object):
    def __init__(self):
        self.weather_url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
        self.ip_url = 'https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'

    def get_location(self):
        loc_js = urlopen(self.ip_url).read().decode()
        loc_dict = json.loads(loc_js)
        city = loc_dict['content']['address_detail']['city']
        return city

    def get_data(self, location):
        url = self.weather_url.format(location)

        js_content = requests.get(url).text
        js_dict = json.loads(js_content)
        return js_dict

def index(request):
    weather = GetWeather()
    location = weather.get_location()
    location = request.GET.get('location', location)
    data_list = weather.get_data(location)['results'][0]
    return render(request, template_name='index.html', context=data_list)













