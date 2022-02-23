"""Languages sounds classes.

Every language class should have SYLLABLE_FORMATS tuple with some
tuples that contain possible letters or digraphs on each position.

Example:

    class MyLanguage(object):
        SYLLABLE_FORMATS = (
            (
                ("schw", "pf", "c", "d"),
                ("a", "e", "i", "o", "u"),
                ("k", "c", "p", "t")
            ),
        )

    # This language can generate "Schwe_Pfa1Cit" or "Cut3Phik-Dot"

"""


class English(object):
    _CONSOLANTS = tuple("bcdfghjklmnpqrstvwxyz")
    _VOWELS = ("a", "e", "i", "o", "u", "ea", "ou")
    _DIGRAPHS_FIRST = (
        "sc",
        "ch",
        "tch",
        "sch",
        "gh",
        "ph",
        "rh",
        "sh",
        "th",
        "wh",
        "zh",
        "wr",
    )
    _DIGRAPHS_LAST = ("ng", "ch", "tch", "ck", "ph", "sh", "th")

    # Public constant
    SYLLABLE_FORMATS = (
        (_CONSOLANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSOLANTS),
        (_CONSOLANTS, _VOWELS, _DIGRAPHS_LAST),
    )


class Italian(object):
    _CONSOLANTS = tuple("bcdfghjklmnpqrstvwxyz")
    _VOWELS = ("a", "e", "i", "o", "u")
    _DIGRAPHS_FIRST = ("ch", "ci", "gh", "gi", "gl", "gn", "sc")
    _DIGRAPHS_LAST = ("ci", "gi")

    # Public constant
    SYLLABLE_FORMATS = (
        (_CONSOLANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSOLANTS),
        (_CONSOLANTS, _VOWELS, _DIGRAPHS_LAST),
    )


class German(object):
    _CONSOLANTS = tuple("bcdfghjklmnpqrstvwxyz")
    _VOWELS = ("a", "e", "i", "o", "u", "ei", "eu")
    _DIGRAPHS_FIRST = ("st", "sp")
    _DIGRAPHS_LAST = "ss"

    # Public constant
    SYLLABLE_FORMATS = (
        (_CONSOLANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSOLANTS),
        (_CONSOLANTS, _VOWELS, _DIGRAPHS_LAST),
        (("schw", "pf"), _VOWELS, _CONSOLANTS),
    )
