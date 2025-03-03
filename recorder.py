# Import required packages
import pyautogui
import cv2
import numpy as np
import sounddevice as sd
import wave
import threading
import moviepy.editor 
from moviepy.editor import VideoFileClip, AudioFileClip

# Specify resolution and file names
resolution = (2560, 1440)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0
audio_filename = "Recording.wav"
final_output = "FinalRecording.mp4"

# Audio configuration
audio_format = 'int16'
channels = 2  # Stereo
rate = 44100
chunk = 1024

# Global recording flag
recording = True

# Function to record audio
def record_audio():
    global recording
    frames = []
    
    def callback(indata, frame_count, time, status):
        if status:
            print(status)
        frames.append(indata.copy())

    with sd.InputStream(samplerate=rate, channels=channels, dtype=audio_format, callback=callback):
        while recording:
            sd.sleep(100)

    # Save the recorded audio
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(np.dtype(audio_format).itemsize)
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Start audio recording in a separate thread
audio_thread = threading.Thread(target=record_audio)
audio_thread.start()

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    # Capture screenshot using PyAutoGUI
    img = pyautogui.screenshot()
    
    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)
    
    # Display the live screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        recording = False
        break

# Ensure audio thread stops properly
audio_thread.join()

# Release resources
out.release()
cv2.destroyAllWindows()

# Merge audio and video using MoviePy
video_clip = VideoFileClip(filename)
audio_clip = AudioFileClip(audio_filename)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(final_output, codec="libx264")

print(f"Recording saved as: {final_output}")
