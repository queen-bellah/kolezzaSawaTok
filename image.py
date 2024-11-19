# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import random
# import time

# # Initialize the main window
# root = tk.Tk()
# root.title("Game Level Selection")
# root.geometry("800x600")  # Set the window size
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Lock to prevent speech overlap
# voice_lock = threading.Lock()

# # List of image paths and their corresponding texts (20 images)
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"},
#     {"image_path": "owl.jpg", "text": "This is an owl"},
#     {"image_path": "bus(1).jpg", "text": "This is a bus"},
#     {"image_path": "bowl.jpg", "text": "This is a banana"},
#     {"image_path": "bell.jpg", "text": "This is a bell"},
#     {"image_path": "ball.jpg", "text": "This is a ball"},
#     {"image_path": "crocodile.jpg", "text": "This is a crocodile"},
#     {"image_path": "whiteduck.jpg", "text": "This is a white duck"},
#     {"image_path": "turtle.jpg", "text": "This is a turtle"},
#     {"image_path": "butterfly.jpg", "text": "This is a butterfly"},
#     {"image_path": "books.jpg", "text": "These are books"},
#     {"image_path": "duck.jpg", "text": "This is a duck"},
#     {"image_path": "bat.jpg", "text": "This is a bat"},
#     {"image_path": "monkey.jpg", "text": "This is a monkey"},
#     {"image_path": "zebra.jpg", "text": "This is a zebra"},
#     {"image_path": "fox.jpg", "text": "This is a fox"},
#     {"image_path": "boat.jpg", "text": "This is a boat"}
# ]

# # Variable to keep track of the current image index
# current_index = 0

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     with voice_lock:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     import simpleaudio as sa
#     wave_obj = sa.WaveObject.from_wave_file(filename)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()

# # Function to resize the image while maintaining aspect ratio
# def resize_image(image, max_width, max_height):
#     img_width, img_height = image.size
#     ratio = min(max_width / img_width, max_height / img_height)
#     new_width = int(img_width * ratio)
#     new_height = int(img_height * ratio)
#     return image.resize((new_width, new_height), Image.ANTIALIAS)

# # Function to update the displayed image and text
# def update_image():
#     global current_index
#     image_path = images_data[current_index]["image_path"]
#     instruction_text = images_data[current_index]["text"]
    
#     # Load and display the image
#     image = Image.open(image_path)
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
    
#     # Resize the image to fit the screen while maintaining the aspect ratio
#     image = resize_image(image, screen_width, screen_height)
#     photo = ImageTk.PhotoImage(image)
#     image_label.config(image=photo)
#     image_label.image = photo  # Keep a reference to avoid garbage collection

#     text_label.config(text=instruction_text)
#     text_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

#     # Delay the speech to ensure the image is displayed first
#     root.after(500, lambda: threading.Thread(target=speak_text, args=(instruction_text,)).start())

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Function to go to the previous image
# def previous_image():
#     global current_index
#     if current_index > 0:
#         current_index -= 1
#     else:
#         current_index = len(images_data) - 1  # Loop back to the last image
#     update_image()

# # Function to switch from game level screen to main image display
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()  # Clear the current screen

#     # Create a label to display the image
#     global image_label
#     image_label = tk.Label(root)
#     image_label.pack(fill=tk.BOTH, expand=True)

#     # Create a label for the instruction text (overlay on image)
#     global text_label
#     text_label = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="black")

#     # Create Previous and Next buttons
#     prev_button = tk.Button(root, text="Previous", font=("Arial", 14), bg="blue", fg="white", width=10, command=previous_image)
#     prev_button.place(relx=0.05, rely=0.9)  # Positioned at the left bottom corner

#     next_button = tk.Button(root, text="Next", font=("Arial", 14), bg="green", fg="white", width=10, command=next_image)
#     next_button.place(relx=0.85, rely=0.9)  # Positioned at the right bottom corner

#     # Initialize by showing the first image
#     update_image()

# # Function to create the game level selection screen
# def game_levels_screen():
#     # Title label
#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     # Create a frame for the game levels
#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Image and button for Easy level
#     easy_img = Image.open("smileydog.jpg")  # Replace with your image path
#     easy_img = easy_img.resize((150, 150), Image.ANTIALIAS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0)

#     easy_text = tk.Label(level_frame, text="Easy", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

#     # Image and button for Medium level (Locked)
#     medium_img = Image.open("boy1.png")  # Replace with your image path
#     medium_img = medium_img.resize((150, 150), Image.ANTIALIAS)
#     medium_photo = ImageTk.PhotoImage(medium_img)

#     medium_label = tk.Label(level_frame, image=medium_photo, bg="white")
#     medium_label.image = medium_photo
#     medium_label.grid(row=0, column=1, padx=30)

#     medium_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     medium_button.grid(row=1, column=1)

#     medium_text = tk.Label(level_frame, text="Medium", font=("Arial", 14), bg="white")
#     medium_text.grid(row=2, column=1, pady=10)

#     # Image and button for Hard level (Locked)
#     hard_img = Image.open("boy1.png")  # Replace with your image path
#     hard_img = hard_img.resize((150, 150), Image.ANTIALIAS)
#     hard_photo = ImageTk.PhotoImage(hard_img)

#     hard_label = tk.Label(level_frame, image=hard_photo, bg="white")
#     hard_label.image = hard_photo
#     hard_label.grid(row=0, column=2, padx=30)

#     hard_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     hard_button.grid(row=1, column=2)

#     hard_text = tk.Label(level_frame, text="Hard", font=("Arial", 14), bg="white")
#     hard_text.grid(row=2, column=2, pady=10)

# # Create a loading screen with a background image and progress bar
# def loading_screen():
#     # Load and display the background image for the loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with your background image path
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
#     bg_photo = ImageTk.PhotoImage(bg_image)
    
#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set the image to cover the full screen

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     # Create the progress bar
#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.1)  # Simulate loading time

#         # Remove loading screen elements
#         load_label.destroy()
#         progress_bar.destroy()
#         bg_label.destroy()

#         # Show the level selection screen
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter event loop
# root.mainloop()


# import tkinter as tk
# # from PIL import Image, ImageTk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import random
# import time
# import simpleaudio as sa

# # Initialize the main window
# root = tk.Tk()
# root.title("Game Level Selection")
# root.geometry("800x600")  # Set the window size
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Lock to prevent speech overlap
# voice_lock = threading.Lock()

# # List of image paths and their corresponding texts (20 images)
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"},
#     {"image_path": "owl.jpg", "text": "This is an owl"},
#     {"image_path": "bus(1).jpg", "text": "This is a bus"},
#     {"image_path": "bowl.jpg", "text": "This is a banana"},
#     {"image_path": "bell.jpg", "text": "This is a bell"},
#     {"image_path": "ball.jpg", "text": "This is a ball"},
#     {"image_path": "crocodile.jpg", "text": "This is a crocodile"},
#     {"image_path": "whiteduck.jpg", "text": "This is a white duck"},
#     {"image_path": "turtle.jpg", "text": "This is a turtle"},
#     {"image_path": "butterfly.jpg", "text": "This is a butterfly"},
#     {"image_path": "books.jpg", "text": "These are books"},
#     {"image_path": "duck.jpg", "text": "This is a duck"},
#     {"image_path": "bat.jpg", "text": "This is a bat"},
#     {"image_path": "monkey.jpg", "text": "This is a monkey"},
#     {"image_path": "zebra.jpg", "text": "This is a zebra"},
#     {"image_path": "fox.jpg", "text": "This is a fox"},
#     {"image_path": "boat.jpg", "text": "This is a boat"}
# ]

# # Variable to keep track of the current image index
# current_index = 0

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     with voice_lock:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     wave_obj = sa.WaveObject.from_wave_file(filename)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()

# # Function to resize the image while maintaining aspect ratio
# def resize_image(image, max_width, max_height):
#     img_width, img_height = image.size
#     ratio = min(max_width / img_width, max_height / img_height)
#     new_width = int(img_width * ratio)
#     new_height = int(img_height * ratio)
#     return image.resize((new_width, new_height), Image.LANCZOS)

# # Function to update the displayed image and text
# def update_image():
#     global current_index
#     image_path = images_data[current_index]["image_path"]
#     instruction_text = images_data[current_index]["text"]
    
#     # Load and display the image
#     image = Image.open(image_path)
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
    
#     # Resize the image to fit the screen while maintaining the aspect ratio
#     image = resize_image(image, screen_width, screen_height)
#     photo = ImageTk.PhotoImage(image)
#     image_label.config(image=photo)
#     image_label.image = photo  # Keep a reference to avoid garbage collection

#     text_label.config(text=instruction_text)
#     text_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

#     # Delay the speech to ensure the image is displayed first
#     root.after(500, lambda: threading.Thread(target=speak_text, args=(instruction_text,)).start())

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Function to go to the previous image
# def previous_image():
#     global current_index
#     if current_index > 0:
#         current_index -= 1
#     else:
#         current_index = len(images_data) - 1  # Loop back to the last image
#     update_image()

# # Function to switch from game level screen to main image display
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()  # Clear the current screen

#     # Create a label to display the image
#     global image_label
#     image_label = tk.Label(root)
#     image_label.pack(fill=tk.BOTH, expand=True)

#     # Create a label for the instruction text (overlay on image)
#     global text_label
#     text_label = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="black")

#     # Create Previous and Next buttons
#     prev_button = tk.Button(root, text="Previous", font=("Arial", 14), bg="blue", fg="white", width=10, command=previous_image)
#     prev_button.place(relx=0.05, rely=0.9)  # Positioned at the left bottom corner

#     next_button = tk.Button(root, text="Next", font=("Arial", 14), bg="green", fg="white", width=10, command=next_image)
#     next_button.place(relx=0.85, rely=0.9)  # Positioned at the right bottom corner

#     # Initialize by showing the first image
#     update_image()

# # Function to create the game level selection screen
# def game_levels_screen():
#     # Title label
#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     # Create a frame for the game levels
#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Image and button for Easy level
#     easy_img = Image.open("smileydog.jpg")  # Replace with your image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0)

#     easy_text = tk.Label(level_frame, text="Easy", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

#     # Image and button for Medium level (Locked)
#     medium_img = Image.open("boy1.png")  # Replace with your image path
#     medium_img = medium_img.resize((150, 150), Image.LANCZOS)
#     medium_photo = ImageTk.PhotoImage(medium_img)

#     medium_label = tk.Label(level_frame, image=medium_photo, bg="white")
#     medium_label.image = medium_photo
#     medium_label.grid(row=0, column=1, padx=30)

#     medium_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     medium_button.grid(row=1, column=1)

#     medium_text = tk.Label(level_frame, text="Medium", font=("Arial", 14), bg="white")
#     medium_text.grid(row=2, column=1, pady=10)

#     # Image and button for Hard level (Locked)
#     hard_img = Image.open("boy1.png")  # Replace with your image path
#     hard_img = hard_img.resize((150, 150), Image.LANCZOS)
#     hard_photo = ImageTk.PhotoImage(hard_img)

#     hard_label = tk.Label(level_frame, image=hard_photo, bg="white")
#     hard_label.image = hard_photo
#     hard_label.grid(row=0, column=2, padx=30)

#     hard_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     hard_button.grid(row=1, column=2)

#     hard_text = tk.Label(level_frame, text="Hard", font=("Arial", 14), bg="white")
#     hard_text.grid(row=2, column=2, pady=10)

# # Create a loading screen with a background image and progress bar
# def loading_screen():
#     # Load and display the background image for the loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with your background image path
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)
    
#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set the image to cover the full screen

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     # Create the progress bar
#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.1)  # Simulate loading time

#         # Remove loading screen elements
#         load_label.destroy()
#         progress_bar.destroy()
#         bg_label.destroy()

#         # Show the level selection screen
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter event loop
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.effects import normalize, low_pass_filter
# import io

# # Initialize the main window
# root = tk.Tk()
# root.title("Game Level Selection")
# root.geometry("800x600")  # Set the window size
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Lock to prevent speech overlap
# voice_lock = threading.Lock()

# # Initialize speech recognizer
# recognizer = sr.Recognizer()
# mic = sr.Microphone()

