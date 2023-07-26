def export_function_output_to_rtf(input_file, output_file):
    with open(input_file, 'r') as python_file:
        python_code = python_file.read()

    code_globals = {}
    exec(python_code, code_globals)

    function_name = 'find_point_distances'
    if function_name in code_globals:
        function = code_globals[function_name]
        function_output = function('dental.xml')
        output_string = str(function_output)
        with open(output_file, 'w') as rtf_file:
            rtf_file.write(output_string)


export_function_output_to_rtf('extract1.py', 'results.rtf')
