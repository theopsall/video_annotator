# video_annotator
Video Annotator Web App
---
![APM](https://img.shields.io/apm/l/vim-mode)

Video Annotator app is an simple and easy to use tool, that helps you to serve videos to annotators
 in random order. Video Annotator Toll is written in flask.

 Web App Usage:
 You have to login with your email, in order to start the annotation process.
 The app will randomly peek a video that you have not annotate already to start the process of annotating.

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