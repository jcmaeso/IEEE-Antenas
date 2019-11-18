import ll_message_sender, math


def system_conf_message(serial, **kwargs):
    parameters={}
    for key, value in kwargs.items():
        if key == "selfTrigDelay" :
            x=str(bin(int(math.log(value,2))-1)[2:])
            for i in range (0,(3-len(x))):
                x = '0' + x
            parameters["selfTrigDelay"]=x
        elif key == "led" :
            if value:
                parameters["led"]="01"
            else:
                parameters["led"]="00"
        elif key == "raw" :
            if value:
                parameters["raw"]="1"
            else:
                parameters["raw"]="0"
        elif key == "agc" :
            if value:
                parameters["agc"]="1"
            else:
                parameters["agc"]="0"
        elif key == "gain" :
            if value == 8:
                parameters["gain"]="00"
            elif value == 21:
                parameters["gain"]="01"
            elif value == 43:
                parameters["gain"]="10"
            elif value == 56:
                parameters["gain"]="11"
        elif key == "ser2" :
            if value:
                parameters["ser2"]="1"
            else:
                parameters["ser2"]="0"
        elif key == "ser1" :
            if value:
                parameters["ser1"]="1"
            else:
                parameters["ser1"]="0"
        elif key == "ext" :
            if value:
                parameters["ext"]="1"
            else:
                parameters["ext"]="0"
        elif key == "st" :
            if value:
                parameters["st"]="1"
            else:
                parameters["st"]="0"
        elif key == "tl" :
            if value:
                parameters["tl"]="1"
            else:
                parameters["tl"]="0"
        elif key == "p" :
            if value:
                parameters["p"]="1"
            else:
                parameters["p"]="0"
        elif key == "c" :
            if value:
                parameters["c"]="1"
            else:
                parameters["c"]="0"
        elif key == "r" :
            if value:
                parameters["r"]="1"
            else:
                parameters["r"]="0"
        elif key == "dc" :
            if value:
                parameters["dc"]="1"
            else:
                parameters["dc"]="0"
        elif key == "slf" :
            if value:
                parameters["slf"]="1"
            else:
                parameters["slf"]="0"
        elif key == "pre" :
            if value:
                parameters["pre"]="1"
            else:
                parameters["pre"]="0"
    ll_message_sender.system_conf_message(serial, **parameters)

def radar_frontend_conf_message(serial, **kwargs):
    parameters={}
    for key, value in kwargs.items():
        if key == "vco" :
            if value == 8 :
                x=str(bin(value)[2:])
                for i in range (0,(13-len(x))):
                    x = '0' + x
                parameters["vco"]=x
        if key == "base_freq" :
            if value <= 524287 :
                x=str(bin(value)[2:])
                for i in range (0,(19-len(x))):
                    x = '0' + x
                parameters["base_freq"]=x
    ll_message_sender.radar_frontend_conf_message(serial, **parameters)

def pll_conf_message(serial, **kwargs):
    parameters={}
    for key, value in kwargs.items():
        if key == "pll" :
            if value <= 32767 & value >= -32768 :
                x=str(bin(value)[2:])
                for i in range (0,(16-len(x))):
                    x = '0' + x
                parameters["pll"]=x
    ll_message_sender.pll_conf_message(serial, **parameters)

def baseband_setup_message(serial, **kwargs):
    parameters={}
    for key, value in kwargs.items():
        if key == "format" :
            if value == 1 :
                parameters["format"]="000"
            elif value == 2 :
                parameters["format"]="001"
            elif value == 3 :
                parameters["format"]="010"
            elif value == 4 :
                parameters["format"]="101"
        elif key == "CFAR_threshold" :
            if value <= 31 & value >= 0 :
                x=str(bin(int(value))[2:])
                for i in range (0,(5-len(x))):
                    x = '0' + x
                parameters["CFAR_threshold"]=x
        elif key == "CFAR_size" :
            if value <= 15 & value >= 0 :
                x=str(bin(int(value))[2:])
                for i in range (0,(4-len(x))):
                    x = '0' + x
                parameters["CFAR_size"]=x
        elif key == "CFAR_grd" :
            if value <= 3 & value >= 0 :
                x=str(bin(int(value))[2:])
                for i in range (0,(2-len(x))):
                    x = '0' + x
                parameters["CFAR_grd"]=x
        elif key == "average_n" :
            if value <= 3 & value >= 0 :
                x=str(bin(int(value))[2:])
                for i in range (0,(3-len(x))):
                    x = '0' + x
                parameters["average_n"]=x
        elif key == "fft_size" :
            x=str(bin(int(math.log(value,2))-5)[2:])
            for i in range (0,(3-len(x))):
                x = '0' + x
            parameters["fft_size"]=x
        elif key == "downsampling" :
            if value <= 2 & value >= 0 :
                x=str(bin(int(value))[2:])
                for i in range (0,(3-len(x))):
                    x = '0' + x
                parameters["downsampling"]=x
            elif value == 4 :
                parameters["downsampling"]="011"
            elif value == 8 :
                parameters["downsampling"]="100"
            elif value == 16 :
                parameters["downsampling"]="101"
            elif value == 32 :
                parameters["downsampling"]="110"
            elif value == 64 :
                parameters["downsampling"]="111"
        elif key == "ramps" :
            if value <= 64 & value >= 0 :
                x=str(bin(int(math.log(value,2)))[2:])
                for i in range (0,(3-len(x))):
                    x = '0' + x
                parameters["ramps"]=x
        elif key == "samples" :
            if value <= 2048 & value >= 32 :
                x=str(bin(int(math.log(value,2))-5)[2:])
                for i in range (0,(3-len(x))):
                    x = '0' + x
                parameters["samples"]=x
        elif key == "ADC_clkdiv" :
            if value <= 8 & value >=1 :
                x=str(bin(int(value)-1)[2:])
                for i in range (0,(3-len(x))):
                    x = '0' + x
                parameters["ADC_clkdiv"]=x
    ll_message_sender.baseband_setup_message(serial, **parameters)


if __name__ == "__main__":
    sys={"selfTrigDelay" : 32,
        "led" : True
        }
    system_conf_message('hola',**sys)
    radar_frontend_conf_message('hola')
    pll_conf_message('hola')
    baseband_setup_message('hola')