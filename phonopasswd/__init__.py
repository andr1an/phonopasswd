#!/usr/bin/env python
"""Phonetic passwords generator."""

from __future__ import print_function
from random import choice
import argparse
import sys

from phonopasswd import languages


__version__ = "1.1"


class PhonoPasswd(object):
    """Main aplication class."""

    def __init__(self, language="en"):
        language_classes = {
            "en": languages.English,
            "it": languages.Italian,
            "de": languages.German,
        }
        if language not in language_classes:
            raise NotImplementedError("This language is not supported")
        self.language_class = language_classes[language]

    def _syllable(self):
        """Returns a random syllable."""
        return "".join(
            [choice(i) for i in choice(self.language_class.SYLLABLE_FORMATS)]
        )

    def generate_password(self):
        """Returns a phonetic password."""
        number_char = str(choice(range(9)))
        glue = choice(
            (
                [number_char, choice("-_")],
                ["-", "_"],
                ["", choice((number_char, "-", "_"))],
            )
        )
        if choice((0, 1)):
            glue.reverse()
        password = self._syllable().title()
        for i in range(1, 3):
            new_syllable = self._syllable()
            while any(_char.lower() in new_syllable for _char in password):
                new_syllable = self._syllable()
            password += glue[i - 1] + new_syllable.title()
        return password


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--language",
        "-l",
        help="Language",
        choices=("en", "it", "de"),
        default="en",
    )
    args = parser.parse_args(argv)
    app = PhonoPasswd(args.language)
    print(app.generate_password())


if __name__ == "__main__":
    main()

# vim: ts=4:sw=4:et:sta:si
