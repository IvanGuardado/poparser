import poparser
import pprint

pp = pprint.PrettyPrinter()

pp.pprint(poparser.parse('test.po'))