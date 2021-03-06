from flask import Flask, request, render_template, jsonify
from modules.weather import weatherTempF, weatherIconF
from modules.webserver_check import server_check

app = Flask(__name__)

@app.route('/')
def index():
    currentTemp = weatherTempF() + ' F'
    weatherIcon = weatherIconF()
    return render_template('index.html', weatherIcon=weatherIcon, currentTemp=currentTemp)


@app.route('/api/v1/weather')
def api_weather():
    current_temp = weatherTempF()
    current_icon = weatherIconF()
    data = {'temperature': current_temp, 'icon': current_icon}
    return jsonify(weather_data=data)


@app.route('/api/v1/server/status')
def api_server_status():
    url = "http://coriewhite.me"
    data = {'statusC': server_check(url)}
    return jsonify(server_status=data)


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
