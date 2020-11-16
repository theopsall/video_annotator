import os
from flask_socketio import SocketIO
from flask import Flask, render_template, request, url_for, redirect, flash, session,Markup
from video_annotator.config import VIDEOS, ANNOTATED
from video_annotator import utils

utils.create_directories()
app = Flask(__name__)

socketio = SocketIO(app)

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

    if "nickname" in session:
        if (len(utils.get_videos()) > len(utils.annotated(session['nickname']))):
            diff = utils.get_difference(session['nickname'])

            video = utils.get_random_video(diff)

            #video = os.path.join(*video)
            video_category = video.split(os.sep)[0]
            video_name = video.split(os.sep)[-1]
            session['video'] = "{0}{1}{2}".format(video_category,os.sep,video_name)

            start_minute = request.form.get('start_minute')
            start_second = request.form.get('start_second')
            end_minute = request.form.get('end_minute')
            end_second = request.form.get('end_second')

            is_reloaded = request.form.get("is_reloaded")

            if is_reloaded:
                session.pop("data", None)

            if start_minute is not None and start_second is not None and end_minute is not None and end_second is not None:

                if "data" in session:
                    data = session["data"]
                    data.append([start_minute, start_second, end_minute, end_second])
                    session["data"] = data
                else:
                    session["data"] = [[start_minute, start_second, end_minute, end_second]]
                # print(session['data'])
            return render_template('annotation.html',
                                   title="Video Annotator Tool",
                                   nickname=session['nickname'],
                                   category=video_category,
                                   video_name=video_name,
                                   filename='Videos' + os.sep + video)
        else:
            return redirect("/profile")
    else:
        return render_template("index.html", title='Home VAT')


@app.route('/finish', methods=['GET', 'POST'])
def finish():
    if request.method == 'POST':
        if "data" not in session:
            message = Markup("<p class='alert alert-danger' role='alert'>\
            Video: {0} <br>failed to be annotated! <br> You have not set timestamps\
            </p>".format(session['video']))
            return render_template('profile.html',
                                title="Annotator's Profile",
                                nickname=session["nickname"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["nickname"]),
                                message = message)
        # save annotations
        message = Markup("<p class='alert alert-success' role='alert'>\
            Congrats you have successfully Annotated {0}</p>".format(session["video"]))
        utils.add_annotation(session['nickname'], session['video'], session['data'] )
        utils.add_video(session['nickname'], session['video'])

        session.pop('video', None)
        session.pop('data', None)

        return render_template('profile.html',
                                title="Annotator's Profile",
                                nickname=session["nickname"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["nickname"]),
                                message = message)
    else:
        message = 'Video {0} failed to be annotated'.format(session['video'])
        return render_template('profile.html',
                                title="Annotator's Profile",
                                nickname=session["nickname"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["nickname"]),
                                message = message)


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if 'nickname' in session:
        return render_template('profile.html',
                                title="Annotator's Profile",
                                nickname=session["nickname"],
                                num_videos=utils.num_videos(),
                                already_annotated=utils.num_annotated(session["nickname"]))

    return render_template("index.html", title='Home VAT')


@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    if request.method == "POST":
        nickname = request.form['nickname']
        if nickname in utils.get_users():
            session["nickname"] = nickname
            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   nickname=nickname,
                                   num_videos=utils.num_videos(),
                                   already_annotated=utils.num_annotated(nickname))
        else:
            error = "User with nickname {} does not exist. Please check your nickname or Sign Up".format(nickname)
            return render_template("login.html", title="Sign in to VAT", error=error)

    return render_template("login.html", title="Sign in to VAT", error=error)


@app.route("/register", methods=["POST", "GET"])
def register():
    error = None
    if request.method == "POST":
        nickname = request.form['nickname']
        if nickname in utils.get_users():
            error = "User with nickname {} already exists. Please check your nickname or Login in".format(nickname)
            return render_template("register.html", title="Sign in to VAT", error=error)
        else:
            session["nickname"] = nickname
            utils.add_user(nickname)
            utils.make_annotation_file(nickname)
            utils.make_annotation_directory(nickname)

            return render_template('profile.html',
                                   title="Annotator's Profile",
                                   nickname=nickname,
                                   num_videos=utils.num_videos(),
                                   already_annotated=utils.num_annotated(nickname))

    return render_template("register.html", title="Sign Up to VAT", error=error)


@app.route('/logout')
def logout():
    session.pop('nickname', None)
    session.pop('video',None)
    session.pop('data',None)
    return render_template("index.html", title="HOME VAT")

@socketio.on('disconnect')
def disconnect_user():
    session.pop('video',None)
    session.pop('data',None)

@app.errorhandler(404)
def not_found(e):
    """
    Handling non existing routes
    Args:
        e: error of not finding the route

    Returns:

    """

    return render_template("404.html")
