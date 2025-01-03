# Blog Application Using Django REST Framework  

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)
---

## Overview  
This is a Blog Application using Django REST Framework where there will be admin/spueruser who will create blog post users and assign them to create, update and delete their own post as well as only viewing other user's posts. The PowerPoint Slides of this project is here: https://docs.google.com/presentation/d/168ZLDkJCQ66C36hx2Kjv3ZbdtGBFlz16IMFwwkhjcP0/edit?usp=sharing

---

## Features  
- View Users List. 
- View & Create Blog Posts. 
- Update & Delete Posts.  
 
---

## Installation  

Follow these steps to set up the project:  

### 1. Clone the Repository  
```bash  
git clone https://github.com/SamiaAurin/AssToken19-BlogApplication.git
cd AssToken19-BlogApplication
```
### 2. Set Up a Virtual Environment

**On Linux/macOS:**
```bash 
python3 -m venv venv  # python -m venv venv 
source venv/bin/activate  
```
**On Windows:**
```bash 
python -m venv venv  
venv\Scripts\activate  
```

### 3. Run the project
```bash
cd blog
python manage.py migrate
python manage.py runserver
```
Then go to: http://localhost:8000/users/
To Log in follow the next steps.

--- 

# Usage 

## 1. Create a Superuser

```bash
python manage.py createsuperuser
```

Then go to: http://localhost:8000/admin/ . Create a Group and assign them access to manage posts. Create as many Users you want.

## 2. API Endpoints

- users/ : One can log in from this endpoint and View All Users.
- users/<int:pk>/ , Example: http://localhost:8000/users/1/ : View Specific Users.
- posts/ : View All Posts.
- posts/<int:pk>/ , Example: http://localhost:8000/posts/1/ : View/Update/Delete Only Own Posts. 