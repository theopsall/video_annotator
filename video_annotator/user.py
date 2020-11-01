from video_annotator import utils


class User():
    def __init__(self):
        """
        Initialiize user
        """
        self._email = None
        self._annotated = None
        self._annotations = []
        self._videoname = None
        self._total_videos = utils.num_videos()

    def login(self, email):
        """
        Login user to the base

        Args:
            email (str): Email of the user
        """
        self._email = email
        self._annotated = utils.num_annotated(self._email)

    def register(self, email):
        """
        Registers user to the base

        Args:
            email (str): Email of the user
        """
        utils.add_user(email)
        utils.make_annotation_directory(email)
        utils.make_annotation_file(email)
        self.login(email)

    def add_annotations(self, data):
        """
        Annotations for the specific self._videoname are stored

        Args:
            data (list): List of annotations
        """
        self._annotations.append(data)

    def finish(self):
        """
        After the annotation of the video, resets the annotations data and the video name
        """
        self._annotations = []
        self._videoname = None

    def set_video(self):
        """
        Set a random video to annotate
        """
        diff = utils.get_difference(self._email)
        video = utils.get_random_video(diff)
        self._videoname = video

    def save_annotations(self):
        """
        Saves the annotations on the base
        """
        utils.add_annotation(self._email, self._videoname, self._annotations)
        utils.add_video(self._email, self._videoname)
        self._annotattions = []
        self._videoname = None

    def logout(self):
        """
        Logout the user from the base
        """
        self._email = None
        self._annotated = None
        self._total_annotated = None
        self._annotations = []
        self._videoname = None

    # Getters
    def get_email(self):
        """
        Returns the email of the current user

        Returns:
            str: The email of the user
        """
        return self._email

    def get_video(self):
        """
        Returns the video name the current user is annotating

        Returns:
            str: Name of the video is currently annoting
        """
        return self._videoname

    def get_annotated(self):
        """
        Returns the total number of annotated videos

        Returns:
            int: The total number of already annotated videos
        """
        return self._annotated

    def get_total_videos(self):
        """
        Returns the total number of videos in the database

        Returns:
            int: The total number of videos
        """
        return self._total_videos
