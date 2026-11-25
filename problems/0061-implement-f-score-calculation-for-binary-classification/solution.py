import numpy as np

def recall(y_true, y_pred):
    TP = sum(y_true[y_pred==1]==1)
    FN = sum(y_true[y_pred==0]==1)
    if (TP + FN) == 0: return 0
    else: return TP / (TP + FN)

def press(y_true, y_pred):
    TP = sum(y_true[y_pred==1]==1)
    FP = sum(y_true[y_pred==1]==0)
    if (TP + FP) == 0: return 0
    else: return TP / (TP + FP)

def f_score(y_true, y_pred, beta):
    r = recall(y_true, y_pred)
    p = press(y_true, y_pred)

    d = (beta**2 * p + r)
    if d == 0: return 0
    else: return ((1 + beta**2) * p * r) / d
