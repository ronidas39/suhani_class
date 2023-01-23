import io

def writeFile(filename,rows):

    with io.open(filename,"w",encoding="utf-8")as f1:
        f1.write("Name,Email,Phone,Company,Department"+"\n")
        for row in rows:
            f1.write(row+","+"IT"+"\n")
        f1.close()