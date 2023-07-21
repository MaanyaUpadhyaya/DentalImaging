
from docxtpl import DocxTemplate

template_path = "sample.docx"
output_path = "result.docx"


to_fill_in = {'Patient_Name': 'Hariharan', 
              'Patient_Age': '85'}


template = DocxTemplate(template_path)


template.render(to_fill_in)


output_path = "output.docx"
template.save(output_path)


