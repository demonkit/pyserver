# -*- coding: utf-8 -*-


class Parser(object):
    """
    Parsers are used to parse the HTTP request headers.
    The base parser class of all parsers. All parser must impletement its
    method of parse, and this method must return value of type dictionary.
    """

    def __init__(self, *args, **kwargs):
        pass

    def parse(self):
        raise NotImplemetedError


class EasyParser(Parser):
    """
    An easy parser just using string parsing."""

    def __init__(self, headers):
        self.headers = headers

    def parse(self):
        header = self.headers.split("\n")
        header_dict = dict([
            item.split(":") for item in header if item.strip()
        ])
        return header_dict


if __name__ == '__main__':
    header = """
    Host: www.joes-hardware.com
    If-Modified-Since: Mar 4th, 2012
    """
    ep = EasyParser(header)
    print ep.parse()
