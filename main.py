# Sebastián Salazar

import os
import customScripterV2

inputPath ='inputFiles'

res = []
inputPath = 'inputFiles'
outputPath = 'outputFiles'
# Iterate directory
for path in os.listdir(inputPath):
    # check if current path is a file
    if os.path.isfile(os.path.join(inputPath, path)):
        #tscribe.write(inputPath+'/'+path, format="docx", save_as=path+".docx")
        inputFile=inputPath+'/'+path
        outputFile=outputPath+'/'+path
        print(inputFile)
        print(outputFile)
        customScripterV2.write(inputFile, format="docx", save_as=outputFile + ".docx")
print(res)

print('TERMINE!!!')

