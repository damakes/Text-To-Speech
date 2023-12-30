from gtts import gTTS
import subprocess
import platform
import os
from gtts import gTTS
import tempfile
import platform
import os

# Finnish reader
def speak(text, output_file):
    tts = gTTS(text=text, lang="fi")
    tts.save(output_file)

    if platform.system() == 'Windows':
        os.startfile(output_file)
    else:
        subprocess.call(['xdg-open', output_file])  # Linux

# Read text from file
text_file = "tieto.txt"
with open(text_file, "r", encoding="utf-8") as file:
    text = file.read()

# Extract the directory path
directory = os.path.dirname(os.path.abspath(text_file))

# Construct the output file path
output_file = os.path.join(directory, "ulos.mp3")

# Call the speak function
speak(text, output_file)