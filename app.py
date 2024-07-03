from flask import Flask, request, render_template
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    user_code = request.form['code']

    # Capture stdout using StringIO
    buffer = io.StringIO()
    sys.stdout = buffer

    try:
        exec(user_code)  # Execute user-provided code
        output = buffer.getvalue()  # Get captured output as a string
        success_message = "Code executed successfully."
    except Exception as e:
        output = str(e)
        success_message = "Error executing code."

    # Restore original stdout
    sys.stdout = sys.__stdout__

    return render_template('result.html', output=output, success_message=success_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

