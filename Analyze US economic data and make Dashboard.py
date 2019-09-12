#!/usr/bin/env python
# coding: utf-8

# <a><img src="https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width="200" align="center"></a>

# <h1>Analyzing US Economic Data and  Building a Dashboard  </h1>
# <h2>Description</h2>
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, one can extract some essential economic indicators from some data, you will then display these economic indicators in a Dashboard.
# <p>
# <a href="https://en.wikipedia.org/wiki/Gross_domestic_product"> Gross domestic product (GDP)</a> is a measure of the market value of all the final goods and services produced in a period. GDP is an indicator of how well the economy is doing. A drop in GDP indicates the economy is producing less; similarly an increase in GDP suggests the economy is performing better. In this lab, you will examine how changes in GDP impact the unemployment rate.</p>

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li><a href="#Section_1"> Define a Function that Makes a Dashboard </a></li>
#     <li><a href="#Section_2">Question 1: Create a dataframe that contains the GDP data and display it</a> </li>
#     <li><a href="#Section_3">Question 2: Create a dataframe that contains the unemployment data and display it</a></li>
#     <li><a href="#Section_4">Question 3: Display a dataframe where unemployment was greater than 8.5%</a></li>
#     <li><a href="#Section_5">Question 4: Use the function make_dashboard to make a dashboard</a></li>
#     </ul>
# 
# </div>
# 
# <hr>

# <h2 id="Section_1"> Define Function that Makes a Dashboard  </h2>

# We will import the following libraries.

# In[1]:


import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()


# In this section, we define the function <code>make_dashboard</code>. 
# The function will produce a dashboard as well as an html file. You can then use this html file to share your dashboard. 

# In[2]:


def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


# The dictionary  <code>links</code> contain the CSV files with all the data. The value for the key <code>GDP</code> is the file that contains the GDP data. The value for the key <code>unemployment</code> contains the unemployment data.

# In[3]:


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# <h3 id="Section_2"> Question 1: Create a dataframe that contains the GDP data and display the first five rows of the dataframe.</h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the GDP data.

# <b>Hint: <code>links["GDP"]</code> contains the path or name of the file.</b>

# In[9]:


# Type your code here
GDP_data=pd.read_csv(links["GDP"])


# Use the method <code>head()</code> to display the first five rows of the GDP data.

# In[7]:


# Type your code here
GDP_data.head()


# <h3 id="Section_2"> Question 2: Create a dataframe that contains the unemployment data. Display the first five rows of the dataframe. </h3>

# Use the dictionary <code>links</code> and the function <code>pd.read_csv</code> to create a Pandas dataframes that contains the unemployment data.

# In[10]:


# Type your code here
Unemployment_data=pd.read_csv(links["unemployment"])


# Use the method <code>head()</code> to display the first five rows of the unemployment data.

# In[11]:


# Type your code here
Unemployment_data.head()


# <h3 id="Section_3">Question 3: Display a dataframe where unemployment was greater than 8.5%.</h3>

# In[14]:


# Type your code here
df1= Unemployment_data[Unemployment_data['unemployment']>8.50]
df1


# <h3 id="Section_4">Question 4: Use the function make_dashboard to make a dashboard</h3>

# In this section, you will call the function  <code>make_dashboard</code> , to produce a dashboard. We will use the convention of giving each variable the same name as the function parameter.

# Create a new dataframe with the column <code>'date'</code> called <code>x</code> from the dataframe that contains the GDP data.

# In[15]:


x = GDP_data[['date']]
# Create your dataframe with column date


# Create a new dataframe with the column <code>'change-current' </code> called <code>gdp_change</code>  from the dataframe that contains the GDP data.

# In[16]:


gdp_change = GDP_data[['change-current']]
# Create the dataframe with column change-current


# Create a new dataframe with the column <code>'unemployment' </code> called <code>unemployment</code>  from the dataframe that contains the  unemployment data.

# In[18]:


unemployment = Unemployment_data[['unemployment']]
# Create the dataframe with column unemployment


# Give your dashboard a string title, and assign it to the variable <code>title</code>

# In[19]:


title = "Making a dashboard"
# Give your dashboard a string title


# Finally, the function <code>make_dashboard</code> will output an <code>.html</code> in your direictory, just like a <code>csv</code> file. The name of the file is <code>"index.html"</code> and it will be stored in the varable  <code>file_name</code>.

# In[21]:


file_name = "index.html"


# Call the function <code>make_dashboard</code> , to produce a dashboard.  Assign the parameter values accordingly.

# In[22]:


# Fill up the parameters in the following function:
make_dashboard(x=x, gdp_change=gdp_change, unemployment=unemployment, title=title, file_name=file_name)


# <h2>References :</h2> 

# <ul>
#  <il>
#      1) <a href="https://research.stlouisfed.org/">Economic Research at the St. Louis Fed </a>:<a href="https://fred.stlouisfed.org/series/UNRATE/"> Civilian Unemployment Rate</a>
#    </il>   
#     <p>
#      <il>
#     2) <a href="https://github.com/datasets">Data Packaged Core Datasets
#        </a>
#    </il> 
#     </p>
#     
# </ul>
# </div>
