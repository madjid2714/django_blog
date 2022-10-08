# django_blog
django_blog

A blog application made on Django.

![alt text](https://github.com/madjid2714/django_blog/blob/main/Blog-home.png)
![alt text](https://github.com/madjid2714/django_blog/blob/main/What-is-Lorem-Ipsum-.png)
![alt text](https://github.com/madjid2714/django_blog/blob/main/Edit-Post.png)
![alt text](https://github.com/madjid2714/django_blog/blob/main/Delete-Post.png)

# post structure 

```
posts/
│
├── migrations/
│   └── __init__.py
├── static
│   └── css
│       ├── reset.css
│       └── style.css
├── templates
│   └── posts
│       ├── blogpost_confirm_delete.html
│       ├── blogpost_create.html
│       ├── blogpost_detail.html
│       ├── blogpost_edit.html
│       └── blogpost_list.html
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── test.py
├── urls.py

```
# Description
This is a simple responsive blog application made with django ,where i used a simple CRUD operations

# project hearchey

# Setup
Clone project
```shell
$ git@github.com:madjid2714/django_blog.git
```
```shell
$ cd django_blog
```
Install requirement
```shell
$ pip install -r requirement.txt
```
enter to postgres:
```shell
$ sudo -u postgres psql
```
create datbase:
```sql
CREATE DATABASE blog;
```
cretae user with password:
```sql
CREATE USER admin WITH PASSWORD 'admin';
```
setting the default encoding to utf-8 and time zone to utc, and default_transactions to read commited:

```sql
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
configure `settings.py` file if you used a diffrent user / password than mentionned in previous query :

migrate databse :
```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
create superuser:
```shell
$ python3 manage.py createsuperuser
```
run server and test the app:
```shell
$ python3 manage.py runserver 0.0.0.0:8000
```

 now you can acces to http://0.0.0.0:8000/admin/ and add some posts with images
 
 see the posts list : http://0.0.0.0:8000/







