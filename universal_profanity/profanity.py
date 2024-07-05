import os
import random
import re
from typing import NoReturn

from universal_profanity._patterns import _PATTERNS

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

_COUNTRY_CODES = (
    'th', 'fr', 'uk', 'gr', 'ge', 'cz',
    'sp', 'bu', 'tc', 'da', 'po', 'en', 'br', 'du',
    'la', 'fi', 'no', 'in', 'ja', 'tu', 'ru', 'ro',
    'sc', 'it', 'ko', 'sw', 'vi', 'hu'
)

_DEFAULT_REPLACE_CHARS = '@#!*$^%'


class UniversalProfanity:
    def __init__(self, country: str | list = 'en', replace_chars: str = _DEFAULT_REPLACE_CHARS):
        self.validate_country(country)
        self._censor_chars = replace_chars
        self._censor_pool = []
        self._profanity_pattern = self.generate_pattern(country)

    @staticmethod
    def validate_country(country: str | list) -> NoReturn:
        if isinstance(country, list):
            for cc in country:
                if cc not in _COUNTRY_CODES:
                    raise ValueError(f"Invalid country code. Allowed codes are: {_COUNTRY_CODES}")
        elif isinstance(country, str):
            if country not in _COUNTRY_CODES:
                raise ValueError(f"Invalid country code. Allowed codes are: {_COUNTRY_CODES}")

    def get_censor_char(self):
        """Plucks a letter out of the censor_pool. If the censor_pool is empty,
        replenishes it. This is done to ensure all censor chars are used before
        grabbing more (avoids ugly duplicates).
        """
        if not self._censor_pool:
            # Censor pool is empty. Fill it back up.
            self._censor_pool = list(self._censor_chars)
        return self._censor_pool.pop(random.randrange(len(self._censor_pool)))

    def set_censor_characters(self, censor_chars):
        """Sets the pool of censor characters. Input should be a single string
        containing all the censor characters you'd like to use.
        Example: "@#$%^"
        """
        self._censor_chars = censor_chars

    @staticmethod
    def generate_pattern(obj):
        if isinstance(obj, list):
            pattern = rf"\b(:?{'|'.join([_PATTERNS[country] for country in obj])})\b"
            return re.compile(pattern, re.IGNORECASE)
        elif isinstance(obj, str):
            pattern = rf"\b(:?{_PATTERNS[obj]})\b"
            return re.compile(pattern, re.IGNORECASE)

    def contains_profanity(self, input_text):
        """Checks the input_text for any profanity and returns True if it does.
        Otherwise, returns False.
        """
        return input_text != self.censor(input_text)

    def censor(self, input_text):
        """Returns the input string with profanity replaced with a random string
        of characters plucked from the censor_characters pool.
        """
        clean_text = input_text

        for curse_word in re.finditer(self._profanity_pattern, input_text):
            censor_text = [self.get_censor_char() for _ in curse_word.group()]
            clean_text = clean_text.replace(curse_word.group(), ''.join(censor_text))

        return clean_text
