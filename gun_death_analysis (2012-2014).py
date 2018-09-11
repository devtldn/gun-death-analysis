
# coding: utf-8

# ## <font color=dodgerblue>U.S. Gun Deaths Analysis (y. 2012-2014)</font>
# 
# **Abstract**
# <br>
# In this analysis, I am utilizing a dataset from _FiveThirtyEight_ that records gun deaths in the U.S. between the years 2012 and 2014.

# In[1]:


import csv

f = open('guns.csv')
csvreader = csv.reader(f)
data = list(csvreader)
print(data[:5])


# In[2]:


data = data[1:]
print(data[:5])


# In[3]:


years = [col[1] for col in data]
print(years[:5])


# In[4]:


year_counts = {}

for year in years:
    if year not in year_counts:
        year_counts[year] = 1
    else:
        year_counts[year] += 1
        
print(year_counts)


# In[5]:


import datetime

dates = [datetime.datetime(year=int(col[1]), month=int(col[2]), day=1) for col in data]

print(dates[:5])


# In[6]:


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    else:
        date_counts[date] += 1
        
print(date_counts)


# In[7]:


sexes = [col[5] for col in data]
sex_counts = {}

for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 1
    else:
        sex_counts[sex] += 1
        
print(sex_counts)


# In[8]:


races = [col[7] for col in data]
race_counts = {}

for race in races:
    if race not in race_counts:
        race_counts[race] = 1
    else:
        race_counts[race] += 1
        
print(race_counts)


# In[9]:


j = open('census.csv')
csvreader1 = csv.reader(j)
census = list(csvreader1)
census = census[1:]
print(census)


# In[10]:


mapping = {
    'Asian/Pacific Islander' : int(census[0][16]),
    'Black' : int(census[0][13]),
    'Native American/Native Alaskan' : int(census[0][14]),
    'Hispanic' : int(census[0][12]),
    'White' : int(census[0][11])
}

print(mapping)


# In[11]:


race_per_hundredk = {}

for race in race_counts:
    val = race_counts[race]
    
    for mapp in mapping:
        rate = round(((val / mapping[mapp]) * 100000), 5)
        race_per_hundredk[race] = rate
        
print(race_per_hundredk)


# In[12]:


months = [col[2] for col in data]
intents = [col[3] for col in data]
genders = [col[5] for col in data]
races = [col[7] for col in data]

homicide_race_counts = {}
homicide_race_rates = {}

homicide_month_counts = {}
homicide_month_rates = {}

homicide_gender_counts = {}
homicide_gender_rates = {}

accidental_gender_counts = {}
accidental_gender_rates = {}

accidental_race_counts = {}
accidental_race_rates = {}

suicide_gender_counts = {}
suicide_gender_rates = {}

suicide_race_counts = {}
suicide_race_rates = {}


def count_rate(g_dict, i_list, intent, counts_dict, rates_dict, m_dict):
    for i, gender in enumerate(g_dict):
        if i_list[i] == intent:
            if gender not in counts_dict:
                counts_dict[gender] = 1
            else:
                counts_dict[gender] += 1
                
    for gender, count in counts_dict.items():
        for eth in m_dict:
            rate = round(((count / m_dict[eth]) * 100000), 5)
            rates_dict[gender] = rate
    
    return counts_dict, rates_dict

hr = count_rate(races, intents, 'Homicide', homicide_race_counts, homicide_race_rates, mapping)
hm = count_rate(months, intents, 'Homicide', homicide_month_counts, homicide_month_rates, mapping)
hg = count_rate(genders, intents, 'Homicide', homicide_gender_counts, homicide_gender_rates, mapping)
ag = count_rate(genders, intents, 'Accidental', accidental_gender_counts, accidental_gender_rates, mapping)
ar = count_rate(races, intents, 'Accidental', accidental_race_counts, accidental_race_rates, mapping)
sg = count_rate(genders, intents, 'Suicide', suicide_gender_counts, suicide_gender_rates, mapping)
sr = count_rate(races, intents, 'Suicide', suicide_race_counts, suicide_race_rates, mapping)


# In[13]:


hr


# In[14]:


hm


# In[15]:


hg


# In[16]:


ag


# In[17]:


ar


# In[18]:


sg


# In[19]:


sr


# In[22]:


locations = [col[9] for col in data]
education = [col[10] for col in data]

counts_by_location = {}
rates_by_location = {}

counts_by_education = {}
rates_by_education = {}

def morecountrate(input_list, counts_dict, mapping_dict, rates_dict):
    for value in input_list:
        if value not in counts_dict:
            counts_dict[value] = 1
        else:
            counts_dict[value] += 1
            
    for place, count in counts_dict.items():
        for eth in mapping_dict:
            rate = round(((count / mapping_dict[eth]) * 100000), 5)
            rates_dict[place] = rate
        
    return counts_dict, rates_dict

cbl = morecountrate(locations, counts_by_location, mapping, rates_by_location)
cbe = morecountrate(education, counts_by_education, mapping, rates_by_education)


# In[23]:


cbl


# In[24]:


cbe

