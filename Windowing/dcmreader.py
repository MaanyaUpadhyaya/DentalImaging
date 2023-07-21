import pydicom
import cv2
import numpy as np

def apply_window(pixel_array, window_center, window_width):
   
    window_min = window_center - window_width / 2
    window_max = window_center + window_width / 2
    pixel_array = np.clip(pixel_array, window_min, window_max)
    pixel_array = (pixel_array - window_min) / (window_max - window_min)
    pixel_array = np.clip(pixel_array, 0.0, 1.0)
    return pixel_array


ds = pydicom.read_file("3DSlice1.dcm")

window_center = ds.WindowCenter
window_width = ds.WindowWidth

pixel_array = ds.pixel_array

windowed_pixel_array = apply_window(pixel_array, window_center, window_width)

windowed_pixel_array = (windowed_pixel_array * 255).astype(np.uint8)

cv2.imwrite("windowed_image.jpg", windowed_pixel_array)
from docxtpl import DocxTemplate
from docxtpl import InlineImage

template_path = "template.docx"
output_path = "result.docx"

to_fill_in = {'img1': 'windowed_image.jpg',
              'img2': 'bg1.jpg'}

template = DocxTemplate(template_path)

for key, value in to_fill_in.items():
    image = InlineImage(template, value)
    context = {key: image}
    template.render(context)

template.save(output_path)