#partial credit to colinoflynn @ https://github.com/colinoflynn/dp832-gui/blob/master/dp832gui/dp832.py 

#!!!!!!!IMPORTANT!!!!!!!
#in your command prompt, type "pip install -U pyvisa"
#then just run this python script. the pyvisa package should be installed to the correct path.
#If not, troubleshoot with instructions from the pyvisa website

import visa
from appJar import gui

############################################################################################################

class RigolDP(object):

    def __init__(self):
        pass

    def conn(self, constr="USB0::0x1AB1::0x0E11::DPXXXXXXXXXXX::INSTR"):
        """Attempt to connect to instrument"""
        rm = visa.ResourceManager()
        self.inst = rm.open_resource(constr)

    def identify(self):
        """Return identify string which has serial number"""
        return self.inst.query("*IDN?")
                  
    def dis(self):
        del self.inst
    
    def writing(self, command=""):
        self.inst.write(command)
        
############################################################################################################

class psuParameters(object):
    def __init__(self):
        pass
    
############################################################################################################
        
def set_button(btn):
    if btn=="ch1v":
        if(app.getEntry("Voltage1")>=0.0 and app.getEntry("Voltage1")<=32.0):
            parameters.v1=app.getEntry("Voltage1")
        else:
            app.errorBox("ch1_v","Channel 1 voltage must be 0.0-32.0 V")
        psu.inst.write(":APPL CH1,"+str(parameters.v1)+","+str(parameters.i1))
    elif btn=="ch1i":
        if app.getEntry("Current1") >=0.0 and app.getEntry("Current1")<=3.2:
            parameters.i1=app.getEntry("Current1")
        else:
            app.errorBox("ch1_i","Channel 1 current must be 0.0-3.2 A")
        psu.inst.write(":APPL CH1,"+str(parameters.v1)+","+str(parameters.i1))
    elif btn=="ch2v":
        if(app.getEntry("Voltage2")>=0.0 and app.getEntry("Voltage2")<=32.0):
            parameters.v2=app.getEntry("Voltage2")
        else:
            app.errorBox("ch2_v","Channel 2 voltage must be 0.0-32.0 V")
        psu.inst.write(":APPL CH2,"+str(parameters.v2)+","+str(parameters.i2))
    elif btn=="ch2i":
        if app.getEntry("Current2") >=0.0 and app.getEntry("Current2")<=3.2:
            parameters.i2=app.getEntry("Current2")
        else:
            app.errorBox("ch2_i","Channel 2 current must be 0.0-3.2 A")
        psu.inst.write(":APPL CH2,"+str(parameters.v2)+","+str(parameters.i2))
    elif btn=="ch3v":
        if(app.getEntry("Voltage3")>=0.0 and app.getEntry("Voltage3")<=5.0):
            parameters.v3=app.getEntry("Voltage3")
        else:
            app.errorBox("ch3_v","Channel 3 voltage must be 0.0-5.0 V")
        psu.inst.write(":APPL CH3,"+str(parameters.v3)+","+str(parameters.i3))
    elif btn=="ch3i":
        if app.getEntry("Current3") >=0.0 and app.getEntry("Current3")<=3.2:
            parameters.i3=app.getEntry("Current3")
        else:
            app.errorBox("ch3_i","Channel 3 current must be 0.0-3.2 A")
        psu.inst.write(":APPL CH3,"+str(parameters.v3)+","+str(parameters.i3))
def on_off_button(btn):
    if btn=="ch1_oo":
        parameters.ch1= not parameters.ch1
        if parameters.ch1:
            output="ON"
            app.setLabelBg("Channel 1", "lime")
        else:
            output="OFF"
            app.setLabelBg("Channel 1", "red")
        psu.inst.write(":OUTP CH1,"+output)
    elif btn=="ch2_oo":
        parameters.ch2= not parameters.ch2
        if parameters.ch2:
            output="ON"
            app.setLabelBg("Channel 2", "lime")
        else:
            output="OFF"
            app.setLabelBg("Channel 2", "red")
        psu.inst.write(":OUTP CH2,"+output)
    elif btn=="ch3_oo":
        parameters.ch3= not parameters.ch3
        if parameters.ch3:
            output="ON"
            app.setLabelBg("Channel 3", "lime")
        else:
            output="OFF"
            app.setLabelBg("Channel 3", "red")
        psu.inst.write(":OUTP CH3,"+output)
def options(btn):
    parameters.ID=app.getOptionBox("Power Supply ID")
    app.stop()
def help_button(btn):
    app.infoBox("Help","How to use:\n\n   1. Enter numerical values in the input boxes and hit \"Set V\" or \"Set I\" to change settings of respective channels \n\n\
    2. The readings will constantly update. Be careful to note that the readings are only valid for when the chanel is on. If the channel is off, the readings may be odd \n\n\
    3. Finally, hitting the ON/OFF button will, yes, turn the channel on and off")
def initial_button(btn):
    flag=True
    if(app.getEntry("Voltage1")>=0.0 and app.getEntry("Voltage1")<=32.0):
        parameters.v1=app.getEntry("Voltage1")
    else:
        app.errorBox("ch1_v","Channel 1 voltage must be 0.0-32.0 V")
        flag=False
        
    if app.getEntry("Current1") >=0.0 and app.getEntry("Current1")<=3.2:
        parameters.i1=app.getEntry("Current1")
    else:
        app.errorBox("ch1_i","Channel 1 current must be 0.0-3.2 A")
        flag=False
        
    if(app.getEntry("Voltage2")>=0.0 and app.getEntry("Voltage2")<=32.0):
        parameters.v2=app.getEntry("Voltage2")
    else:
        app.errorBox("ch2_v","Channel 2 voltage must be 0.0-32.0 V")
        flag=False
        
    if app.getEntry("Current2") >=0.0 and app.getEntry("Current2")<=3.2:
        parameters.i2=app.getEntry("Current2")
    else:
        app.errorBox("ch2_i","Channel 2 current must be 0.0-3.2 A")
        flag=False
        
    if(app.getEntry("Voltage3")>=0.0 and app.getEntry("Voltage3")<=5.0):
        parameters.v3=app.getEntry("Voltage3")
    else:
        app.errorBox("ch3_v","Channel 3 voltage must be 0.0-5.0 V")
        flag=False
        
    if app.getEntry("Current3") >=0.0 and app.getEntry("Current3")<=3.2:
        parameters.i3=app.getEntry("Current3")
    else:
        app.errorBox("ch3_i","Channel 3 current must be 0.0-3.2 A")
        flag=False
    if flag:
        if (parameters.v1==0 or parameters.v2==0 or parameters.v3==0 or parameters.i1==0 or parameters.i2==0 or parameters.i3==0):
            yes=app.questionBox("input","Some values entered are of zero value: are you certain all inputs are what you would like?")
            if yes=="yes":
                app.stop()
        else:
            app.stop()
def update_readings():
    app.setMessage("ch1_readings", "Voltage at: "+psu.inst.query(":MEAS? CH1")+"\nCurrent at: "+psu.inst.query(":MEAS:CURR? CH1")+"\nPower at: "+psu.inst.query(":MEAS:POWE? CH1"))
    app.setMessage("ch2_readings", "Voltage at: "+psu.inst.query(":MEAS? CH2")+"\nCurrent at: "+psu.inst.query(":MEAS:CURR? CH2")+"\nPower at: "+psu.inst.query(":MEAS:POWE? CH2"))
    app.setMessage("ch3_readings", "Voltage at: "+psu.inst.query(":MEAS? CH3")+"\nCurrent at: "+psu.inst.query(":MEAS:CURR? CH3")+"\nPower at: "+psu.inst.query(":MEAS:POWE? CH3"))
