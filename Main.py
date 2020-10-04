import random
from collections import Counter
import matplotlib.pyplot as plt

PROB_ARR = []
DAYS_ARR = []
MAIN_CNT = 0

def NLLFunc():
   print("Hello")

def NLLFunc():
   print("Hello") 

def NLLFunc():
   print("Hello")
   
def RDG():
    DAYS_ARR.append(random.randrange(1, 365))


def ARPRO(DAYS_ARR):
    DAYS_ARR.sort()
    DAYS_ARR = Counter(DAYS_ARR)
    DAYS_ARR = DAYS_ARR.most_common(1)
    return DAYS_ARR[0]

def RUNNER():
    for x in range(100):
        RDG()
    L = ARPRO(DAYS_ARR)
    print(L[1])

RUNNER()
