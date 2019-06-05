### Logging ELK Stack in python


### Python setting up project
    
##### Step1 : Creating virtual environment
    csk@csk-ai-revolution:~/PycharmProjects/git$ conda create -n elk python=3.6
    Collecting package metadata: done
    Solving environment: done
##### Step2 : Install django & create django app
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git$ pip install django
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git$ pip install djangorestframework
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git$ django-admin startproject logging_elk_stack
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git$ cd logging_elk_stack
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git/logging_elk_stack$ python manage.py startapp logging_app
     
     *** Also make necessary changes in 
        - settings.py
        - urls.py
        - view.py
    
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git/logging_elk_stack$ python3 manage.py migrate
    (elk) csk@csk-ai-revolution:~/PycharmProjects/git/logging_elk_stack$ python3 manage.py runserver 8000
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    June 05, 2019 - 06:55:05
    Django version 2.2.2, using settings 'logging_elk_stack.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C