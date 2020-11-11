from flask import Flask

app = Flask(__name__)
app.secret_key = "a2f8a7fa-fb61-11ea-8c89-0f4248d2074f"
from video_annotator import routes
