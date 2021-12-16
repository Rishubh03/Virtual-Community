# Virtual Community App
This web application provides a single platform to students, teachers, and Universities for communicating in today’s socially connected networked environment. 
Users can share, build and organize knowledge, opportunities, and resources for learning, and studying.

## A User 
User:- dummy <br />
Password:- #12Password <br />
<br />
A User app allows users to register, login, update profile, forgot password, reset password.


![Users App screenshot](/images/users-app.png)


The models and templates of this app can be found in the `users` folder.

## A Blog
A Simple blog app where user can view recents posts, list all the categories, search, blog detailed view, create post.


![Users App screenshot](/images/blog-app.png)


The models and templates of this app can be found in the `blog` folder.

## A Forum
A Simple forum app where user can ask question, reply to questions, search.


![Users App screenshot](/images/forum-app.png)


The models and templates of this app can be found in the `forum` folder.

## A Wiki
A Simple wiki app where users can view articles, search, article detailed view, any user can edit.


![Users App screenshot](/images/wiki-app.png)


The models and templates of this app can be found in the `encyclopedia` folder.

## Tech Stacks

* **Langauge:** Python 3.8
* **Framework:** Django 4.0
* **File Storage:** Azure Blob Storage
* **Database** Azure Database for PostgreSQL
* **Deployment** Azure App Services

## Installation Instructions
If you want to work with this project or create a version of it make sure to follow the steps below!

1. Install `python 3`, `pip` and `virtualenv`
2. Clone this repo `git clone https://github.com/Rishubh03/Virtual-Community.git`
3. Install dependencies `pipenv install requirements.txt`
4. Activate the virtual environment `pipenv shell`
5. Make Migrations `python manage.py makemigrations`
6. Migrate `python manage.py migrate`
7. Create a super user `python manage.py createsuperuser`
8. Runserver `python manage.py runserver`

