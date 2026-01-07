import string
import random


class URLShortener:
    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}
        self.base_url = "http://localhost:5000/"

    def _generate_code(self, length=6):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def shorten_url(self, long_url):
        if long_url in self.long_to_short:
            return self.base_url + self.long_to_short[long_url]

        code = self._generate_code()
        while code in self.short_to_long:
            code = self._generate_code()

        self.long_to_short[long_url] = code
        self.short_to_long[code] = long_url
        return self.base_url + code

    def expand_url(self, code):
        return self.short_to_long.get(code)
