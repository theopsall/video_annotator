# Video Annotator Web App Tool
---
![APM](https://img.shields.io/apm/l/vim-mode)
[![Generic badge](https://img.shields.io/badge/python->=3-green.svg)](https://shields.io/)

Video Annotator app is a simple and easy to use tool, that helps you to serve videos to annotators
 in random order. Video Annotator Tool is written in flask.

 ### Web App Usage:

 You have to register/login with your email, in order to start the annotation process.
 The app will randomly peek a video that you have not annotate already to begin with.


## Installation
```bash
pip install -r requirements.txt
```

## Start Annotator Tool:
```bash
python3 run.py
```

Tree Structure
---
```
├───.users
├───static
│   ├───Annotated
│   └───Videos
```
Under the ./users direcroty you can find the users.txt file which contains the emails of the registered users on the Web app, in order to wrok the login and register mechanism.

Under the static folder you can find the Annotated directory which contains a {email}.txt file for each user with the annotated videos and a directory for each user with the labels in .csv for each video that have been annotated from the user.

Under the static folder you can find the Video directory which contains the dataset.