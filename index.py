from flask import Flask,render_template,request,redirect
import radar.message_sender as sender
import libraries.guiDefaultValues as default

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sc')
def system_configuration():
    trama = sender.system_conf_message('serial')
    print(trama)
    defaultValues = default.scSetDefultValues()
    return render_template('sc.html',trama=trama,registro="sc",**defaultValues)

@app.route('/rfc')
def radar_frontend_conf():
    trama = sender.radar_frontend_conf_message('serial')
    print(trama)
    return render_template('sc.html',trama=trama,registro="rfc")

@app.route('/pc')
def pll_conf():
    trama = sender.pll_conf_message('serial')
    print(trama)
    return render_template('sc.html',trama=trama,registro="pc")

@app.route('/bs')
def baseband_setup():
    trama = sender.baseband_setup_message('serial')
    print(trama)
    return render_template('sc.html',trama=trama,registro="bs")

@app.route('/pepe')
def pepe():
    trama = sender.radar_frontend_conf_message('serial')
    print(trama)
    return render_template('sc.html',trama=trama)



@app.route('/sysconfig', methods=["POST"])
def sysconfig():
    parameters={}
    registro = request.args.get('registro')

    parameters["selfTrigDelay"] = int(request.form.get("selfTrigDelay"))
    parameters["led"] = request.form.get("led")
    parameters["raw"] = request.form.get("raw")
    parameters["agc"] = request.form.get("agc")
    parameters["gain"] = int(request.form.get("gain"))
    parameters["ser2"] = request.form.get("ser2")
    parameters["ser1"] = request.form.get("ser1")
    parameters["ext"] = request.form.get("ext")

    parameters["st"] = request.form.get("st")
    parameters["tl"] = request.form.get("tl")
    parameters["p"] = request.form.get("p")
    parameters["c"] = request.form.get("c")
    parameters["r"] = request.form.get("r")
    parameters["dc"] = request.form.get("dc")
    parameters["slf"] = request.form.get("slf")
    parameters["pre"] = request.form.get("pre")
    
    trama = sender.system_conf_message('serial',**parameters)

    previousValues = default.scSetPreviousValues(**parameters)

    return render_template('sc.html', trama = trama, registro = registro, **previousValues)




if __name__ == '__main__':
    app.run()