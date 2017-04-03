# Rigol-DP800-Series-Power-Supplies
Python script for a gui for Rigol DP800 Series Power Supplies

The python script runs pyvisa to interact with the Rigol power supplies and appJar for the GUI

appJar source code in included in a folder called appJar: both your script and the appJar folder should be in the same directory

In your command prompt, type "pip install -U pyvisa" to instal pyvisa
Then just run this python script. the pyvisa package should be installed to the correct path.
If not, troubleshoot with instructions from the pyvisa website

The GUI will ask you to pick an initial ID for your power supply. This ID is hardcoded in the dp832.py file and should be changed
according to the power supplies you will be using (the ID can be found using Ultra Sigma or be reading the stick at the back of the power supply)

Lastly, the script will only work when the power supply is connected and the connection between your computer and the device is established.
Comment out any line of code that uses the object "psu" if you wish to see how the GUI looks
