#!/usr/bin/env python
# coding: utf-8

# # Task1: Restaurant Reviews

# ## Analyze the text reviews to identify the most common positive and negative keywords

# In[121]:


import pandas as pd


# In[122]:


df = pd.read_csv("Dataset.csv")
df.head()


# In[123]:


rat_counts = df["Rating text"].value_counts()
rat_counts


# In[124]:


new_df = pd.DataFrame({'Rating Text':rat_counts.index,'Counts':rat_counts.values})
new_df.head()


# In[164]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x=new_df["Rating Text"],y=new_df["Counts"],data=new_df)
plt.title("Positive Vs Negative Rating")
plt.show()


#  ## Calculate the average length of reviews and explore if there is a relationship between review length and rating

# In[126]:


df["length"] = df["Rating text"].apply(len).values
df.head(2)


# In[127]:


rating = df["Aggregate rating"].values
rating


# In[128]:


sns.barplot(y=df.length,x=rating)
plt.xlabel("Ratings")
plt.ylabel("Length of Review")
plt.title("Relationship b/w Review length and Rating")
plt.xticks(rotation=90,ha='right')
plt.show()


# In[129]:


corr = df["length"].corr(df["Aggregate rating"])
corr


# In[130]:


#Correlation is negative which means there is an inverse relationship between Review length and ratings


# # Task2: Votes Analysis

#  ## Identify the restaurants with the highest and lowest number of votes

# In[131]:


df.head(2)


# In[132]:


highest = df[df["Votes"]==df["Votes"].max()]
highest  #Restaurant with highest number of Votes is "Toit" in "Bangalore" with Total votes=10934


# In[133]:


lowest = df[df["Votes"]==df["Votes"].min()]
lowest.shape  #Total No. of Restaurants with lowest votes are 1094


# In[134]:


#Top 5 Restaurants with lowest votes
lowest.head(5)


# ## Analyze if there is a correlation between the number of votes and the rating of a restaurant

# In[135]:


corr1 = df["Votes"].corr(df["Aggregate rating"])
corr1


# In[136]:


import plotly.express as px


# In[137]:


fig = px.violin(df,x=df["Aggregate rating"],y=df["Votes"],title="Relation of Votes and Ratings")
fig.update_layout(xaxis_title="Rating",yaxis_title="Votes")
fig.show()


# # Task3: Price Range vs. Online Delivery and Table Booking

# ## Analyze if there is a relationship between the price range and the availability of online delivery and table booking

# In[138]:


df.head(2)


# In[139]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


# In[140]:


df["Has Online delivery"]=le.fit_transform(df["Has Online delivery"])
df["Has Table booking"]=le.fit_transform(df["Has Table booking"])


# In[141]:


df.head(2)


# In[142]:


corr3 = df["Price range"].corr(df["Has Online delivery"])
corr3


# In[143]:


fig2 = px.histogram(df,x=df["Price range"],y=df["Has Online delivery"],color=df["Price range"])
fig2.update_layout(xaxis_title="Price Range",yaxis_title="Restaurant Having Online Delivery")
fig2.show()


# In[149]:


corr4 = df["Price range"].corr(df["Has Table booking"])
corr4


# In[151]:


fig3 = px.histogram(df,x=df["Price range"],y=df["Has Table booking"],color=df["Price range"])
fig3.update_layout(xaxis_title="Price Range",yaxis_title="Restaurant Having Table bookings ")
fig3.show()


# ## Determine if higher-priced restaurants are more likely to offer these services

# In[ ]:


df.head(2)


# In[ ]:


new_df2 = df[df["Price range"]>3]
new_df2.head(2)


# In[152]:


values = new_df2["Has Table booking"].value_counts()
values


# In[153]:


percent = (values/len(new_df2))*100
percent


# In[154]:


online = new_df2["Has Online delivery"].value_counts()
online


# In[155]:


online_per = online/len(new_df2)*100
online_per


# In[156]:


total_sales_per = percent+online_per
total_sales_per


# In[157]:


fig3 = px.pie(values=total_sales_per.values,names=['No sales','Sales'],color_discrete_sequence=['#ff0000','#40ff00'])
fig3.show()


# In[ ]:





# In[ ]:




