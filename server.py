from os import path
from json import dumps
from flask import Flask, request

app = Flask(__name__);

def store_data(json_data):
    ''' Place the json file containing problem info in ~/Document/Problem \info '''
    problem_data_path = path.join(path.expanduser('~'), 'Documents', 
            'Problem info', 'problem data')
    problem_data_file = open(problem_data_path, 'w+')
    problem_data_file.write(dumps(json_data))
    problem_data_file.close()

@app.route('/', methods=['POST'])
def test_cases():
    ''' Receive the problem infos '''
    json_data = request.get_json()
    store_data(json_data)
    return ''

if __name__ == '__main__':
    app.run(debug = True, port = 8080)
