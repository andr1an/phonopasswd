"""Languages sounds classes.

Every language class should have SYLLABLE_FORMATS tuple with some
tuples that contain possible letters or digraphs on each position.

Example:

    class MyLanguage:
        SYLLABLE_FORMATS = (
            (
                ("schw", "pf", "c", "d"),
                ("a", "e", "i", "o", "u"),
                ("k", "c", "p", "t")
            ),
        )

    # This language can generate "Schwe_Pfa1Cit" or "Cut3Phik-Dot"

"""


class English:
    _CONSONANTS = tuple("bcdfghjklmnpqrstvwxyz")
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
        (_CONSONANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSONANTS),
        (_CONSONANTS, _VOWELS, _DIGRAPHS_LAST),
    )


class Italian:
    _CONSONANTS = tuple("bcdfghjklmnpqrstvwxyz")
    _VOWELS = ("a", "e", "i", "o", "u")
    _DIGRAPHS_FIRST = ("ch", "ci", "gh", "gi", "gl", "gn", "sc")
    _DIGRAPHS_LAST = ("ci", "gi")

    # Public constant
    SYLLABLE_FORMATS = (
        (_CONSONANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSONANTS),
        (_CONSONANTS, _VOWELS, _DIGRAPHS_LAST),
    )


class German:
    _CONSONANTS = tuple("bcdfghjklmnpqrstvwxyz")
    _VOWELS = ("a", "e", "i", "o", "u", "ei", "eu")
    _DIGRAPHS_FIRST = ("st", "sp")
    _DIGRAPHS_LAST = "ss"

    # Public constant
    SYLLABLE_FORMATS = (
        (_CONSONANTS + _DIGRAPHS_FIRST, _VOWELS, _CONSONANTS),
        (_CONSONANTS, _VOWELS, _DIGRAPHS_LAST),
        (("schw", "pf"), _VOWELS, _CONSONANTS),
    )


class French:
    _CONSONANTS = tuple("bcdfghjklmnpqrstvwxz")
    _VOWELS = ("a", "e", "i", "o", "u", "y")
    _DIPHTHONGS = (
        "ai", "au", "ei", "eu", "ie", "oi", "ou", "ui", "ue"
    )
    _NASALS = ("an", "en", "in", "on", "un", "yn", "ain", "ien", "oin")

    _DIGRAPHS_FIRST = (
        "ch", "gn", "ph", "qu"
    )
    _DIGRAPHS_LAST = (
        "ch", "gn", "ph", "qu", "ct", "rt", "nt", "rd", "rs", "lt", "mp", "nd"
    )

    # Public constant
    SYLLABLE_FORMATS = (
        (
            _CONSONANTS + _DIGRAPHS_FIRST,
            _VOWELS + _DIPHTHONGS + _NASALS,
            _CONSONANTS + _DIGRAPHS_LAST
        ),
        (_CONSONANTS, _NASALS),
        (_DIPHTHONGS, _CONSONANTS),
    )
