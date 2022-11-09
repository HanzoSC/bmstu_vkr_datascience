from flask import Flask, request, render_template

import tensorflow as tf

app = Flask(__name__)


@app.route('/')
def choose_prediction_method():
    return render_template('main.html')


def mn_prediction(params):
    model = tf.keras.models.load_model('models/mn_model_0.73')
    pred = model.predict([params])
    return pred


@app.route('/mn/', methods=['POST', 'GET'])
def mn_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('plot', 'mup', 'ko', 'seg', 'tv', 'pp', 'mup', 'pr', 'ps', 'yn', 'shn', 'pln')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Спрогнозированное Соотношение матрица-наполнитель для введенных параметров: {mn_prediction(params)}'
    return render_template('mn.html', message=message)


if __name__ == '__main__':
    app.run()
