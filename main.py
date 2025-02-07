import pytesseract
from PIL import ImageGrab
import pyperclip
import os
from convert import convert
# Set the path to Tesseract executable (just the executable name)
pytesseract.pytesseract.tesseract_cmd = '/home/mohammad/apps/tesseract/tesseract-5.5.0-x86_64.AppImage'  # Ensure tesseract is in your PATH

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, 'files')
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

 

def extract_text_from_clipboard_image():
    # Grab the image from the clipboard
    image = ImageGrab.grabclipboard()

    if image is None:
        print("No image found in clipboard.")
        return

    # Convert the image to text using Tesseract OCR
    text = pytesseract.image_to_string(image).replace("\n"," ")
    print("Extracted Text:")
    print(text)

    # Optionally, copy the extracted text back to clipboard
    pyperclip.copy(text)
    print("Text copied to clipboard. You can paste it using Ctrl + V.")

    # Convert text to MP3
    convert(text)
    

if __name__ == "__main__":
    extract_text_from_clipboard_image()
