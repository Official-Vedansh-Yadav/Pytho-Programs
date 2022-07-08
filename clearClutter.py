import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def moveFiles(folderName,files):
    count = 0
    for file in files:
        os.replace(file, f"{folderName}/{file}")
        count += 1
    if (not(files == [])):
        print(f"Following Files are added to the folder {folderName} : {files} and the Total Number of files is {count}")
    else :
        print(f"No Clutter to add in the folder {folderName}")

files = os.listdir()
pyFiles = [file for file in files if os.path.splitext(file)[1].lower() == ".py"]

for i in pyFiles:
    files.remove(i)
print(f"Name of all the files : {files}\n")

createIfNotExist("Images")
createIfNotExist("Media")
createIfNotExist("Docs")
createIfNotExist("Others")
createIfNotExist("Zips")

imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt", ".docx", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".webm", ".opus"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

zipExts = [".zip", ".rar"]
zips = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in zipExts) and (os.path.isfile(file)):
        others.append(file)


moveFiles("Images", images)
moveFiles("Media", medias)
moveFiles("Docs", docs)
moveFiles("Others", others)
moveFiles("Zips", zips)