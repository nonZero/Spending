# Spending 🤑💰🏧

A simple [Django](https://www.djangoproject.com/) project.

## Prerequisites

* Python (3.6/3.5 recommended. Python 2.7, mmm... well... OK.)
* Python and pip should be available from the command line:

        python --version
        pip --version

* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) .  To install:
    *  Windows:

            pip install virtualenv virtualenvwrapper-win

    * Ubuntu Linux:

            sudo apt-get install virtualenvwrapper

    * Other Linux:

            sudo pip install virtualenvwrapper
            sudo updatedb
            locate virtualenvwrapper.sh

        and add to your `.bashrc`:

            source /your/path/to/virtualenvwrapper.sh

## Setup
### Create a virtualenv
Create a clean virtualenv with your global python:

    $ mkvirtualenv spendingenv

Or, to force creation of a python 3 env on linux:

    $ mkvirtualenv spendingenv -p $(which python3)

Or, to force creation of a python 3 env on windows:

    > mkvirtualenv spendingenv -p c:\the\path\to\your\python3\python.exe

To reactivate an exisiting env use:

    $ workon spendingenv


### Clone repo

    git clone https://github.com/nonZero/Spending.git
    cd Spending

### Upgrade pip and install packages

    pip install -U pip
    pip install -r requirements.txt

## Some more commands

Create a db and run all exisiting migrations:

    python manage.py migrate

Create a superuser (for admin access):

    python manage.py createsuperuser

Create sample data (see [make_data.py](./expenses/management/commands/make_data.py))

    python manage.py make_data 50

Run the development web server:

    python manage.py runserver

Run all tests:

    python manage.py test

Run shell and import all models:

    python manage.py shell_plus

Start pycharm and create a project:

    charm .
