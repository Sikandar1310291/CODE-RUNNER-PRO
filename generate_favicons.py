from PIL import Image
import os

def generate_favicons(source_image_path):
    if not os.path.exists(source_image_path):
        print(f"Error: {source_image_path} not found.")
        return

    img = Image.open(source_image_path)
    
    # Ensure it's square, if not, crop center
    width, height = img.size
    if width != height:
        new_size = min(width, height)
        left = (width - new_size)/2
        top = (height - new_size)/2
        right = (width + new_size)/2
        bottom = (height + new_size)/2
        img = img.crop((left, top, right, bottom))
    
    sizes = [48, 96, 192, 512]
    
    # Generate PNGs
    for size in sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(f"favicon-{size}x{size}.png")
        print(f"Created favicon-{size}x{size}.png")

    # Generate ICO (16, 32, 48)
    img.save("favicon.ico", format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("Created favicon.ico")

if __name__ == "__main__":
    generate_favicons("logo.png")