# # List of image paths and their corresponding texts (20 images)
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"},
#     {"image_path": "owl.jpg", "text": "This is an owl"},
#     {"image_path": "bus(1).jpg", "text": "This is a bus"},
#     {"image_path": "bowl.jpg", "text": "This is a banana"},
#     {"image_path": "bell.jpg", "text": "This is a bell"},
#     {"image_path": "ball.jpg", "text": "This is a ball"},
#     {"image_path": "crocodile.jpg", "text": "This is a crocodile"},
#     {"image_path": "whiteduck.jpg", "text": "This is a white duck"},
#     {"image_path": "turtle.jpg", "text": "This is a turtle"},
#     {"image_path": "butterfly.jpg", "text": "This is a butterfly"},
#     {"image_path": "books.jpg", "text": "These are books"},
#     {"image_path": "duck.jpg", "text": "This is a duck"},
#     {"image_path": "bat.jpg", "text": "This is a bat"},
#     {"image_path": "monkey.jpg", "text": "This is a monkey"},
#     {"image_path": "zebra.jpg", "text": "This is a zebra"},
#     {"image_path": "fox.jpg", "text": "This is a fox"},
#     {"image_path": "boat.jpg", "text": "This is a boat"}
# ]

# # Variable to keep track of the current image index
# current_index = 0
# best_time = float('inf')

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     with voice_lock:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     wave_obj = sa.WaveObject.from_wave_file(filename)
#     play_obj = wave_obj.play()
#     play_obj.wait_done()

# # Function to resize the image while maintaining aspect ratio
# def resize_image(image, max_width, max_height):
#     img_width, img_height = image.size
#     ratio = min(max_width / img_width, max_height / img_height)
#     new_width = int(img_width * ratio)
#     new_height = int(img_height * ratio)
#     return image.resize((new_width, new_height), Image.LANCZOS)

# # Function to reduce noise and smooth the child's voice
# def process_audio_for_smoothing(audio_data):
#     # Convert the audio to an AudioSegment
#     audio_segment = AudioSegment(
#         data=audio_data.get_wav_data(),
#         sample_width=2,
#         frame_rate=audio_data.sample_rate,
#         channels=1
#     )

#     # Apply noise reduction and smoothing techniques
#     audio_segment = normalize(audio_segment)  # Normalize the volume
#     audio_segment = low_pass_filter(audio_segment, cutoff=3000)  # Low pass filter for smoother voice

#     # Convert back to byte data
#     byte_io = io.BytesIO()
#     audio_segment.export(byte_io, format="wav")
#     return byte_io.getvalue()

# # Function to listen for the child’s speech and time the response
# def listen_for_response(prompt, target_text):
#     global best_time
#     print(prompt)
#     speak_text(prompt)

#     with mic as source:
#         recognizer.adjust_for_ambient_noise(source)
#         start_time = time.time()
#         print("Listening...")
#         audio = recognizer.listen(source, timeout=60)  # Listen for 60 seconds max

#     try:
#         print("Processing audio for noise reduction and smoothing...")
#         # Process the audio for noise reduction and smoothing
#         processed_audio = sr.AudioData(process_audio_for_smoothing(audio), audio.sample_rate, audio.sample_width)

#         print("Recognizing...")
#         speech_text = recognizer.recognize_google(processed_audio)
#         print(f"Child said: {speech_text}")
        
#         # Check if the child's response matches the expected text
#         if target_text.lower() in speech_text.lower():
#             elapsed_time = time.time() - start_time
#             print(f"Time taken: {elapsed_time:.2f} seconds")
            
#             # Check if the child improved their time
#             if elapsed_time < best_time and 40 <= elapsed_time <= 60:
#                 best_time = elapsed_time
#                 print("Improved! Moving to the next image.")
#                 next_image()
#             else:
#                 print("Try again!")
#         else:
#             print("Response doesn't match. Try again!")

#     except sr.UnknownValueError:
#         print("Sorry, I couldn't understand that. Please try again.")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")

# # Function to update the displayed image and text
# def update_image():
#     global current_index
#     image_path = images_data[current_index]["image_path"]
#     instruction_text = images_data[current_index]["text"]
    
#     # Load and display the image
#     image = Image.open(image_path)
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
    
#     # Resize the image to fit the screen while maintaining the aspect ratio
#     image = resize_image(image, screen_width, screen_height)
#     photo = ImageTk.PhotoImage(image)
#     image_label.config(image=photo)
#     image_label.image = photo  # Keep a reference to avoid garbage collection

#     text_label.config(text=instruction_text)
#     text_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

#     # Speak the instruction and prompt for repetition
#     root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

# # Function to handle speaking and listening interaction
# def handle_speech_interaction(instruction_text):
#     speak_text(instruction_text)
#     time.sleep(1)  # Pause before prompting the child
#     listen_for_response("Repeat after me.", instruction_text)

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Function to go to the previous image
# def previous_image():
#     global current_index
#     if current_index > 0:
#         current_index -= 1
#     else:
#         current_index = len(images_data) - 1  # Loop back to the last image
#     update_image()

# # Function to switch from game level screen to main image display
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()  # Clear the current screen

#     # Create a label to display the image
#     global image_label
#     image_label = tk.Label(root)
#     image_label.pack(fill=tk.BOTH, expand=True)

#     # Create a label for the instruction text (overlay on image)
#     global text_label
#     text_label = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="black")

#     # Create Previous and Next buttons
#     prev_button = tk.Button(root, text="Previous", font=("Arial", 14), bg="blue", fg="white", width=10, command=previous_image)
#     prev_button.place(relx=0.05, rely=0.9)  # Positioned at the left bottom corner

#     next_button = tk.Button(root, text="Next", font=("Arial", 14), bg="green", fg="white", width=10, command=next_image)
#     next_button.place(relx=0.85, rely=0.9)  # Positioned at the right bottom corner

#     # Initialize by showing the first image
#     update_image()

# # Function to create the game level selection screen
# def game_levels_screen():
#     # Title label
#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     # Create a frame for the game levels
#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level
#     easy_img = Image.open("smileydog.jpg")
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0)

#     easy_text = tk.Label(level_frame, text="Easy", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

#     # Medium level
#     medium_img = Image.open("boy1.png")
#     medium_img = medium_img.resize((150, 150), Image.LANCZOS)
#     medium_photo = ImageTk.PhotoImage(medium_img)

#     medium_label = tk.Label(level_frame, image=medium_photo, bg="white")
#     medium_label.image = medium_photo
#     medium_label.grid(row=0, column=1, padx=30)

#     medium_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     medium_button.grid(row=1, column=1)

#     medium_text = tk.Label(level_frame, text="Medium", font=("Arial", 14), bg="white")
#     medium_text.grid(row=2, column=1, pady=10)

#     # Hard level
#     hard_img = Image.open("boy1.png")
#     hard_img = hard_img.resize((150, 150), Image.LANCZOS)
#     hard_photo = ImageTk.PhotoImage(hard_img)

#     hard_label = tk.Label(level_frame, image=hard_photo, bg="white")
#     hard_label.image = hard_photo
#     hard_label.grid(row=0, column=2, padx=30)

#     hard_button = tk.Button(level_frame, text="Locked", state="disabled", bg="gray", fg="white", font=("Arial", 12))
#     hard_button.grid(row=1, column=2)

#     hard_text = tk.Label(level_frame, text="Hard", font=("Arial", 14), bg="white")
#     hard_text.grid(row=2, column=2, pady=10)

# # Create a loading screen with a background image and progress bar
# def loading_screen():
#     # Load and display the background image for the loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with your background image path
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)
    
#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Set the image to cover the full screen

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     # Create the progress bar
#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.1)  # Simulate loading time

#         # Remove loading screen elements
#         load_label.destroy()
#         progress_bar.destroy()
#         bg_label.destroy()

#         # Show the level selection screen
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter event loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import speech_recognition as sr

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.geometry("800x600")
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Variables for tracking current image and recording
# current_index = 0
# audio_data = []
# start_time = 0

# # Dynamic feedback messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     tts.tts_to_file(text=text, file_path="tts_output.wav")
#     play_audio("tts_output.wav")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()  # Start playing the audio
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Function to resize the image while maintaining aspect ratio
# def resize_image(image, max_width, max_height):
#     img_width, img_height = image.size
#     ratio = min(max_width / img_width, max_height / img_height)
#     return image.resize((int(img_width * ratio), int(img_height * ratio)), Image.LANCZOS)

# # Function to update the displayed image and text
# def update_image():
#     global current_index
#     image_path = images_data[current_index]["image_path"]
#     instruction_text = images_data[current_index]["text"]

#     # Load and display the image
#     image = Image.open(image_path)
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     image = resize_image(image, screen_width, screen_height)
#     photo = ImageTk.PhotoImage(image)
#     image_label.config(image=photo)
#     image_label.image = photo

#     text_label.config(text=instruction_text)
#     text_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

#     # Start TTS and automatic recording after a short delay
#     root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     speak_text(instruction_text)
#     time.sleep(1)  # Pause before starting the recording
#     start_recording()

# # Function to start recording
# def start_recording():
#     global start_time, audio_data
#     start_time = time.time()  # Initialize start time
#     audio_data = []  # Clear previous data

#     try:
#         fs = 44100  # Sample rate
#         duration = 10  # Max recording duration (for safety, not fixed to 40s)
#         print("Recording... Speak now!")

#         # Start recording
#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()  # Wait until recording is finished or stopped

#         elapsed_time = time.time() - start_time  # Measure elapsed time
#         analyze_speech(elapsed_time)

#     except Exception as e:
#         print(f"Recording error: {e}")
#         feedback_label.config(text="Error in recording, please try again.")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         feedback_label.config(text=f"{feedback}\nYou took {elapsed_time:.2f} seconds.")
#         speak_text(feedback)  # Speak the success message using TTS
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         feedback_label.config(text=f"{feedback}\nYou took {elapsed_time:.2f} seconds.")
#         speak_text(feedback)  # Speak the retry message using TTS
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Initialize the main screen
# image_label = tk.Label(root)
# image_label.pack(fill=tk.BOTH, expand=True)

# text_label = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="black")
# feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
# feedback_label.pack(pady=10)

# # Start by showing the first image
# update_image()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((600, 400), Image.LANCZOS)  # Adjust size for fullscreen display
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction after a short delay
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         root.after(0, lambda: analyze_speech(elapsed_time))

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)  # Make images bigger
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((800, 500), Image.LANCZOS)  # Make images bigger
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction after a short delay
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         root.after(0, lambda: analyze_speech(elapsed_time))

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to create multiple star pop-up effects
# def animate_star_effect():
#     for _ in range(30):  # Create 30 stars
#         x_pos = random.uniform(0.1, 0.9)
#         y_pos = random.uniform(0.1, 0.9)
#         star_label = tk.Label(root, text="★", font=("Arial", 24), fg="gold", bg="white")
#         star_label.place(relx=x_pos, rely=y_pos, anchor="center")

#         # Animate star fading away
#         def fade_star(star_label):
#             for size in range(24, 1, -1):
#                 star_label.config(font=("Arial", size))
#                 root.update_idletasks()
#                 time.sleep(0.03)
#             star_label.destroy()

#         threading.Thread(target=fade_star, args=(star_label,), daemon=True).start()

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         threading.Thread(target=animate_star_effect).start()  # Show multiple stars pop-up effect
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)  # Make images bigger
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((800, 500), Image.LANCZOS)  # Make images bigger
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction after a short delay
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         root.after(0, lambda: analyze_speech(elapsed_time))

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to create multiple star pop-up effects
# def animate_star_effect():
#     for _ in range(50):  # Create 50 stars
#         x_pos = random.uniform(0.1, 0.9)
#         y_pos = random.uniform(0.1, 0.9)
#         star_label = tk.Label(root, text="★", font=("Arial", 24), fg="gold", bg="white")
#         star_label.place(relx=x_pos, rely=y_pos, anchor="center")

#         # Animate star staying for 2 seconds before fading
#         def fade_star(star_label):
#             time.sleep(2)  # Star stays for 2 seconds
#             for size in range(24, 1, -1):
#                 star_label.config(font=("Arial", size))
#                 root.update_idletasks()
#                 time.sleep(0.03)
#             star_label.destroy()

