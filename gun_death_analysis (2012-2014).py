
# coding: utf-8

# ## <font color=dodgerblue>U.S. Gun Deaths Analysis (y. 2012-2014)</font>
# 
# **Abstract**
# <br>
# In this analysis, I am utilizing a dataset from _FiveThirtyEight_ that records gun deaths in the U.S. between the years 2012 and 2014.

# In[1]:


# Using guns.csv

import csv

f = open('guns.csv')
csvreader = csv.reader(f)
data = list(csvreader)

print(data[:5])


# In[2]:


data = data[1:]

print(data[:5])


# In[3]:


# List comprehension for 'year' column

years = [col[1] for col in data]

print(years[:5])


# In[4]:


# Counting instances of each year

year_counts = {}

for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else:
        year_counts[year] += 1
        
print(year_counts)


# In[5]:


# Constructing datetime instance using 'year' and 'month' column

import datetime

dates = [datetime.datetime(year=int(col[1]), month=int(col[2]), day=1) for col in data]

print(dates[:5])


# In[6]:


# Counting date occurrences using dates

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else:
        date_counts[date] += 1
        
print(date_counts)


# In[7]:


# List comp and count for 'sex' column

sexes = [col[5] for col in data]

sex_counts = {}

for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 1
    else:
        sex_counts[sex] += 1
        
print(sex_counts)


# In[8]:


# List comp and count for 'race' column

races = [col[7] for col in data]

race_counts = {}

for race in races:
    if race not in race_counts:
        race_counts[race] = 1
    else:
        race_counts[race] += 1
        
print(race_counts)


# In[9]:


# Using census.csv

j = open('census.csv')
csvreader1 = csv.reader(j)
census = list(csvreader1)

print(census)


# In[10]:


census = census[1:]

print(census)


# In[18]:


# Manual dictionary creation to blend census.csv data

mapping = {
    'Asian/Pacific Islander' : int(census[0][16]),
    'Black' : int(census[0][13]),
    'Native American/Native Alaskan' : int(census[0][14]),
    'Hispanic' : int(census[0][12]),
    'White' : int(census[0][11])
}

print(mapping)


# In[34]:


race_per_hundredk = {}

for race in race_counts:
    val = race_counts[race]
    
    for mapp in mapping:
        rate = round(((val / mapping[mapp]) * 100000), 5)
        race_per_hundredk[race] = rate
        
print(race_per_hundredk)


# In[35]:


intents = [col[3] for col in data]
races = [col[7] for col in data]

homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1

for count in homicide_race_counts:
    val = homicide_race_counts[count]
    
    for mapp in mapping:
        rate = round(((val / mapping[mapp]) * 100000), 5)
        homicide_race_counts[count] = rate
            
print(homicide_race_counts)


# > Computing rates of gun deaths per race/homicide; filtering by intent column
