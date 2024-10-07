from PIL import ImageOps, Image, ImageFilter

FG_IMG_PATH = "./Test/Test01.out.jpeg"
BG_IMG_PATH = "./Templates/background.jpg"

def load_image(path):
    """Load an image using PIL."""
    return Image.open(path)

def extract_alpha(image):
    """Extract the alpha channel from an image."""
    return image.split()[-1]

def create_shadow_from_alpha(alpha, blur_radius):
    """Create a shadow based on a blurred version of the alpha channel."""
    alpha_blur = alpha.filter(ImageFilter.BoxBlur(blur_radius))
    shadow = Image.new(mode="RGB", size=alpha_blur.size)
    shadow.putalpha(alpha_blur)
    return shadow

def composite_images(bg, fg, shadow):
    """Composite the shadow and foreground onto the background."""
    bg.paste(shadow, (0, 0), shadow)
    bg.paste(fg, (0, 0), fg)
    return bg

if __name__ == "__main__":
    # Load the images
    fg = load_image(FG_IMG_PATH)
    #bg = load_image(BG_IMG_PATH)
    
    bg = Image.new("RGB", fg.size, (255, 255, 255))

    # Create the shadow based on the alpha channel of the foreground
    alpha = extract_alpha(fg)
    shadow = create_shadow_from_alpha(alpha, blur_radius=25)

    # Composite the shadow and foreground onto the background
    final_image = composite_images(bg, fg, shadow)

    # Display the final image (optional)
    final_image.show()

