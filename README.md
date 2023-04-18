# CSE550-Electron-Django

This github contains the HTML/CSS/JS/JSON files for the Electron app, but none of the Electron setup.

TO SETUP:

 - Install Electron globally using npm install -g electron
 - Install Django using pip install django
 - Install Django REST framework using pip install djangorestframework
 - In the root project folder, add a folder called "AppElectron"
 - In AppElectron, run "npm install electron". This should add the node_modules folder that is missing from the project.
 - Move the files from AppElectronNoModule into AppElectron and repalce any files of the same name

To run Electron: navigate to AppElectron and run "npm start"

To run Django: navigate to ProjectDjango and run "python manage.py runserver". server can be viewed at http://127.0.0.1:8000/.
