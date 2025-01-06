# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()
'''
df = pd.read_csv('medical_examination.csv')
df['overweight']=np.where((df['weight']/((df['height']/100)**2))> 25, 1,0)
df['cholesterol']=np.where(df['cholesterol']==1, 0 ,1)
df['gluc']=np.where(df['gluc']==1, 0 ,1)

df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])]

df_heat=df_heat.loc[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]

df_heat=df_heat.loc[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

corr = df_heat.corr()

mask = np.triu(np.ones(corr.shape[0]),k=0)
sns.heatmap(corr, annot=True, mask=mask, fmt="0.1f" )
plt.show()

'''


# Run unit tests automatically
main(module='test_module', exit=False)