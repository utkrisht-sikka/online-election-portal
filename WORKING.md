# Guide to writing django code for the project


#CSE222 
### 3 easy pieces:
 There are 3 things you need to learn before you can contribute to the django codebase:
1. Modifying the urls.py file 
2. Modifying the views.py file 
3. Using jinja for server side page generation 


Before we cover these topics, clone the repo and lets go over the directory structure.
```
├── django_dbms
│   ├── django_dbms
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── election <----------------------------------------------------------
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   ├── candidate_registration.html
│   │   │   ├── cand_profile.html
│   │   │   ├── home.html
│   │   │   ├── index.php
│   │   │   ├── login.html
│   │   │   ├── official_registration.html
│   │   │   ├── party_registration.html
│   │   │   ├── register.html
│   │   │   └── voter_registration.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── Procfile
│   ├── requirenments.txt
│   ├── runtime.txt
│   └── staticfiles <-------------------------------------------------------
│       ├── admin
│       │   ├── css
│       │   ├── fonts
│       │   ├── img
│       │   └── js
│       ├── css
│       │   ├── bootstrap.css
│       │   ├── cand_profilestyle.css
│       │   ├── homestyle.css
│       │   ├── login.css
│       │   └── regstyle.css
│       ├── images
│       │   ├── Carousel_Placeholder.png
│       │   ├── ChoosingWisely-CMYK-taglineR.jpg
│       │   ├── Click-here-to-register-online.gif
│       │   ├── election.jpg
│       │   ├── Image-10 (1).jpg
│       │   ├── Image-10.jpg
│       │   ├── register now.jpg
│       │   ├── register.png
│       │   ├── registration_bg.jpg
│       │   ├── results2.png
│       │   ├── results.jpg
│       │   ├── Thumbnail_Placeholder.png
│       │   ├── Vote-Online-for-President-Now.png
│       │   └── voter.png
│       ├── js
│       │   ├── ajax-utils.js
│       │   ├── bootstrap.js
│       │   ├── bootstrap.min.js
│       │   ├── jquery-2.1.4.min.js
│       │   ├── npm.js
│       │   ├── register.js
│       │   ├── script.js
│       │   └── showpassword.js
│       └── staticfiles.json
├── Procfile
├── README.md
├── requirements.txt
```

The directory we will be spending the most time in is the **election** directory. and the **staticfiles** directory.

### Staticfiles
This directory contains all css, javascript and images we will be using on our website (in the css,images,js directories resp.)
```
├── admin
│   ├── css
│   ├── fonts
│   ├── img
│   └── js
├── css
│   ├── bootstrap.css
│   ├── cand_profilestyle.css
│   ├── homestyle.css
│   ├── login.css
│   └── regstyle.css
├── images
│   ├── Carousel_Placeholder.png
│   ├── ChoosingWisely-CMYK-taglineR.jpg
│   ├── Click-here-to-register-online.gif
│   ├── election.jpg
│   ├── Image-10 (1).jpg
│   ├── Image-10.jpg
│   ├── register now.jpg
│   ├── register.png
│   ├── registration_bg.jpg
│   ├── results2.png
│   ├── results.jpg
│   ├── Thumbnail_Placeholder.png
│   ├── Vote-Online-for-President-Now.png
│   └── voter.png
├── js
│   ├── ajax-utils.js
│   ├── bootstrap.js
│   ├── bootstrap.min.js
│   ├── jquery-2.1.4.min.js
│   ├── npm.js
│   ├── register.js
│   ├── script.js
│   └── showpassword.js
```
### Election directory
Here, we will be working in urls.py, views.py and in the templates directory, where we will have all the html files for our project
```
.
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── templates
│   ├── base.html
│   ├── candidate_registration.html
│   ├── cand_profile.html
│   ├── home.html
│   ├── login.html
│   ├── official_registration.html
│   ├── party_registration.html
│   ├── register.html
│   └── voter_registration.html
├── tests.py
├── urls.py
└── views.py
```

### Essential workflow
As mentioned above, the files we will be using are the urls.py, views.py and the templates directory.

#### views.py

views.py is where we will be writing the python code which returns a webpage when the user visits our website, or if they send  a `POST` request such as when submitting the forms for login/reg.

```
   def home(request):
      return render(request, "home.html")

```
The above function simply returns the home page for our website. 
We can use the `request` object to get a lot of other information, such as the type of request(`GET`,`POST`), or whether the user is logged in and authenticated or whether they are not.
Here `home.html` is in our templates directory.


Its in these view functions where we will be writing our embedded SQL queries. for the user views.

##### Getting form data:
Often times we use forms to get data from the user for registration, login etc.
since we dont want to display sensitive info in the url, we use POST request for this:
Here is how we extract the data from the post request server side.
```
  def register_voter(request):
      if(request.method == "POST"):
              dict = request.POST.dict()
              if(not(User.objects.filter(username=dict['Username']).exists())):
                  user = User.objects.create_user(dict['Username'],dict['firstName']+"@gmail.    com",dict['password']);
  
                  user.first_name,user.last_name = dict['firstName'],dict['lastName']
                  user.save();
                  return HttpResponse('new user created');
              else:
                  return HttpResponse('user already exists');
      return render(request, "voter_registration.html")
```


1. Check if the request is of `POST` type.
2. get dict from the request, this is a normal python dictionary for our purposes
3. get the data from the dict.

We will cover the corresponding html code when we cover the templates.

##### Dynamic server side generation, views.py
We will encounter cases where some of the information on the html pages needs to be modified based on who is visiting our website, or, perhaps we want to place queried MySQL data into our html page, for this we need to tell django to place the data into the html page before it serves this to the website visitor.

We can pass python objects to our html pages and embed pseudo-python(jinja) code which is executed before the user gets the page.

*eg*
Instead of
```return render(request,'solution.html')```  
we can do :
```
return render(request,'solution.html',{'data':zip(ri,la),'count':ctr}
```


Here im passing the info I need as python objects `zip(ri,la)  (an nx2 array)` and `ctr (int value)`  and these are mapped to `data` and `count`
respectively. We will use data and count in our html files to generate dynamic web pages.



 #### urls.py

The functions  in views.py are 'mapped' to specific urls for our website.
When a person visits our home page, we need to tell django to 'call' a function from views.py.
Which paths are mapped to which functions, is determined by the *urls.py* file.
```
from .views import home, login, cand_profile, register_candidate, register_party, register_voter, register_official, register
   
   urlpatterns = [
       path('', home, name='home'),
       path('login', login, name='login'),
       path('register', register_voter, name='register'),
	   ]
```

This is the relevant code from the urls.py file, here, we first import the view function we defined earlier.

Now in the `urlpatterns` list, we will add a new `path` entry, remember to append a comma at the end.

1. The first argument inside the path function is the path name, for example, the first one we have is
`path('', home, name='home'),`
2. Here ``''`` tells us that the root directory of our website is mapped to the home view function (second argument).
3. The third argument assigns a name to the url so that we can easily place these urls in the hyperlinks when we are making out html files.
 
*Another example:* 
`path('login', login, name='login'),` maps `<website>/login` to the `login` view function.


### Templates/
##### Adding urls and css links to html files 
**urls**

 We assigned a name to the urls for our website using `name = 'login'` in 
 in `path('login', login, name='login')` .
 we can now use these names in our html files like so:
```<a href="{% url 'login' %}">Login</a>```
on clicking this link we will be sent to the login page.



**css and javascript**
Before we can use static resources, we need to add the line 
```{% load static %}```

Once we add the css and javascript files to the staticfiles directory, we can now include the css and javascript like so:

eg 1 : ``` <link href="{% static 'css/regstyle.css' %}" rel="stylesheet" type="text/css">```


eg 2 : ```<script src="{% static 'js/bootstrap.min.js' %}"></script>```

Here is all the other information you need to know for the templates:


##### [Using variables in django templates](https://www.geeksforgeeks.org/variables-django-templates/#:~:text=Django%20templates%20not%20only%20allow,object%20mapping%20keys%20to%20values.)
##### [Using for loops in django templates](https://www.geeksforgeeks.org/for-loop-django-template-tags/)
##### [Using django template inheritance](https://docs.djangoproject.com/en/3.1/ref/templates/language/)
