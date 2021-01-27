"""
    This library contains the functions that allows the GUI to 
    obtain the default and the previous values of the configuration
"""

#System Configuration default values
def scSetDefultValues():
    defaultValues = {}
    defaultValues["std2"] = "selected"
    defaultValues["gain"] = "selected"
    defaultValues["ledChecked"] = "checked"
    defaultValues["agcChecked"] = "checked"
    defaultValues["ser2Checked"] = "checked"
    defaultValues["stChecked"] = "checked"
    defaultValues["tlChecked"] = "checked"
    defaultValues["cChecked"] = "checked"
    defaultValues["rChecked"] = "checked"
    defaultValues["dcChecked"] = "checked"
    defaultValues["slfChecked"] = "checked"
    return defaultValues

#System Configuration previous values
def scSetPreviousValues(**parameters):
    previousValues={}
    for key,value in parameters.items():
        #========#
        if key == "selfTrigDelay":
            if(value==2):
                previousValues["std2"] = "selected"
            if(value==4):
                previousValues["std4"] = "selected"
            if(value==8):
                previousValues["std8"] = "selected"
            if(value==16):
                previousValues["std16"] = "selected"
            if(value==32):
                previousValues["std32"] = "selected"
            if(value==64):
                previousValues["std64"] = "selected"
            if(value==128):
                previousValues["std128"] = "selected"
            if(value==256):
                previousValues["std256"] = "selected"
        #========#
        if key == "led":
            ledChecked = ""
            if value:
                ledChecked = "checked"
            previousValues["ledChecked"] = ledChecked
        #========#
        if key == "raw":
            rawChecked = ""
            if value:
                rawChecked = "checked"
            previousValues["rawChecked"] = rawChecked
        #========#
        if key == "agc":
            agcChecked = ""
            if value:
                agcChecked = "checked"
            previousValues["agcChecked"] = agcChecked
        if key == "gain":
            if(value==8):
                previousValues["gain8"] = "selected"
            if(value==21):
                previousValues["gain21"] = "selected"
            if(value==43):
                previousValues["gain43"] = "selected"
            if(value==56):
                previousValues["gain56"] = "selected"
        #========#
        if key == "ser2":
            ser2Checked = ""
            if value:
                ser2Checked = "checked"
            previousValues["ser2Checked"] = ser2Checked
        if key == "ser1":
            ser1Checked = ""
            if value:
                ser1Checked = "checked"
            previousValues["ser1Checked"] = ser1Checked
        if key == "ext":
            extChecked = ""
            if value:
                extChecked = "checked"
            previousValues["extChecked"] = extChecked
        if key == "st":
            stChecked = ""
            if value:
                stChecked = "checked"
            previousValues["stChecked"] = stChecked
        #========#
        if key == "tl":
            tlChecked = ""
            if value:
                tlChecked = "checked"
            previousValues["tlChecked"] = tlChecked
        if key == "p":
            pChecked = ""
            if value:
                pChecked = "checked"
            previousValues["pChecked"] = pChecked
        if key == "c":
            cChecked = ""
            if value:
                cChecked = "checked"
            previousValues["cChecked"] = cChecked
        if key == "r":
            rChecked = ""
            if value:
                rChecked = "checked"
            previousValues["rChecked"] = rChecked
        #========#
        if key == "dc":
            dcChecked = ""
            if value:
                dcChecked = "checked"
            previousValues["dcChecked"] = dcChecked
        if key == "slf":
            slfChecked = ""
            if value:
                slfChecked = "checked"
            previousValues["slfChecked"] = slfChecked
        if key == "pre":
            preChecked = ""
            if value:
                preChecked = "checked"
            previousValues["preChecked"] = preChecked
        #========#
    return previousValues