#         threading.Thread(target=fade_star, args=(star_label,), daemon=True).start()

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         threading.Thread(target=animate_star_effect).start()  # Show multiple stars pop-up effect
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.240:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws: print("WebSocket connection closed"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned
#         }
#         send_data_to_websocket(progress_data)

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         threading.Thread(target=animate_star_effect).start()
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json
# import os

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.240:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws, code, msg: print(f"WebSocket connection closed: {code}, {msg}"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#             print(f"Data sent to WebSocket: {data}")
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     # {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Check if all images are available
# def check_images():
#     for image_data in images_data:
#         if not os.path.exists(image_data["image_path"]):
#             print(f"Image not found: {image_data['image_path']}")
#             return False
#     return True

# if not check_images():
#     print("Please ensure all image files are present in the directory.")
#     exit()

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = "boy.jpg"  # Replace with the correct path if needed
#     if os.path.exists(bg_image):
#         image = Image.open(bg_image)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)

#         bg_label = tk.Label(root, image=photo)
#         bg_label.image = photo
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#     else:
#         print(f"Background image not found: {bg_image}")

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         if os.path.exists(level["image"]):
#             img = Image.open(level["image"])
#             img = img.resize((200, 200), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(img)

#             level_label = tk.Label(level_frame, image=photo, bg="white")
#             level_label.image = photo
#             level_label.grid(row=0, column=index, padx=20, pady=10)

#             level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                      bg="green", fg="white", font=("Arial", 14))
#             level_button.grid(row=1, column=index, pady=10)
#         else:
#             print(f"Level image not found: {level['image']}")

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json
# import os

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.240:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws: print("WebSocket connection closed"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         try:
#             # Check if the image file exists
#             if os.path.exists(level["image"]):
#                 img = Image.open(level["image"])
#                 img = img.resize((200, 200), Image.LANCZOS)
#                 photo = ImageTk.PhotoImage(img)

#                 level_label = tk.Label(level_frame, image=photo, bg="white")
#                 level_label.image = photo
#                 level_label.grid(row=0, column=index, padx=20, pady=10)

#                 level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                          bg="green", fg="white", font=("Arial", 14))
#                 level_button.grid(row=1, column=index, pady=10)
#             else:
#                 print(f"Image not found: {level['image']}")
#                 level_button = tk.Button(level_frame, text=f"{level['name']} (No Image)",
#                                          command=level["command"], bg="red", fg="white", font=("Arial", 14))
#                 level_button.grid(row=1, column=index, padx=20, pady=10)

#         except Exception as e:
#             print(f"Error loading level image: {e}")

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned
#         }
#         send_data_to_websocket(progress_data)

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         threading.Thread(target=animate_star_effect).start()
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to create multiple star pop-up effects
# def animate_star_effect():
#     for _ in range(50):  # Create 50 stars
#         x_pos = random.uniform(0.1, 0.9)
#         y_pos = random.uniform(0.1, 0.9)
#         star_label = tk.Label(root, text="★", font=("Arial", 24), fg="gold", bg="white")
#         star_label.place(relx=x_pos, rely=y_pos, anchor="center")

#         def fade_star(star_label):
#             time.sleep(2)  # Star stays for 2 seconds
#             for size in range(24, 1, -1):
#                 star_label.config(font=("Arial", size))
#                 root.update_idletasks()
#                 time.sleep(0.03)
#             star_label.destroy()

#         threading.Thread(target=fade_star, args=(star_label,), daemon=True).start()

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json
# import os

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.240:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws: print("WebSocket connection closed"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img_path = level["image"]
#         if os.path.exists(img_path):
#             img = Image.open(img_path)
#             img = img.resize((200, 200), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(img)

#             level_label = tk.Label(level_frame, image=photo, bg="white")
#             level_label.image = photo
#             level_label.grid(row=0, column=index, padx=20, pady=10)

#             level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                      bg="green", fg="white", font=("Arial", 14))
#             level_button.grid(row=1, column=index, pady=10)
#         else:
#             print(f"Image not found: {img_path}")
#             tk.Label(level_frame, text=f"{level['name']} (No Image)", bg="red", fg="white", font=("Arial", 14)).grid(row=1, column=index)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned
#         }
#         send_data_to_websocket(progress_data)

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         threading.Thread(target=animate_star_effect).start()
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.77:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws: print("WebSocket connection closed"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned
#         }
#         send_data_to_websocket(progress_data)

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         threading.Thread(target=animate_star_effect).start()
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.77:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws: print("WebSocket connection closed"),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=lambda ws, message: print(f"Received message: {message}")
#     )
#     ws.run_forever()

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#             print(f"Data sent to WebSocket: {data}")
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = duration
#         print(f"Elapsed Time: {elapsed_time} seconds")

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_websocket(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, update_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.77:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws, close_status_code, close_msg: print("WebSocket connection closed:", close_msg),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=handle_websocket_message
#     )
#     ws.run_forever()

# # WebSocket message handler
# def handle_websocket_message(ws, message):
#     print(f"Received message: {message}")

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#             print("Data sent to WebSocket:", data)
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = random.uniform(1.5, 4.5)  # Simulate a realistic elapsed time

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_websocket(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()
import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import websocket
# import json

# # WebSocket Server URL
# WS_SERVER_URL = "ws://192.168.100.77:8765"

# # Global WebSocket variable
# ws = None

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize WebSocket connection
# def start_websocket():
#     global ws
#     ws = websocket.WebSocketApp(
#         WS_SERVER_URL,
#         on_open=lambda ws: print("WebSocket connection opened"),
#         on_close=lambda ws, close_status_code, close_msg: print("WebSocket connection closed:", close_msg),
#         on_error=lambda ws, error: print(f"WebSocket error: {error}"),
#         on_message=handle_websocket_message
#     )
#     ws.run_forever()

# # WebSocket message handler
# def handle_websocket_message(ws, message):
#     print(f"Received message: {message}")

# # Start the WebSocket connection in a separate thread
# def run_websocket():
#     threading.Thread(target=start_websocket, daemon=True).start()

# # Check if WebSocket is open before sending data
# def send_data_to_websocket(data):
#     global ws
#     try:
#         if ws and ws.sock and ws.sock.connected:
#             ws.send(json.dumps(data))
#             print("Data sent to WebSocket:", data)
#         else:
#             print("WebSocket connection is not open")
#     except Exception as e:
#         print(f"Error sending data to WebSocket: {e}")

# # Start the WebSocket connection
# run_websocket()

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = random.uniform(1.5, 4.5)  # Simulate a realistic elapsed time

#         # Send progress data to WebSocket
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_websocket(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()




# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import json

# # HTTP Server URL (Fixed IP for the laptop with the dashboard)
# SERVER_URL = "http://192.168.100.54:8000/update"  # Adjust with the correct port and path

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.01)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = random.uniform(1.5, 4.5)  # Simulate a realistic elapsed time

#         # Send progress data to HTTP server
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_server(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to send data to HTTP server
# def send_data_to_server(data):
#     try:
#         response = requests.post(SERVER_URL, json=data)
#         if response.status_code == 200:
#             print("Data sent to server:", data)
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending data: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()



# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import json

# # ThingsBoard server URL and access token
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "UDHxTegz8gMhVdfwjgzF"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.3)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = random.uniform(1.5, 4.5)  # Simulate a realistic elapsed time

#         # Send progress data to ThingsBoard
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_thingsboard(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to send data to ThingsBoard
# def send_data_to_thingsboard(data):
#     try:
#         headers = {"Content-Type": "application/json"}
#         response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#         if response.status_code == 200:
#             print("Data sent to ThingsBoard:", data)
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending data to ThingsBoard: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "fox.jpg", "text": "This is a fox"},
#     {"image_path": "bag (1).jpg", "text": "This is a fox"},
    
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((600, 400), Image.LANCZOS)  # Adjust size for fullscreen display
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction after a short delay
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         elapsed_time = 3.5  # Mock elapsed time for testing
#         root.after(0, lambda: analyze_speech(elapsed_time))

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "soccer_player_dribbling_gif (800×600).gif", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((600, 400), Image.LANCZOS)  # Adjust size for fullscreen display
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction after a short delay
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         elapsed_time = duration  # Mock elapsed time for testing
#         analyze_speech(elapsed_time)  # Pass elapsed_time for analysis

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter
# gif_frames = None
# current_frame = 0

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "celebration1.gif", "text": "Yay keep it up"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "clapping.gif", "text": "Amazing"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 5:  # Check if 5 seconds have passed
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         # After 5 seconds, proceed with speech interaction
#         root.after(0, lambda: threading.Thread(target=handle_speech_interaction, args=(images_data[current_index]["text"],)).start())

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             # Handle GIF
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 update_gif(start_time)
#         else:
#             # Handle static image
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             # Start TTS and speech interaction after a short delay
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         elapsed_time = duration  # Mock elapsed time for testing
#         analyze_speech(elapsed_time)  # Pass elapsed_time for analysis

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter
# gif_frames = None
# current_frame = 0

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "/home/kolezza/SawaTok/all.jpg", "text": "This is a ball"},
#     {"image_path": "/home/kolezza/SawaTok/cat.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "/home/kolezza/SawaTok/bag.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/bed.jpg", "text": "This is a bed"},
#     {"image_path": "/home/kolezza/SawaTok/clapping.gif", "text": "Amazing"},
#     {"image_path": "/home/kolezza/SawaTok/bell.jpg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("/home/kolezza/SawaTok/boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("/home/kolezza/SawaTok/smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="/home/kolezza/SawaTok/Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 3:  # Check if 5 seconds have passed
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         # After 5 seconds, move to next image
#         root.after(0, next_image)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             # Handle GIF
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 # For GIFs, just speak the text without interaction
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             # Handle static image
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             # Start TTS and speech interaction after a short delay
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         elapsed_time = duration  # Mock elapsed time for testing
#         analyze_speech(elapsed_time)  # Pass elapsed_time for analysis

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Global variables
# current_index = 0
# stars_earned = 0
# gif_frames = None
# current_frame = 0

# # Image data and feedback messages
# images_data = [
#     {"image_path": "/home/kolezza/SawaTok/all.jpg", "text": "This is a ball"},
#     {"image_path": "/home/kolezza/SawaTok/cat.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "/home/kolezza/SawaTok/bag.jpg", "text": "This is a bag"},
#     {"image_path": "/home/kolezza/SawaTok/bed.jpg", "text": "This is a bed"},
#     {"image_path": "/home/kolezza/SawaTok/clapping.gif", "text": "Amazing"},
#     {"image_path": "/home/kolezza/SawaTok/bell.jpg", "text": "This is a bell"}
# ]

# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You are improving!"
# ]

# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# def speak_text(text):
#     """Function to convert text to speech and play it"""
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# def play_audio(filename):
#     """Function to play audio files"""
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# def loading_screen():
#     """Display initial loading screen"""
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load background image
#     bg_image = Image.open("/home/kolezza/SawaTok/boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# def game_levels_screen():
#     """Display game level selection screen"""
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     easy_img = Image.open("/home/kolezza/SawaTok/smileydog.jpg")
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, 
#                            bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     """Update GIF animation frames"""
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 5:
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         root.after(0, next_image)

# def show_main_screen():
#     """Initialize and display the main game screen"""
#     global image_label, text_label, feedback_label, stars_label

#     for widget in root.winfo_children():
#         widget.destroy()

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# def update_image():
#     """Update the displayed image and handle GIF/static image logic"""
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             # Handle GIF
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             # Handle static image
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, 
#                                                    args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# def handle_speech_interaction(instruction_text):
#     """Handle the speech interaction flow"""
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# def start_recording():
#     """Start audio recording and handle the recording process"""
#     try:
#         fs = 44100  # Sample rate
#         duration = 10  # Recording duration in seconds
#         start_time = time.time()
#         print("Recording... Speak now!")

#         # Record audio
#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()
        
#         # Calculate actual recording duration
#         elapsed_time = time.time() - start_time

#         # Save recording to temporary file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Analyze the recording
#         analyze_speech(elapsed_time, temp_wav_file.name)

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# def analyze_speech(elapsed_time, audio_file):
#     """Analyze the recorded speech and provide feedback"""
#     global stars_earned, current_index

#     try:
#         # Initialize speech recognizer
#         recognizer = sr.Recognizer()
        
#         with sr.AudioFile(audio_file) as source:
#             audio = recognizer.record(source)
            
#             try:
#                 # Attempt to detect speech
#                 text = recognizer.recognize_google(audio)
#                 has_speech = True
#             except sr.UnknownValueError:
#                 has_speech = False
            
#             if has_speech:
#                 if elapsed_time <= 40:
#                     # Success case
#                     feedback = random.choice(success_feedbacks)
#                     stars_earned += 1
#                     stars_label.config(text=f"★ {stars_earned}")
                    
#                     def proceed_to_next():
#                         speak_text(feedback)
#                         root.after(3000, next_image)
                    
#                     root.after(0, proceed_to_next)
#                 else:
#                     # Too slow case
#                     feedback = random.choice(retry_feedbacks)
                    
#                     def retry_current():
#                         speak_text(feedback)
#                         root.after(3000, lambda: handle_speech_interaction(images_data[current_index]["text"]))
                    
#                     root.after(0, retry_current)
#             else:
#                 # No speech detected case
#                 def prompt_retry():
#                     speak_text("I couldn't hear you. Please try again.")
#                     root.after(2000, lambda: handle_speech_interaction(images_data[current_index]["text"]))
                
#                 root.after(0, prompt_retry)

#     except Exception as e:
#         print(f"Speech analysis error: {e}")
#         root.after(0, lambda: feedback_label.config(text="Error analyzing speech. Please try again."))

# def next_image():
#     """Move to the next image in the sequence"""
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0
#     update_image()

# # Start the application
# if __name__ == "__main__":
#     loading_screen()
#     root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter
# gif_frames = None
# current_frame = 0

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "/home/kolezza/SawaTok/all.jpg", "text": "This is a ball"},
#     {"image_path": "/home/kolezza/SawaTok/cat.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "/home/kolezza/SawaTok/bag.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/bed.jpg", "text": "This is a bed"},
#     {"image_path": "/home/kolezza/SawaTok/clapping.gif", "text": "Amazing"},
#     {"image_path": "/home/kolezza/SawaTok/bell.jpg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load the background image for loading screen
#     bg_image = Image.open("/home/kolezza/SawaTok/boy.jpg")  # Replace with the actual image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     # Easy level with image
#     easy_img = Image.open("/home/kolezza/SawaTok/smileydog.jpg")  # Replace with the actual image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="/home/kolezza/SawaTok/Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 3:  # Check if 5 seconds have passed
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         # After 5 seconds, move to next image
#         root.after(0, next_image)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()  # Start showing images

# # Function to update the displayed image and text
# def update_image():
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             # Handle GIF
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 # For GIFs, just speak the text without interaction
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             # Handle static image
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             # Start TTS and speech interaction after a short delay
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         elapsed_time = duration  # Mock elapsed time for testing
#         analyze_speech(elapsed_time)  # Pass elapsed_time for analysis

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)  # Speak out the feedback
#         root.after(4000, next_image)  # Move to the next image after feedback
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)  # Speak out the retry feedback
#         root.after(4000, update_image)  # Retry the same image

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0  # Loop back to the first image
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0
# gif_frames = None
# current_frame = 0

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "bag.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "clapping.gif", "text": "Amazing"},
#     {"image_path": "bell.jpg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     easy_img = Image.open("smileydog.jpg")
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 5:
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         root.after(0, next_image)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording():
#     try:
#         fs = 44100
#         duration = 5
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         elapsed_time = duration
#         analyze_speech(elapsed_time)

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time):
#     global stars_earned

#     if elapsed_time <= 12:
#         feedback = random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0
#     update_image()

# # Start with the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0
# gif_frames = None
# current_frame = 0

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "bag.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "clapping.gif", "text": "Amazing"},
#     {"image_path": "bell.jpg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     easy_img = Image.open("smileydog.jpg")
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 5:
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         root.after(0, next_image)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording
# def start_recording(expected_text):
#     try:
#         fs = 44100
#         duration = 5
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         analyze_speech(temp_wav_file.name, expected_text)
#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")

# # Function to analyze speech content and time
# def analyze_speech(audio_path, expected_text):
#     global stars_earned

#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         try:
#             recognized_text = recognizer.recognize_google(audio_data).lower()
#             correct = expected_text.lower() in recognized_text

#             if correct:
#                 stars_earned += 1
#                 feedback = random.choice(success_feedbacks)
#                 stars_label.config(text=f"★ {stars_earned}")
#                 speak_text(feedback)
#                 root.after(4000, next_image)
#             else:
#                 feedback = random.choice(retry_feedbacks)
#                 speak_text(feedback)
#                 root.after(4000, update_image)

#         except sr.UnknownValueError:
#             feedback_label.config(text="Couldn't understand, please try again.")
#             root.after(4000, update_image)
#         except sr.RequestError as e:
#             feedback_label.config(text="Recognition error.")
#             print(f"Recognition error: {e}")

# # Function to go to the next image
# def next_image():
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0
#     update_image()

# loading_screen()
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)  # Make the window fullscreen
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter
# gif_frames = None
# current_frame = 0
# recording_duration = 12  # Duration in seconds to display as a timer
# recognizer = sr.Recognizer()  # Speech recognizer

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "/home/kolezza/SawaTok/all.jpg", "text": "This is a ball"},
#     {"image_path": "/home/kolezza/SawaTok/cat.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "/home/kolezza/SawaTok/bag.jpg", "text": "This is a cat"},
#     {"image_path": "/home/kolezza/SawaTok/bed.jpg", "text": "This is a bed"},
#     {"image_path": "/home/kolezza/SawaTok/clapping.gif", "text": "Amazing"},
#     {"image_path": "/home/kolezza/SawaTok/bell.jpg", "text": "This is a donkey"}
# ]

