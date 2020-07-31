# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path,sep=',', delimiter=None, header='infer',names=None, index_col=None, usecols=None)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
print(data.head(10))
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
better_event = data['Better_Event'].value_counts().index[0]
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]
column = ''
df=[]
def top_ten(df,column):
    top_10=df.nlargest(10,column)
    return top_10
top_10_summer = list(top_ten(top_countries,'Total_Summer') ['Country_Name'])   
top_10_winter = list(top_ten(top_countries,'Total_Winter') ['Country_Name'])
top_10 = list(top_ten(top_countries,'Total_Medals') ['Country_Name'])
common = list(set(top_10_summer) & (set(top_10_winter) & set(top_10)))
print(common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
f,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(15,7))
summer_df[['Country_Name','Total_Summer']].plot.bar(ax=ax1)
ax1.set_xticklabels(list(summer_df['Country_Name']),fontsize=8)
#plt.xticks(df['Country_Name'])


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
[[summer_country_gold, summer_max_ratio]] = summer_df[['Country_Name','Golden_Ratio']][summer_df.Golden_Ratio==summer_df.Golden_Ratio.max()].values
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
[[winter_country_gold,winter_max_ratio]] = winter_df[['Country_Name','Golden_Ratio']][winter_df.Golden_Ratio==winter_df.Golden_Ratio.max()].values
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
[[top_country_gold, top_max_ratio]] = top_df[['Country_Name','Golden_Ratio']][top_df.Golden_Ratio==top_df.Golden_Ratio.max()].values


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
[[best_country,most_points]] = data_1[['Country_Name','Total_Points']][data_1.Total_Points==data_1.Total_Points.max()].values
print(best_country,most_points)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45,label = 'United States')


