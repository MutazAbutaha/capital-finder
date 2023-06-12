from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
   
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dict = dict(query_list)

    if 'country' in my_dict:
      word = my_dict.get('country')
      url= 'https://restcountries.com/v3.1/name/'
      res = requests.get(url+word)
      data = res.json()
      for word_data in data :
          definition = word_data['capital'][0]
          message = f"The capital of {word} is {definition}"

    elif 'capital' in my_dict:
      word = my_dict.get('capital')
      url= 'https://restcountries.com/v3.1/capital/'
      res = requests.get(url+word)
      data = res.json()
      for word_data in data :
        definition = word_data['name']['common']
        message = f"{word} The Capital of {definition}"


    self.wfile.write(message.encode())
    return