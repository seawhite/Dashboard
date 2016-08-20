from flask import Flask, render_template
from modules.weather import weatherTempF, weatherIconF

app = Flask(__name__)


@app.route('/')
def index():
    currentTemp = weatherTempF() + ' F'
    weatherIcon = weatherIconF()
    return render_template('index.html', weatherIcon=weatherIcon, currentTemp=currentTemp)


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/bootstrap-elements')
def bsElements():
    return render_template('bootstrap-elements.html')


@app.route('/bootstrap-grid')
def bsGrid():
    return render_template('bootstrap-grid.html')


@app.route('/blank-page')
def blankPage():
    return render_template('blank-page.html')


if __name__ == '__main__':
    app.run(debug=True)
