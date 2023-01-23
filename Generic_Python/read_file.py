import io

def readFile(fileName,emails):
    with io.open(fileName,"r",encoding="utf-8")as f1:
        data=f1.read()
        f1.close()
    lines=data.split("\n")[1:]
    row=[]
    for email in emails:
        for line in lines:
            emailFromFile=line.split(",")[1]
            if emailFromFile==email:
                row.append(line)
                break
    return row


