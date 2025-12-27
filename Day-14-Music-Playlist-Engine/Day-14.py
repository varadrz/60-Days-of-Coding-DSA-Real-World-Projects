# Day 14 - Music Playlist Engine
# Focus: Linked List
# Language: Python 3


class SongNode:
    def __init__(self, song_name):
        self.song = song_name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name):
        new_song = SongNode(song_name)

        if not self.head:
            self.head = new_song
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_song

    def remove_song(self, song_name):
        if not self.head:
            print("Playlist is empty.")
            return

        if self.head.song == song_name:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.song == song_name:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Song not found.")

    def play_all(self):
        if not self.head:
            print("Playlist is empty.")
            return

        current = self.head
        print("\nPlaying Playlist:")
        while current:
            print(f"Playing: {current.song}")
            current = current.next

    def show_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return

        current = self.head
        print("\nPlaylist:")
        while current:
            print(current.song)
            current = current.next


def main():
    playlist = Playlist()

    playlist.add_song("Song A")
    playlist.add_song("Song B")
    playlist.add_song("Song C")

    playlist.show_playlist()
    playlist.play_all()

    playlist.remove_song("Song B")
    playlist.show_playlist()


if __name__ == "__main__":
    main()
