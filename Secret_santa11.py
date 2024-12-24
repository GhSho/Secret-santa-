from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mapping of unique ID to the recipien.

# Import the mapping from the shuffled file
from gifting_mapping import gifting_mapping

@app.route('/')
def index():
    return render_template('index.html', error_message=None)

@app.route('/get_id', methods=['POST'])
def get_id():
    unique_id = request.form.get('unique_id')
    if unique_id in gifting_mapping:
        recipient = gifting_mapping[unique_id]
        return render_template('gift.html', recipient=recipient)
    else:
        error_message = "Invalid ID. Please try again."
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
