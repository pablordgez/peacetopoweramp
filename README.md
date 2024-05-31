# peacetopoweramp
Script that converts a PeaceEQ preset to PowerampEQ format

How to use:
  1. Put your peace preset on the same folder as peacetopoweramp.py and rename the preset to preset.peace
  2. Double click peacetopoweramp.py or open a terminal, navigate to the folder with the script and run it using py/python/python3
  3. A file preset.json has been generated, that is the poweramp preset that you can import
You need Python 3 in order to use this script

Features implemented:
  Convert all bands with their gains and Qs
  
Features missing (might be added when I have time):
  1. Convert preamp
  2. Convert filter type (now all are converted as peak filters)
  3. Allow to run from terminal with arguments to set file name or path
  4. Convert Poweramp to Peace
  5. Refactor all the code, because it's very unreadable and there probably is a better way to write json than this, same goes for reading the source file
