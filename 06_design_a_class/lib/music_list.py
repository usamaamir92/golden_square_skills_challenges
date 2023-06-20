class MusicList():
    def __init__(self):
        self.track_list = []

    def add(self,track):
        self.track_list.append(track)

    def list_tracks(self):
        if self.track_list != []:
            return self.track_list
        else:
            return "Track list is empty!"

