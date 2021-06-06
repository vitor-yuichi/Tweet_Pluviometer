#!/usr/bin/env python
# coding: utf-8

# In[5]:


from scipy.stats import t 
import numpy as np
import scipy


def teste_hipotese(x,y,alfa=0.05):
    
    
    '''T-test hypothesis testing for regression. Returns 1 if null Hypthotesis can be rejected (considering the chosen alfa )
    and 0 if it can't.
    
    Parameters:
    -------------------------------------------
    x and y: Variables 
    alfa: Desired statistical significance.'''
    
    n = len(x)
    xmed = np.sum(x)/n;
    ymed = np.sum(y)/n;
    i = 0
    ttable = 1.960
    reject=0       
    reject0=0     
    Sxy = 0
    Sxx = 0 
    Syy = 0
    for i in range(n):
        Sxy = Sxy + ((x[i]-xmed)*(y[i]-ymed))
        Sxx = Sxx + np.power(x[i]-xmed, 2)

    b1 = Sxy/Sxx
    b0 = ymed-b1*xmed

    for i in range(n):
        Syy = Syy + np.power(y[i]-ymed, 2)

    R2 = np.power(Sxy,2)/(Sxx*Syy)
    R2a = 1 - ((n-1)/(n-2))*(1-R2)
    QME = (Syy-(b1*Sxy))/(n-2)
    bla = (1.0/n) + (xmed*xmed)/(Sxx)
    t0 = b0 / np.sqrt(QME*bla)
    t = b1 / np.sqrt(QME/Sxx)
    
        
    pvalue = 2*(1 - scipy.stats.t.cdf(np.abs(t),df=n-2))
    if np.abs(pvalue)<=alfa:
        reject=1
    else:
        reject=0
    
    return reject,pvalue


# In[ ]:




