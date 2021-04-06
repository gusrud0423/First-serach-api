# json 형식으로 메세지 처리하기 
from flask import Flask, request
# HTTP의 상태코드를 전송 할 수 있는 라이브러리
from http import HTTPStatus


app = Flask(__name__)

# get   localhost:포트번호/

@app.route('/', methods = ['GET'])  
           # /는 path 부분 ex ) https://www.naver.com/  이거랑 같은 것  / 뒤에 아무것도 없다(리눅스의 루트경로랑 똑같은거다)
def hello_world() :
    return 'HELLO WORLD'

@ app.route('/act', methods = ['GET'])
def act( ) :
    ret = {'count': 2,
            'students' : [
                {'name' : '길동', 'age' : 30},
                {'name' : '김나나', 'age' : 25}
            ]
    }
    return ret

# 두개의 숫자를 클라이언트에게 받는다. x ,y     # 이거 실행할 때 안되면 그이유는 이 함수 쓴게 반영이 되지않아 원래 실행했던것을 컨트롤 c 로 종료 후 다시 실행해야 한다 
#  받은 두 숫자를 더해서, 클라이언트에게 리스판스
@app.route('/add_two_nums', methods = ['POST'])
def add_two_nums() :
    data = request.get_json()   # 이게 포스트맨의 밑에 데이터와 연결됨 
    # 포스트맨 바디에 data = { "x" : 345 , "y" : 789} 썼음

    if 'x' not in data or 'y' not in data :    # KeyError: 'x' 이거 포스트맨에 없으면 에러뜬다 그래서 예외 처리 해줘야 한다
        return {'message' : '파라미터 오류'}, HTTPStatus.BAD_REQUEST         # 근데 이렇게 하니  포스트맨에 y 만 있을 때 파라미터 오류라 뜨는데 200 ok 라 뜬다 그래서 HTTP 라이브러리 써야한다

    x = data['x']   # 변수는 다름이름 으로 해도 됨 num1,2 로
    y = data['y']

    z = x + y

    ret = {'sum' : z}
    
    return ret ,HTTPStatus.BAD_REQUEST   # 아무거나 리턴 받아봐  그리고 app.run(port=5001) 로 하면 포트만 바뀌고 똑같이 뜬다 
                                          

if __name__ == "__main__" :
    app.run(port=5001)