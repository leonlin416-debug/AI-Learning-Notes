import json
def json_update(filename,data):
    with open(filename,"r",encoding="utf-8") as f:
        old_data = json.load(f)
        old_data.append(data)

    #重新以写入模式打开文件,并写入,直接用"w"会把原来的覆盖
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(old_data, f, ensure_ascii=False, indent=4)

books = {"编号":"A002","标题":"老人与海","作者":"海明威"}

json_update("books.json",books)