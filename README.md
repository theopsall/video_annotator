# Video Annotator Web App Tool
Annotate important timestamps of a video

![APM](https://img.shields.io/apm/l/vim-mode)
[![Generic badge](https://img.shields.io/badge/python->=3-green.svg)](https://shields.io/)

About
----
Video Annotator app is a simple and easy to use tool, that helps you to serve videos to annotators
 in random order. Video Annotator Tool is written in flask.

 ## Web App Usage:

 You have to register/login with your email, in order to start the annotation process.
 The app will randomly peek a video that you have not already annotate to begin with.


## Installation
```bash
git clone https://github.com/theopsall/video_annotator.git
cd video_annotator
pip install -r requirements.txt
```

## Running:
```bash
python3 run.py
```

## Production deployment
In case you want production deploymment you can find the source code located at the [server_ready](https://github.com/theopsall/video_annotator/tree/server_ready) branch of this repo.


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

Under the static folder you can find the Video directory which contains the dataset seperated in class subdirectories.


