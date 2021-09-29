#!/usr/bin/env python3
from dev_aberto import hello
from babel.dates import format_datetime
from datetime import datetime
import gettext

gettext.install('hello', localedir='locale')

if __name__ == '__main__':
    date, name = hello()
    date = format_datetime(datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ'))
    print(_('Ultimo commit feito em: '), date, _(' por '), name)