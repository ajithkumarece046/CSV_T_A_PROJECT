from flask import Flask, request, render_template, app, redirect

from werkzeug.utils import secure_filename

import os

import pandas as pd

recieved_df=[]
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('home_template.html')


@app.route('/upload', methods = ['POST'])
def get_df():
    global recieved_df
    if request.method == "POST":
        file = request.files['csvfile']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = os.path.join('files', filename)
            file.save(save_location)
            # return redirect('/')   
            data=pd.read_csv(save_location)
            # data.to_html(classes='table table-bordered',index=False)
            df_head=data.head(10)
            df_head_html=df_head.to_html(classes='table table-bordered',index=False)
            recieved_df = list(data.columns)
        return render_template('data_source.html', df_head_html = df_head_html)
        
@app.route('/analysis', methods = ['GET'])
def analysis():
    global recieved_df
    cols = recieved_df
    return render_template('analysis.html', cols = cols)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



