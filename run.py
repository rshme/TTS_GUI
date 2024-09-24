import tkinter as tk
from core.voice_speaking import VoiceSpeaking
from core.ui import CoquiUI

# Text to speech to a file
text = """
That's great dedication! Here are a few suggestions to help you learn English like a native speaker:

1. Practice Speaking Daily: Try to have conversations in English as much as possible. If you don't have someone to practice with, you can record yourself or use language exchange apps.

2. Immerse Yourself in English: Watch movies, TV shows, and YouTube videos in English. Pay attention to how native speakers pronounce words and phrases. Try to mimic their pronunciation and intonation.

3. Read Regularly: Read books, articles, or blogs in English. This will help you expand your vocabulary and understand sentence structure. Start with topics that interest you to keep it enjoyable.

4. Listen to Podcasts or Audiobooks: Listening to native speakers will help you get used to the rhythm and flow of the language. Choose topics that interest you to keep it engaging.

5. Practice Writing: Write a journal or short stories in English. This will help you improve your grammar and sentence structure. You can also ask someone to review your writing for feedback.

6. Join Online Communities: Participate in English-speaking forums or social media groups. Engaging in discussions with native speakers will help you practice real-life communication.

7. Use Language Learning Apps: Apps like Duolingo, Babbel, or Anki can be great for vocabulary building and grammar practice.

8. Stay Consistent: Consistency is key. Even on days when you're busy or tired, try to do at least a little practice.

Would you like to focus on any specific area today, like speaking, listening, or writing?
"""

# voiceSpeaking = VoiceSpeaking(text=text, language="en", source_path="./sources/changli-voice.wav", result_path="./outputs/changli-result-class.wav")
# voiceSpeaking.generateVoice()

# Text to speech to a file
# Init TTS Conversation
# tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=True).to(device)
# tts.voice_conversion_to_file(source_wav="./targets/bebi-short-wav.wav", target_wav="./sources/ayaka-voice-wav.wav", file_path="./outputs/ayaka-sx-wav.wav")

if __name__ == "__main__":
    window = tk.Tk()
    app = CoquiUI(window)
    window.mainloop()
