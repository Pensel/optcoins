import web_crawler_price
import web_crawler_diff


def ausgabe_dict(made_dict):
    for keys, values in made_dict.items():
        print(str(keys) + ": " + str(values))  # Ausgabe Dictionary


def print_legende():
    print("Legende: ")
    ausgabe_dict(web_crawler_price.make_legend())
    print("\n")


def print_preise():
    print("Preis in Euro:")
    ausgabe_dict(web_crawler_price.make_a_dict())
    print("\n")

def print_difficulty():
    print("Difficulty")
    ausgabe_dict(web_crawler_diff.get_diff(web_crawler_price.make_legend()))
    print("\n")