import tkinter as tk
import pygame

story_data = {
    "display":{
        "text" : "HEY!, I AM ALICE AND I WILL BE WATCHING YOU THROUGH OUT THE GAME.\nYOUR CHOICES IN GAME WILL HELP ME TO KNOW ABOUT YOUR PERSONALITY",
        "CHOICE" : {
            "ADVANCE" : "start"
        }
    },
    "start":{
        "text" : "YOUR ARE ST3012, NICKNAMED AS CONNER, ONE OF THE MOST ADVANCE DETROIT MADE CYBERLIFE. YOUR ARE PROGRAMMED TO SOLVE COMPLEX CASE.\nYou are assigned a case of detroit who assaulted the the owner and ran away with his daughter.\n   REMEMBER:-THE CHOICES YOU MAKE WILL DECIDE THE FUTURE",
        "CHOICE" : {"PLAY" : "house"}
    },
    "house" :{
        "text" : "YOU ARE AT THE CRIME SCENE, WHAT DO WANT TO DO?",
        "CHOICE" : {
            "INVESTIGATE THE CRIME SCENE" : "investigate",
            "TALK TO HANK" : "hank"
        }
    },
    "investigate" : {
        "text" : "INVESTIGATE THE CRIME SCENE AND DEAD BODY AND FIND THE GIRL",
        "CHOICE" : {
            "SCAN THE PHOTO" : "scan",
            "CHECK THE DEADY body" : "dead",
            "SCAN THE WALL" : "wall"
        }
    },
    "hank" : {
        "text" : "HANK TELL ABOUT THE NUMBER OF INCREASE IN CASES SIMILAR TO THIS",
        "CHOICE" : {
            "ASK ABOUT DETROIT" : "detroit",
            "COMMON THING IN ALL CASES" : "common"
        }
    }
}
def update_story(scene):
    story = story_data[scene]
    story_text.set(story["text"])

    if scene == "house":
        play_audio()

    for widget in choice_button_frame.winfo_children():
        widget.destroy()

    for choice_text, next_scene in story["CHOICE"].items():
        choice_button = tk.Button(
            choice_button_frame, 
            text=choice_text, 
            command=lambda next_scene=next_scene: update_story(next_scene),
            bg="black",       
            fg="white",     
            activebackground="gray",  
            activeforeground="yellow",
            font=("Arial", 12, "bold"), 
            relief="raised"   
        )
        choice_button.pack(pady=5) 

#background audio
def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("risk.mp3") 
    pygame.mixer.music.set_volume(0.5)  
    pygame.mixer.music.play(-1, 0.0) 


conner = tk.Tk()
conner.title("DETROIT: JUST A MACHINE?")

story_text = tk.StringVar()
story_label = tk.Label(conner, textvariable=story_text, wraplength=400)
story_label.pack(pady=20)

# Frame for choice buttons
choice_button_frame = tk.Frame(conner)
choice_button_frame.pack(pady=20)

# Start the game
update_story("display")

conner.mainloop()
