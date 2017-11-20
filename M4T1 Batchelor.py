
# coding: utf-8

# <h3>Step 1: Import the requests library</h3>

# In[7]:

import requests


# <h3>Step 2: Send an HTTP request, get the response, and save in a variable</h3>

# In[8]:

response = requests.get("https://en.wikipedia.org/wiki/Main_Page")


# <h3>Step 3: Check the response status code to see if everything went as planned</h3>
# <li>status code 200: the request response cycle was successful
# <li>any other status code: it didn't work (e.g., 404 = page not found)

# In[9]:

print(response.status_code)


# <h3>Step 4: Get the content of the response</h3>
# <li>Convert to utf-8 if necessary

# In[10]:

text = response.content.decode('utf-8')


# <h4>Problem: Get the contents of Wikipedia's main page and look for the string "Did you know" in it</h4>

# In[15]:

url = "https://en.wikipedia.org/wiki/main_page"
#The rest of your code should go below this line
location = text.find('Did you know')
if  location > -1:
    print(text[location: location+1500])
else:
    print('Not Found')


