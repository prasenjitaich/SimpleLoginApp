

## Registration and Login:
create a new user. New users can then log in/log out. 




## Django setup instructions.


1. Create a python virtual environment using below command.

   `python3 -m venv virtual-env`

2. Activate the environment.

   `source virtual-env/bin/activate`

3. Install dependencies.

   `pip install -r requirements.txt`

4. You can configure the DB for local/production if you wish in `settings.local.py/production.py`


5. If you are using a fresh database in local, execute these commands.

   `python manage.py makemigrations `

   `python manage.py migrate`

6. Run this command and your django app should be running on port `8000`

   `python manage.py runserver`


