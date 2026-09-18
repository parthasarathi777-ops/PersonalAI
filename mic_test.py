import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Listening... Speak now!")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("❌ I couldn't understand you.")

except sr.RequestError as e:
    print("❌ Speech recognition service error:", e)
    