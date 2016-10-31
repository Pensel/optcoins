import requests
import itertools  # for repeat
# all data from https://anycoindirect.eu/api


def repeat(function, repeats):
    for _ in itertools.repeat(None, repeats):
        function()


def get_coin_codes():
    coin_codes = []
    api_call = "https://anycoindirect.eu/api/public/coins"
    r = requests.get(api_call)

    if r.status_code != 200:
        print("API ERROR")
    else:
        for code in r.json()["Data"]:
            coin_codes.append(code["Code"])
        return coin_codes


def get_coin_names():
    coin_names = []
    api_call = "https://anycoindirect.eu/api/public/coins"
    r = requests.get(api_call)

    if r.status_code != 200:
        print("API ERROR")
    else:
        for code in r.json()["Data"]:
            coin_names.append(code["Name"])
        return coin_names


def make_legend():
    legend = {}
    i = 0
    for code in get_coin_codes():
        legend[code] = get_coin_names()[i].lower()
        i += 1
    legend["DASH"] = "darkcoin"
    legend["PPC"] ="ppcoin"
    return legend


def get_buy_price(coin_code):

    api_call = "https://anycoindirect.eu/api/public/buyprices?CoinCode=" + coin_code + "&FiatCode=EUR&CoinAmount=1"
    r = requests.get(api_call)

    if r.status_code != 200:
        print("API ERROR")
    else:
        buy_price = r.json()["Data"][0]["FiatAmount"]
        for i in r.json()["Data"]:
            buy_price = round((buy_price + i["FiatAmount"]) / 2,  2)
        # print(str(coin_code) + "  " + str(buy_price) + "€")
        return buy_price


def make_a_dict():
    dict_price = {}
    for code in get_coin_codes():
        dict_price[code] = get_buy_price(code)
    return dict_price



