import pydicom
import cv2
import numpy as np
from PIL import Image,ImageDraw
from docxtpl import DocxTemplate
from docxtpl import InlineImage

def draw_line(image, p1, p2):
    draw = ImageDraw.Draw(image)
    draw.line([p1, p2], fill='green', width=3)
    return image

def add_text(image,pt,text_to_display):
    I1 = ImageDraw.Draw(image)
    I1.text(pt, text_to_display, fill="green")
    return image

def apply_window(pixel_array, window_center, window_width):
    window_min = window_center - window_width / 2
    window_max = window_center + window_width / 2
    pixel_array = np.clip(pixel_array, window_min, window_max)
    pixel_array = (pixel_array - window_min) / (window_max - window_min)
    pixel_array = np.clip(pixel_array, 0.0, 1.0)
    return pixel_array

def fillimage_report(template_path, to_fill_in, output_path):
    template = DocxTemplate(template_path)
    context={}
    for key, value in to_fill_in.items():
        image = InlineImage(template, value)
        context[key] = image
    template.render(context)
    template.save(output_path)


ds = pydicom.read_file("3DSlice1.dcm")
window_center = ds.WindowCenter
window_width = ds.WindowWidth

pixel_array = ds.pixel_array
windowed_pixel_array = apply_window(pixel_array, window_center, window_width)

windowed_pixel_array = (windowed_pixel_array * 255).astype(np.uint8)
cv2.imwrite("windowed_image.jpg", windowed_pixel_array)

image = Image.open("windowed_image.jpg")
image = image.convert('RGB')
image = draw_line(image, (100,200), (200,300))

rows = ds.Rows
columns = ds.Columns

point1 = (rows // 2, 0)
point2 = (0, columns // 2)
point3 = (rows // 2, columns)
point4 = (rows, columns // 2)

image = add_text(image, (200,300), "200mm")
image = add_text(image, (169,0), "H")
image = add_text(image, (0,169), "R")
image = add_text(image, (169,330), "F")
image = add_text(image, (330,169), "L")

image.save("result.jpg")

to_fill_in = {'img1': 'result.jpg',
              'img2': 'result.jpg'}

fillimage_report("template.docx", to_fill_in, "result.docx")

