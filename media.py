import webbrowser

class Movie():
    """This class defines a movie and key information about it."""
    def __init__(self, title, release_year, poster_image, trailer_youtube):
        self.title = title
        self.release_year = release_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
