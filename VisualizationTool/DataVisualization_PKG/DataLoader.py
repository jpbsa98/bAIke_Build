#!/usr/bin/env python3
import pandas as pd
import numpy as np
import re

FRAME_DO_GRAFICO_PARADO=1050
FRAME_DO_VIDEO_PARADO=1330
LEITURAS_POR_SEG_SENSORES = 24 
LEITURAS_POR_SEG_CAMERA=24
PERDA=(FRAME_DO_VIDEO_PARADO-FRAME_DO_GRAFICO_PARADO) 
PERDA=0 # to comment
class DataLoader():
    def __init__(self):
        self.loadData()
        self.TreatData()
        #self.Plot_Acceleration()
    def loadData(self):
        headers=['master_acc_x', 'master_acc_y', 'master_acc_z', 'master_gyro_x', 'master_gyro_y', 'master_gyro_z', 'slave_acc_x', 'slave_acc_y', 'slave_acc_z', 'slave_gyro_x', 'slave_gyro_y', 'slave_gyro_z', 'mag_x', 'mag_y', 'mag_z', 'master_temp', 'slave_temp']
        self.df = pd.read_csv('/home/mrflint/Documents/projects/Pei2020_Models/Data/rund_dec_8/extracteData.csv')

    def TreatData(self):
        regularExpression=re.compile("slave*")
        columns_to_remove = list(filter(regularExpression.match,self.df.columns))
        self.df=self.df.drop(columns=columns_to_remove)
        n_cols=self.df.shape[1]

        df_temp= pd.DataFrame(data=np.zeros(shape=(PERDA,n_cols)),columns=self.df.columns)
        pandas_dfs=[df_temp,self.df]

        self.df=pd.concat(pandas_dfs,ignore_index=True)

    def GetLine(self,line):
        return self.df.loc[[line]]
 
