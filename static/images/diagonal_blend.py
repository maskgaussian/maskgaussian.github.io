import cv2
import numpy as np
import argparse

def diagonal_split_blend(image1_path, image2_path, output_path):
    # Load images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)
    
    if img1 is None or img2 is None:
        raise ValueError("Error loading images. Please check the file paths.")
    
    # Ensure images are the same size
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions.")
    
    h, w, _ = img1.shape
    
    # Create a mask with a diagonal split
    mask = np.zeros((h, w), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            if y > (h/w) * x:  # Defines the diagonal line
                mask[y, x] = 255
    
    # Convert mask to 3-channel
    mask_3ch = cv2.merge([mask, mask, mask])
    
    # Apply the mask to create the blended image
    result = np.where(mask_3ch == 255, img1, img2)
    
    # Save the output
    cv2.imwrite(output_path, result)
    print(f"Output saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blend two images with a diagonal split.")
    parser.add_argument("image1", help="Path to the first image")
    parser.add_argument("image2", help="Path to the second image")
    parser.add_argument("output", help="Path to save the output image")
    
    args = parser.parse_args()
    diagonal_split_blend(args.image1, args.image2, args.output)

