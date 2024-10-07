from PIL import Image, ImageFilter, ImageOps, ImageDraw

def add_photoroom_style_shadow(image_path, save_path, shadow_color=(0,0,0,100), shadow_blur=20, perspective=0.5):
    # Open the image
    with Image.open(image_path) as img:
        # Ensure image has an alpha channel
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create a new image for the shadow with a transparent background
        shadow = Image.new('RGBA', img.size, (0,0,0,0))
        
        # Create a drawing context
        draw = ImageDraw.Draw(shadow)
        
        # Get the bounding box of non-transparent pixels
        bbox = img.getbbox()
        
        # Draw an ellipse for the shadow
        ellipse_height = int((bbox[3] - bbox[1]) * 0.1)  # 10% of object height
        draw.ellipse([bbox[0], bbox[3], bbox[2], bbox[3] + ellipse_height], 
                     fill=shadow_color)
        
        # Apply perspective transform
        width, height = img.size
        shadow = shadow.transform(img.size, Image.PERSPECTIVE,
                                  [1, 0, 0, 0, 1, height * perspective, 0, 0], 
                                  Image.BICUBIC)
        
        # Blur the shadow
        shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur))
        
        # Create the final image
        result = Image.new('RGBA', (width, int(height * (1 + perspective))), (255,255,255,0))
        
        # Paste the shadow
        result.paste(shadow, (0, int(height * perspective)), shadow)
        
        # Paste the original image
        result.paste(img, (0, 0), img)
        
        # Save the result
        result.save(save_path)

# Usage
add_photoroom_style_shadow('./Test/Test01.out.jpeg', 'output_image_with_shadow.png')