from flask import Flask 

app = Flask(__name__)

# get   localhost:포트번호/

@app.route('/', methods = ['GET'])  
           # /는 path 부분 ex ) https://www.naver.com/  이거랑 같은 것  / 뒤에 아무것도 없다(리눅스의 루트경로랑 똑같은거다)
def hello_world() :
    return 'HELLO WORLD'




if __name__ == "__main__" :
    app.run()

# 그냥 쓴글