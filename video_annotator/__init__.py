from flask import Flask

app = Flask(__name__)
from video_annotator import routes
