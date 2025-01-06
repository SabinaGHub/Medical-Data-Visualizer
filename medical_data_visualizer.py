import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
# 2
df['overweight']=np.where((df['weight']/((df['height']/100)**2))> 25, 1,0)
# 3
df['cholesterol']=np.where(df['cholesterol']==1, 0 ,1)
df['gluc']=np.where(df['gluc']==1, 0 ,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, value_vars=['cholesterol','gluc','smoke','alco','active','overweight'], id_vars=['cardio'])
    

    # 6
    df_cat = df_cat.groupby(['value', 'variable', 'cardio']).size().reset_index()
    df_cat = df_cat.rename(columns={0:'total'})
    # 7
    myplot=sns.catplot(data=df_cat, kind='bar',x='variable',y='total', hue='value', col='cardio')

    # 8
    fig = myplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])]
    df_heat=df_heat.loc[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))]
    df_heat=df_heat.loc[(df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]


    # 12
    corr = round(df_heat.corr(),1)

    # 13
    mask = np.triu(np.ones(corr.shape[0]),k=0)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt="0.1f" )


    # 16
    fig.savefig('heatmap.png')
    return fig
