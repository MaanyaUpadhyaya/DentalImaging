def export_python_to_rtf(input_file, output_file):
    with open(input_file, 'r') as python_file:
        python_code = python_file.read()

    rtf_content = python_code.replace('\\', '\\\\').replace('{', '\\{').replace('}', '\\}')

    with open(output_file, 'w') as rtf_file:
        rtf_file.write(rtf_content)

# Usage:
export_python_to_rtf('demo.py', 'extract2.rtf')
