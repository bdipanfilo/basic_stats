#!/usr/bin/env python
# coding: utf-8

# In[4]:


def Basic_stats(x):
    

    import matplotlib.pyplot as plt
    
    L=0
    for Number in x:
        L=L+1
    
    S=0
    for Number in x:
        S=Number+S

    Mean=S/L

    V=0
    for Number in x:
        V=(Number-Mean)**2+V
        SD=(V/L)**(1/2)
    
    print('Mean is', Mean)
    print('Standard Deviation is', SD)
    plt.hist(x,5)
    plt.show()
    
    return




