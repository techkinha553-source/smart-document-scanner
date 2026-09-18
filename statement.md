SmartDoc Vision – Smart Document Scanner

1. Problem Statement

Taking photographs of physical documents using a mobile phone or camera often produces images that are tilted, distorted, poorly illuminated, or contain unnecessary background areas.

Manually correcting these images can be time-consuming. A document scanner should automatically identify the document area, correct its perspective, and enhance the final image so that it resembles a digitally scanned document.

The objective of SmartDoc Vision is to develop a simple Computer Vision based document scanner that automatically detects a document in an input image, removes perspective distortion, and produces an enhanced scanned version.

⸻

2. Scope of the Project

The project focuses on processing images containing a single clearly visible document.

The system performs:

* Image reading and preprocessing
* Image resizing
* Grayscale conversion
* Gaussian blurring
* Canny edge detection
* Contour detection
* Document boundary detection
* Four-corner detection
* Perspective transformation
* Image enhancement
* Adaptive thresholding
* Saving the final scanned document

The project is designed as a small academic Computer Vision application and does not aim to replace professional document-scanning software.

⸻

3. Target Users

The target users include:

* College students
* Teachers and educators
* Office users
* Researchers
* Small businesses
* Anyone who needs to digitally scan physical documents using a camera

⸻

4. High-Level Features

4.1 Automatic Document Detection

The system identifies the largest suitable four-sided contour in the input image and treats it as the document.

4.2 Edge Detection

Canny Edge Detection is used to identify strong edges in the image.

4.3 Document Boundary Detection

Contours are analyzed to locate the four corners of the document.

4.4 Perspective Correction

Perspective transformation converts a tilted document photograph into a rectangular scanned document.

4.5 Image Enhancement

The system improves the document using contrast enhancement and adaptive thresholding.

4.6 Command-Line Execution

The project can be executed completely from a terminal using a Python command.

⸻

5. Expected Output

The system takes an image such as a photograph of a document and generates a cleaned and perspective-corrected scanned document.

Example workflow:

Input Image
→ Preprocessing
→ Edge Detection
→ Contour Detection
→ Document Detection
→ Perspective Correction
→ Enhancement
→ Scanned Document

⸻

6. Limitations

The current version works best when:

* The document has a clear boundary.
* The document is reasonably separated from the background.
* The image contains one main document.
* The document has four visible corners.
* Lighting is reasonably good.

The system may have difficulty with heavily folded documents, very dark images, complex backgrounds, or multiple overlapping documents.