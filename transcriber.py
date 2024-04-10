# import openai

# #Convertir audio en texto
# class Transcriber:
#     def __init__(self):
#         pass
        
#     #Siempre guarda y lee del archivo audio.mp3
#     #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
#     def transcribe(self, audio):
#         audio.save("audio.mp3")
#         audio_file= open("audio.mp3", "rb")
#         transcript = openai.Audio.transcribe("whisper-1", audio_file)
#         return transcript.text



# import speech_recognition as sr
# from pydub import AudioSegment
# import io






# class Transcriber:
#     def __init__(self):
#         pass
        
#     #Siempre guarda y lee del archivo audio.mp3
#     #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
#     def transcribe(self, audio):
        
#         audio_bytes = audio.read()

#         # Convertir los bytes a un objeto AudioSegment de pydub
#         audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")

#         # Guardar el audio como un archivo WAV temporal
#         audio_wav_temp = io.BytesIO()
#         audio_segment.export(audio_wav_temp, format="wav")
#         audio_wav_temp.seek(0)

#         # Convertir el archivo WAV temporal a texto utilizando SpeechRecognition
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(audio_wav_temp) as source:
#             audio_data = recognizer.record(source)
#             text = recognizer.recognize_google(audio_data)
#             return text



import pyttsx3
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

print(voices)

author = "Tony"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    speak(f"Welcome {author}, I am jarvis")

   

