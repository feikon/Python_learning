import numpy as np
from icecream import ic

a = np.arange(6)
ic(a)
a2 = a[np.newaxis, :]
a2.shape
ic(a2)
