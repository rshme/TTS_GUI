import torch
from TTS.api import TTS

class VoiceCloning:
    source_path = ""
    target_path = ""
    result_path = ""

    def __init__(self, source_path, target_path, result_path) : 
        self.source_path = source_path
        self.target_path = target_path
        self.result_path = result_path

    def getDevice(self) : 
        return "cuda" if torch.cuda.is_available() else "cpu"

    def generateVoice(self) : 
        device = self.getDevice()
        tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=True).to(device)
        tts.voice_conversion_to_file(source_wav=self.target_path, target_wav=self.source_path, file_path=self.result_path)