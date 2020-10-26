from video_annotator import app
from video_annotator.utils import create_directorys

if __name__ == "__main__":
    create_directorys()
    app.run()