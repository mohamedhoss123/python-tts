# Image-to-Speech with Clipboard and Text Extraction

**Important:** This project requires Python 3.11.

This project allows you to capture images from your clipboard, extract text from those images, and then generate text-to-speech (TTS) audio from the extracted text.

## How to Use

1. **Configure Tesseract:**

   You need to tell the `pytesseract` library where to find your Tesseract installation.  Open `main.py` and set the `pytesseract.pytesseract.tesseract_cmd` variable to the correct path.

   For example:

   ```python
   pytesseract.pytesseract.tesseract_cmd = '/home/mohammad/apps/tesseract/tesseract-5.5.0-x86_64.AppImage'  # Example path
   ```
2. **Install Dependencies:**

   The project's dependencies are listed in `requirements.txt`.  You can install them using `pip`:

   ```bash
   pip install -r requirements.txt