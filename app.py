from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict.html')
def inputs():
    return render_template('predict.html')

@app.route('/desc.html')
def desc():
    return render_template('desc.html')


@app.route('/predict', methods=['POST'])
def predict():
    dataf = request.form['fname']
    datal = request.form['lname']
    data1 = int(request.form['age'])
    data2 = int(request.form['gender'])
    data3 = int(request.form['chestpain'])
    data4 = int(request.form['rbp'])
    data5 = int(request.form['chol'])
    data6 = int(request.form['fbs'])
    data7 = int(request.form['recg'])
    data8 = int(request.form['hr'])
    data9 = int(request.form['ani'])
    data10 = float(request.form['oldpeak'])
    data11 = int(request.form['slope'])
    data12 = int(request.form['vessels'])
    data13 = int(request.form['thal'])

    arr = np.array([[data1, data2, data3, data4, data5, data6,
                   data7, data8, data9, data10, data11, data12, data13]])
    prediction = model.predict(arr)
    output = round(prediction[0], 2)

    return render_template('result.html', data=output, name=dataf + " " + datal)


model = pickle.load(open('model.pkl', 'rb'))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
