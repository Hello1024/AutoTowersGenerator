import glob
import os
import platform
import subprocess

from UM.Logger import Logger



class OpenScadInterface:
    OpenScadPath = None



    def __init__(self):
        # Determine the default path of the OpenSCAD command

        # For Linux, OpenSCAD should be in the default path
        if platform.system() == 'Linux':
            self.OpenScadPath = 'openscad'

        # This path for macs was stolen from Thopiekar's OpenSCAD Integration plugin (https://thopiekar.eu/cura/cad/openscad)
        # I have no way of verifying this, though...
        elif platform.system() == 'Darwin':
            self.OpenScadPath = '/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD'

        # For Windows, OpenSCAD should be installed in the Program Files folder
        elif platform.system() == 'Windows':
            self.OpenScadPath = os.path.join(os.getenv('PROGRAMFILES'), 'OpenSCAD', "openscad.exe")

        # If none of the above apply, try a default that might work
        else:
            self.OpenScadPath = 'openscad'



    def GenerateStl(self, inputFilePath, parameters, outputFilePath):
        # Start the command array with the OpenSCAD command
        command = [self.OpenScadPath]

        # Tell OpenSCAD to automatically generate an STL file
        command.append(f'-o{outputFilePath}')

        # Add each variable setting parameter
        for parameter in parameters:
            # Retrieve the parameter value
            value = parameters[parameter]

            # If the value is a string, add escaped quotes around it
            if type(value) == str:
                value = f'\"{value}\"'

            command.append(f'-D{parameter}={value}')

        # Finally, specify the OpenSCAD source file
        command.append(inputFilePath)

        # Execute the command
        subprocess.run(command)