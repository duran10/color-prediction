from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Store the predictions in a global variable
predictions = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global predictions
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        day = request.form['day']

        # create a list of trials
        trials = list(range(1,481))

        # create a dataframe with the input data
        data = {'year': [year]*480, 'month': [month]*480, 'day': [day]*480, 'trial': trials}
        df = pd.DataFrame(data)
        scaler = StandardScaler()
        scaler.fit(df)
        df_tr = scaler.transform(df)

        # load model and predict
        model = pickle.load(open("color_model.pkl", "rb"))
        predictions = model.predict(df_tr)
        predictions = ["Red" if p == 1 else "Green" for p in predictions]

        return render_template('predict.html', predictions=predictions)
    else:
        return render_template('predict.html')

@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    global predictions
    selected_trial = int(request.form['trial_number'])
    selected_prediction = predictions[selected_trial]
    return render_template('predict.html', predictions=predictions, selected_trial=selected_trial+1, selected_prediction=selected_prediction)

if __name__ == '__main__':
    app.run()
