import requests
import json

class Flypme:
    def __init__(self):
        self.api_url = "https://flyp.me/api/v1/"

    def __get_request(self, url):
        final_url = self.api_url + url
        headers = self.__headers()
        response = requests.get(final_url, headers=headers, verify=False)

        return response.json()

    def __post_request(self, url, message):
        final_url = self.api_url + url
        headers = self.__headers()
        serialized_data = json.dumps(message)
        response = requests.post(final_url, headers=headers, data=serialized_data, verify=False)
        
        return response.json()

    def __headers(self):
        flypme_headers = {'Content-type': 'application/json'}
        return flypme_headers

    def new_order(self, from_currency, to_currency, ordered_amount, destination):
        url = "order/create"
        message = {
            "order": {
                "from_currency": from_currency,
                "to_currency": to_currency,
                "ordered_amount": ordered_amount,
                "destination": destination
            }
        }

        return self.__post_request(url, message)

    def check_order(self, uuid):
        url = "order/check"
        message = {
            "uuid": uuid
        }

        return self.__post_request(url, message)

    def info_order(self, uuid):
        url = "order/info"
        message = {
            "uuid": uuid
        }

        return self.__post_request(url, message)

    def cancel_order(self, uuid):
        url = "order/cancel"
        message = {
            "uuid": uuid
        }

        return self.__post_request(url, message)

    def exchange_rates(self):
        url = "data/exchange_rates"
        return self.__get_request(url)

    def active_currencies(self):
        url = "currencies"
        return self.__get_request(url)

    def order_limits(self):
        url = "order/limits"
        return self.__post_request(url, "")