# # Success and retry messages
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Display loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")  # Background image path
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     easy_img = Image.open("smileydog.jpg")  # Easy level image path
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label, timer_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     # Timer label to show elapsed time
#     timer_label = tk.Label(root, text="Timer: 0s", font=("Arial", 18), bg="white", fg="black")
#     timer_label.pack(pady=10)

#     update_image()

# def update_image():
#     global current_index

#     image_path = images_data[current_index]["image_path"]
#     instruction_text = images_data[current_index]["text"]
#     text_label.config(text=instruction_text)

#     if image_path.lower().endswith('.gif'):
#         # Handle GIF display
#         show_gif(image_path)
#     else:
#         # Handle static image
#         image = Image.open(image_path)
#         image = image.resize((600, 400), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo
#         root.after(500, lambda: threading.Thread(target=handle_speech_interaction, args=(instruction_text,)).start())

# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to update timer
# def update_timer(start_time):
#     elapsed_time = time.time() - start_time
#     timer_label.config(text=f"Timer: {int(elapsed_time)}s")
#     if elapsed_time < recording_duration:
#         root.after(1000, update_timer, start_time)

# # Function to start recording and timer
# def start_recording():
#     fs = 44100  # Sample rate
#     duration = 5  # Recording duration in seconds
#     print("Recording... Speak now!")

#     start_time = time.time()  # Start timer
#     update_timer(start_time)  # Update timer on screen

#     audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#     sd.wait()

#     # Save to a temporary WAV file
#     temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#     wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#     analyze_speech(temp_wav_file.name)

# def analyze_speech(audio_path):
#     global stars_earned

#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#         try:
#             recognized_text = recognizer.recognize_google(audio_data).lower()
#             if recognized_text:
#                 elapsed_time = time.time() - start_time
#                 if elapsed_time <= recording_duration:
#                     feedback = random.choice(success_feedbacks)
#                     stars_earned += 1
#                     stars_label.config(text=f"★ {stars_earned}")
#                     speak_text(feedback)
#                     root.after(4000, next_image)
#                 else:
#                     feedback = random.choice(retry_feedbacks)
#                     speak_text(feedback)
#                     root.after(4000, update_image)
#             else:
#                 feedback = "Couldn't understand, please try again."
#                 feedback_label.config(text=feedback)
#                 speak_text(feedback)
#                 root.after(4000, update_image)
#         except sr.UnknownValueError:
#             feedback = "Couldn't understand, please try again."
#             feedback_label.config(text=feedback)
#             speak_text(feedback)
#             root.after(4000, update_image)

# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# loading_screen()
# root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import random

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Global variables
# current_index = 0
# stars_earned = 0
# gif_frames = None
# current_frame = 0

# # Image data and feedback messages
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "celebration1.gif", "text": "Yay yay yay keep it up"},
#     {"image_path": "bag.jpg", "text": "This is a bag"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "clapping.gif", "text": "Amazing"},
#     {"image_path": "bell.jpg", "text": "This is a bell"}
# ]

# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]

# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# TIME_LIMIT = 12  # Time limit in seconds

# def speak_text(text):
#     """Function to convert text to speech and play it"""
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# def play_audio(filename):
#     """Function to play audio files"""
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# def loading_screen():
#     """Display initial loading screen"""
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Load background image
#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.05)

#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar).start()

# def game_levels_screen():
#     """Display game level selection screen"""
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(pady=20)

#     easy_img = Image.open("smileydog.jpg")
#     easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#     easy_photo = ImageTk.PhotoImage(easy_img)

#     easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#     easy_label.image = easy_photo
#     easy_label.grid(row=0, column=0, padx=30)

#     easy_button = tk.Button(level_frame, text="Start", command=show_main_screen, 
#                            bg="green", fg="white", font=("Arial", 12))
#     easy_button.grid(row=1, column=0, pady=10)

#     easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#     easy_text.grid(row=2, column=0, pady=10)

# def update_gif(start_time):
#     """Update GIF animation frames"""
#     global current_frame, gif_frames
#     if gif_frames and time.time() - start_time < 3:
#         current_frame = (current_frame + 1) % len(gif_frames)
#         image_label.configure(image=gif_frames[current_frame])
#         root.after(100, lambda: update_gif(start_time))
#     else:
#         root.after(0, next_image)

# def show_main_screen():
#     """Initialize and display the main game screen"""
#     global image_label, text_label, feedback_label, stars_label

#     for widget in root.winfo_children():
#         widget.destroy()

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.pack(pady=20)

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# def update_image():
#     """Update the displayed image and handle GIF/static image logic"""
#     global current_index, gif_frames, current_frame

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]
#         text_label.config(text=instruction_text)

#         if image_path.lower().endswith('.gif'):
#             # Handle GIF
#             gif = Image.open(image_path)
#             gif_frames = []
#             current_frame = 0
            
#             try:
#                 while True:
#                     gif_frame = gif.copy()
#                     gif_frame = gif_frame.resize((600, 400), Image.LANCZOS)
#                     gif_frames.append(ImageTk.PhotoImage(gif_frame))
#                     gif.seek(gif.tell() + 1)
#             except EOFError:
#                 pass

#             if gif_frames:
#                 image_label.config(image=gif_frames[0])
#                 start_time = time.time()
#                 threading.Thread(target=speak_text, args=(instruction_text,)).start()
#                 update_gif(start_time)
#         else:
#             # Handle static image
#             gif_frames = None
#             image = Image.open(image_path)
#             image = image.resize((600, 400), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image_label.config(image=photo)
#             image_label.image = photo
            
#             root.after(500, lambda: threading.Thread(target=handle_speech_interaction, 
#                                                    args=(instruction_text,)).start())

#     except Exception as e:
#         print(f"Image loading error: {e}")

# def handle_speech_interaction(instruction_text):
#     """Handle the speech interaction flow"""
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)
#         start_recording()
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# def start_recording():
#     """Start audio recording and handle the recording process"""
#     try:
#         fs = 44100  # Sample rate
#         duration = TIME_LIMIT  # Recording duration in seconds
#         start_time = time.time()
#         print("Recording... Speak now!")

#         # Record audio
#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()
        
#         # Calculate actual recording duration
#         elapsed_time = time.time() - start_time

#         # Save recording to temporary file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Analyze the recording
#         analyze_speech(elapsed_time, temp_wav_file.name)

#     except Exception as e:
#         root.after(0, lambda: feedback_label.config(text="Error in recording, please try again."))
#         print(f"Recording error: {e}")



# def analyze_speech(elapsed_time, audio_file):
#     """Analyze the recorded speech and provide feedback"""
#     global stars_earned, current_index

#     try:
#         # Initialize speech recognizer
#         recognizer = sr.Recognizer()
        
#         with sr.AudioFile(audio_file) as source:
#             audio = recognizer.record(source)
            
#             try:
#                 # Attempt to detect speech
#                 text = recognizer.recognize_google(audio)
#                 has_speech = True
#             except sr.UnknownValueError:
#                 has_speech = False
            
#             if has_speech:
#                 if elapsed_time <= TIME_LIMIT:
#                     # Success case
#                     feedback = random.choice(success_feedbacks)
#                     stars_earned += 1
#                     stars_label.config(text=f"★ {stars_earned}")
                    
#                     def proceed_to_next():
#                         speak_text(feedback)
#                         root.after(3000, next_image)
                    
