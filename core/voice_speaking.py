import torch
from TTS.api import TTS

class VoiceSpeaking:
    text = ""
    language = ""
    source_path = ""
    result_path = ""

    def __init__(self, text, language, source_path, result_path) : 
        self.text = text
        self.language = language
        self.source_path = source_path
        self.result_path = result_path

    def getDevice(self) : 
        return "cuda" if torch.cuda.is_available() else "cpu"

    def generateVoice(self) : 
        device = self.getDevice()
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
        tts.tts_to_file(text=self.text, speaker_wav=self.source_path, language=self.language, file_path=self.result_path)