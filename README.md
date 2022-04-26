# My Study Plan

A web app to plan and track revision and assignment tasks

## Get Started

### Django
1. Clone Repository
``` 
git clone https://github.com/super-hxman/MyStudyPlan.git
```
2. Install python module
```
pip install django djangorestframework
```
2. Generate a secret key
```
python -c 'from django.core.management.utils import get_random_secret_key; \
            print(get_random_secret_key())'
```
3. Store the key in a file called secretkey.txt in the root directory of the project

4. Run Project
```
python ./manage.py runserver
```