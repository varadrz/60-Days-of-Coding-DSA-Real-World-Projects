# Day 55 - URL Shortener
# Focus: System Design Lite + DSA (Hashing)
# Language: Python 3

import string
import random


class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "https://short.ly/"

    def _generate_key(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def shorten_url(self, long_url):
        key = self._generate_key()
        while key in self.url_map:
            key = self._generate_key()

        self.url_map[key] = long_url
        return self.base_url + key

    def expand_url(self, short_url):
        key = short_url.replace(self.base_url, "")
        return self.url_map.get(key, "URL not found")


def main():
    shortener = URLShortener()

    long_url = input("Enter long URL: ").strip()
    short_url = shortener.shorten_url(long_url)

    print("\nShort URL:", short_url)
    print("Expanded URL:", shortener.expand_url(short_url))


if __name__ == "__main__":
    main()
