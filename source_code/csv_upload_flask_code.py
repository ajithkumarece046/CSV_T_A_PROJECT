from flask import Flask, request, render_template, app, redirect

from werkzeug.utils import secure_filename

import os

import pandas as pd


ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('home_template.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['csvfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = os.path.join('files', filename)
            file.save(save_location)
            return redirect('/')     
           

                     


    return render_template('data_source.html')        








    # if csv_file:
    #     return 'CSV file uploaded and processed successfully.'
    # else:
    #     return 'No CSV file selected.'      

if __name__ == '__main__':

    app.run(debug=True, port=5000)
