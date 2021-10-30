"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Converts fahrenheit to celsius"""
    fahrenheit = (float(celsius) * 9.0 / 5 + 32)
    return f" {celsius} degrees Celsius = {str(fahrenheit)} degrees Fahrenheit"


if __name__ == '__main__':
    app.run()
