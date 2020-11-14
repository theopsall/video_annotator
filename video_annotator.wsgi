import sys
sys.path.insert(0,"/var/www/video_annotator/")

from video_annotator import app as application
application.secret_key = 'a2f8a7fa-fb61-11ea-8c89-0f4248d2074f'