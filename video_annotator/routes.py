import os
from flask import Flask, render_template, request, url_for, redirect, flash
from video_annotator.config import VIDEOS, ANNOTATED
from video_annotator import app
from video_annotator import utils
from video_annotator.user import User


user = User()


@app.route('/')
@app.route('/home')
def home():
    """
    Home page

    Returns:
        [type]: [description]
    """

    return render_template("index.html", title='Home VAT')


@app.route('/annotate', methods=['GET', 'POST'])
def annotate():

    if user.get_email() is not None:
        if user.get_total_videos() > user.get_annotated():
            start_minute = request.form.get('start_minute')
            start_second = request.form.get('start_second')
            end_minute = request.form.get('end_minute')
            end_second = request.form.get('end_second')
            if start_minute is not None and start_second is not None and end_minute is not None and end_second is not None:
                user.add_annotations([start_minute, start_second, end_minute, end_second])
            user.set_video()
            return render_template('annotation.html',
                                   title="Video Annotator Tool",
                                   username=user.get_email(),
                                   filename='Videos' + os.sep + user.get_video())
        else:

            return redirect("/profile")
    else:
        return render_template("index.html", title='Home VAT')


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    if request.method == 'POST':
        # save annotations
        message = 'Congrats you have successfully Annotated {0}'.format(user.get_video())
        user.save_annotations()

        return render_template('profile.html',
                               title="Annotator's Profile",
                               username=user.get_email(),
                               num_videos=user.get_total_videos(),
                               already_annotated=user.get_annotated(),message = message)
    else:
        message = 'Video {0} failed to be annotated'.format(user.get_video())
        return render_template('profile.html',
                               title="Annotator's Profile",
                               username=user.get_email(),
                               num_videos=user.get_total_videos(),
                               already_annotated=user.get_annotated(),
                               message=message)


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if user.get_email() is not None:
        message = None
        return render_template('profile.html',
                               title="Annotator's Profile",
                               username=user.get_email(),
                               num_videos=user.get_total_videos(),
                               already_annotated=user.get_annotated(),
                               message=message)
    return render_template("index.html", title='Home VAT')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        email = request.form['email']
        if email in utils.get_users():
            user.login(email)
            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   username=user.get_email(),
                                   num_videos=user.get_total_videos(),
                                   already_annotated=user.get_annotated())
        else:
            error = "User with email {} does not exist. Please check your email or Sign Up".format(email)
            return render_template("login.html", title="Sign in to VAT", error=error)

    return render_template("login.html", title="Sign in to VAT", error=error)


@app.route("/register", methods=["POST", "GET"])
def register():
    error = None
    if request.method == "POST":
        email = request.form['email']
        if email in utils.get_users():
            error = "User with email {} already exists. Please check your email or Login in".format(email)
            return render_template("register.html", title="Sign in to VAT", error=error)
        else:
            user.register(email)
            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   username=user.get_email(),
                                   num_videos=user.get_total_videos(),
                                   already_annotated=user.get_annotated())

    return render_template("register.html", title="Sign Up to VAT", error=error)


@app.route('/logout')
def logout():
    user.logout()
    return render_template("index.html", title="HOME VAT")


@app.errorhandler(404)
def not_found(e):
    """
    Handling non existing routes
    Args:
        e: error of not finding the route

    Returns:

    """

    return render_template("404.html")
