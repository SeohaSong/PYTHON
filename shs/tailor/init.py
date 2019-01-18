
import numpy as np


def calc_f1_score(trues, preds):
    trues = np.array(trues)*1
    preds = np.array(preds)*1
    p1, = np.where(preds == 1)
    t1, = np.where(trues == 1)
    tp = np.intersect1d(p1, t1)
    p = len(tp)/len(p1)
    r = len(tp)/len(t1)
    score = (2*p*r)/(p+r)
    return score
