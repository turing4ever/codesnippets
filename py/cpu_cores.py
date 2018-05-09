# how to count cpu cores
import multiprocessing
print(multiprocessing.cpu_count())

import psutil
print(psutil.cpu_count())
