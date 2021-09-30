from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from src.get_data import read_params

# parameter path
params_path = "params.yaml"
# web app path
webapp_root = "webapp" # folder name

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates") # these are required here templeates in under webapp folder

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

# defineing predict methode
def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"] # path to molde.pkl file
    model = joblib.load(model_dir_path)
    prediction = model.predict(data) # prediction on array: data
    print(prediction)
    return prediction[0]

# api response
def api_response(request):
    try:
        data = np.array([list(request.json.values())]) # getting feature extract from dict
        response = predict(data) # predict the data
        response = {"response": response}
        return response
    except Exception as e:
        return {"error": str(e)} # showing the error.




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            if request.form:
                data = dict(request.form).values() # getting all value at once
                data = [list(map(float, data))] # creating 2d list
                response = predict(data)
                return render_template('index.html', response=response)
            elif request.json:
                response = api_response(request)
                return jsonify(response)
        except Exception as e:
            error = {"error": " SOMETHING WENT WRONG!! Try Againg"}
            return render_template("404.html", error=error) 
            
    else:
        return render_template('index.html')







if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)