#                     root.after(0, proceed_to_next)
#                 else:
#                     # Too slow case
#                     feedback = random.choice(retry_feedbacks)
                    
#                     def retry_current():
#                         speak_text(feedback)
#                         root.after(3000, lambda: handle_speech_interaction(images_data[current_index]["text"]))
                    
#                     root.after(0, retry_current)
#             else:
#                 # No speech detected case
#                 def prompt_retry():
#                     speak_text("I couldn't hear you. Please try again.")
#                     root.after(2000, lambda: handle_speech_interaction(images_data[current_index]["text"]))
                
#                 root.after(0, prompt_retry)

#     except Exception as e:
#         print(f"Speech analysis error: {e}")
#         root.after(0, lambda: feedback_label.config(text="Error analyzing speech. Please try again."))

# def next_image():
#     """Move to the next image in the sequence"""
#     global current_index
#     if current_index < len(images_data) - 1:
#         current_index += 1
#     else:
#         current_index = 0
#     update_image()

# if __name__ == "__main__":
#     loading_screen()
#     root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import json

# # ThingsBoard server URL and access token
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Success and retry feedbacks
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# # Initialize the main window
# root = tk.Tk()
# root.title("Speech Game")
# root.attributes('-fullscreen', True)
# root.configure(bg="white")

# # Initialize Coqui TTS
# tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# # Variables for tracking current image and recording
# current_index = 0
# stars_earned = 0  # Star counter

# # List of image paths and their corresponding texts
# images_data = [
#     {"image_path": "all.jpg", "text": "This is a ball"},
#     {"image_path": "cat.jpg", "text": "This is a cat"},
#     {"image_path": "bed.jpg", "text": "This is a bed"},
#     {"image_path": "donkey.jpeg", "text": "This is a donkey"}
# ]

# # Function to use Coqui TTS to speak the text
# def speak_text(text):
#     try:
#         print(f"Speaking: {text}")
#         tts.tts_to_file(text=text, file_path="tts_output.wav")
#         play_audio("tts_output.wav")
#     except Exception as e:
#         print(f"TTS error: {e}")

# # Function to play audio using simpleaudio
# def play_audio(filename):
#     try:
#         wave_obj = sa.WaveObject.from_wave_file(filename)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()  # Wait until the audio finishes
#     except Exception as e:
#         print(f"Audio playback error: {e}")

# # Loading screen
# def loading_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     bg_image = Image.open("boy.jpg")
#     bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#     bg_photo = ImageTk.PhotoImage(bg_image)

#     bg_label = tk.Label(root, image=bg_photo)
#     bg_label.image = bg_photo
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     load_label = tk.Label(root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#     load_label.pack(pady=200)

#     progress_bar = tk.Canvas(root, width=400, height=30, bg="white", highlightthickness=0)
#     progress_bar.pack(pady=20)
#     load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#     def fill_bar():
#         for i in range(1, 101, 10):
#             progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#             root.update_idletasks()
#             time.sleep(0.3)
#         bg_label.destroy()
#         load_label.destroy()
#         progress_bar.destroy()
#         game_levels_screen()

#     threading.Thread(target=fill_bar, daemon=True).start()

# # Game level selection screen
# def game_levels_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     title_label = tk.Label(root, text="Game Levels", font=("Arial", 30), bg="white")
#     title_label.pack(pady=20)

#     level_frame = tk.Frame(root, bg="white")
#     level_frame.pack(expand=True)

#     levels_data = [
#         {"image": "smileydog.jpg", "name": "Easy Level", "command": show_main_screen},
#         {"image": "boy1.png", "name": "Medium Level", "command": show_main_screen},
#         {"image": "boy2.png", "name": "Hard Level", "command": show_main_screen}
#     ]

#     for index, level in enumerate(levels_data):
#         img = Image.open(level["image"])
#         img = img.resize((200, 200), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(img)

#         level_label = tk.Label(level_frame, image=photo, bg="white")
#         level_label.image = photo
#         level_label.grid(row=0, column=index, padx=20, pady=10)

#         level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                  bg="green", fg="white", font=("Arial", 14))
#         level_button.grid(row=1, column=index, pady=10)

# # Show the main screen with images and text
# def show_main_screen():
#     for widget in root.winfo_children():
#         widget.destroy()

#     global image_label, text_label, feedback_label, stars_label

#     image_label = tk.Label(root)
#     image_label.pack(expand=True)

#     text_label = tk.Label(root, text="", font=("Arial", 24), bg="white", fg="black")
#     text_label.place(relx=0.5, rely=0.8, anchor="center")

#     stars_label = tk.Label(root, text=f"★ {stars_earned}", font=("Arial", 14), bg="white", fg="black")
#     stars_label.pack(pady=5)

#     feedback_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", fg="black")
#     feedback_label.pack(pady=10)

#     update_image()

# # Function to update the displayed image and text
# def update_image():
#     global current_index

#     try:
#         image_path = images_data[current_index]["image_path"]
#         instruction_text = images_data[current_index]["text"]

#         image = Image.open(image_path)
#         image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
#         photo = ImageTk.PhotoImage(image)
#         image_label.config(image=photo)
#         image_label.image = photo

#         text_label.config(text=instruction_text)

#         # Start TTS and speech interaction
#         threading.Thread(target=handle_speech_interaction, args=(instruction_text,), daemon=True).start()

#     except Exception as e:
#         print(f"Image loading error: {e}")

# # Function to handle speaking and automatic recording interaction
# def handle_speech_interaction(instruction_text):
#     try:
#         speak_text(instruction_text)
#         time.sleep(1)
#         speak_text("Repeat after me.")
#         time.sleep(1)  # Wait for TTS playback to finish
#         start_recording(instruction_text)
#     except Exception as e:
#         print(f"Speech interaction error: {e}")

# # Function to start recording and validate speech
# def start_recording(expected_text):
#     try:
#         fs = 44100  # Sample rate
#         duration = 5  # Max recording duration
#         print("Recording... Speak now!")

#         audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#         sd.wait()

#         # Save to a temporary WAV file
#         temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#         # Load the recorded audio for recognition
#         recorded_audio = sr.AudioFile(temp_wav_file.name)

#         with recorded_audio as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.record(source)

#         recognized_text = recognizer.recognize_google(audio).lower()
#         correct = expected_text.lower() in recognized_text

#         elapsed_time = random.uniform(1.5, 4.5)  # Simulate a realistic elapsed time

#         # Send progress data to ThingsBoard
#         progress_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "correct": correct,
#             "stars_earned": stars_earned,
#             "elapsed_time": elapsed_time
#         }
#         send_data_to_thingsboard(progress_data)

#         analyze_speech(elapsed_time, correct)

#     except Exception as e:
#         feedback_label.config(text="Error in recording, please try again.")
#         print(f"Recording error: {e}")

# # Function to send data to ThingsBoard
# def send_data_to_thingsboard(data):
#     try:
#         headers = {"Content-Type": "application/json"}
#         response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#         if response.status_code == 200:
#             print("Data sent to ThingsBoard:", data)
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending data to ThingsBoard: {e}")

# # Function to analyze speech duration and provide feedback
# def analyze_speech(elapsed_time, correct):
#     global stars_earned

#     if correct and elapsed_time <= 40:
#         feedback = np.random.choice(success_feedbacks)
#         stars_earned += 1
#         stars_label.config(text=f"★ {stars_earned}")
#         speak_text(feedback)
#         root.after(4000, next_image)
#     else:
#         feedback = np.random.choice(retry_feedbacks)
#         speak_text(feedback)
#         root.after(4000, update_image)

# # Function to go to the next image
# def next_image():
#     global current_index
#     current_index = (current_index + 1) % len(images_data)
#     update_image()

# # Start the loading screen
# loading_screen()

# # Run the Tkinter main loop
# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import time
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import random
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import requests
# import json

# # ThingsBoard configuration remains the same
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages remain the same
# success_feedbacks = [
#     "Great job! You were really quick!",
#     "Awesome work! You completed it in time.",
#     "Well done! You said it perfectly.",
#     "Excellent! You're improving!"
# ]
# retry_feedbacks = [
#     "Don't worry, you'll get faster!",
#     "Keep trying, you're almost there!",
#     "Try again, and aim to be quicker.",
#     "Keep it up! You can do this."
# ]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
#         self.is_processing = False
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav")
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename):
#         try:
#             wave_obj = sa.WaveObject.from_wave_file(filename)
#             play_obj = wave_obj.play()
#             play_obj.wait_done()
#         except Exception as e:
#             print(f"Audio playback error: {e}")

#     def start_recording(self, expected_text):
#         if self.is_processing:
#             return
            
#         self.is_processing = True
#         try:
#             fs = 44100
#             duration = 5
#             print("Recording... Speak now!")

#             audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#             sd.wait()

#             temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#             wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))

#             with sr.AudioFile(temp_wav_file.name) as source:
#                 self.recognizer.adjust_for_ambient_noise(source)
#                 audio = self.recognizer.record(source)

#             recognized_text = self.recognizer.recognize_google(audio).lower()
#             correct = expected_text.lower() in recognized_text
#             elapsed_time = random.uniform(1.5, 4.5)

#             # Send data to ThingsBoard
#             progress_data = {
#                 "expected_text": expected_text,
#                 "recognized_text": recognized_text,
#                 "correct": correct,
#                 "stars_earned": self.stars_earned,
#                 "elapsed_time": elapsed_time
#             }
#             self.send_data_to_thingsboard(progress_data)
            
#             # Schedule feedback handling
#             self.root.after(0, lambda: self.handle_speech_result(elapsed_time, correct))

#         except Exception as e:
#             print(f"Recording error: {e}")
#             self.feedback_label.config(text="Error in recording, please try again.")
#             self.is_processing = False
#             self.root.after(2000, lambda: self.update_image())

#     def handle_speech_result(self, elapsed_time, correct):
#         if correct and elapsed_time <= 40:
#             feedback = random.choice(success_feedbacks)
#             self.stars_earned += 1
#             self.stars_label.config(text=f"★ {self.stars_earned}")
            
#             def proceed_to_next():
#                 self.speak_text(feedback)
#                 self.is_processing = False
#                 self.root.after(4000, self.next_image)
                
#             self.root.after(0, proceed_to_next)
#         else:
#             feedback = random.choice(retry_feedbacks)
            
#             def retry_current():
#                 self.speak_text(feedback)
#                 self.is_processing = False
#                 self.root.after(4000, self.update_image)
                
#             self.root.after(0, retry_current)

#     def update_image(self):
#         if self.is_processing:
#             return
            
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), 
#                                Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             def start_interaction():
#                 self.speak_text(instruction_text)
#                 time.sleep(1)
#                 self.speak_text("Repeat after me.")
#                 time.sleep(1)
#                 self.start_recording(instruction_text)

#             threading.Thread(target=start_interaction, daemon=True).start()

#         except Exception as e:
#             print(f"Image loading error: {e}")
#             self.is_processing = False

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#             if response.status_code == 200:
#                 print("Data sent to ThingsBoard:", data)
#             else:
#                 print(f"Failed to send data. Status code: {response.status_code}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), 
#                                  bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", 
#                                   font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), 
#                                      bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.show_main_screen()
#     root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import random
# import requests
# import json

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = ["Great job!", "Awesome work!", "Well done!", "Excellent!"]
# retry_feedbacks = ["Try again!", "Keep practicing!", "Don't give up!", "Almost there!"]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
        
#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self, expected_text):
#         def record_audio():
#             try:
#                 print("Recording... Speak now!")
#                 fs = 44100
#                 duration = 5

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     self.recognizer.adjust_for_ambient_noise(source, duration=1)
#                     audio = self.recognizer.record(source)
#                 recognized_text = self.recognizer.recognize_google(audio).lower()
#                 print(f"Recognized: {recognized_text}")

#                 # Check if correct
#                 correct = expected_text.lower() in recognized_text
#                 self.handle_speech_result(correct)
#             except Exception as e:
#                 print(f"Recording error: {e}")
#                 self.feedback_label.config(text="Recording failed. Try again.")
#             finally:
#                 if os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def handle_speech_result(self, correct):
#         if correct:
#             feedback = random.choice(success_feedbacks)
#             self.stars_earned += 1
#             self.stars_label.config(text=f"★ {self.stars_earned}")
#             self.speak_text(feedback, self.next_image)
#         else:
#             feedback = random.choice(retry_feedbacks)
#             self.speak_text(feedback, self.update_image)

