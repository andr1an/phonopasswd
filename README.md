phonopasswd
===========

[![Build Status](https://travis-ci.org/andr1an/phonopasswd.svg?branch=master)](https://travis-ci.org/andr1an/phonopasswd)

Phonetic passwords generator written in Python.

Generated passwords are quite secure and easy to remember:

    Pock-Heth_Ris
    SeamBuy1Jok
    Koy0Wred_Tash

*WARNING! Do NOT use any of the passwords above for securing your accounts,
services etc!*

## Installation

The simplest way is to use `pip`:

    pip install git+https://github.com/andr1an/phonopasswd.git

Command `phonopasswd` is now available on the command line. Also you could use
the generator in your Python projects:

```python
>>> from phonopasswd import generate_password
>>> generate_password()
'Zim-Ruck_Saph'
```

## Contributing

 * Fork it (https://github.com/andr1an/phonopasswd/fork)
 * Create your feature branch (`git checkout -b feature/fooBar`)
 * Commit your changes (`git commit -am 'Add some fooBar'`)
 * Push to the branch (`git push origin feature/fooBar`)
 * Create a new Pull Request

## License

This project is licensed under the GPLv3 license - see [LICENSE](LICENSE) for
details.
