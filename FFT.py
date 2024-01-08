"""
Copyright (C) 2024
@ Name: FFT.py
@ Time: 2024/1/4 10:36
@ Author: YuAn_L
@ Eamil: yuan_l1106@163.com
@ Software: PyCharm
"""

import numpy as np
import pandas as pd
import torch
import torch.fft
import seaborn as sns
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import kpss,acf
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import spearmanr,pearsonr

print(torch.__version__)
d = pd.read_csv('C:\Study\Code\数据集\PP_GAS\gt_2011.csv',header=0)

data = d.values
name = d.columns


xf = torch.fft.rfft(torch.tensor(data,dtype=torch.float32),dim=0)
freq = torch.fft.fftfreq(data.shape[0])
freq_list = abs(xf).mean(0)
freq_list[0] = 0
print(freq_list)
_, top_list = torch.topk(freq_list,k=3)
period = data.shape[0]//top_list
print(period)
print(data.shape[0]//period[0])

if data.shape[0] % int(period[0]) != 0:
    length = (data.shape[0] // period[0] + 1)  * period[0]
    padding = torch.zeros(size=[length-data.shape[0],data.shape[1]])
    data = torch.cat([torch.tensor(data,dtype=torch.float32),padding],dim=0)

x = data.reshape(int(data.shape[0]//period[0]),int(period[0]),data.shape[-1])

fig, axs = plt.subplots(3,4,layout='constrained')

for i in range(data.shape[1]):

    ax = axs.flat[i]
    fft_result = torch.fft.fft(torch.tensor(data[:,i]),dim=-1)
    fft_freq = torch.fft.fftfreq(data.shape[0],1)
    positive_freqs = fft_freq > 0
    temp = torch.abs(fft_result[positive_freqs])
    ax.plot(fft_freq[positive_freqs], torch.abs(fft_result[positive_freqs]),label=name[i])  # 使用绝对值表示幅度
    ax.set_title('FFT of Signal')
    ax.set_xlabel('Frequency [Hz]')
    ax.set_ylabel('Amplitude')
    ax.grid()
    ax.legend()
if data.shape[1] % 2 != 0:
    plt.delaxes(axs[-1, -1])


plt.show()
print(1)