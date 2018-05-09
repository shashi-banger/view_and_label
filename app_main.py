
from flask import Flask, request
app = Flask(__name__, static_url_path='', static_folder='')
app.debug = True

@app.route('/')
def hello_world():
    print "hello"
    return app.send_static_file('index.html')

@app.route('/<asset>', methods=['GET'])
def api_article(asset):
    print "Got get for " + asset
    return app.send_static_file(asset)

@app.route('/', methods=['POST'])
def post_handle():
    print "Post recvd"
    print request.data
    with open('data.json', 'w') as fd:
        fd.write(request.data)
    return ''



if __name__ == '__main__':
  app.run()
