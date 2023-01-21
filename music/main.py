import tkinter as tk
import os
from playsound import playsound
from helpers import ordered, unordered, shuffle_

music_list = os.listdir('musics')

def playMusic(list):
    print(list)
    for m in list:
        print(m)
        playsound(f'E:\\Brijesh gondaliay\\JBSPython\\music\\musics\\{m}')


print(
"""
Press 1 : for play music in ordered  
Press 2 : for play music in un-ordered
Press 3 : for play music in shuffle way
"""
)
musicEvent = int(input("Press number: " ))

if musicEvent == 1:
    print(ordered.__doc__)
    playMusic(ordered(music_list))
elif musicEvent == 2:
    print(unordered.__doc__)
    playMusic(unordered(music_list))
elif musicEvent == 3:
    print(shuffle_.__doc__)
    playMusic(shuffle_(music_list))
else:
    print("Invalid input, Please press number 1 or 2 or 3 only")
    
print(musicEvent)
        
# playMusic(shuffle_(music_list))





# screen = tk.Tk()

# screen.title("JBSMusic")

# screen.geometry('400x400')

# screen.mainloop()