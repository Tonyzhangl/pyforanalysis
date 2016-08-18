# -*- coding:utf-8 -*-
import numpy as np


def LoadDataSet():
    #posting_list 是训练集文本
    #class_vec 是每个文本对应的分类
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him', 'my'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
            ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop','him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    class_vec = [0, 1, 0, 1, 0, 1]

    return posting_list, class_vec


class NBayesClass(object):
    """ 贝叶斯算法类"""

    def __init__(self):
        self.vocabulary = []
        self.idf = 0
        self.tf = 0
        self.tdm = 0
        self.Pcates = {}
        self.labels = []
        self.doclength = 0
        self.vocablen = 0
        self.testset = 0

    def train_set(self, trainset, classvec):
        self.cate_prob(classvec)
        self.doclength = len(trainset)
        tempset = set()
        [tempset.add(word) for doc in trainset for word in doc]
        self.vocabulary = list(tempset)
        self.vocablen = len(self.vocabulary)
        self.calc_wordfreq(trainset)
        self.build_tdm()

    def cate_prob(self, classvec):
        self.labels = classvec
        labeltemps = set(self.labels)
        for labeltemp in labeltemps:
            self.Pcates[labeltemp] =float(self.labels.count(labeltemp)) / float(len(self.labels))

    def calc_wordfreq(self, trainset):
        self.idf = np.zeros([1, self.vocablen])
        self.tf = np.zeros([self.doclength, self.vocablen])
        for index in xrange(self.doclength):
            for word in trainset[index]:
                self.tf[index, self.vocabulary.index(word)] += 1
            for signleword in set(trainset[index]):
                self.idf[0, self.vocabulary.index(signleword)] += 1

    def build_tdm(self):
        self.tdm = np.zeros([len(self.Pcates), self.vocablen])
        sumlist = np.zeros([len(self.Pcates), 1])
        for index in xrange(self.doclength):
            self.tdm[self.labels[index]] += self.tf[index]
            sumlist[self.labels[index]] = np.sum(self.tdm[self.labels[index]])
        self.tdm = self.tdm/sumlist

    def map2vocab(self, testdata):
        self.testset = np.zeros([1, self.vocablen])
        for word in testdata:
            self.testset[0, self.vocabulary.index(word)] += 1

    def predict(self, testset):
        if np.shape(testset)[1] != self.vocablen:
            print "输入错误！！！"
            exit(0)
        predvalue = 0
        predclass = ""
        for tdm_vect, keyclass in zip(self.tdm, self.Pcates):
            temp = np.sum(testset*tdm_vect*self.Pcates[keyclass])
            if temp > predvalue:
                predvalue = temp
                predclass = keyclass
        return predclass

#    test

dataSet,listClasses = LoadDataSet()
nb =NBayesClass()
nb.train_set(dataSet, listClasses)
nb.map2vocab(dataSet[0])
print ">>>>>> 输出分类结果 >>>>>"
print nb.predict(nb.testset)
