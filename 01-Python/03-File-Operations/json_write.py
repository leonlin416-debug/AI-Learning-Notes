import json

def json_write(filename,data):
    with open(filename,"w",encoding="utf-8") as f:  #“w”会覆盖写入
        json.dump(data,f,ensure_ascii=False,indent=4)
        #ensure_ascii=False 保持中文不要转变成Unicode
        #indent 缩进四个字符
books = [{
    "编号":"A001",
    "标题":"堂吉诃德",
    "作者":"塞万提斯"
}]

json_write("books.json",books)#自动在目录下创建并写入