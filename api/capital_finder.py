from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests.

        Parses the URL, extracts query parameters, and determines whether to search for a capital or a country.
        Sends an HTTP response with the capital or country information.

        Returns:
            capital_country_finder()
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        my_query = dict(query_list)

        def capital_country_finder():
            """
            Find capital or country information based on the provided query.

            Returns:
                message(The capital of {country} is {capitals}) 
                or 
                message({capital} The Capital of {countries})
            """
            if "country" in my_query:
                country = my_query.get("country")
                url = "https://restcountries.com/v3.1/name/"
                res = requests.get(url + country)
                data = res.json()
                for word_data in data:
                    capitals = word_data["capital"][0]
                    message = f"The capital of {country} is {capitals}"

            elif "capital" in my_query:
                capital = my_query.get("capital")
                url = "https://restcountries.com/v3.1/capital/"
                res = requests.get(url + capital)
                data = res.json()
                for word_data in data:
                    countries = word_data["name"]["common"]
                    message = f"{capital} The Capital of {countries}"

            return self.wfile.write(message.encode())

        return capital_country_finder()
