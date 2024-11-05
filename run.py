import tkinter as tk
from core.voice_speaking import VoiceSpeaking
from core.ui import CoquiUI

# Text to speech to a file
text = """
The Echo of Time

Time drifts, like rivers sweeping past,
a silent surge, swift yet so vast.
In moments, we clutch for sands that fall,
and memories, like shadows, call.

Yesterday's laughter, bright and bold,
now softened, tinged in shades of old.
The echoes fade but never die,
they linger, wrapped in a quiet sigh.

Faces and places blur and blend,
forgotten smiles, the curve of a friend—
in corners of mind, they patiently wait,
frozen in snapshots, dusted by fate.

For time slips slyly from our grip,
a lover we can't hold or sip.
It trickles, it tumbles, unbidden, unseen,
yet in memory’s flicker, it’s sharp and keen.

So I carry it all, my years, my scars,
in a pocket stitched with gentle stars,
a tapestry woven of joy and ache,
all the things that time can’t take.

And when I turn to face the past,
the shadows smile, they hold fast.
Time may flow, may carry, may bind—
but memories, dear, live outside of mind.
"""

# Text to speech to a file
# Init TTS Conversation
# tts = TTS("tts_models/eng/fairseq/vits").to("cuda")
# tts.tts_with_vc_to_file(text, speaker_wav="./sources/source-voice.wav", file_path="./outputs/target.wav")

if __name__ == "__main__":
    window = tk.Tk()
    app = CoquiUI(window)
    window.mainloop()
