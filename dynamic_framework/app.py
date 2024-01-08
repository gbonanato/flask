from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Main"

@app.route('/success/<int:mark>')
def success(mark):
    return "Mark was a success. The mark was: " + str(mark)

@app.route('/fail/<int:mark>')
def fail(mark):
    return "Mark was a fail. The mark was: " + str(mark)

@app.route('/test/<int:score>')
def test(score):
    result = ''
    if score > 50:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result, mark=score))
# Here we dynammically redirect our URL according to the value set on the test page. If it is above 50
# we redirect to success page. Otherwise we redirect to fail page, togheter with the mark value.

if __name__ == '__main__':
    app.run(debug=True)