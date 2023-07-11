# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:37:07 2023

@author: jkf
"""

import numpy as np

from tqdm import tqdm

from func_by_jkf import *
import os
D=disk(1024,1024,500)

gain=0.99
savepath='/data1/huzy/xeuvi/xeuvi_out/4.15/fits{}/'.format(gain)#保存路径
mkdir(savepath)
filelist='/data1/huzy/xeuvi/xeuvi_out/4.15/fits/'#文件所在路径
filelist=sorted(glob.glob(filelist+'/*fits'))
IM=[]
HD = []
NAME = []
for file in tqdm(filelist):
    im,h=fitsread(file)
    IM.append(im)
    HD.append(h)
    NAME.append(os.path.basename(file))
plt.close('all')    
IM=np.array(IM).squeeze()
Dr=disk(1024,1024,500)^disk(1024,1024,420)

tot=IM.shape[0]

im=IM.copy()
 

T=0.05

ssa=[]
for i in tqdm(range(1,tot)): 

    tmp=IM[i].copy()    
    IM[i]=IM[i-1]*gain+(1-gain)*IM[i]
    s=im[i]/IM[i]
    s=removenan(s)

    ss=s[D].std() 
    ssa.append(ss)
    print(ss)
    if ss>T:

       im[i]=IM[i]
        
    fitswrite(savepath+'/'+NAME[i],im[i].astype('float32'),header=HD[i])
# #####################################################
