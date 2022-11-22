import pathlib
import tscribe
import os

# to get the current working directory
directory = os.getcwd()

print(directory)
inputPath = 'inputFiles/outcome11-CDH.json'
outputPath = 'outputFiles/outcome11-CDH.docx'
p = pathlib.Path(inputPath).exists()
print(p)

tscribe.write(inputPath, format="docx", save_as=outputPath)
