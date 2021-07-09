import requests

def get_EUR_GBP_exchange():

    api_key = '5efad85ac008571f2d938413de17d8ab'
    end_point = 'http://api.exchangeratesapi.io/v1/latest?access_key=5efad85ac008571f2d938413de17d8ab'#&base=GBP'
    response = requests.get(end_point)
    #print(response.status_code)
    response_dict = response.json()
    GBP_value = response_dict["rates"]['GBP']
    print(GBP_value)
    return GBP_value

