# -*- coding: utf-8 -*-
import enum
import functools

__all__ = ['DownloadableStates', 'integer']


class DownloadableStates(enum.Enum):
    FREE = 1
    PAID = 2

    NOT_FOR_SALE = None


def integer(func):
    @functools.wraps(func)
    def converter(*args, **kwargs):
        arg = func(*args, **kwargs)
        if arg is not None:
            arg = int(arg)

        return arg

    return converter