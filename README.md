SmartDoc Vision – Smart Document Scanner

Overview

SmartDoc Vision is a Computer Vision based document scanner developed using Python and OpenCV.

The system takes a photograph of a physical document as input and automatically detects the document boundary. It then corrects perspective distortion and enhances the document to produce a clean scanned version.

The project demonstrates several fundamental Computer Vision techniques including image preprocessing, Canny edge detection, contour detection, perspective transformation, contrast enhancement, and adaptive thresholding.

⸻

Features

* Automatic document boundary detection
* Canny edge detection
* Contour detection
* Four-corner document detection
* Perspective correction
* Contrast enhancement
* Adaptive thresholding
* Clean scanned document generation
* Command-line execution
* No GUI-based setup required

⸻

Technologies and Tools Used

Programming Language

* Python 3

Libraries

* OpenCV
* NumPy

Development Tools

* Visual Studio Code
* Git
* GitHub

⸻

Project Structure

smart-document-scanner/
│
├── app.py
├── scanner.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
│
├── input/
│   └── .gitkeep
│
├── output/
│   └── .gitkeep
│
└── screenshots/
    └── .gitkeep

⸻

Installation and Setup

Step 1: Clone the Repository

Clone the repository using:

git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd smart-document-scanner

⸻

Step 2: Create a Virtual Environment

Create a Python virtual environment:

macOS/Linux

python3 -m venv venv

Activate it:

source venv/bin/activate

Windows

python -m venv venv

Activate it:

venv\Scripts\activate

⸻

Step 3: Install Dependencies

Install the required libraries:

pip install -r requirements.txt

⸻

How to Run the Project

Step 1: Add an Input Image

Place a photograph of a document inside the input folder.

For example:

input/document.jpg

The document should be clearly visible and preferably have a contrasting background.

⸻

Step 2: Run the Scanner

From the project root directory, execute:

macOS/Linux

python3 app.py input/document.jpg

Windows

python app.py input/document.jpg

⸻

Step 3: Check the Output

If the document is successfully detected, the processed image will be saved at:

output/scanned_document.jpg

The detected document boundary will also be saved at:

output/detected_document.jpg

⸻

Testing Instructions

Test Case 1 – Clear Document

Use a photograph containing one clearly visible rectangular document.

Expected result:

* Document boundary should be detected.
* Perspective should be corrected.
* Enhanced scanned image should be generated.

⸻

Test Case 2 – Tilted Document

Use a document photographed at an angle.

Expected result:

* Four document corners should be detected.
* Perspective transformation should convert the document into a rectangular shape.

⸻

Test Case 3 – Invalid Image

Run the program using a nonexistent file:

python app.py input/not_found.jpg

Expected result:

Error: File not found

⸻

Test Case 4 – Document Not Detected

Use an image where the document boundary is unclear.

Expected result:

Error: Document boundary could not be detected.

⸻

Computer Vision Pipeline

The project follows the following processing pipeline:

Input Image
     ↓
Image Resizing
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Contour Detection
     ↓
Document Boundary Detection
     ↓
Perspective Transformation
     ↓
Contrast Enhancement
     ↓
Adaptive Thresholding
     ↓
Scanned Document

⸻

Computer Vision Techniques

1. Grayscale Conversion

The input image is converted from a color image into grayscale.

This simplifies processing by reducing the image from three color channels to one intensity channel.

⸻

2. Gaussian Blur

Gaussian blur reduces noise in the image before edge detection.

This helps produce cleaner edges.

⸻

3. Canny Edge Detection

Canny Edge Detection identifies strong intensity changes in the image.

These edges are useful for finding the boundaries of the document.

⸻

4. Contour Detection

Contours represent continuous boundaries around objects.

The project searches through detected contours and looks for a large contour having approximately four corners.

⸻

5. Perspective Transformation

A photograph may show a rectangular document as a distorted quadrilateral because of the camera angle.

Perspective transformation maps the four detected corners into a rectangular output.

⸻

6. Image Enhancement

The scanned document is converted to grayscale and enhanced using CLAHE.

Adaptive thresholding is then applied to produce a cleaner document appearance.

⸻

Output

The application generates:

output/scanned_document.jpg

and:

output/detected_document.jpg

The first file is the final scanned document.

The second file shows the detected document boundary.

⸻

Limitations

The system works best with:

* One document per image
* Clearly visible document boundaries
* Four visible document corners
* Reasonable lighting
* Limited background clutter

It may not work correctly when:

* Multiple documents overlap.
* The document has no clear boundary.
* The image is extremely dark.
* The document is heavily folded.
* One or more corners are hidden.

⸻

Future Improvements

Possible future improvements include:

* Real-time camera scanning
* Multiple document detection
* Automatic rotation correction
* PDF generation
* OCR-based text extraction
* Automatic shadow removal
* Mobile application
* Web-based interface
* Machine-learning based document detection

⸻

Conclusion

SmartDoc Vision demonstrates how fundamental Computer Vision techniques can be combined to create a practical document-scanning application.

The project detects the document boundary, corrects perspective distortion, enhances the image, and generates a digital scanned document using Python and OpenCV.

⸻

Author

Nikhil 

Computer Science and Engineering

⸻

License

This project is developed for academic and educational purposes.