#封装request
import requests
class Request():
    def __init__(self):
        pass

    def parse(self, response):#格式编码转换成中文
        return response.decode('unicode_escape')
    def requst_api(self,protocol,method,url,header = None,data = None):
        if protocol.lower() == "http" or "https":
            pass
            if method.lower() == "get":
                result = requests.get(url=url,data = data,headers = header).text
                return result
            elif method.lower() == "post":
                result = requests.post(url = url,json=data,headers = header).content
                return result
            elif method.lower() == "head":
                pass
            elif method.lower() == "put":
                pass
            elif method.lower() == "delete":
                pass
        else:
            pass
if __name__ == "__main__":
    test = Request()
    header = {'content-type': "application/json"}
    result = test.requst_api("http","post","http://127.0.0.1:5000/login",{"username":123,"password":123})
    decode_result = test.parse(result)
    get_result = test.requst_api("http","get","http://127.0.0.1:5000/logincode",header)
    print( decode_result)
    print(get_result)