#Project I: Take a Music Break 

"""
Do you know a friend who works too many hours? We will write a program that schedules breaks throughout
the day -- reminding your friend to listen to his favorite music in the web browser, get up and dance to 
it or just walk away from the computer if he wants to, then go back to work when his favorite music finishes to play.

"""

# def music_break(break_duration, number_of_breaks):
#     pass

import webbrowser, time

def music_break(nb_breaks, break_duration, music_url):
    
    counter = 0 # Initializing counter
    while counter < nb_breaks:
        webbrowser.open(music_url)
        time.sleep(break_duration) # Delaying my code for some seconds
        counter += 1 
    

# Test Zone

music_break(3, 25, "https://www.youtube.com/watch?v=zOWJqNPeifU")