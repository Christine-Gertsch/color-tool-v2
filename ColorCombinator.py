"""
To use Color Combinator start with pressing run or cmd r.
Select the number of Colors.
Choose hues, saturations, luminances.
Check FixColor if you want to keep values.
Developed by Christine Gertsch. © 2025
"""


from colorsys import hls_to_rgb

Variable([
    dict(name="Colors", ui="RadioGroup", 
         args=dict(titles=['2', '3', '4'], isVertical=False)),
    
    dict(name="FixColor_1", ui="CheckBox"),
    dict(name="Hue_1", ui="Slider",
         args=dict(value=180, minValue=0, maxValue=360)),
    dict(name="Saturation_1", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    dict(name="Luminosity_1", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    
    dict(name="FixColor_2", ui="CheckBox"),
    dict(name="Hue_2", ui="Slider",
         args=dict(value=180, minValue=0, maxValue=360)),
    dict(name="Saturation_2", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    dict(name="Luminosity_2", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    
    dict(name="FixColor_3", ui="CheckBox"),
    dict(name="Hue_3", ui="Slider",
         args=dict(value=180, minValue=0, maxValue=360)),
    dict(name="Saturation_3", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    dict(name="Luminosity_3", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    
    dict(name="FixColor_4", ui="CheckBox"),
    dict(name="Hue_4", ui="Slider",
         args=dict(value=180, minValue=0, maxValue=360)),
    dict(name="Saturation_4", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    dict(name="Luminosity_4", ui="Slider",
         args=dict(value=50, minValue=0, maxValue=100)),
    
    dict(name="showColorNr", ui="CheckBox"),
], globals())


textX = 20
textY = 15
size(1000, 1000) # adjust size and format if needed
w, h = width(), height()


def create_color(saturation, luminosity, locked=False, Hue=None):
    # generate random Color - or keep current when FixColor
    if locked and Hue is not None:
        hue = Hue / 360
    else:
        hue = randint(0, 360) / 360
    return hls_to_rgb(hue, luminosity / 100, saturation / 100)

def print_rgb(color, number):
    rgb = tuple(round(c * 255) for c in color)
    print(f"Color {number}:")
    print(f"RGB: {rgb[0]} | {rgb[1]} | {rgb[2]}")
    print(f"Hex: {'#%02x%02x%02x' %(rgb[0], rgb[1], rgb[2])}")
    print(" ")

def draw_polygon(points, color):
    fill(*color)
    newPath()
    moveTo(points[0])
    for point in points[1:]:
        lineTo(point)
    closePath()
    drawPath()

def draw_text_label(showText, x, y, align="left"):
    fill(255)
    fontSize(30)
    text(showText, (x, y), align)


colors = [
    create_color(Saturation_1, Luminosity_1, FixColor_1, Hue_1 if FixColor_1 else None),
    create_color(Saturation_2, Luminosity_2, FixColor_2, Hue_2 if FixColor_2 else None),
    create_color(Saturation_3, Luminosity_3, FixColor_3, Hue_3 if FixColor_3 else None),
    create_color(Saturation_4, Luminosity_4, FixColor_4, Hue_4 if FixColor_4 else None)
]

num_colors = Colors + 2

# Background (= Color 1)
fill(*colors[0])
rect(0, 0, w, h)
print_rgb(colors[0], 1)

if num_colors == 2:
    fill(*colors[1])
    rect(w/2, 0, w/2, h)
    print_rgb(colors[1], 2)
    
    if showColorNr:
        draw_text_label("Color 1", textX, textY)
        draw_text_label("Color 2", w/2 + textX, textY)

elif num_colors == 3:
    draw_polygon([
        (w/2, h),
        (w/2, h * 0.6),
        (0, 0),
        (0, h)
    ], colors[1])
    
    draw_polygon([
        (w/2, h),
        (w/2, h * 0.6),
        (w, 0),
        (w, h)
    ], colors[2])
    
    print_rgb(colors[1], 2)
    print_rgb(colors[2], 3)
    
    if showColorNr:
        draw_text_label("Color 1", w/2, textY, "center")
        draw_text_label("Color 2", textX, h - 40)
        draw_text_label("Color 3", w/2 + textX, h - 40)

else:  # num_colors == 4
    fill(*colors[1])
    rect(w/2, h/2, w/2, h/2)
    
    fill(*colors[2])
    rect(0, 0, w/2, h/2)
    
    fill(*colors[3])
    rect(w/2, 0, w/2, h/2)
    
    print_rgb(colors[1], 2)
    print_rgb(colors[2], 3)
    print_rgb(colors[3], 4)
    
    if showColorNr:
        draw_text_label("Color 1", textX, h - 40)
        draw_text_label("Color 2", w/2 + textX, h - 40)
        draw_text_label("Color 3", textX, textY)
        draw_text_label("Color 4", w/2 + textX, textY)