import json

def json_read(filename):
    with open(filename,"r",encoding="utf-8") as f:
        data = json.load(f) #json->python对象
    return data

# json.load(f)	        从 JSON 文件读取数据
# json.loads(s)	        从 JSON 字符串读取数据
# json.dump(data, f)	将 Python 对象写入 JSON 文件
# json.dumps(data)	    将 Python 对象转换成 JSON strings