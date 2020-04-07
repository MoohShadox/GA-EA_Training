import sys
import cma
import cma.purecma as purecma
from deap import benchmarks
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import random
from scipy.optimize import minimize

from plot import *

import benchmarkRobot as pSG

import myEvalFn

##############


def launch_cmaes_full(center, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    res = cma.CMAEvolutionStrategy(center, sigma).optimize(ma_func,maxfun=nbeval).result
    print("res = ",res)
    return res[1]

def launch_cmaes_full_genotype(center, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    res = cma.CMAEvolutionStrategy(center, sigma).optimize(ma_func,maxfun=nbeval).result
    print("res = ",res)
    return res[0]


# do not use restart
def launch_cmaes_pure(center, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    res = purecma.fmin(ma_func,center,sigma,maxfevals=nbeval)
    return res[1].result[1]

