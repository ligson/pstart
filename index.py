# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys, os

from whoosh.index import create_in
from whoosh.fields import *

from jieba.analyse import ChineseAnalyzer

analyzer = ChineseAnalyzer()

schema = Schema(name=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True))
if not os.path.exists("tmp"):
    os.mkdir("tmp")

ix = create_in("tmp", schema)  # for create new index
# ix = open_dir("tmp") # for read only
writer = ix.writer()


def add_doc(file):
    writer.add_document(name=os.path.basename(file), path=os.path.abspath(file))


def commit():
    writer.commit()
