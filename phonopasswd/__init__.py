#!/usr/bin/env python
"""Phonetic passwords generator."""

from random import choice


__version__ = '1.0'


VOWELS = ('a', 'e', 'i', 'o', 'u', 'ea', 'ou')
CONSOLANTS = tuple('bcdfghjklmnpqrstvwxyz')
DIGRAPHS_FIRST = ('sc', 'ch', 'tch', 'sch', 'gh', 'ph', 'rh', 'sh', 'th', 'wh',
                  'zh', 'wr')
DIGRAPHS_LAST = ('ng', 'ch', 'tch', 'ck', 'ph', 'sh', 'th')
SYLLABLE_FORMATS = (
    (CONSOLANTS + DIGRAPHS_FIRST, VOWELS, CONSOLANTS),
    (CONSOLANTS, VOWELS, DIGRAPHS_LAST),
)


def syllable():
    """Returns a random syllable."""
    return (''.join([choice(i) for i in choice(SYLLABLE_FORMATS)]))


def generate_password():
    """Returns a phonetic password."""
    number_char = str(choice(range(9)))
    glue = choice((
        [number_char, choice('-_')],
        ['-', '_'],
        ['', choice((number_char, '-', '_'))],
    ))
    if choice((0, 1)):
        glue.reverse()
    password = syllable().title()
    for i in range(1, 3):
        new_syllable = syllable()
        while any(_char.lower() in new_syllable for _char in password):
            new_syllable = syllable()
        password += glue[i - 1] + new_syllable.title()
    return password


def main():
    print(generate_password())


if __name__ == '__main__':
    main()

# vim: ts=4:sw=4:et:sta:si
