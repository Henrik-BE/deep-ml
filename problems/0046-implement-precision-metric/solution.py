import numpy as np
def precision(y_true, y_pred):
    TP = sum(y_true[y_pred==1]==1)
    FP = sum(y_true[y_pred==1]==0)
    if (TP + FP) == 0: return 0
    else: return TP / (TP + FP)
