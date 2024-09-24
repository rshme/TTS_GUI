from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, ttk, filedialog, Entry, Text, Button, PhotoImage, StringVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/rafiseptianhadi/CLIApps/tts_gui_ui/assets/frame0")

class CoquiUI:
    def __init__(self, window):
        self.window = window
        self.setup_window()
        self.create_canvas()
        self.create_base_widgets()
        self.create_vs_widgets()

    def setup_window(self):
        self.window.geometry("750x600")
        self.window.configure(bg="#F5F5F5")
        self.window.resizable(False, False)

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#F5F5F5",
            height=600,
            width=750,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0, 0.0, 345.0, 600.0,
            fill="#E1F5DB", outline=""
        )
        self.canvas.create_text(
            99.0, 268.0, anchor="nw",
            text="Coqui GUI",
            fill="#303030",
            font=("Inter Bold", 30 * -1)
        )
        self.canvas.create_text(
            90.0, 311.0, anchor="nw",
            text="A TTS AI Built with Coqui",
            fill="#303030",
            font=("Poppins Regular", 14 * -1)
        )
        
    def create_base_widgets(self):
        # TTS Model Selector
        self.canvas.create_text(
            366.0, 31.0, anchor="nw",
            text="Select TTS Model",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )
        self.model = ttk.Combobox(
            self.window, state="readonly",
            values=["Voice Speaking", "Voice Cloning"]
        )
        self.model.place(x=366.0, y=54.0)
        self.model.set("Voice Speaking")
        self.model.bind("<<ComboboxSelected>>", self.generateModelLayout)
        
        self.drawGenerateButton()
        
    def generateModelLayout(self, event):
        """ Switch dynamic form here between create_vs_widgets and create_vc_widgets """

    def create_vs_widgets(self):
        # Language Selector
        self.canvas.create_text(
            366.0, 104.0, anchor="nw",
            text="Select Language",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )
        self.select_lang = ttk.Combobox(
            self.window, state="readonly",
            values=["en", "ru", "ja", "zh-cn", "es", "fr", "ko"]
        )
        self.select_lang.place(x=366.0, y=127.0)

        # Text-to-Speech Area
        self.canvas.create_text(
            366.0, 177.0, anchor="nw",
            text="Text to Speech",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )
        self.textarea_bg = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(508.5, 262.5, image=self.textarea_bg)
        self.text_to_speech = Text(
            self.window, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0
        )
        self.text_to_speech.place(x=373.0, y=200.0, width=271.0, height=123.0)

        # Select Source Path
        self.drawSourcePath(posY=345.0)

        # Select Output Path
        self.drawOutputPath(posY=418.0)

    def create_vc_widgets(self):
        self.drawSourcePath(posY=104.0)
        self.drawTargetPath(posY=177.0)
        self.drawOutputPath(posY=250.0)

    def drawSourcePath(self, posY):
        self.canvas.create_text(
            366.0,
            posY,
            anchor="nw",
            text="Select source path (.wav)",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )

        self.sourcePath = StringVar()
        self.btnImageSourcePath = PhotoImage(
            file=self.relative_to_assets("button_upload.png"))
        sourcePathBtn = Button(
            image=self.btnImageSourcePath,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.sourcePath.set(filedialog.askopenfilename()),
            relief="flat"
        )
        sourcePathBtn.place(
            x=366.0,
            y=posY + 25.0,
            width=285.0,
            height=30.0
        )
    
    def drawTargetPath(self, posY):
        self.canvas.create_text(
            366.0,
            posY,
            anchor="nw",
            text="Select target path (.wav)",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )

        self.targetPath = StringVar()
        self.btnImageTargetPath = PhotoImage(
            file=self.relative_to_assets("button_upload.png"))
        targetPathBtn = Button(
            image=self.btnImageTargetPath,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.targetPath.set(filedialog.askopenfilename()),
            relief="flat"
        )
        targetPathBtn.place(
            x=366.0,
            y=posY + 25.0,
            width=285.0,
            height=30.0
        )
    
    def drawOutputPath(self, posY):
        self.canvas.create_text(
            366.0,
            posY,
            anchor="nw",
            text="Select output path",
            fill="#303030",
            font=("Poppins Regular", 12 * -1)
        )

        self.outputPath = StringVar()
        self.btnImageOutputPath = PhotoImage(
            file=self.relative_to_assets("button_upload.png"))
        outputPathBtn = Button(
            image=self.btnImageOutputPath,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.outputPath.set(filedialog.asksaveasfilename()),
            relief="flat"
        )
        outputPathBtn.place(
            x=366.0,
            y=posY + 25.0,
            width=285.0,
            height=30.0
        )

    def drawGenerateButton(self):
        self.btnImgBg = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        btnGenerate = Button(
            image=self.btnImgBg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Button generate clicked"),
            relief="flat"
        )
        btnGenerate.place(
            x=366.0,
            y=521.0,
            width=120.0,
            height=32.0
        )

    def select_source_path(self):
        return filedialog.askopenfilename()

    def select_output_path(self):
        return filedialog.asksaveasfilename()

    def generate_voice(self):
        print(self.output_path.get())
        
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)