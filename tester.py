from re import sub
from sys import argv
from time import time
from json import loads
from os import path, system

def get_data(file_path):
    ''' Get data from file '''
    infile = open(file_path, 'r')
    data = infile.read()
    infile.close()
    return data

def store_data(file_path, data):
    ''' Store data in file '''
    file_path = open(file_path, 'w+')
    file_path.write(data)
    file_path.close()

def main():
    exec_name = 'a'

    if len(argv) > 1: # given a custom name for the executable file
        exec_name = argv[1]

    # path of the json file containing the info
    data_path = path.join(path.expanduser('~'), 'Documents', 'Problem info')

    data = get_data(path.join(data_path, 'problem data'))
    json_data = loads(data) # loading the info into a json dictionary

    passed_samples = True

    for test in json_data['tests']:
        print('=' * 50)

        current_input_path = path.join(data_path, 'in')
        store_data(current_input_path, test['input'])

        print('INPUT\n' + test['input']) # input from the site

        start_time = time()
        system('./' + exec_name + ' < "' + current_input_path + '" > .outfile') # ./a is the cpp program that is compiled and to be executed
        end_time = time()

        output = get_data('.outfile')
        system('rm .outfile')

        print('OUTPUT')
        print(output) # output of your program

        print('ACCEPTED')
        print(test['output']) # output from the site

        print('STATUS: ', end='')
        if end_time - start_time > float(json_data['timeLimit'] / 1000.0): # check for time limit
            passed_samples = False
            print('TLE')
        elif output == test['output']: # check for correct solution
            print('Ok')
        else: # wrong answer
            passed_samples = False
            print('Different Output')

        print('EXECUTION TIME:', '{:.5f} sec'.format(end_time - start_time)) # execution time of your program

        print('=' * 50)

    if passed_samples: # results of testing
        print('\nALL SAMPLES PASSED')
    else:
        print('\nFAILED SAMPLE TESTS')

if __name__ == '__main__':
    main()
