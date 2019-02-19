
import numpy as np


class Score():

    def __init__(self, trues, preds, reverse=False):
        trues = np.array(trues)*1
        preds = np.array(preds)*1
        if reverse:
            trues = 1-np.array(trues)
            preds = 1-np.array(preds)
        p1 = np.where(preds == 1)[0]
        t1 = np.where(trues == 1)[0]
        tp = np.intersect1d(p1, t1)
        self._p1 = p1
        self._t1 = t1
        self._tp = tp


    def calc_f1(self):
        p = self.calc_precision()
        r = self.calc_recall()
        score = 2/(1/p+1/r)
        return score


    def calc_precision(self):
        p1 = self._p1
        tp = self._tp
        score = len(tp)/len(p1)
        return score


    def calc_recall(self):
        t1 = self._t1
        tp = self._tp
        score = len(tp)/len(t1)
        return score
