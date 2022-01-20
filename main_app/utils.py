from django.urls.base import reverse
import requests

# CONFIG
BASE_SEARCH_API_URL = "http://openlibrary.org/search.json"
BASE_IMAGE_API_URL = "https://covers.openlibrary.org/b/{0}/{1}-{2}.jpg"
BASE_BOOK_API_URL = "https://openlibrary.org/works/{0}.json"
BASE_IMAGE_KEYS = [
      "cover_i",
      "isbm",
      "oclc",
      "lccn",
      "olid"
]
BASE_IMAGE_URL = "/static/images/base.png"
BASE_IMAGE_SIZE = "M"

BOOK_KEYS = [
      "title",
      "author_name",
      "key"
] + BASE_IMAGE_KEYS


def get_image_url(key_name, image_id, size = BASE_IMAGE_SIZE):
      # Just return image url with given attributes
      return BASE_IMAGE_API_URL.format(key_name, image_id, size)

def add_image_to_book(book_dict):
      book_dict['image'] = BASE_IMAGE_URL
      
      for image_key in BASE_IMAGE_KEYS:
                  # if book has image_key value set book['image']
                  if image_id_list := book_dict.get(image_key, None):
                        if image_key == "cover_i":
                              image_key = "id"
                              image_id_list = [image_id_list,]
                        book_dict['image'] = get_image_url(key_name = image_key, image_id = image_id_list[0])
                        break
      return book_dict

def add_images_to_books(books_list):
      return list(map(add_image_to_book, books_list))

def prepare_data(response, book_keys, no_of_results):

      response = response[:no_of_results]
      result = []

      for res_dict in response:
            # create new dict containing only neccessary book keys to reduce size
            new_dict = {key: res_dict[key] for key in res_dict if key in book_keys}
            
            # take only the first author of the book
            new_dict['author_name'] = new_dict.get("author_name", [""])[0]
            new_dict['key'] = new_dict.get("key", "").split("/")[-1]
            
            # append new dict contains less keys - values pairs
            result.append(new_dict)

      return result

def search_books(search_query):

      request_url = BASE_SEARCH_API_URL + '?q=' + search_query
      books = requests.get(request_url).json()['docs']

      # narrow down search results to 20 and outputs only the necessary keys for reading
      books = prepare_data(books, BOOK_KEYS, 20)

      # add images urls for books
      books = add_images_to_books(books)

      return books