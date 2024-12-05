# Flask Blog

## To get started

clone this repo

```bash
git clone git@github.com:Routine-Solution/Xenia.git
```

## The Tech Stack

### FrameWork

The backend framework used in this project is Flask, a lightweight and versatile Python web framework. You can learn more about Flask by checking out their [documentation] (https://flask.palletsprojects.com/en/2.0.x/).

### Getting your Project to run

After you have cloned this repository, `cd` to the project directory `Flask_Blog` and set up your virtual environment. To do this, run:

```bash
python3 -m venv venv
```

Activating the virtual environment
Depending on your operating system:

```bash
python3 -m venv venv
```

To run your virtual enviroment

if you're on

- Linux

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

After this you can install the project requirements by installing the requirements.txt

```bash
pip install -r requirements.txt
```

To apply the migration run

```bash
flask --app flaskblog db migrate -m "initial migration"
```

Flask needs to know where this application instance (app) is located. Since this app instance is defined in a file directory flaskblog, you need to specify this to Flask.

You can do this in two ways:

1. Using the --app Option
   Run the flask command with the

```bash
flask --app flaskblog db init
```

to initialize the db.

To Creates a migration file based on model changes.
run this command

```bash
flask --app flaskblog db migrate -m "initial migration"
```

To apply the migration to the database.
run this command

```bash
 flask --app flaskblog db upgrade
```

To run your project you can run the below command

```bash
flask --app run.py run --debug
```
