from video_annotator import app
from video_annotator.utils import create_directories

if __name__ == "__main__":
    create_directories()
    app.run()