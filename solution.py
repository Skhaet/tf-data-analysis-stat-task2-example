import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    l = x.max()
    r = x.max()/((1-p)**(1/len(x)))
    return l, r
