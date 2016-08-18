# -*- coding:utf-8 -*-

import sys
from sklearn.datasets.base import Bunch
import cPickle as cp
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer


def readbunchobj(path):
    file_obj = open(path, "rb")
    bunch = cp.load(file_obj)
    file_obj.close()
    return bunch


path = "xxxxx"
bunch = readbunchobj(path)


tfidfpace = Bunch(target_name=bunch.name, label=bunch.label,filenames=bunch.filenames, tdm=[], vocabulary={})

vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True,max_df=0.5, transformer=TfidfTransformer())

tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)