def update_settings():
    settings1=psu.inst.query(":APPL? CH1")
    settings2=psu.inst.query(":APPL? CH2")
    settings3=psu.inst.query(":APPL? CH3")
    app.setMessage("ch1_settings", "Voltage set: "+settings1[11:16]+"\nCurrent set: "+settings1[-6:-2])
    app.setMessage("ch2_settings", "Voltage set: "+settings2[11:16]+"\nCurrent set: "+settings2[-6:-2])
    app.setMessage("ch3_settings", "Voltage set: "+settings3[10:14]+"\nCurrent set: "+settings3[-6:-2])
    #app.setMessage("ch1_settings", "Voltage set: "+str(parameters.v1)+"\nCurrent set: "+str(parameters.i1))
    #app.setMessage("ch2_settings", "Voltage set: "+str(parameters.v2)+"\nCurrent set: "+str(parameters.i2))
    #app.setMessage("ch3_settings", "Voltage set: "+str(parameters.v3)+"\nCurrent set: "+str(parameters.i3))
        
############################################################################################################

#initialize gui start up
app = gui("ID Selection")
app=gui("Rigol", "500x200")
app.setBg("White")
app.setFont(10)
                        
#initialize variables
parameters=psuParameters()
parameters.ch1=False
parameters.ch2=False
parameters.ch3=False
parameters.v1=0.0
parameters.v2=0.0
parameters.v3=0.0
parameters.i1=0.0
parameters.i2=0.0
parameters.i3=0.0
parameters.ID=""

app.addMessage("note","Select the Rigol ID for your power supply (found using Ultra Sigma (downloadable from the Rigol website or, it is printed on \
a sticker on the rear of the psu): ")
app.addOptionBox("Power Supply ID", ["USB0::0x1AB1::0x0E11::DP8C182402078::INSTR"]) #add any other power supply IDs you may have
app.addNamedButton("Select", "select",options)
app.setMessageWidth("note",500)
app.go()

psu = RigolDP()
psu.conn(parameters.ID)

#initialize the gui second phase gui interface (asking for initial input values)
app = gui("Initial Settings")
app=gui("Rigol", "800x200")
app.setBg("White")
app.setFont(20)
app.addLabel("initial channel settings","Please enter initial channel settings",0,1)

#create channel 1 control center
app.addLabel("Channel 1", "Channel 1",1,0)
app.setLabelBg("Channel 1", "yellow")
app.getLabelWidget("Channel 1").config(font="Verdana 20")
app.addNumericEntry("Voltage1",2,0)
app.setEntryDefault("Voltage1","Voltage")
app.addNumericEntry("Current1",3,0)
app.setEntryDefault("Current1","Current")

#create channel 2 control center
app.addLabel("Channel 2", "Channel 2",1,1)
app.setLabelBg("Channel 2", "yellow")
app.getLabelWidget("Channel 2").config(font="Verdana 20")
app.addNumericEntry("Voltage2",2,1)
app.setEntryDefault("Voltage2","Voltage")
app.addNumericEntry("Current2",3,1)
app.setEntryDefault("Current2","Current")

#create channel 3 control center
app.addLabel("Channel 3", "Channel 3",1,2)
app.setLabelBg("Channel 3", "yellow")
app.getLabelWidget("Channel 3").config(font="Verdana 20")
app.addNumericEntry("Voltage3",2,2)
app.setEntryDefault("Voltage3","Voltage")
app.addNumericEntry("Current3",3,2)
app.setEntryDefault("Current3","Current")

app.addNamedButton("Finalize Initial Input","finalize",initial_button,4,1)

app.go()

#initialize the final gui interface
app = gui("Rigol")
app=gui("Rigol", "800x500")
app.setBg("White")
app.setFont(20)

#initialize channels by setting them off and making values equal to initial values
psu.inst.write(":OUTP CH1,OFF")
psu.inst.write(":OUTP CH2,OFF")
psu.inst.write(":OUTP CH3,OFF")
psu.inst.write(":APPL CH1,"+str(parameters.v1)+","+str(parameters.i1))
psu.inst.write(":APPL CH2,"+str(parameters.v2)+","+str(parameters.i2))
psu.inst.write(":APPL CH3,"+str(parameters.v3)+","+str(parameters.i3))

#help button
app.addNamedButton("Help","help",help_button,9,2)
app.setButtonBg("help","magenta")