#     def update_image(self):
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", lambda: self.start_recording(instruction_text)))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def show_main_screen(self):
#         # Clear screen
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # UI elements
#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.show_main_screen()
#     root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import random
# import requests
# import time

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = ["Great job!", "Awesome work!", "Well done!", "Excellent!"]
# retry_feedbacks = ["You can say it faster next time.", "Try to be quicker.", "Keep practicing!"]
# error_feedbacks = ["You said '{}', but it should be '{}'.", "Let's try again. You said '{}', but it should be '{}'."]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
        
#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self, expected_text):
#         start_time = time.time()  # Start timing
#         def record_audio():
#             try:
#                 print("Recording... Speak now!")
#                 fs = 44100
#                 duration = 5

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     self.recognizer.adjust_for_ambient_noise(source, duration=1)
#                     audio = self.recognizer.record(source)
#                 recognized_text = self.recognizer.recognize_google(audio).lower()
#                 print(f"Recognized: {recognized_text}")

#                 # Check if correct
#                 elapsed_time = time.time() - start_time
#                 correct = expected_text.lower() in recognized_text

#                 # Prepare data to send
#                 data = {
#                     "expected_text": expected_text,
#                     "recognized_text": recognized_text,
#                     "correct": correct,
#                     "stars_earned": self.stars_earned,
#                     "elapsed_time": elapsed_time
#                 }

#                 # Send data to ThingsBoard
#                 self.send_data_to_thingsboard(data)

#                 # Handle feedback
#                 self.handle_speech_result(correct, expected_text, recognized_text, elapsed_time)
#             except Exception as e:
#                 print(f"Recording error: {e}")
#                 self.feedback_label.config(text="Recording failed. Try again.")
#             finally:
#                 if os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def handle_speech_result(self, correct, expected_text, recognized_text, elapsed_time):
#         print(f"Elapsed Time: {elapsed_time:.2f} seconds")
#         if correct:
#             if elapsed_time <= 5:  # Timely response
#                 feedback = random.choice(success_feedbacks)
#                 self.stars_earned += 1
#                 self.stars_label.config(text=f"★ {self.stars_earned}")
#                 self.speak_text(feedback, self.next_image)
#             else:  # Slow but correct
#                 feedback = random.choice(retry_feedbacks)
#                 self.speak_text(feedback, self.update_image)
#         else:  # Incorrect response
#             feedback = random.choice(error_feedbacks).format(recognized_text, expected_text)
#             self.speak_text(feedback, self.update_image)

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#             if response.status_code == 200:
#                 print("Data sent to ThingsBoard:", data)
#             else:
#                 print(f"Failed to send data. Status code: {response.status_code}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def update_image(self):
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", lambda: self.start_recording(instruction_text)))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def loading_screen(self):
#         # Clear screen
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Loading page UI
#         bg_label = tk.Label(self.root, text="Loading...", font=("Arial", 40), bg="white", fg="green")
#         bg_label.pack(expand=True)

#         progress_bar = tk.Canvas(self.root, width=400, height=30, bg="white", highlightthickness=0)
#         progress_bar.pack(pady=20)
#         load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#         def fill_bar():
#             for i in range(1, 101, 10):
#                 progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#                 self.root.update_idletasks()
#                 time.sleep(0.3)
#             bg_label.destroy()
#             progress_bar.destroy()
#             self.level_selection_screen()

#         threading.Thread(target=fill_bar, daemon=True).start()

#     def level_selection_screen(self):
#         # Clear screen
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Level selection UI
#         title_label = tk.Label(self.root, text="Select Level", font=("Arial", 30), bg="white")
#         title_label.pack(pady=20)

#         level_frame = tk.Frame(self.root, bg="white")
#         level_frame.pack(expand=True)

#         levels_data = [
#             {"image": "smileydog.jpg", "name": "Easy Level", "command": self.show_main_screen},
#             {"image": "boy1.png", "name": "Medium Level", "command": self.show_main_screen},
#             {"image": "boy2.png", "name": "Hard Level", "command": self.show_main_screen}
#         ]

#         for index, level in enumerate(levels_data):
#             img = Image.open(level["image"])
#             img = img.resize((200, 200), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(img)

#             level_label = tk.Label(level_frame, image=photo, bg="white")
#             level_label.image = photo
#             level_label.grid(row=0, column=index, padx=20, pady=10)

#             level_button = tk.Button(level_frame, text=level["name"], command=level["command"], 
#                                      bg="green", fg="white", font=("Arial", 14))
#             level_button.grid(row=1, column=index, pady=10)

#     def show_main_screen(self):
#         # Clear screen
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Main game UI
#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.loading_screen()
#     root.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import random
# import requests
# import time

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = ["Great job!", "Awesome work!", "Well done!", "Excellent!"]
# retry_feedbacks = ["Try to say it faster this time.", "Try to be quicker.", "You can do this!"]
# error_feedbacks = ["You said '{}', but it should be '{}'.", "Let's try again. You said '{}', but it should be '{}'."]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
        
#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self, expected_text):
#         start_time = time.time()  # Start timing
#         def record_audio():
#             try:
#                 print("Recording... Speak now!")
#                 fs = 44100
#                 duration = 5

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     self.recognizer.adjust_for_ambient_noise(source, duration=1)
#                     audio = self.recognizer.record(source)
#                 recognized_text = self.recognizer.recognize_google(audio).lower()
#                 print(f"Recognized: {recognized_text}")

#                 # Check if correct
#                 elapsed_time = time.time() - start_time
#                 correct = expected_text.lower() in recognized_text

#                 # Prepare data to send
#                 data = {
#                     "expected_text": expected_text,
#                     "recognized_text": recognized_text,
#                     "correct": correct,
#                     "stars_earned": self.stars_earned,
#                     "elapsed_time": elapsed_time
#                 }

#                 # Send data to ThingsBoard
#                 self.send_data_to_thingsboard(data)

#                 # Handle feedback
#                 self.handle_speech_result(correct, expected_text, recognized_text, elapsed_time)
#             except Exception as e:
#                 print(f"Recording error: {e}")
#                 self.feedback_label.config(text="Recording failed. Try again.")
#             finally:
#                 if os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def handle_speech_result(self, correct, expected_text, recognized_text, elapsed_time):
#         print(f"Elapsed Time: {elapsed_time:.2f} seconds")
#         if correct:
#             if elapsed_time <= 8:  # Timely response
#                 feedback = random.choice(success_feedbacks)
#                 self.stars_earned += 1
#                 self.stars_label.config(text=f"★ {self.stars_earned}")
#                 self.speak_text(feedback, self.next_image)
#             else:  # Slow but correct
#                 feedback = random.choice(retry_feedbacks)
#                 self.speak_text(feedback, self.update_image)
#         else:  # Incorrect response
#             feedback = random.choice(error_feedbacks).format(recognized_text, expected_text)
#             self.speak_text(feedback, self.update_image)

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#             if response.status_code == 200:
#                 print("Data sent to ThingsBoard:", data)
#             else:
#                 print(f"Failed to send data. Status code: {response.status_code}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def update_image(self):
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", lambda: self.start_recording(instruction_text)))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def loading_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Load the background image for loading screen
#         bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#         bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#         bg_photo = ImageTk.PhotoImage(bg_image)

#         bg_label = tk.Label(self.root, image=bg_photo)
#         bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         load_label = tk.Label(self.root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#         load_label.pack(pady=200)

#         progress_bar = tk.Canvas(self.root, width=400, height=30, bg="white", highlightthickness=0)
#         progress_bar.pack(pady=20)
#         load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#         def fill_bar():
#             for i in range(1, 101):
#                 progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#                 self.root.update_idletasks()
#                 time.sleep(0.05)

#             bg_label.destroy()
#             load_label.destroy()
#             progress_bar.destroy()
#             self.level_selection_screen()

#         threading.Thread(target=fill_bar).start()

#     def level_selection_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Level selection screen title
#         title_label = tk.Label(self.root, text="Game Levels", font=("Arial", 30), bg="white")
#         title_label.pack(pady=20)

#         level_frame = tk.Frame(self.root, bg="white")
#         level_frame.pack(pady=20)

#         # Easy level with image
#         easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#         easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#         easy_photo = ImageTk.PhotoImage(easy_img)

#         easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#         easy_label.image = easy_photo  # Keep a reference to avoid garbage collection
#         easy_label.grid(row=0, column=0, padx=30)

#         easy_button = tk.Button(level_frame, text="Start", command=self.show_main_screen, bg="green", fg="white", font=("Arial", 12))
#         easy_button.grid(row=1, column=0, pady=10)

#         easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#         easy_text.grid(row=2, column=0, pady=10)

#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.loading_screen()
#     root.mainloop()




# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import random
# import requests
# import time

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = ["Great job!", "Awesome work!", "Well done!", "Excellent!"]
# retry_feedbacks = ["Try to say it faster this time.", "Try to be quicker.", "You can do this!"]
# error_feedbacks = ["You said '{}', but it should be '{}'.", "Let's try again. You said '{}', but it should be '{}'."]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
        
#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self, expected_text):
#         start_time = time.time()  # Start timing

#         def record_audio():
#             try:
#                 print("Recording... Speak now!")
#                 fs = 44100
#                 duration = 3  # Reduced recording duration

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     self.recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Shorter adjustment duration
#                     audio = self.recognizer.record(source)
#                 recognized_text = self.recognizer.recognize_google(audio).lower()
#                 print(f"Recognized: {recognized_text}")

#                 # Check if correct
#                 elapsed_time = time.time() - start_time
#                 correct = expected_text.lower() in recognized_text

#                 # Handle feedback
#                 self.handle_speech_result(correct, expected_text, recognized_text, elapsed_time)
                
#                 # Send data to ThingsBoard asynchronously
#                 threading.Thread(target=self.send_data_to_thingsboard, args=({
#                     "expected_text": expected_text,
#                     "recognized_text": recognized_text,
#                     "correct": correct,
#                     "stars_earned": self.stars_earned,
#                     "elapsed_time": elapsed_time
#                 },)).start()
#             except Exception as e:
#                 print(f"Recording error: {e}")
#                 self.feedback_label.config(text="Recording failed. Try again.")
#             finally:
#                 if os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def handle_speech_result(self, correct, expected_text, recognized_text, elapsed_time):
#         print(f"Elapsed Time: {elapsed_time:.2f} seconds")
#         if correct:
#             if elapsed_time <= 8:  # Timely response
#                 feedback = random.choice(success_feedbacks)
#                 self.stars_earned += 1
#                 self.stars_label.config(text=f"★ {self.stars_earned}")
#                 self.speak_text(feedback, self.next_image)
#             else:  # Slow but correct
#                 feedback = random.choice(retry_feedbacks)
#                 self.speak_text(feedback, self.update_image)
#         else:  # Incorrect response
#             feedback = random.choice(error_feedbacks).format(recognized_text, expected_text)
#             self.speak_text(feedback, self.update_image)

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#             if response.status_code == 200:
#                 print("Data sent to ThingsBoard:", data)
#             else:
#                 print(f"Failed to send data. Status code: {response.status_code}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def update_image(self):
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", lambda: self.start_recording(instruction_text)))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def loading_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Load the background image for loading screen
#         bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#         bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#         bg_photo = ImageTk.PhotoImage(bg_image)

#         bg_label = tk.Label(self.root, image=bg_photo)
#         bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         load_label = tk.Label(self.root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#         load_label.pack(pady=200)

#         progress_bar = tk.Canvas(self.root, width=400, height=30, bg="white", highlightthickness=0)
#         progress_bar.pack(pady=20)
#         load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#         def fill_bar():
#             for i in range(1, 101):
#                 progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#                 self.root.update_idletasks()
#                 time.sleep(0.05)

#             bg_label.destroy()
#             load_label.destroy()
#             progress_bar.destroy()
#             self.level_selection_screen()

#         threading.Thread(target=fill_bar).start()

#     def level_selection_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Level selection screen title
#         title_label = tk.Label(self.root, text="Game Levels", font=("Arial", 30), bg="white")
#         title_label.pack(pady=20)

#         level_frame = tk.Frame(self.root, bg="white")
#         level_frame.pack(pady=20)

#         # Easy level with image
#         easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#         easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#         easy_photo = ImageTk.PhotoImage(easy_img)

#         easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#         easy_label.image = easy_photo  # Keep a reference to avoid garbage collection
#         easy_label.grid(row=0, column=0, padx=30)

