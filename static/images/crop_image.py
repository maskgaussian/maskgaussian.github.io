from PIL import Image
import sys

def crop_image(image_path, width_start, width_end, height_start, height_end, output_path="cropped_image.png"):
    # Load the image
    img = Image.open(image_path)

    # Validate percentage inputs
    if not (0 <= width_start < width_end <= 100 and 0 <= height_start < height_end <= 100):
        raise ValueError("Percentages must be between 0 and 100, and start must be less than end.")

    # Convert percentages to pixel coordinates
    left = int(img.width * (width_start / 100))
    right = int(img.width * (width_end / 100))
    top = int(img.height * (height_start / 100))
    bottom = int(img.height * (height_end / 100))

    # Perform cropping
    cropped_img = img.crop((left, top, right, bottom))

    # Save the output image
    cropped_img.save(output_path)

    print(f"Cropped image saved as '{output_path}'")

# Example usage from command line:
if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python crop_image.py image.png width_start width_end height_start height_end [output.png]")
    else:
        image_path = sys.argv[1]
        width_start = float(sys.argv[2])
        width_end = float(sys.argv[3])
        height_start = float(sys.argv[4])
        height_end = float(sys.argv[5])
        output_path = sys.argv[6] if len(sys.argv) > 6 else "cropped_image.png"

        crop_image(image_path, width_start, width_end, height_start, height_end, output_path)

