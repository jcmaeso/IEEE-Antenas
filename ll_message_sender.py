""" def concatenar:

    package_type:   Define el tipo de trama que se va a enviar
    *args:          Conjunto de bits de configuración que se concatenan en la trama

    Descripción:    Función que comprueba primero el tipo de trama y después realiza una serie de operaciones
                    para formatearla de la forma correcta
"""

def concatenar(package_type,*args):
    cadena=''
    possible_types = ('S','F','B','P')
    if package_type not in possible_types:
        return bytes(cadena,'ascii')
    for i in args:
        cadena+=str(i)
    cadena = hex(int(cadena,2))
    cadena = cadena[2:]
    for i in range (0,(8-len(cadena))):
        cadena = '0' + cadena
    return bytes("!"+str(package_type) + '' + cadena.upper() + '' + "\r\n", 'ascii')

""" def test:

    trama:          Cadena de texto que contiene la trama a comprobar

    Descripción:    Función que comprueba que el formato de la trama es el correcto: 
                    Verifica la longitud y que sesa ded tipo hexadecimal
"""
def test(trama):
    trama=trama[4:-5]
    if (len(trama)!=8):
        return False
    hex_characters = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    for i in trama:
        if i not in hex_characters:
            print('Error with Hexadecimal System')
            return False
    return True

""" def send:

    serial:         Instancia del serial por el que se enviará la trama. DE MOMENTO NO SE USA
    trama:          Trama a enviar
    nombre:         Nombre de la trama para sacar por pantalla en caso de error
"""
def send(serial,trama,nombre='Trama'):
    if test(str(trama)):
        print(trama)
        #serial.write(trama)
    else:
        print('Error in ' + nombre + '\r\n')
        
    


    
#==================FUNCIONES DE BAJO NIVEL==================#


    # led -> true -> false
    # ganancia -> numero a pincho -> compruebas que está en rango

def system_conf_message(serial, selfTrigDelay="000", led="00", raw="0", agc="1", gain="00", ser2="1", ser1="0", ext="0", st="0", tl="0", p="0", c="0", r="0", dc="1", slf="1", pre="0"):
    trama=concatenar('S',selfTrigDelay,"000",led,"0000000",raw,"0",agc,gain,ser2,ser1,ext,st,tl,p,c,r,dc,"0",slf,pre)
    send('serial',trama,'System configuration')
    

def radar_frontend_conf_message(serial, vco="0000000001000", base_freq="0000101110111000000"): #VCO_div=8 y Base_freq=24000MHz
    trama=concatenar('F',vco,base_freq,'\r\n')
    send('serial',trama,'Radar Frontend Configuration')

def pll_conf_message(serial, pll="001111101000"): #BW PLL=500MHz Banda ISM
  trama=concatenar('P','0000000000000000',pll,'\r\n')
  send('serial',trama,'PLL configuration')

def baseband_setup_message(serial, format="101",CFAR_threshold="10000",CFAR_size="0011",CFAR_grd="01",average_n="001",fft_size="100",downsampling="000",ramps="100",samples="100",ADC_clkdiv="101"):
  trama = concatenar('B',format, CFAR_threshold,CFAR_size,CFAR_grd,average_n,fft_size,downsampling,ramps,samples,ADC_clkdiv,'\r\n')
  send('serial',trama,'Baseband setup')



if __name__ == "__main__":
    system_conf_message('hola')
    radar_frontend_conf_message('hola')
    pll_conf_message('hola')
    baseband_setup_message('hola')







# !B default calculation
# B034C125
#1011 0000 0011 0100 1100 0001 0010 0101
#101 10000 0011 01 001 100 000 100 100 101
