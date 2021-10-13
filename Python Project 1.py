#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Physical Wellness - reflecting your fitness and healthy habits (FRUITS_VEGGIES, SLEEP_HOURS, DAILY_STEPS)
# Social Connection - assessing the strength of your social network (CORE_CIRCLE, SOCIAL_NETWORK)
# Meaning - evaluating your compassion and generosity (DONATION, SUPPORTING_OTHERS)
# Productivity - reflecting your attitude for continued improvement (FLOW, TODO_COMPLETED)
# Achievement - assesing how ambitious, goal-focused, self-disciplined you are (ACHIEVEMENT, PERSONAL_AWARDS, LIVE_VISION) 


# In[ ]:


##Limitations: 
#self reported 
#the sample may not be a good representation of the population (online survey, very little information about the participants)


# In[2]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy.stats as stats
from scipy.stats import bartlett


# In[3]:


data = pd.read_csv('Wellbeing_and_lifestyle_data_Kaggle.csv')


# In[5]:


data.head(5)


# In[6]:


print(data.columns)


# In[33]:


data.describe()


# In[8]:


data['AGE']=data['AGE'].replace('Less than 20', '20 or less')
data_flow = data.pivot_table(values='FLOW', index=['AGE'], columns=['GENDER'])
data_flow.head()


# In[9]:


data['DAILY_STRESS']=pd.to_numeric(data['DAILY_STRESS'],errors = 'coerce')
data_stress = data.pivot_table(values='DAILY_STRESS', index=['AGE'], columns=['GENDER'], )
data_stress.head()


# In[36]:


sns.kdeplot(data['FLOW'], shade = True, label = 'Hours of Flow')


# In[11]:


#pd.cut(df['age'], bins=5).value_counts(sort=False)

#labels = ['Generation Z','Millennials', 'Generation X', 'Baby Boomers', 'The Silent Generation']

#create a new column for the age group
#df['age_group'] = pd.cut(df['age'], bins=5, labels=labels)

#df


# In[4]:


data['Productivity'] = data['TODO_COMPLETED'] + data['FLOW']
data['Social Connection'] = data['CORE_CIRCLE'] + data['SOCIAL_NETWORK']
data['Meaning'] = data['SUPPORTING_OTHERS'] + data['DONATION']*2


# In[5]:


pd.cut(data['Social Connection'], bins=3).value_counts(sort=False)
labels = ['Strong', 'Ordinary', 'Weak']
data['Level of Social Connection'] = pd.cut(data['Social Connection'], bins=3).value_counts(sort=False)
data['Level of Social Connection'].head(10)


# In[6]:


pd.cut(data['Meaning'], bins=3).value_counts(sort=False)
labels = ['Strong', 'Ordinary', 'Weak']
data['Level of Meaning'] = pd.cut(data['Meaning'], bins=3).value_counts(sort=False)
data['Level of Meaning'].head(10)


# In[7]:


data.head()


# In[15]:


sns.boxplot(x = 'GENDER', y = 'Productivity', data = data)


# In[16]:


sns.boxplot(x = 'Level of Social Connection', y = 'Productivity', data = data)


# In[17]:


sns.boxplot(x = 'Level of Social Connection', y = 'Productivity', data = data)


# In[18]:


sns.boxplot(x = 'Level of Meaning', y = 'Productivity', data = data)


# In[19]:


sns.boxplot(x = 'Level of Social Connection', y = 'FLOW', data = data)


# In[ ]:


##here I check the correlation between productivity and Social Connection 


# In[24]:


# The stats.pearsonr() returns 2 values the correlation coefficient and the p-value
r, p_value = stats.pearsonr(data['Productivity'], data['Social Connection'])
print(f"Correlation coefficient of Productivity and Social Connection = {r}")
print(f"The p value is {p_value}")


# In[25]:


r, p_value = stats.pearsonr(data['Productivity'], data['CORE_CIRCLE'])
print(f"Correlation coefficient of Productivity and CORE_CIRCLE = {r}")
print(f"The p value is {p_value}")


# In[26]:


r, p_value = stats.pearsonr(data['Productivity'], data['SOCIAL_NETWORK'])
print(f"Correlation coefficient of Productivity and SOCIAL_NETWORK = {r}")
print(f"The p value is {p_value}")


# In[ ]:


##here I check the correlation between productivity and ACHIEVEMENT


# In[35]:


r, p_value = stats.pearsonr(data['Productivity'], data['ACHIEVEMENT'])
print(f"Correlation coefficient of Productivity and ACHIEVEMENT = {r}")
print(f"The p value is {p_value}")


# In[ ]:




