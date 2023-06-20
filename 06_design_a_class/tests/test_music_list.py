"""1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see 
a list of them.

2. Design the Class Interface
The interface of a class includes:

The class will be called MusicList.
It will have an initialiser function with no 
parameters and an empty list to store the tracks.
It will have an add function that add's tracks
to the list, this function will take a string
as an argument, and will not return anything.
There will be another function called list_tracks,
which will take no arguments and return a list
of tracks in the list.

There is other potential functionality to be added
such as removing tracks and checking for duplicates
but the user story did not explicity mention these
so will not be added.

3. Create Examples as Tests

A test to check that the add function adds to the
list.

A test to check that the list function returns the
complete list of tracks.

A test to check that the list function returns a
message stating empty list if the track list is
empty.

4. Implement the Behaviour"""

from lib.music_list import *
import pytest

def test_add_to_list():
    music_list = MusicList()
    music_list.add("Track 1")
    result = music_list.list_tracks()
    assert result == ["Track 1"]

def test_list_multiple_tracks():
    music_list = MusicList()
    music_list.add("Track 1")
    music_list.add("Track 2")
    music_list.add("Track 3")
    result = music_list.list_tracks()
    assert result == ["Track 1","Track 2","Track 3"]    

def test_list_track_for_empty_list():
    music_list = MusicList()
    result = music_list.list_tracks()
    assert result == "Track list is empty!"    
