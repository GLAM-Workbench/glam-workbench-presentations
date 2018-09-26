from IPython.display import display, HTML
import requests
import time
from IPython.display import display, HTML, clear_output

def show_page(url):
    display(HTML('<iframe height="500" width="800" src="{}"></iframe>'.format(url)))
    
def title():
    display(HTML('<h1>Small data and hand-crafted infrastructures</h1>'))

def update_corrections():
    params = {
        'q': 'has:corrections',
        'zone': 'newspaper',
        'encoding': 'json',
        'n': '0',
        'key': 'ju3rgk0jp354ikmh'
    }
    try:
        while True:
            clear_output(wait=True)
            response = requests.get('http://api.trove.nla.gov.au/v2/result', params=params)
            data = response.json()
            total = int(data['response']['zone'][0]['records']['total'])
            display(HTML('<p style="line-height: 15rem;">Trove users have corrected <span style="font-size: 10rem;">{:,}</span> newspaper articles.</p>'.format(total)))
            time.sleep(5)
    except KeyboardInterrupt:
        pass

    
def update_tags():
    params = {
        'q': 'has:tags',
        'zone': 'newspaper',
        'encoding': 'json',
        'n': '0',
        'key': 'ju3rgk0jp354ikmh'
    }
    try:
        while True:
            clear_output(wait=True)
            response = requests.get('http://api.trove.nla.gov.au/v2/result', params=params)
            data = response.json()
            total = int(data['response']['zone'][0]['records']['total'])
            display(HTML('<p style="line-height: 15rem;">Trove users have tagged <span style="font-size: 10rem;">{:,}</span> newspaper articles.</p>'.format(total)))
            time.sleep(5)
    except KeyboardInterrupt:
        pass