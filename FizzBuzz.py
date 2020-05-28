import pandas as pd
import numpy as np


# 3の倍数はFizz, 5の倍数はBuzz, 15の倍数はFizz Buzz と出力する
for x in range(1, 21):
    if x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        pass
