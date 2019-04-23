# OJ-test-case-parser

### Overview
This is a tool to parse sample cases from certain online judges and automate the testing. This tool is designed to work 
with [competitive-companion](https://github.com/jmerle/competitive-companion) and currently work only with c++ programs.

### Requirement
- [Python 3+](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [competitive-companion](https://github.com/jmerle/competitive-companion) (configure it to send to port 8080)
- You need to create a direcotry '~/Document/Problem \info' where the problem info will be saved

### How to use
1. start the server to listen on port 8080 and leave it running in the background
```bash
python3 <the directory where server.py is>/server.py
```
2. go to the problem you are solving and press the '+' sign of competitive companion or just press Ctrl+Shift+U
3. compile your program
4. run the tester program and give it an argument the name of the executable file (default 'a')
```bash
python3 <the directory where tester.py is>/tester.py <executable name>
```
### What this tool do
- parse the input and output from the online judge
- test the output of your code with the output of the judge
- calculate your execution time and check for TLE
- [TODO] give warning if the input/output is not from standard input
