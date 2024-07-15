@app.route('/cpp')
def cpp():
    return render_template('cpp.html')

@app.route('/cpp_code', methods=['POST'])
def cpp_code():
    # Get the code from the POST request
    code = request.json['code']

    # Save the code to a .cpp file
    with open("Temp.cpp", "w") as file:
        file.write(code)

    # Compile C++ code
    compile_process = subprocess.run(['g++', 'Temp.cpp', '-o', 'Temp'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        response = "Compilation Error:\n" + compile_process.stderr
    else:
        # If compilation succeeds, run the executable
        run_process = subprocess.run(['./Temp'], capture_output=True, text=True)
        if run_process.returncode == 0:
            response = "Execution Output:\n" + run_process.stdout
        else:
            response = "Runtime Error:\n" + run_process.stderr

    

    # Clean up compiled files and executables
    os.remove("Temp.cpp")
    if os.path.exists("Temp"):
        os.remove("Temp")

    return jsonify({'output': response})