#         easy_button = tk.Button(level_frame, text="Start", command=self.show_main_screen, bg="green", fg="white", font=("Arial", 12))
#         easy_button.grid(row=1, column=0, pady=10)

#         easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#         easy_text.grid(row=2, column=0, pady=10)

#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.loading_screen()
#     root.mainloop()






# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import numpy as np
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import random
# import re  # For stuttering analysis
# import requests
# import time

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"http://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = ["Great job!", "Awesome work!", "Well done!", "Excellent!"]
# retry_feedbacks = ["Try to say it faster this time.", "Try to be quicker.", "You can do this!"]
# error_feedbacks = ["You said '{}', but it should be '{}'.", "Let's try again. You said '{}', but it should be '{}'."]

# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
        
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", 
#                       vocoder_path="vocoder_models/en/ljspeech/hifigan_v2")
#         self.recognizer = sr.Recognizer()
        
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
        
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
        
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpeg", "text": "This is a donkey"}
#         ]

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
        
#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self, expected_text):
#         start_time = time.time()  # Start timing

#         def record_audio():
#             try:
#                 print("Recording... Speak now!")
#                 fs = 44100
#                 duration = 3  # Reduced recording duration

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     self.recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Shorter adjustment duration
#                     audio = self.recognizer.record(source)
#                 recognized_text = self.recognizer.recognize_google(audio).lower()
#                 print(f"Recognized: {recognized_text}")

#                 # Check if correct
#                 elapsed_time = time.time() - start_time
#                 correct = expected_text.lower() in recognized_text

#                 # Handle feedback
#                 self.handle_speech_result(correct, expected_text, recognized_text, elapsed_time)
                
#                 # Send data to ThingsBoard asynchronously
#                 threading.Thread(target=self.send_data_to_thingsboard, args=({
#                     "expected_text": expected_text,
#                     "recognized_text": recognized_text,
#                     "correct": correct,
#                     "stars_earned": self.stars_earned,
#                     "elapsed_time": elapsed_time
#                 },)).start()
#             except Exception as e:
#                 print(f"Recording error: {e}")
#                 self.feedback_label.config(text="Recording failed. Try again.")
#             finally:
#                 if os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def detect_stutter(self, text):
#         """Detects stuttering patterns in text."""
#         # Simple regex for detecting repeated words
#         stutter_pattern = r'\b(\w+)\b(?:\s+\1\b)+'
#         return re.findall(stutter_pattern, text)

#     def handle_speech_result(self, correct, expected_text, recognized_text, elapsed_time):
#         print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        
#         stutters = self.detect_stutter(recognized_text)
#         if stutters:
#             feedback = f"I noticed some stuttering: {' '.join(stutters)}. Let's try to speak more smoothly."
#             self.speak_text(feedback, self.update_image)
#             return

#         if correct:
#             if elapsed_time <= 8:  # Timely response
#                 feedback = random.choice(success_feedbacks)
#                 self.stars_earned += 1
#                 self.stars_label.config(text=f"★ {self.stars_earned}")
#                 self.speak_text(feedback, self.next_image)
#             else:  # Slow but correct
#                 feedback = random.choice(retry_feedbacks)
#                 self.speak_text(feedback, self.update_image)
#         else:  # Incorrect response
#             feedback = random.choice(error_feedbacks).format(recognized_text, expected_text)
#             self.speak_text(feedback, self.update_image)

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, json=data, headers=headers)
#             if response.status_code == 200:
#                 print("Data sent to ThingsBoard:", data)
#             else:
#                 print(f"Failed to send data. Status code: {response.status_code}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def update_image(self):
#         try:
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", lambda: self.start_recording(instruction_text)))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)
#         self.update_image()

#     def loading_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Load the background image for loading screen
#         bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#         bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#         bg_photo = ImageTk.PhotoImage(bg_image)

#         bg_label = tk.Label(self.root, image=bg_photo)
#         bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#         load_label = tk.Label(self.root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#         load_label.pack(pady=200)

#         progress_bar = tk.Canvas(self.root, width=400, height=30, bg="white", highlightthickness=0)
#         progress_bar.pack(pady=20)
#         load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")

#         def fill_bar():
#             for i in range(1, 101):
#                 progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#                 self.root.update_idletasks()
#                 time.sleep(0.05)

#             bg_label.destroy()
#             load_label.destroy()
#             progress_bar.destroy()
#             self.level_selection_screen()

#         threading.Thread(target=fill_bar).start()

#     def level_selection_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         # Level selection screen title
#         title_label = tk.Label(self.root, text="Game Levels", font=("Arial", 30), bg="white")
#         title_label.pack(pady=20)

#         level_frame = tk.Frame(self.root, bg="white")
#         level_frame.pack(pady=20)

#         # Easy level with image
#         easy_img = Image.open("smileydog.jpg")  # Replace with the actual image path
#         easy_img = easy_img.resize((150, 150), Image.LANCZOS)
#         easy_photo = ImageTk.PhotoImage(easy_img)

#         easy_label = tk.Label(level_frame, image=easy_photo, bg="white")
#         easy_label.image = easy_photo  # Keep a reference to avoid garbage collection
#         easy_label.grid(row=0, column=0, padx=30)

#         easy_button = tk.Button(level_frame, text="Start", command=self.show_main_screen, bg="green", fg="white", font=("Arial", 12))
#         easy_button.grid(row=1, column=0, pady=10)

#         easy_text = tk.Label(level_frame, text="Easy Level", font=("Arial", 14), bg="white")
#         easy_text.grid(row=2, column=0, pady=10)

#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.8, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()

# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.loading_screen()
#     root.mainloop()







# import librosa
# import numpy as np
# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import traceback
# from fuzzywuzzy import fuzz
# import requests
# import json

# unrecognized_feedback = [
#     "I couldn't understand you clearly. Let's try again!",
# ]

# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# # Feedback messages
# success_feedbacks = [
#     "Hooray! You said it perfectly!Now we go to the next interesting image!",
# ]
# retry_feedbacks = [
#     "You have improved little champ, but now say with me:",
# ]
# stuttering_feedbacks = [
#     "Hmm, I don't think you said the right thing. Let's try to articulate it a bit better:",
# ]
# unrecognized_feedback = [
#     "I couldn't understand you clearly. Let's try again!",
# ]


# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")

#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
#         self.recognizer = sr.Recognizer()

#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
#         self.recording_in_progress = False

#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
#         self.result_label = None  # New label for result message

#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpg", "text": "This is a donkey"},
#         ]

#         # Set default device to system default microphone
#         sd.default.device = None

#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")

#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")

#         threading.Thread(target=play, daemon=True).start()

#     def start_recording(self):
#         if self.recording_in_progress:
#             print("Recording is already in progress. Skipping new request.")
#             return

#         self.recording_in_progress = True
#         expected_text = self.images_data[self.current_index]["text"]

#         def record_audio():
#             try:
#                 print(f"Recording... Expected text: {expected_text}")
#                 fs = 16000
#                 duration = 5

#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()

#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")

#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     print("Adjusting for ambient noise...")
#                     self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
#                     audio = self.recognizer.record(source)

#                 try:
#                     recognized_text = self.recognizer.recognize_google(audio).lower()
#                     print(f"Recognized text: {recognized_text}")
#                 except sr.UnknownValueError:
#                     print("Google Speech Recognition could not understand the audio.")
#                     self.handle_feedback(unrecognized_feedback[0])
#                     return
#                 except sr.RequestError as e:
#                     print(f"Google API error: {e}")
#                     self.handle_feedback("Speech service is unavailable. Please try again later.")
#                     return

#                 # Handle feedback
#                 self.handle_speech_result(expected_text, recognized_text)
#             except Exception as e:
#                 print("Recording error:")
#                 traceback.print_exc()
#             finally:
#                 self.recording_in_progress = False
#                 if 'temp_wav_file' in locals() and os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)

#         threading.Thread(target=record_audio, daemon=True).start()

#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, headers=headers, data=json.dumps(data))
#             if response.status_code == 200:
#                 print("Data sent successfully to ThingsBoard.")
#             else:
#                 print(f"Failed to send data to ThingsBoard: {response.status_code}, {response.text}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")

#     def handle_speech_result(self, expected_text, recognized_text):
#         similarity = fuzz.ratio(recognized_text, expected_text.lower())
#         print(f"Text similarity: {similarity}%")

#         # Prepare telemetry data
#         telemetry_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "similarity": similarity,
#             "level": self.current_index + 1,
#             "stars_earned": self.stars_earned,
#         }

#         self.send_data_to_thingsboard(telemetry_data)

#         # Update the result message
#         result_message = "Let’s take a closer look at what you said!"
#         self.result_label.config(text=result_message)
#         self.speak_text(result_message)  # Speak the result message

#         if similarity >= 75:  # Success threshold
#             feedback = success_feedbacks[0]
#             self.stars_earned += 1
#             self.stars_label.config(text=f"★ {self.stars_earned}")
#             self.speak_text(feedback, self.next_image)
#         else:
#             feedback = retry_feedbacks[0] + f" {expected_text}"
#             self.speak_text(feedback, self.start_recording)

#     def handle_feedback(self, message):
#         self.feedback_label.config(text=message)
#         self.speak_text(message, self.start_recording)

#     def update_image(self):
#         try:
#             # Clear the result message when updating the image
#             self.result_label.config(text="")

#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]

#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)

#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", self.start_recording))
#         except Exception as e:
#             print(f"Image loading error: {e}")

#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)  # Cycle through images
#         self.update_image()

#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()

#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)

#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.7, anchor="center")

#         self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="blue")
#         self.result_label.place(relx=0.5, rely=0.75, anchor="center")

#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)

#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)

#         self.update_image()


# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.show_main_screen()
#     root.mainloop()

