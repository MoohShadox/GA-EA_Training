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

def launch_oneplusone(center, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    parent = np.array(center)
    i=0
    j=0
    parentFit = ma_func(parent)
    bestFit = parentFit
    bestIt = 0
    print("Parent : ", parent)
    while i<nbeval:

        child = parent + sigma*np.random.normal(0,np.ones(parent.shape),parent.shape)
        childFit = ma_func(child)
        if childFit <= parentFit:
            parentFit = childFit
            parent = np.copy(child)
            if bestFit > parentFit:
                bestFit = parentFit
                bestIt = i
        j+=1
        solutions = np.array([parent])
        if display and ((j<10) or (j%100==0)):
            plot_results(ma_func,solutions, title="Gen %d"%(j))
        i+=1
    print ("Best fit",bestFit,"at iteration",bestIt)
    return bestFit

def launch_ESonefifthRule(center, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    parent = np.array(center)
    i = 0
    j = 0
    parentFit = ma_func(parent)
    bestFit = parentFit
    bestIt = 0
    print("Parent : ", parent)
    while i < nbeval:

        child = parent + sigma * np.random.normal(0, np.ones(parent.shape), parent.shape)
        childFit = ma_func(child)
        if childFit <= parentFit:
            parentFit = childFit
            parent = np.copy(child)
            sigma = sigma*2
            if bestFit > parentFit:
                bestFit = parentFit
                bestIt = i
        else:
            sigma = sigma*(2**(-(1/4)))
        j += 1
        solutions = np.array([parent])
        if display and ((j < 10) or (j % 100 == 0)):
            plot_results(ma_func, solutions, title="Gen %d" % (j))
        i += 1
    print("Best fit", bestFit, "at iteration", bestIt)
    return bestFit

def launch_LambdaES(center, _lambda, sigma, nbeval=10000, display=True, ma_func=myEvalFn.sphere):
    center = np.array(center)
    parent = center + sigma * np.random.normal(0, center.shape, center.shape[0])
    i = 0
    j = 0
    parentFit = ma_func(parent)
    bestFit = parentFit
    bestIt = 0
    print("Parent : ", parent)
    while i < nbeval:

        for k in range(_lambda):

            child = parent + sigma * np.random.normal(0, np.ones(parent.shape), parent.shape)
            childFit = ma_func(child)
            if childFit <= parentFit:
                parentFit = childFit
                parent = np.copy(child)
                sigma = sigma * 2
                if bestFit > parentFit:
                    bestFit = parentFit
                    bestIt = i
            else:
                sigma = sigma * (2 ** (-(1 / 4)))
            j += 1
            solutions = np.array([parent])
            if display and ((j < 10) or (j % 100 == 0)):
                plot_results(ma_func, solutions, title="Gen %d" % (j))
        i += 1
    print("Best fit", bestFit, "at iteration", bestIt)
    return bestFit