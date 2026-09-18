import sys
import os

from scanner import scan_document


def main():

    print("=" * 50)
    print("        SMARTDOC VISION")
    print("     Smart Document Scanner")
    print("=" * 50)

    # Check command-line argument
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("python app.py <input_image>")
        print("\nExample:")
        print("python app.py input/document.jpg")
        return

    input_path = sys.argv[1]

    # Check input file
    if not os.path.exists(input_path):
        print(f"\nError: File not found: {input_path}")
        return

    # Create output directory if necessary
    os.makedirs("output", exist_ok=True)

    output_path = "output/scanned_document.jpg"

    print(f"\nInput : {input_path}")
    print("Processing document...")

    success = scan_document(
        input_path,
        output_path
    )

    if success:
        print("\n" + "=" * 50)
        print("SUCCESS")
        print("=" * 50)
        print(f"Scanned document: {output_path}")
        print("Detected boundary: output/detected_document.jpg")
    else:
        print("\nScanning failed.")


if __name__ == "__main__":
    main()