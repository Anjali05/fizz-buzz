import re
from flask import Flask, Response
app = Flask(__name__)

@app.route('/fizzbuzz/')
def api_root():
    return 'Hello World'

@app.route('/fizzbuzz/<num>', methods = ['GET'])
def api_article(num):
    temp = re.search('[a-zA-Z]+',num)
    print temp
    if temp == None:
        if int(num) % 2 == 0:
            return Response("fizz", status=200)
        else:
            return Response("buzz", status=200)
    else:
        return Response("error", status=400)


if __name__ == '__main__':
    app.run()
