import numpy as np
from flask import Flask, request, render_template
import pickle

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model from the pickle file
model = pickle.load(open('best_log_reg.pkl', 'rb'))

# Define the top 10 features that the model expects
top_10_features = ['hemo', 'sc', 'sg', 'al', 'rbc', 'htn', 'dm', 'bu', 'sod', 'bgr']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction', methods=['POST'])
def getprediction():
    # Get the form inputs and convert them to a list of floats
    input_data = [float(x) for x in request.form.values()]
    
    # Convert the input list to a NumPy array and reshape it
    final_input = np.array([input_data])
    
    # Make the prediction using the loaded model
    prediction = model.predict(final_input)
    
    # Render the result back to the 'index.html' template
    return render_template('index.html', output='Predicted Class: {}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True)
