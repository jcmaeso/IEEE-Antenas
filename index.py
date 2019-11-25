from flask import Flask,render_template
import message_sender as sender

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sc')
def system_configuration():
    trama = sender.system_conf_message('serial',led=True)
    print(trama)
    return render_template('pepe.html',trama=trama)

@app.route('/rfc')
def radar_frontend_conf():
    trama = sender.radar_frontend_conf_message('serial')
    print(trama)
    return render_template('pepe.html',trama=trama)

@app.route('/pc')
def pll_conf():
    trama = sender.pll_conf_message('serial')
    print(trama)
    return render_template('pepe.html',trama=trama)

@app.route('/bs')
def baseband_setup():
    trama = sender.baseband_setup_message('serial')
    print(trama)
    return render_template('pepe.html',trama=trama)

@app.route('/pepe')
def pepe():
    trama = sender.radar_frontend_conf_message('serial')
    print(trama)
    return render_template('pepe.html',trama=trama)


if __name__ == '__main__':
    app.run()