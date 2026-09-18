import cv2
import numpy as np


def resize_image(image, width=1000):
    """Resize image while maintaining aspect ratio."""

    height, current_width = image.shape[:2]

    if current_width <= width:
        return image

    ratio = width / current_width
    new_height = int(height * ratio)

    return cv2.resize(image, (width, new_height))


def order_points(points):
    """Order points as top-left, top-right, bottom-right, bottom-left."""

    points = np.array(points, dtype=np.float32)

    ordered = np.zeros((4, 2), dtype=np.float32)

    sums = points.sum(axis=1)
    differences = np.diff(points, axis=1).flatten()

    ordered[0] = points[np.argmin(sums)]          # Top-left
    ordered[2] = points[np.argmax(sums)]          # Bottom-right
    ordered[1] = points[np.argmin(differences)]  # Top-right
    ordered[3] = points[np.argmax(differences)]  # Bottom-left

    return ordered


def four_point_transform(image, points):
    """Apply perspective transformation."""

    rect = order_points(points)

    top_left, top_right, bottom_right, bottom_left = rect

    width_top = np.linalg.norm(top_right - top_left)
    width_bottom = np.linalg.norm(bottom_right - bottom_left)

    max_width = max(int(width_top), int(width_bottom))

    height_right = np.linalg.norm(bottom_right - top_right)
    height_left = np.linalg.norm(bottom_left - top_left)

    max_height = max(int(height_right), int(height_left))

    destination = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(
        rect,
        destination
    )

    warped = cv2.warpPerspective(
        image,
        matrix,
        (max_width, max_height)
    )

    return warped


def find_document_contour(image):
    """
    Detect the largest document-like contour.

    Several preprocessing methods are tried so that
    the scanner works with different lighting conditions.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(
        blurred,
        50,
        150
    )

    # Close small gaps in document edges
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (5, 5)
    )

    edges = cv2.morphologyEx(
        edges,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    # Find external contours
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Sort by area
    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    image_area = image.shape[0] * image.shape[1]

    # Try the largest contours
    for contour in contours[:20]:

        area = cv2.contourArea(contour)

        # Document should occupy a reasonable portion
        # of the image.
        if area < image_area * 0.08:
            continue

        perimeter = cv2.arcLength(
            contour,
            True
        )

        approximation = cv2.approxPolyDP(
            contour,
            0.03 * perimeter,
            True
        )

        # Direct 4-corner detection
        if len(approximation) == 4:
            return approximation.reshape(4, 2)

    # Fallback:
    # If exact 4-corner detection fails, use
    # the minimum-area rectangle around the largest
    # suitable contour.
    for contour in contours[:10]:

        area = cv2.contourArea(contour)

        if area < image_area * 0.20:
            continue

        rectangle = cv2.minAreaRect(contour)

        box = cv2.boxPoints(rectangle)

        box = np.int32(box)

        return box

    return None


def enhance_document(document):
    """Enhance the scanned document."""

    gray = cv2.cvtColor(
        document,
        cv2.COLOR_BGR2GRAY
    )

    # Improve local contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Adaptive threshold
    scanned = cv2.adaptiveThreshold(
        enhanced,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        21,
        10
    )

    return scanned


def scan_document(input_path, output_path):

    image = cv2.imread(input_path)

    if image is None:
        print("Error: Could not read the input image.")
        return False

    # Resize image
    image = resize_image(image)

    # Find document
    document_points = find_document_contour(image)

    if document_points is None:
        print("Error: Document boundary could not be detected.")
        print()
        print("Tips:")
        print("- Place the document on a contrasting background.")
        print("- Make sure all four corners are visible.")
        print("- Avoid very dark or blurry images.")
        return False

    # Create detection preview
    preview = image.copy()

    cv2.polylines(
        preview,
        [document_points.astype(np.int32)],
        True,
        (0, 255, 0),
        4
    )

    cv2.imwrite(
        "output/detected_document.jpg",
        preview
    )

    # Perspective correction
    scanned = four_point_transform(
        image,
        document_points
    )

    # Enhancement
    enhanced = enhance_document(
        scanned
    )

    # Save final document
    cv2.imwrite(
        output_path,
        enhanced
    )

    print()
    print("Document scanning completed successfully.")
    print(f"Output saved at: {output_path}")
    print("Detected boundary saved at: output/detected_document.jpg")

    return True