#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd


# In[136]:


data1=pd.read_csv(r"C:\Users\yuges\Downloads\deliveries.csv")


# In[137]:


data2=pd.read_csv(r"C:\Users\yuges\Downloads\matches.csv")


# #### Which of the following is the right way to merge 2 datasets for getting better insights from the data

# In[138]:


data=pd.concat([data1,data2],axis=1)


# In[139]:


data


# In[140]:


data2


# #### Column with most missing values

# In[141]:


data1.isna().sum()


# In[142]:


data2.isna().sum()


# #### City which hosted most number of seasons

# In[143]:


array=data2["city"].unique()


# In[144]:


len(array)


# In[145]:


data2


# In[146]:


d={}
for i in array:
    key=i
    value=len(data2[data2["city"]==i]["season"])
    d[key]=value


# In[147]:


for i,j in zip(d.keys(),d.values()):
    print(f"{i}->{j}")


# #### Which year has the most number of matches played

# In[148]:


data2


# In[149]:


data2["season"].value_counts()


# #### Maximum wins by Mumbai Indians in 2011 are

# In[150]:


data2


# In[151]:


len(data2[(data2["winner"]=="Mumbai Indians") & (data2["season"]==2011)]["winner"])


# #### For toss_decision Feature what kind of plot is suitable

# In[152]:


data2.dtypes


# #### Because toss_decision feature is a categorical datatype i.e. discrete. We can use barplot, piechart

# In[153]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[154]:


plt.figure(figsize=(5,5))
data2["toss_decision"].value_counts().plot.bar(color=["red","blue"],width=0.3)
plt.show()


# In[155]:


data2["toss_decision"].value_counts().plot.pie(autopct="%.2f")
plt.show()


# #### What is the percentage of getting bat and field in feature toss_decision 

# In[156]:


data2


# In[157]:


data2["toss_decision"].value_counts().plot.pie(autopct="%.2f")
plt.show()


# #### Which Statement holds true

# In[158]:


data2


# In[159]:


sum(data2[(data2["toss_decision"]=="field") & (data2["toss_winner"]==data2["winner"])]["winner"].value_counts())


# In[160]:


sum(data2[(data2["toss_winner"]==data2["winner"]) & (data2["toss_decision"]=="bat")]["winner"].value_counts())


# ####  In which years where taking batting second have won more number of matches

# In[161]:


data2


# In[167]:


m=data2[(data2["toss_decision"]=="field") & (data2["toss_winner"]==data2["winner"])]


# In[170]:


m.pivot_table(index="season",values="winner",aggfunc="count")


# #### To plot the most consistent batsmen among top 10 run getters what plotting technique we use

# In[29]:


data1


# #### As batsman is categorical i.e. discrete and batsman_runs is continuous we can use barplot,countplot.

# #### 11) In 2019 which batsman scored highest number of runs by hitting 6's and 4's

# In[30]:


data1


# In[174]:


n=data[(data["season"]==2019) & ((data["batsman_runs"]==6) | (data["batsman_runs"]==4))]


# In[177]:


n.pivot_table(index="batsman",values="batsman_runs",aggfunc="sum")


# #### 12) Most number of wickets taken by the bowler is

# In[185]:


data1


# In[196]:


k=data[data["dismissal_kind"].isin(["caught","bowled","caught and bowled","hit wicket","lbw","obstructing the field","retired hurt","run out","stumped"])]


# In[199]:


o=k.pivot_table(index="bowler",values="dismissal_kind",aggfunc="count")


# In[204]:


o.sort_values("dismissal_kind",ascending=False)


# In[201]:


o


# #### 13) What is the strike rate of Kohli in 2016

# In[181]:


r=data[(data["season"]==2016)&(data["batsman"]=="V Kohli")]


# In[182]:


r


# #### Bowlers with maximum number of extras

# In[35]:


data["extra_runs"].max()


# In[36]:


data[data["extra_runs"]==7][["extra_runs","bowler"]]


# ### Which venue has hosted most number of IPL matches

# In[37]:


data["venue"].value_counts()


# #### In 2017 when sunrisers hyderabad clashed against Royal Challengers Bangalore which team player won player of the match?

# In[44]:


data[(data["season"]==2017.0) & (data["winner"]=="Sunrisers Hyderabad")]["player_of_match"]


# #### 17) Across seasons who are the top three batsman's with most number of run out?

# In[56]:


data2


# #### What are the total runs scored by V Kohli when the bowler was JJ Burmah?

# In[67]:


data1[(data1["batsman"]=="V Kohli") & (data1["bowler"]=="JJ Bumrah")]["total_runs"].sum()


# #### Across all seasons which player was dismissed the maximum number of times via caught and bowled

# In[130]:


Max=data1[["player_dismissed","dismissal_kind"]]


# In[131]:


a=Max[(Max["dismissal_kind"]=="caught and bowled")].groupby(by=["player_dismissed"])["player_dismissed"].count()


# In[132]:


a


# In[133]:


b=a.sort_values(ascending=False)


# In[134]:


b


# #### 20) which player has the highest hard-hitting ability?
# 

# In[ ]:




