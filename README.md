# phonopasswd

![build status](https://github.com/andr1an/phonopasswd/actions/workflows/tests.yaml/badge.svg)

Phonetic password generator in Python.

Passwords composed of random character sequences are often hard to remember
because they could not be pronounced like real words. Phonopasswd generates
passwords based on the syllable-building rules of a selected language, making
them easier to recall. Examples:

```
# English
Pock-Heth_Ris
SeamBuy1Jok

# French
Bun-OivLyq
Won-RierdAup

# German
PfeufTaw6Liv
Schwus_Pfeiq-Rog
```

*WARNING! Do not use any of the passwords above for securing your personal or
business accounts!*

## Installation

The package is not published into PyPI, but you can use `pip` with URL:

```bash
pip install git+https://github.com/andr1an/phonopasswd.git
```

## Usage

The package includes CLI tool `phonopasswd`:

```
phonopasswd [-h] [-l|--language {en,it,de,fr}] [-V|--version]
```

Also you can use the generator in your Python projects:

```python
>>> from phonopasswd import PhonoPasswd
>>> passwordgen = PhonoPasswd(language="en")
>>> passwordgen.generate_password()
'Zim-Ruck_Saph'
```

## Language support

The generator supports various syllable structures based on language-specific
rules. The currently supported languages are:

 * `en`
 * `fr`
 * `it`
 * `de`

## Contributing

 * Fork it (https://github.com/andr1an/phonopasswd/fork)
 * Create your feature branch (`git checkout -b feature/fooBar`)
 * Commit your changes (`git commit -am 'Add some fooBar'`)
 * Push to the branch (`git push origin feature/fooBar`)
 * Create a new Pull Request

## License

This project is licensed under the GPLv3 license - see [LICENSE](LICENSE) for
details.
