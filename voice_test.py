from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import wave
MODEL_SIZE = "small"
SAMPLE_RATE = 16000
RECORD_SECONDS = 5
MICROPHONE_INDEX = 1

print("Loading Whisper...")
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

print("Ritt voice test ready.")
print("Speak for 5 seconds...")

audio = sd.rec(
    int(RECORD_SECONDS * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16",
    device=MICROPHONE_INDEX
)


sd.wait()

audio = audio.flatten()

with wave.open("voice_test.wav", "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio.tobytes())

segments, info = model.transcribe(
    "voice_test.wav",
    language="en",
initial_prompt="Ritt, open YouTube. Ritt, open Google. Ritt, shut down my laptop.",
    beam_size=5
)

text = " ".join(segment.text for segment in segments)

print("\nYou said:")
print(text)