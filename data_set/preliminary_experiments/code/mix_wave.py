#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf
 
tmfile = '/Users/jin237/Documents/juxtaphony_project/new_iinodemo/Audio/throat_iinodemo_03.wav'
cmfile = '/Users/jin237/Documents/juxtaphony_project/new_iinodemo/Audio/conde_iinodemo_01.wav'
data_tm, samplerate_tm = sf.read(tmfile)
data_cm, samplerate_cm = sf.read(cmfile)
t_tm = np.arange(0, len(data_tm))/samplerate_tm
t_cm = np.arange(0, len(data_cm))/samplerate_cm
plt.title('mix wave')
plt.grid()
plt.margins(x=0,y=0.1)
plt.plot(t_tm, data_tm, alpha=0.6)
plt.plot(t_cm, data_cm, alpha=0.6)
plt.savefig('mix_wave.png')


# In[ ]:




