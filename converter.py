from PIL import Image

# Open the JPG image
image = Image.open("/Users/bias./Documents/tutu_round.jpg")

# Convert to ICO and save
image.save("images/favicon/tutu.ico", format="ICO", sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])


# from PIL import Image, ImageDraw
#
#
# def make_round_image(input_path, output_path):
#     # Open the image
#     img = Image.open(input_path).convert("RGBA")
#
#     # Ensure the image is square (crop to square if needed)
#     size = min(img.size)
#     img = img.crop(((img.width - size) // 2, (img.height - size) // 2,
#                     (img.width + size) // 2, (img.height + size) // 2))
#
#     # Create a circular mask
#     mask = Image.new("L", (size, size), 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, size, size), fill=255)
#
#     # Apply the mask to the image
#     rounded_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))  # Transparent background
#     rounded_img.paste(img, (0, 0), mask)
#
#     # Save the output image
#     rounded_img.save(output_path, format="PNG")
#
#
# # Example usage
# make_round_image("/Users/bias./Documents/tutu.jpg", "/Users/bias./Documents/tutu_round.jpg")

