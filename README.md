# hospital_app
```python
login: hospital.admin
password: 9900py
```

Project deployed to Render(https://hospital-mc.onrender.com/)

An application for managing medical practice in a hospital by an administrator.
All users can see the first "Home" page. 
To view, edit, or delete info on this page you must have an Admin login and password.
After login, you have access to read or edit info.
Here is an implementation of these features: 
1. Login, logout for Admin user
2. Hidden info before login
3. Buttons for deleting and updating info for all categories
4. Button for a new entry in the table ("Create new...")
5. Searching and pagination for every table
6. Navigation between models, where possible and appropriate, using clickable links between models

```python
Installation:
git clone https://github.com/ZaichenkoViktoriia/hospital_app/
cd hospital_app
python3 -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

if you want to use previous info for this project you can run this command and load some info
```python
python manage.py loaddata db.json
```
or you can use the button "Create" to create new info for this project


[Demo](static/image/demo.jpg)
