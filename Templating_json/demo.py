import json
import pydicom
from docxtpl import DocxTemplate

def read_dcm_file(dcm_file, parameters):
    ds = pydicom.dcmread(dcm_file) 
    print(ds)
    attributes = {}
    for param in parameters:
        attributes[param['name']]=ds[param['name']].value
        print(attributes[param['name']])
        print(ds[param['name']].value)
    return attributes


dcm_file = '3DSlice2.dcm'
json_file = 'middle.json'
template_file = 'dental_Report_template.docx'

with open(json_file) as f:
    json_data = json.load(f)

    attribute_tags = json_data['content']

    attributes = read_dcm_file(dcm_file, attribute_tags)

print("Attributes from DICOM file:", attributes)


template = DocxTemplate(template_file)
template.render(attributes)

output_file = "output2.docx"
template.save(output_file)
print("Values filled in the Word document.")