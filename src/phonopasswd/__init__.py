#!/usr/bin/env python3
"""Phonetic password generator."""

from random import choice
import argparse
import sys

from phonopasswd import languages


__version__ = "2.0.0"


LANGUAGE_CLASSES = {
    "en": languages.English,
    "it": languages.Italian,
    "de": languages.German,
    "fr": languages.French,
}


class PhonoPasswd(object):
    """Main application class."""

    def __init__(self, language="en"):
        if language not in LANGUAGE_CLASSES:
            raise NotImplementedError("This language is not supported")
        self.language_class = LANGUAGE_CLASSES[language]

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
        choices=LANGUAGE_CLASSES.keys(),
        default="en",
    )
    parser.add_argument(
        "--version",
        "-V",
        help="Print version and exit",
        action="store_true",
    )
    args = parser.parse_args(argv)
    if args.version:
        print(__version__)
        sys.exit(0)
    app = PhonoPasswd(args.language)
    print(app.generate_password())


if __name__ == "__main__":
    main()
