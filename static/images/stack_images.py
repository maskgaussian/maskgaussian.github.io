from PIL import Image
import sys

def stack_images_vertically(image1_path, image2_path, output_path="stacked_image.png"):
    # Load the two images
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Ensure both images have the same width
    if img1.width != img2.width:
        raise ValueError("Images must have the same width")

    # Create a new blank image with the combined height
    combined_width = img1.width
    combined_height = img1.height + img2.height

    output_image = Image.new("RGBA", (combined_width, combined_height))

    # Paste the two images one above the other
    output_image.paste(img1, (0, 0))
    output_image.paste(img2, (0, img1.height))

    # Save the output image
    output_image.save(output_path)

    print(f"Stacked image saved as '{output_path}'")

# Example usage from command line:
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python stack_images.py image1.png image2.png [output.png]")
    else:
        image1_path = sys.argv[1]
        image2_path = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "stacked_image.png"
        stack_images_vertically(image1_path, image2_path, output_path)

