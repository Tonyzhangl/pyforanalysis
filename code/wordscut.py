# -*- coding:utf-8 -*-
import sys
import jieba


msg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=False)
print ">>1 >>>"
print ' '.join(msg_list)


msg_list = jieba.cut("小明1995年毕业于北京清华大学")
print ">>2 >>"
print ' '.join(msg_list)


msg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=True)
print ">>3 >>"
print ' '.join(msg_list)