# import librosa
# import numpy as np
# import tkinter as tk
# from PIL import Image, ImageTk
# from TTS.api import TTS
# import threading
# import simpleaudio as sa
# import sounddevice as sd
# import scipy.io.wavfile as wavfile
# import tempfile
# import speech_recognition as sr
# import os
# import traceback
# from fuzzywuzzy import fuzz
# import requests
# import json
# import time
# unrecognized_feedback = [
#     "I couldn't understand you clearly. Let's try again!",
# ]
# # ThingsBoard configuration
# THINGSBOARD_HOST = "thingsboard.cloud"
# ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
# THINGSBOARD_URL = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"
# # Feedback messages
# success_feedbacks = [
#     "Hooray! You said it perfectly!Now we go to the next interesting image!",
# ]
# retry_feedbacks = [
#     "You have improved little champ, but now say with me:",
# ]
# stuttering_feedbacks = [
#     "Hmm, I don't think you said the right thing. Let's try to articulate it a bit better:",
# ]
# unrecognized_feedback = [
#     "I couldn't understand you clearly. Let's try again!",
# ]
# class SpeechGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Speech Game")
#         self.root.attributes('-fullscreen', True)
#         self.root.configure(bg="white")
#         # Initialize TTS and recognizer
#         self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
#         self.recognizer = sr.Recognizer()
#         # Game state
#         self.current_index = 0
#         self.stars_earned = 0
#         self.recording_in_progress = False
#         # UI elements
#         self.image_label = None
#         self.text_label = None
#         self.feedback_label = None
#         self.stars_label = None
#         self.result_label = None  # New label for result message
#         # Image data
#         self.images_data = [
#             {"image_path": "all.jpg", "text": "This is a ball"},
#             {"image_path": "cat.jpg", "text": "This is a cat"},
#             {"image_path": "bed.jpg", "text": "This is a bed"},
#             {"image_path": "donkey.jpg", "text": "This is a donkey"},
#         ]
#         # Set default device to system default microphone
#         sd.default.device = None
#     def loading_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()
#         # Load the background image for loading screen
#         bg_image = Image.open("boy.jpg")  # Replace with the actual image path
#         bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#         bg_photo = ImageTk.PhotoImage(bg_image)
#         bg_label = tk.Label(self.root, image=bg_photo)
#         bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#         load_label = tk.Label(self.root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
#         load_labe@Christine Akinyi l.pack(pady=200)
#         progress_bar = tk.Canvas(self.root, width=400, height=30, bg="white", highlightthickness=0)
#         progress_bar.pack(pady=20)
#         load_progress = progress_bar.create_rectangle(0, 0, 0, 30, fill="green")
#         def fill_bar():
#             for i in range(1, 101):
#                 progress_bar.coords(load_progress, (0, 0, i * 4, 30))
#                 self.root.update_idletasks()
#                 time.sleep(0.05)
#             bg_label.destroy()
#             load_label.destroy()
#             progress_bar.destroy()
#             self.show_main_screen()
#         threading.Thread(target=fill_bar).start()
#     def speak_text(self, text, callback=None):
#         try:
#             print(f"Speaking: {text}")
#             self.tts.tts_to_file(text=text, file_path="tts_output.wav")
#             self.play_audio("tts_output.wav", callback)
#         except Exception as e:
#             print(f"TTS error: {e}")
#     def play_audio(self, filename, callback=None):
#         def play():
#             try:
#                 wave_obj = sa.WaveObject.from_wave_file(filename)
#                 play_obj = wave_obj.play()
#                 play_obj.wait_done()
#                 if callback:
#                     callback()
#             except Exception as e:
#                 print(f"Audio playback error: {e}")
#         threading.Thread(target=play, daemon=True).start()
#     def start_recording(self):
#         if self.recording_in_progress:
#             print("Recording is already in progress. Skipping new request.")
#             return
#         self.recording_in_progress = True
#         expected_text = self.images_data[self.current_index]["text"]
#         def record_audio():
#             try:
#                 print(f"Recording... Expected text: {expected_text}")
#                 fs = 16000
#                 duration = 5
#                 # Record audio
#                 audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
#                 sd.wait()
#                 # Save to temporary WAV file
#                 temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#                 wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
#                 print(f"Audio saved to {temp_wav_file.name}")
#                 # Recognize speech
#                 with sr.AudioFile(temp_wav_file.name) as source:
#                     print("Adjusting for ambient noise...")
#                     self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
#                     audio = self.recognizer.record(source)
#                 try:
#                     recognized_text = self.recognizer.recognize_google(audio).lower()
#                     print(f"Recognized text: {recognized_text}")
#                 except sr.UnknownValueError:
#                     print("Google Speech Recognition could not understand the audio.")
#                     self.handle_feedback(unrecognized_feedback[0])
#                     return
#                 except sr.RequestError as e:
#                     print(f"Google API error: {e}")
#                     self.handle_feedback("Speech service is unavailable. Please try again later.")
#                     return
#                 # Handle feedback
#                 self.handle_speech_result(expected_text, recognized_text)
#             except Exception as e:
#                 print("Recording error:")
#                 traceback.print_exc()
#             finally:
#                 self.recording_in_progress = False
#                 if 'temp_wav_file' in locals() and os.path.exists(temp_wav_file.name):
#                     os.unlink(temp_wav_file.name)
#         threading.Thread(target=record_audio, daemon=True).start()
#     def send_data_to_thingsboard(self, data):
#         try:
#             headers = {"Content-Type": "application/json"}
#             response = requests.post(THINGSBOARD_URL, headers=headers, data=json.dumps(data))
#             if response.status_code == 200:
#                 print("Data sent successfully to ThingsBoard.")
#             else:
#                 print(f"Failed to send data to ThingsBoard: {response.status_code}, {response.text}")
#         except Exception as e:
#             print(f"Error sending data to ThingsBoard: {e}")
#     def handle_speech_result(self, expected_text, recognized_text):
#         similarity = fuzz.ratio(recognized_text, expected_text.lower())
#         print(f"Text similarity: {similarity}%")
#         # Prepare telemetry data
#         telemetry_data = {
#             "expected_text": expected_text,
#             "recognized_text": recognized_text,
#             "similarity": similarity,
#             "level": self.current_index + 1,
#             "stars_earned": self.stars_earned,
#         }
#         self.send_data_to_thingsboard(telemetry_data)
#         # Update the result message
#         result_message = "Let’s take a closer look at what you said!"
#         self.result_label.config(text=result_message)
#         self.speak_text(result_message)  # Speak the result message
#         if similarity >= 75:  # Success threshold
#             feedback = success_feedbacks[0]
#             self.stars_earned += 1
#             self.stars_label.config(text=f"★ {self.stars_earned}")
#             self.speak_text(feedback, self.next_image)
#         else:
#             feedback = retry_feedbacks[0] + f" {expected_text}"
#             self.speak_text(feedback, self.start_recording)
#     def handle_feedback(self, message):
#         self.feedback_label.config(text=message)
#         self.speak_text(message, self.start_recording)
#     def update_image(self):
#         try:
#             # Clear the result message when updating the image
#             self.result_label.config(text="")
#             image_path = self.images_data[self.current_index]["image_path"]
#             instruction_text = self.images_data[self.current_index]["text"]
#             # Load and display image
#             image = Image.open(image_path)
#             image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             self.image_label.config(image=photo)
#             self.image_label.image = photo
#             self.text_label.config(text=instruction_text)
#             # Speak text and start recording
#             self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", self.start_recording))
#         except Exception as e:
#             print(f"Image loading error: {e}")
#     def next_image(self):
#         self.current_index = (self.current_index + 1) % len(self.images_data)  # Cycle through images
#         self.update_image()
#     def show_main_screen(self):
#         for widget in self.root.winfo_children():
#             widget.destroy()
#         self.image_label = tk.Label(self.root)
#         self.image_label.pack(expand=True)
#         self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
#         self.text_label.place(relx=0.5, rely=0.7, anchor="center")
#         self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="blue")
#         self.result_label.place(relx=0.5, rely=0.75, anchor="center")
#         self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
#         self.stars_label.pack(pady=5)
#         self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
#         self.feedback_label.pack(pady=10)
#         self.update_image()
# # Initialize and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = SpeechGame(root)
#     game.loading_screen()  # Start with the loading screen
#     root.mainloop()


import librosa
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
from TTS.api import TTS
import threading
import simpleaudio as sa
import sounddevice as sd
import scipy.io.wavfile as wavfile
import tempfile
import speech_recognition as sr
import os
import traceback
from fuzzywuzzy import fuzz
import requests
import json
import time

unrecognized_feedback = [
    "I couldn't understand you clearly. Let's try again!",
]

# ThingsBoard configuration
THINGSBOARD_HOST = "thingsboard.cloud"
ACCESS_TOKEN = "zmncLhcZs6o08d4pkLIK"
THINGSBOARD_URL = f"https://{THINGSBOARD_HOST}/api/v1/{ACCESS_TOKEN}/telemetry"

# Feedback messages
success_feedbacks = [
    "Hooray! You said it perfectly!Now we go to the next interesting image!",
]
retry_feedbacks = [
    "You have improved little champ, but now say with me:",
]
stuttering_feedbacks = [
    "Hmm, I don't think you said the right thing. Let's try to articulate it a bit better:",
]
unrecognized_feedback = [
    "I couldn't understand you clearly. Let's try again!",
]


class SpeechGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Game")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="white")

        # Initialize TTS and recognizer
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
        self.recognizer = sr.Recognizer()

        # Game state
        self.current_index = 0
        self.stars_earned = 0
        self.recording_in_progress = False

        # UI elements
        self.image_label = None
        self.text_label = None
        self.feedback_label = None
        self.stars_label = None
        self.result_label = None  # New label for result message

        # Image data
        self.images_data = [
            {"image_path": "all.jpg", "text": "This is a ball"},
            {"image_path": "cat.jpg", "text": "This is a cat"},
            {"image_path": "bed.jpg", "text": "This is a bed"},
            {"image_path": "donkey.jpg", "text": "This is a donkey"},
        ]

        # Set default device to system default microphone
        sd.default.device = None

    def loading_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Load the background image for loading screen
        bg_image = Image.open("boy.jpg")  # Replace with the actual image path
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=bg_photo)
        bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        load_label = tk.Label(self.root, text="Unlock Your Full Potential", font=("Arial", 40), fg="green", bg="lightblue")
        load_label.pack(pady=200)

        start_button = tk.Button(
            self.root,
            text="Start",
            font=("Arial", 20),
            bg="green",
            fg="white",
            command=self.show_main_screen
        )
        start_button.pack(pady=20)

    def speak_text(self, text, callback=None):
        try:
            print(f"Speaking: {text}")
            self.tts.tts_to_file(text=text, file_path="tts_output.wav")
            self.play_audio("tts_output.wav", callback)
        except Exception as e:
            print(f"TTS error: {e}")

    def play_audio(self, filename, callback=None):
        def play():
            try:
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()
                if callback:
                    callback()
            except Exception as e:
                print(f"Audio playback error: {e}")

        threading.Thread(target=play, daemon=True).start()

    def start_recording(self):
        if self.recording_in_progress:
            print("Recording is already in progress. Skipping new request.")
            return

        self.recording_in_progress = True
        expected_text = self.images_data[self.current_index]["text"]

        def record_audio():
            try:
                print(f"Recording... Expected text: {expected_text}")
                fs = 16000
                duration = 5

                # Record audio
                audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
                sd.wait()

                # Save to temporary WAV file
                temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
                wavfile.write(temp_wav_file.name, fs, (audio_data * 32767).astype(np.int16))
                print(f"Audio saved to {temp_wav_file.name}")

                # Recognize speech
                with sr.AudioFile(temp_wav_file.name) as source:
                    print("Adjusting for ambient noise...")
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.record(source)

                try:
                    recognized_text = self.recognizer.recognize_google(audio).lower()
                    print(f"Recognized text: {recognized_text}")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand the audio.")
                    self.handle_feedback(unrecognized_feedback[0])
                    return
                except sr.RequestError as e:
                    print(f"Google API error: {e}")
                    self.handle_feedback("Speech service is unavailable. Please try again later.")
                    return

                # Handle feedback
                self.handle_speech_result(expected_text, recognized_text)
            except Exception as e:
                print("Recording error:")
                traceback.print_exc()
            finally:
                self.recording_in_progress = False
                if 'temp_wav_file' in locals() and os.path.exists(temp_wav_file.name):
                    os.unlink(temp_wav_file.name)

        threading.Thread(target=record_audio, daemon=True).start()

    def send_data_to_thingsboard(self, data):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(THINGSBOARD_URL, headers=headers, data=json.dumps(data))
            if response.status_code == 200:
                print("Data sent successfully to ThingsBoard.")
            else:
                print(f"Failed to send data to ThingsBoard: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error sending data to ThingsBoard: {e}")

    def handle_speech_result(self, expected_text, recognized_text):
        similarity = fuzz.ratio(recognized_text, expected_text.lower())
        print(f"Text similarity: {similarity}%")

        # Prepare telemetry data
        telemetry_data = {
            "expected_text": expected_text,
            "recognized_text": recognized_text,
            "similarity": similarity,
            "level": self.current_index + 1,
            "stars_earned": self.stars_earned,
        }
        self.send_data_to_thingsboard(telemetry_data)

        # Update the result message
        result_message = "Let's take a closer look at what you said!"
        self.result_label.config(text=result_message)
        self.speak_text(result_message)  # Speak the result message

        if similarity >= 75:  # Success threshold
            feedback = success_feedbacks[0]
            self.stars_earned += 1
            self.stars_label.config(text=f"★ {self.stars_earned}")
            self.speak_text(feedback, self.next_image)
        else:
            feedback = retry_feedbacks[0] + f" {expected_text}"
            self.speak_text(feedback, self.start_recording)

    def handle_feedback(self, message):
        self.feedback_label.config(text=message)
        self.speak_text(message, self.start_recording)

    def update_image(self):
        try:
            # Clear the result message when updating the image
            self.result_label.config(text="")

            image_path = self.images_data[self.current_index]["image_path"]
            instruction_text = self.images_data[self.current_index]["text"]

            # Load and display image
            image = Image.open(image_path)
            image = image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.text_label.config(text=instruction_text)

            # Speak text and start recording
            self.speak_text(instruction_text, lambda: self.speak_text("Repeat after me.", self.start_recording))
        except Exception as e:
            print(f"Image loading error: {e}")

    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.images_data)  # Cycle through images
        self.update_image()

    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.image_label = tk.Label(self.root)
        self.image_label.pack(expand=True)

        self.text_label = tk.Label(self.root, text="", font=("Arial", 24), bg="white", fg="black")
        self.text_label.place(relx=0.5, rely=0.7, anchor="center")

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="blue")
        self.result_label.place(relx=0.5, rely=0.75, anchor="center")

        self.stars_label = tk.Label(self.root, text=f"★ {self.stars_earned}", font=("Arial", 14), bg="white", fg="black")
        self.stars_label.pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="white", fg="black")
        self.feedback_label.pack(pady=10)

        self.update_image()


# Initialize and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SpeechGame(root)
    game.loading_screen()  # Start with the loading screen
    root.mainloop()