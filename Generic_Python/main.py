import read_file,write_file

inputfilename="input.csv"
outputyfilename="output.csv"

emails=["libero@google.org","tempus.non@aol.edu","ipsum.curabitur@google.couk","auctor.vitae@hotmail.com"]
fileData=read_file.readFile(inputfilename,emails)
write_file.writeFile(outputyfilename,fileData)

