from flask import Flask  # Flask is a web framework tool to develop web interfaces with Python

app = Flask(__name__)  # This creates a flask instance with the file __name__ variable

@app.route('/')
# This create a python artifact (an output) based on the condition of accessing the root path of a web
# address, created by the Flask object instantiated.

# The function bellow the artifact route is executed everytime a GET request is sent to the root path
def welcome(): 
    return 'Welcome to Flask'

if __name__ == '__main__':  # Checks if .py file is run as a main program. If so, it runs the created app. 
    app.run(debug=True)
# Quando setamos debug para true, conseguimos ver mensagens dos erros de quando rodamos o app,
# e assim que salvamos qualquer alteração, o app é rodado novamente.


# In python depending on how you run a .py file, the python algorithm determines a vaue for a special
# variable '__name__'. If the .py file is beeing run as a main program, python sets the variable '__name__'
# to '__main__'. Otherwise, it sets the variable '__name__' to the name of the python file (in this case
# it would be 'app'). This is relevant when you import functions and data from another python file.