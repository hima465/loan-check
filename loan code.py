#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('train.csv')
df.head()


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.isnull().sum()


# In[6]:


df['CreditScore'] = df['CreditScore'].fillna(df['CreditScore'].median())


# In[7]:


df.dropna(inplace=True)


# In[8]:


df.isnull().sum()


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns

# Check if the DataFrame is empty
if df.empty:
    print("The DataFrame is empty.")
else:
    # Check the shape of the DataFrame
    print("DataFrame shape:", df.shape)

    # Check for missing values in relevant columns
    print("Missing values in columns:")
    print(df[['MaritalStatus', 'Default', 'Education', 'EmploymentType', 'HasDependents', 'LoanPurpose']].isnull().sum())

    # Drop rows with missing values in relevant columns if needed
    df = df.dropna(subset=['MaritalStatus', 'Default', 'Education', 'EmploymentType', 'HasDependents', 'LoanPurpose'])

    # Set figure size and font scale for better readability
    plt.figure(figsize=(20, 10))
    sns.set(font_scale=2)

    # Plot 1: Marital Status vs Loan Default
    plt.subplot(231)
    sns.countplot(x='MaritalStatus', hue='Default', data=df, palette='pastel')
    plt.title('Marital Status vs Loan Default')

    # Plot 2: Education vs Loan Default
    plt.subplot(232)
    sns.countplot(x='Education', hue='Default', data=df, palette='pastel')
    plt.title('Education vs Loan Default')

    # Plot 3: Employment Type vs Loan Default
    plt.subplot(233)
    sns.countplot(x='EmploymentType', hue='Default', data=df, palette='pastel')
    plt.title('Employment Type vs Loan Default')

    # Plot 4: Has Dependents vs Loan Default
    plt.subplot(234)
    sns.countplot(x='HasDependents', hue='Default', data=df, palette='pastel')
    plt.title('Has Dependents vs Loan Default')

    # Plot 5: Loan Purpose vs Loan Default
    plt.subplot(235)
    sns.countplot(x='LoanPurpose', hue='Default', data=df, palette='pastel')
    plt.title('Loan Purpose vs Loan Default')

    # Adjust the layout to prevent overlap
    plt.tight_layout()
    plt.show()


# In[10]:


df['Default'].value_counts()


# In[11]:


df['MaritalStatus'] = df['MaritalStatus'].map({'Married': 1, 'Single': 0})
df['MaritalStatus'].value_counts()


# In[12]:


df['MaritalStatus'] = df['MaritalStatus'].map({'Married': 1, 'Single': 0})
df['MaritalStatus'].value_counts()


# In[13]:


df['HasDependents'] = df['HasDependents'].map({'0': 0, '1': 1, '2': 2, '3+': 3})
df['HasDependents'].value_counts()


# In[14]:


df['Default'].replace('Y', 1, inplace=True)
df['Default'].replace('N', 0, inplace=True)


# In[15]:


df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())


# In[16]:


df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Education'].value_counts()


# In[17]:


df['EmploymentType'] = df['EmploymentType'].map({'Yes': 1, 'No': 0})
df['EmploymentType'].value_counts()


# In[18]:


df['LoanPurpose'] = df['LoanPurpose'].map({'Home': 0, 'Car': 1, 'Education': 2, 'Personal': 3})
df['LoanPurpose'].value_counts()


# In[19]:


df['LoanAmount'].value_counts()


# In[20]:


df.shape


# In[21]:


df['LoanTerm'].value_counts()


# In[22]:


df['CreditScore'].value_counts()


# In[ ]:




