# Python Course

<p>This is a course that I am taking from the programming with mosh videos.</p>

<p>Here are some quick links to navigate to a specific section<p>

<li><a href="#section1">Primitive Types</a></li>
<li><a href="#section2">Control Flow</a></li>
<li><a href="#section3">Functions</a></li>
<li><a href="#section4">Data Stuctures</a></li>
<li><a href="#section5">Expections</a></li>
<li><a href="#section6">Classes</a></li>
<li><a href="#section7">Modules</a></li>
<li><a href="#section8">Python Standard Library</a></li>
<li><a href="#section9">Python Library</a></li>
<li><a href="#section10">Popular Python Packages</a></li>
<li><a href="#section11">Django</a></li>


<h2 id="section1">Primitive Types</h2>

First section of the videos just going over the basics of python. <br>
This section included:


<li>Expressions</li>
<li>Pylint</li>
<li>Syntax</li>
<li>Numbers</li>
<li>Strings</li>


<h2 id="section2">Control Flow</h2>
Second section of the videos.<br>
This section included:

<li>For Loops</li>
<li>Nested Loops</li>
<li>Conditionals</li>
<li>For Else</li>
<li>Operators</li>
<li>Ternary Operators</li>
<li>While Loops</li>

<h2 id="section3">Functions</h2>
Third section of videos on python.
<br>
In this section I learned a lot about how functions worked.
I created a cool fizzbuzz program in python that didn't take me very long to make.

Also learned the difference between arguments and parameters that a lot of young coders miss.
<br>
This section included:

<li>Arguments</li>
<li>Debugging</li>
<li>Defining Functions</li>
<li>Keyword arguments</li>
<li>xargs</li>
<li>xxargs</li>
<li>Types of Functions</li>

<h2 id="section4">Data Stuctures</h2>
Fourth section of my videos on python.
<br>

In this section I learned a lot about loops, dictionaries,
tuples and so much more.

I learned to iterate through these and how to add, remove, delete and to use more of their various methods.

The exercise for this section was a interesting one I figured out a solution to the problem but I now realize it code be improved. This is great because this is one of the interview questions.
<br>

This section included:

<li>Accessing Items</li>
<li>Adding and Removing Items</li>
<li>Arrays</li>
<li>Dictionaries</li>
<li>Filter Functions</li>
<li>Map Functions</li>
<li>Finding Items</li>
<li>Lambda Functions</li>
<li>List</li>
<li>Looping List</li>
<li>Unpacking</li>
<li>Tuples</li>
<li>Zip Functions</li>

<h2 id="section5">Expections</h2>
 Expections are errors exterminates the excution of a program.
 <br>

 Learned about the risk of raising your own expections in a function.
 Slows down program greatly try to avoid it if possible.
 <br>

 This section included:

<li>Handling Expections</li>
<li>Handling Different Expections</li> 
<li>Raising Expections</li>
<li>With Statements</li>

<h2 id="section6">Classes</h2>
 Are the blueprint for creating new objects

 <p>Classes can Inherit methods from each other to help keep the code dry.</p>

 <p>We want to be careful when we are using inheritance tho because we don't want it were we have multi-leveled classes going off eachother. This is because if one crash it can cause a chain reaction causing you to go back to find the issue and causing the same or different issue to another class.</p>

<p>We also want to be careful having multiple classes going of one class. It is ok to have anywhere from 2 - 3 going of one class otherwise you'll start to see you are having classes to have classes.</p>


This section included:
<li>Arithmetic Operators</li>
<li>Classes</li>
<li>Constructors</li>
<li>Data Classes</li>
<li>Inheritance</li>
<li>Magic Methods</li>
<li>Private Members</li>
<li>Polymorphism</li>
<li>Properties</li>
<li>Creating Custom Containers</li>

<h2 id="section7">Modules</h2>
<p> Are files that have some python code. They can have:</p>

<li>Classes</li>
<li>Functions</li>
<li>Methods</li>
<li>Attributes and Etc.</li>
<br>

<p> We can also compile our python files. By compiling the files we are speeding up the modules load time. This does not speed up the file itself though. Also when you update the file Python will go and check the compiler and update it for you when it runs.</p>

<p>Packages in python  are containers for 1 or more modules.</p>

<p>When you add  <b>__init__.py </b>  python will look at the folder as a package.</p>

<h2 id="section8">Python Standard Library</h2> 

<p>In this section I learned a lot about the Python library and what it has to offer. I've practice with and learned a lot from packages such as Time Delta, webbrowser and so much more.</p>

<p>I learned also how to make csv files right inside of python, and how to use SQLite and Json</p>

<p>This Section included:</p>
<br>

<li>Sending Emails</li>
<li>Opening Browsers with Python</li>
<li>Working with CSV</li>
<li>Working with JSON</li>
<li>SQLite</li>
<li>Zip Files</li>
<li>Generating Random Values</li>

<h2 id="section9">Python Packaging Index</h2>
<p>In this section I learned a lot of the basics of using pip3 and all the awesome things I can do with it.</p>

<p>I learned a lot of useful terminal commands as shown below, learned how to updated my dependencies and create a virtual enviroment.</p>

```
pypi.org
pip3 install
pip3 install --upgrade pip
```

<h2 id="section10">Popular Python Packages</h2>

<p>In this section I will be learning about Popular packages in python and learning about some APIs </p>

<p><strong>HEADS UP!</strong> Majority of this work was done in a virtual machine and if you are not comfortable or don't know how to use virtual machines you can try to install the packages locally by using pip3 (mac) or pip (windows)</p>

<p><strong>Also</strong> if you run into a issue with vscode where you use the code runner and it says it can not find the module you can run it by typing the the command below in the terminal either in vscode or other terminals.</p>

```
Mac:
python3 "nameOfFile.py"

Windows:
python "nameOfFile.py"
```

Tools Needed:
<li>Yelp Api</li>
<li>Twilio</li>
<li>Selenium</li>
<li>Numpy</li>
<li>Openpyxl</li>
<li>Pypdf</li>
<li>Beautifulsoup</li>
<li>.gitignore</li>


```
pipenv install request
pipenv install pylint --dev
pipenv install autopep8 --dev
pipenv install twilio
pipenv install numpy
pipenv install selenium
pipenv install openpyxl
pipenv install pypdf2
```
<br>

<p>This section Included:</p>
<li>Creating Virtual Machines</li>
<li>Working with Excel Spreadsheets</li>
<li>Browser Automation</li>
<li>Sending Text Messages using python</li>
<li>Using Numpy</li>
<li>Using Yelp Api</li>

<br>

<h2 id="section11">Django</h2>
<a href='https://gentle-depths-43829.herokuapp.com/'>WamBuster</a>
<p>Welcome to my django movie project</p>
<p>This movie project is being used to demostrate the ability to contect to heroku, connecting to databases and adding bootstrap to a django project.</p>
<p>I plan on coming back to this project and making it nicer.</p>
<p> the "." is to open it in the current directory)</p>

```
pipenv install django==2.1.5
pipenv shell
jango-admin startproject "Project name" .
python3 manage.py server
python3 manage.py startapp movies
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
pipenv install gunicorn
heruko login
heruko create
git init
git add .
git push heroku master
heroku ps:scale web=1
heroku open
```

<p>This command will let you see the table commands used to make the table</p>

```
python3 manage.py sqlmigrate movies 0001

```

<p><strong>Very Important Information</strong>  When making this project please use django versions higher than 2.1. There is an exception thrown when youn are trying to add to the database and it is only in this version. if you have to update please delete you DBSqlite file and run your migrations all over again</p>