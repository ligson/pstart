# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys, os

sys.path.append("../")
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()

ix = open_dir("tmp")

searcher = ix.searcher()
parser = QueryParser("name", schema=ix.schema)
q = parser.parse(u"name")
results = searcher.search(q)
print(results)
for hit in results:
    print("----------------")
    print(hit.highlights("name"))
    print(hit["path"])
