import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# prompt the user to input the path to the audio file
audio_path = input("Please enter the path to the audio file: ")

# load the audio file
with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)

# set the keyword(s) to detect
keywords = ["pyar"]

# set the minimum number of times a keyword must be detected to trigger a match
threshold = 1

# perform keyword detection
matches = 0
for keyword in keywords:
    if r.recognize_google(audio_data).lower().count(keyword) >= threshold:
        matches += 1

# if at least one keyword is detected, print a match message
if matches > 0:
    print(f"Match found: {matches} keyword(s) detected.")
else:
    print("No match found.")