#create channel 1 control center
app.addLabel("Channel 1", "Channel 1",0,0,2)
app.setLabelBg("Channel 1", "red")
app.getLabelWidget("Channel 1").config(font="Verdana 20")
app.addNumericEntry("Voltage1",1,0,2)
app.setEntryDefault("Voltage1","Voltage")
app.addNumericEntry("Current1",2,0,2)
app.setEntryDefault("Current1","Current")
app.addNamedButton("Set V","ch1v",set_button,3,0,1)
app.addNamedButton("Set I","ch1i",set_button,3,1,1)
app.addNamedButton("ON/OFF","ch1_oo",on_off_button,4,0,2)


#create channel 2 control center
app.addLabel("Channel 2", "Channel 2",0,2,2)
app.setLabelBg("Channel 2", "red")
app.getLabelWidget("Channel 2").config(font="Verdana 20")
app.addNumericEntry("Voltage2",1,2,2)
app.setEntryDefault("Voltage2","Voltage")
app.addNumericEntry("Current2",2,2,2)
app.setEntryDefault("Current2","Current")
app.addNamedButton("Set V","ch2v",set_button,3,2,1)
app.addNamedButton("Set I","ch2i",set_button,3,3,1)
app.addNamedButton("ON/OFF","ch2_oo",on_off_button,4,2,2)

#create channel 3 control center
app.addLabel("Channel 3", "Channel 3",0,4,2)
app.setLabelBg("Channel 3", "red")
app.getLabelWidget("Channel 3").config(font="Verdana 20")
app.addNumericEntry("Voltage3",1,4,2)
app.setEntryDefault("Voltage3","Voltage")
app.addNumericEntry("Current3",2,4,2)
app.setEntryDefault("Current3","Current")
app.addNamedButton("Set V","ch3v",set_button,3,4,1)
app.addNamedButton("Set I","ch3i",set_button,3,5,1)
app.addNamedButton("ON/OFF","ch3_oo",on_off_button,4,4,2)

#display current settings that were inputed by user
app.setSticky("w")
app.addLabel("ch1_settings_label","Settings",5,0)
app.setLabelBg("ch1_settings_label", "yellow")
app.getLabelWidget("ch1_settings_label").config(font="Verdana 20 underline")

app.addLabel("ch2_settings_label","Settings",5,2)
app.setLabelBg("ch2_settings_label", "yellow")
app.getLabelWidget("ch2_settings_label").config(font="Verdana 20 underline")

app.addLabel("ch3_settings_label","Settings",5,4)
app.setLabelBg("ch3_settings_label", "yellow")
app.getLabelWidget("ch3_settings_label").config(font="Verdana 20 underline")


app.addMessage("ch1_settings", "Voltage set: "+str(parameters.v1)+"\nCurrent set: "+str(parameters.i1),6,0)
app.addMessage("ch2_settings", "Voltage set: "+str(parameters.v2)+"\nCurrent set: "+str(parameters.i2),6,2)
app.addMessage("ch3_settings", "Voltage set: "+str(parameters.v3)+"\nCurrent set: "+str(parameters.i3),6,4)

#create message area to display the current readings on the psu
app.addLabel("ch1_readings_label","Readings",7,0)
app.setLabelBg("ch1_readings_label", "cyan")
app.getLabelWidget("ch1_readings_label").config(font="Verdana 20 underline")

app.addLabel("ch2_readings_label","Readings",7,2)
app.setLabelBg("ch2_readings_label", "cyan")
app.getLabelWidget("ch2_readings_label").config(font="Verdana 20 underline")

app.addLabel("ch3_readings_label","Readings",7,4)
app.setLabelBg("ch3_readings_label", "cyan")
app.getLabelWidget("ch3_readings_label").config(font="Verdana 20 underline")

app.addMessage("ch1_readings", "Voltage at: \nCurrent at: \nPower at: ",8,0)
app.addMessage("ch2_readings", "Voltage at: \nCurrent at: \nPower at: ",8,2)
app.addMessage("ch3_readings", "Voltage at: \nCurrent at: \nPower at: ",8,4)

#loop for constantly checking the values
app.registerEvent(update_settings)
app.setPollTime(100)
app.registerEvent(update_readings)

#start the final gui
app.go()

#after closing, turn off channels
psu.inst.write(":OUTP CH1,OFF")
psu.inst.write(":OUTP CH2,OFF")
psu.inst.write(":OUTP CH3,OFF")
