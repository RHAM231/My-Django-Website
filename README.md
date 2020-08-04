# My Django Website

This is the code for my portfolio website where I showcase my projects.

# Motivation

I wanted to learn web development and opted for the Django framework for back end development and the Bootstrap framework for front end development.

# Goals

I needed a site up and running quickly without cutting corners on learning how to do front end and back end design. I used the methods outlined below to achieve a fully deployed website.

# My Thought Process and Methods

Software development is a group endeavor. I consider clean, readable code following established standards and explained with helpful comments as 100% essential to a successful project.

### Apps

Following Django convention, I split the project into apps based on function. The apps include:

##### 'base_pages'
Serves generic site pages such as 'home', 'about', etc. Also establishes a base.html template that all other templates inherit from. This allows me to write code for the header, footer, and other elements common to every page only once.

##### 'contact'
Renders the contact page and houses all the contact form logic.

##### 'my_website'
The default generated app when the Django project was created. Controls admin functions such as overall url mapping, email settings, security settings, installed Django apps, etc.

##### 'projects'
Houses all logic for storing and rendering projects on my website.

### Checklist
I implemented a checklist at the end of the development process to ensure a smooth deployment and an overall high quality project. It can be found [here](https://rexhmitchell.com/portfolio-project/project_checklist/).

### Style Guides
The project is written following style guides for each language to the fullest extent possible. They are as follows:

##### Python
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [Django Documentation: Coding style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
##### HTML
* [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)
* [w3schools.com: HTML Style Guide and Coding Conventions](https://www.w3schools.com/html/html5_syntax.asp)
* [GitHub: HTML Style Guide](https://gist.github.com/ryansechrest/8693303)
##### CSS
* [CSS {guide:lines;}: High-level advice and guidelines for writing sane, manageable, scalable CSS](https://cssguidelin.es/)
* [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)

### Comments
Code is useless without liberal documentation. I include comments in all the source code, explaining what pieces of code are, what they do, and how they talk to other parts of the project. If customized code is needed, such as custom Django template tags, I explain that too.

# Security

I take security seriously. My site scores an A on [SecurityHeaders.com](https://securityheaders.com/?q=https%3A%2F%2Frexhmitchell.com%2F). In addition to the standard SSL certificate which provides https access, I utilize Django's extensive built in security settings, Django-CSP, and AWS Security Groups.

### Django Security Settings

I use Django's settings to easily provide Strict-Transport-Security, X-Frame-Options, a Referrer-Policy, X-Content-Type-Options, a Session Cookie, a CSRF token, and a Content Security Policy. All sensitive information such as secret keys, passwords, and usernames are protected using a config file.

### Django-CSP

My content security policy uses Django-CSP. I customize eight of the twenty four settings to ensure that only the necessary content will display on my site. This helps further protect the site from different types of content injection such as XSS, and clickjacking.

### AWS Security Groups

I use AWS's security group settings to restrict access to my server resources. Only IP addresses I designate can access the backend of the server and the database.

# Build Status

Deployed. Projects being added.

# Languages/Frameworks/Tools Used

Python, Pycharm, Django, Bootstrap, HTML, CSS, AWS, Apache2, Ubuntu, Postgres

# License

Copyright 2020 © Rex Mitchell
