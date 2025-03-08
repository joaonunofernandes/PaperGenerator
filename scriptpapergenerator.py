from PIL import Image, ImageDraw

# Define the size of the image (A4 at 300 DPI)
width, height = 2480, 3508  # A4 size in pixels at 300 DPI

# Create a blank white image
img = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(img)

# Define line spacing and margin properties
line_spacing = 100  # pixels between lines
left_margin = 250  # pixels for the red margin line
# right_margin = width - 150  # pixels for the reg margin line
line_color = (200, 200, 255)  # light blue for horizontal lines
margin_color = (255, 0, 0)  # red for the vertical margin

# Draw the vertical margin line
draw.line([(left_margin, 0), (left_margin, height)], fill=margin_color, width=2)
#draw.line([(right_margin, 0), (right_margin, height)], fill=margin_color, width=2)

# Draw the horizontal lines
for y in range(line_spacing, height, line_spacing):
    draw.line([(0, y), (width, y)], fill=line_color, width=2)


# Save the image as a PNG
file_path = "/Users/jnf/Library/CloudStorage/OneDrive-Personal/Documentos/Paper Generator/A4_DoubleLines.png"
img.save(file_path)