from PIL import Image
import os

def convert_to_square(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file
    for file in files:
        if file.lower().endswith(".webp"):
            # Open the image
            image_path = os.path.join(input_folder, file)
            img = Image.open(image_path)

            # Determine the longer and shorter sides of the image
            max_side = max(img.size)
            min_side = min(img.size)

            # Create a new blank square image
            new_img = Image.new("RGBA", (max_side, max_side), (0, 0, 0, 0))

            # Calculate the position to center the original image within the square
            position = ((max_side - img.width) // 2, (max_side - img.height) // 2)

            # Paste the original image onto the blank square
            new_img.paste(img, position)

            # Save the result in the output folder
            output_path = os.path.join(output_folder, file)
            new_img.save(output_path, "webp")

if __name__ == "__main__":
    input_folder = "./assets/images"
    output_folder = "./assets/contain-images"

    convert_to_square(input_folder, output_folder)
