from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/python')
def python_editor():
    return render_template('python.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json['code']
    process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return jsonify({'output': output, 'error': error})


@app.route('/java')
def java_editor():
    return render_template('java.html')

@app.route('/runcode', methods=['POST'])
def runcode():
    code = request.json['code']

    # Save the code to a .java file
    with open("Temp.java", "w") as file:
        file.write(code)
    
    # Compile Java code
    compile_process = subprocess.Popen(['javac', 'Temp.java'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    compile_output, compile_error = compile_process.communicate()

    if compile_error:
        return jsonify({'output': '', 'error': compile_error})

    # Run Java program
    run_process = subprocess.Popen(['java', 'Temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = run_process.communicate()

    # Clean up .class files
    if os.path.exists("Temp.class"):
        os.remove("Temp.class")

    return jsonify({'output': output, 'error': error})

@app.route('/c')
def c():
    return render_template('C.html')

@app.route('/code', methods=['POST'])
def code():
    code = request.json['code']

    # Save the code to a .c file
    with open("Temp.c", "w") as file:
        file.write(code)
    
    # Compile C code
    compile_process = subprocess.Popen(['gcc', '-o', 'Temp', 'Temp.c'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    compile_output, compile_error = compile_process.communicate()

    if compile_error:
        return jsonify({'output': '', 'error': compile_error})

    # Run C program
    run_process = subprocess.Popen(['./Temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = run_process.communicate()

    # Clean up compiled files
    if os.path.exists("Temp"):
        os.remove("Temp")
    if os.path.exists("Temp.c"):
        os.remove("Temp.c")

    return jsonify({'output': output, 'error': error})
@app.route('/htmlcss')
def htmlcss():
    # Serve a page with HTML and CSS editors
    return render_template('htmlcss.html')

@app.route('/html_css_code', methods=['POST'])
def html_css_code():
    # Retrieve HTML and CSS from the request
    html_code = request.json.get('html', '')
    css_code = request.json.get('css', '')

    # Embed the CSS into the HTML
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        {css_code}
        </style>
    </head>
    <body>
        {html_code}
    </body>
    </html>
    """

    # Send the complete HTML back to the client
    return jsonify({'renderedHtml': full_html})

@app.route('/javascript')
def javascript():
    return render_template('javascript.html')
@app.route('/javascript_code', methods=['POST'])
def javascript_code():
    # Retrieve JavaScript code from the request
    js_code = request.json.get('js', '')

    # Template for the HTML with embedded JavaScript
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JavaScript Execution</title>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-12">
                    <textarea id="codeEditor" class="form-control" rows="10" placeholder="Write your JavaScript code here..."></textarea>
                    <button id="runButton" class="btn btn-primary mt-3">Run</button>
                    <textarea id="outputArea" class="form-control mt-3" rows="5" readonly></textarea>
                </div>
            </div>
        </div>
        <script>
            document.getElementById('runButton').addEventListener('click', function() {{
                try {{
                    const userCode = document.getElementById('codeEditor').value;
                    const output = eval(userCode);
                    document.getElementById('outputArea').value = output;
                }} catch (error) {{
                    document.getElementById('outputArea').value = 'Error: ' + error;
                }}
            }});
        </script>
        <script>
        {js_code}
        </script>
    </body>
    </html>
    """

    # Send the complete HTML back to the client
    return jsonify({'renderedHtml': full_html})
@app.route('/cpp')
def cpp():
    return render_template('cpp.html')

@app.route('/cpp_code', methods=['POST'])
def cpp_code():
    code = request.json['code']
    with open("Temp.cpp", "w") as file:
        file.write(code)
    
    # Compile C++ code
    compile_process = subprocess.Popen(['g++', 'Temp.cpp', '-o', 'Temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    compile_output, compile_error = compile_process.communicate()

    if compile_error:
        return jsonify({'error': compile_error})
    else:
        # Run C++ program
        run_process = subprocess.Popen(['./Temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = run_process.communicate()
        if error:
            return jsonify({'error': error})
        else:
            return jsonify({'output': output})
        if os.path.exists("Temp"):
                os.remove("Temp")
        if os.path.exists("Temp.cpp"):
            os.remove("Temp.cpp")



@app.route('/ruby')



def ruby():
    return render_template('ruby.html')
@app.route('/run_ruby_code', methods=['POST'])
def run_ruby_code():
    code = request.json['code']
    with open("Temp.rb", "w") as file:
        file.write(code)

    # Execute Ruby code
    run_process = subprocess.run(['ruby', 'Temp.rb'], capture_output=True, text=True)
    response = run_process.stderr if run_process.stderr else run_process.stdout

    # Clean up .rb files
    os.remove("Temp.rb")

    return jsonify({'output': response})

@app.route('/r')
def r():
    return render_template('r.html')
@app.route('/run_r_code', methods=['POST'])
def run_r_code():
    code = request.json['code']
    with open("Temp.R", "w") as file:
        file.write(code)

    # Execute R code
    run_process = subprocess.run(['Rscript', 'Temp.R'], capture_output=True, text=True)
    response = run_process.stderr if run_process.stderr else run_process.stdout

    # Clean up .rb files
    os.remove("Temp.R")

    return jsonify({'output': response})
@app.route('/php')
def php():
    return render_template('php.html')
@app.route('/run_php_code', methods=['POST'])
def run_php_code():
    code = request.json['code']
    with open("Temp.php", "w") as file:
        file.write(code)

    # Execute PHP code
    run_process = subprocess.run(['php', 'Temp.php'], capture_output=True, text=True)
    response = run_process.stderr if run_process.stderr else run_process.stdout

    # Clean up the temporary PHP file
    os.remove("Temp.php")

    return jsonify({'output': response})



if __name__ == '__main__':
    app.run(debug=True)