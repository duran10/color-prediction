# Color Prediction Webapp
This webapp is built using Flask, a Python web framework, and HTML for the front-end. The app uses a Random Forest model to predict the colors based on the date and trial entered by the user.

### Running the Flask App
To run the Flask app, you will need to have Python and Flask installed on your machine. You can check if you have Python installed by running python --version in your command line. If it is not installed, you can download it from the official website: https://www.python.org/downloads/. The python code for the flask was made with python version 3.11.

Once you have Python installed, you can install Flask by running in your command line:

pip install flask

The next step is to download the all the files in the repository including the folder of templates.

### File description
color_flask.py : Is the flask code you should run to access the webapp.

color_model.pkl : Is the Random Forest model the webapp is going to use to predict the colors of each date and trial.

Templates Folder : Contains the file "predict.html" which is the layout for the webapp. It's really important to keep it inside the folder. 

### Required Libraries
The following libraries are required to run the app:
- Flask

- scikit-learn

- pandas

You can install these libraries by running the following commands:

pip install flask

pip install scikit-learn

pip install pandas

### Running the webapp
After downloading the files, installing python and installing the libraries. You can start running the webappp.

To start running the webapp you should run the python file "color_flask.py".

Once you run the python code it will give you an output with the link were you can access the webapp locally.

This link is: http://127.0.0.1:5000

It is important to understand that you can access this link only locally and only while the python code is being runned.

### Webapp usage information
Once you managed to access the webapp the first thing you will see is the initial page. To start with your predictions you should introduce the year, month and day you want to predict. After introducing the inputs you can press the button "predict". This will take you to another page that will ask you for the trial number you want to predict, after scrolling to choose your trial number you can press the button to predict.

To understand how to choose your inputs you should access to: https://cooe.in/#/win

In the link for Emerd you will see a column named "Period". This column tells the year, month, day and trial.

For example the last period record is "20230128095" this means that the year is equal to 2023, the month is 1, the day is 28 and the trial number is 95. 

Suppose you want to predict the next trial number for that date you should introduce in the webapp for year: 2023, for month: 1, for day: 28 and select the trial number 96. After introducing these inputs the webapp will give you the predicted color being "Red" or "Green".

An important note is that the maximum numbers of trials the game runs in a day is 480. The the game will start again the next day from trial number 1.

#### Important!

When you stop using the webapp it is important that you stop the running process of the python file. If you want to use the webapp again you should run again the python file "color_flask.py" and follow the steps said before.

### Model
The model used in this app is a Random Forest Classifier model, which is a type of ensemble learning method that combines multiple decision trees to improve the accuracy of the predictions. The purpose of this model is to predict if the color is going to be "Red" or "Green" for a date and trial. The model used for this project has been trained and tested on more than 20000 samples. The model has been tuned and several methods were applied to prevent overfitting. 
