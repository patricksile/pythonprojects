#Project I: Take a Music Break 

"""
Do you know a friend who works too many hours? We will write a program that schedules breaks throughout
the day -- reminding your friend to listen to his favorite music in the web browser, get up and dance to 
it or just walk away from the computer if he wants to, then go back to work when his favorite music finishes to play.

"""

import webbrowser, time

def music_break(break_duration, nb_breaks, music_url):

    counter = 0
    while counter < nb_breaks:
        webbrowser.open(music_url)
        time.sleep(break_duration)
        counter += 1


# Test Zone

music_break(25, 3, "https://www.youtube.com/watch?v=zOWJqNPeifU")
    

