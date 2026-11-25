import numpy as np

def recall(y_true, y_pred):
    TP = sum(y_true[y_pred==1]==1)
    FN = sum(y_true[y_pred==0]==1)
    if (TP + FN) == 0: return 0
    else: return TP / (TP + FN)
