import requests
import web_crawler_price
from bs4 import BeautifulSoup


def make_request(code):
    r = requests.get("https://bitinfocharts.com/" + code + "/")
    return r


def process_diff(raw_diff):
    removed_comma = raw_diff.replace(",", "")
    removed_blank = removed_comma.replace(" ", "")
    removed_backslash_1 = removed_blank.replace("\uf061", "")
    removed_backslash_2 = removed_backslash_1.replace("\uf062", "")
    removed_backslash_3 = removed_backslash_2.replace("\uf063", "")
    removed_backslash_final = removed_backslash_3.replace("\uf064", "")

    if "T" in removed_backslash_final:
        factorized = removed_backslash_final.replace("T", "")
        factorized = int(float(factorized)) * 1000000
    else:
        factorized = removed_backslash_final
    return factorized


def get_diff(dictionary):
    dict_value_diff = {}
    for key, value in dictionary.items():
        request = make_request(value)
        soup = BeautifulSoup(request.content, "html.parser")
        diff = soup.find("td", {"id": "tdid15"}).text
        diff = process_diff(diff)
        dict_value_diff[value] = diff
    return dict_value_diff


