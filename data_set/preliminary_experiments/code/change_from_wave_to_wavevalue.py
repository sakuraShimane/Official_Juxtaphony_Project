#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy.io.wavfile import read
import numpy as np
rate, data = read('/Users/jin237/Documents/juxtaphony_project/new_iinodemo/Audio/throat_iinodemo_03.wav')

np.savetxt('sample.csv',data,delimiter=',')


# In[ ]:




