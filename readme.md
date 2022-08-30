# Idea
> Build a platform for users where they can sell their courses as well as become a freelancer

> Freelancers will be evaluted based on the Credit System which will save the client more time, as the person who is going to hire a freelancer without looking into the portfolio and other projects.

> This way newbie can easily get client for the freelancer.

> And for courses, we are planning to make it more accessible for the people, by including various methods.

##### My pov
> Here, we will let the user decide in which language they would like to create course, we will have our people voice over
that in various other language, saving time for the user who creates the course, and making it accessible.

# What is a credit system?
> It is a scoring system which will be used to evalute the freelancer based on their past work, reviews, connections, completion of the project, client interaction.

> The way it will be evaluted is yet to be decided.

# Authentication
> Using django - allauth, which comes with various prebuilt packages for all the types of third party authentication, we can easily create new autheticated users.

## Things to implement
> 1. A credit system
> 2. Users authentication system
> 3. Courses enrolling system
> 4. Database management
> 5. Payment gateway

## Project
> Till today, we have implemented an api, for connecting the frontend which going to be react. Then we have Accounts app where we can list users, and create [[Users authentication System]], management system etc.

> Then we have Courses app, which will store enroll, courses details and video details. Till today, we have implemented storing courses and enroll and being able to view the data through api, we can upload videos and we can receive the data from api of which course the video belong.

> Then we have freelancershala app, where we keep the list of order with their order id, we still figuring out what to do in this app folder. Planning to implement the algorithm for credit system here

### Packages and framework used

Python, javascript(not yet confirmed)- programming language
frontend framework - [react](https://reactjs.org/)

backend framework-[django](https://docs.djangoproject.com/en/4.1/)

other packages-[django-rest-framework](https://www.django-rest-framework.org/), [django-allauth](https://django-allauth.readthedocs.io/en/latest/), [Razorpay](https://razorpay.com/docs/payments/server-integration/python/install/)

database - Postgresql(Relational database)

hosting - [aws](https://aws.amazon.com/) or google cloud

This is the rough idea till today



## Run
> open terminal and type `python3 -m venv env && source env/bin/activate && pip install poetry`. Then, type `poetry install` to install all the packages. Then type `python manage.py runserver <PORT>` (default is 8000)

### Super User
> To access the admin panel, create a super user using the terminal.
> In the terminal, type `python manage.py createsuperuser`, then enter the credetials and then you are done.

## Info
- [ ] Detailed implementaion of Courses and Enrolling function
- [ ] Creating different roles based on the type of business
- [ ] Creating Social Authentication System
- [ ] Implementing payment gateway


### Packages Used:-
> djangorestframework <br>
> psycopg-binary <br>
> django-allauth <br>
> google-api-python-client <br>
> Razorpay Python SDK

#### Note
> project is in progress! 
