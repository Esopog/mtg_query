import requests
import json
from io import BytesIO
from PIL import Image
import urllib

class MTGQueryBuilder:
    
    def __init__(self):
        self._api_url = "https://api.scryfall.com/"
        self._named = "cards/named"
   
    def search_card_exact(self, card_name):
        url = "{api}{method}?exact={card_name}".format(api=self._api_url, method=self._named, card_name=card_name.replace(" ", "+"))
        response = requests.get(url)
        content = json.loads(response.text)
        png_url = content["image_uris"]["png"]

        fd = urllib.request.urlopen(png_url)
        image_file = BytesIO(fd.read())
        im = Image.open(image_file)
        im.show()


def main():
    query_builder = MTGQueryBuilder()

    query_builder.search_card_exact("birds of paradise")


if __name__ == "__main__":
    main()