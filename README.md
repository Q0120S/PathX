# PathX
PathX takes a URL and a string as input, and returns a list of modified URLs with the string appended to the URL path in different ways.

This tool can help you to Identify **Path XSS** and other stuffs.
## Installation
```console
git clone https://github.com/Q0120S/pathx.git
cd pathx
python3 pathx.py -h
```
## Usage
```bash
cat urls.txt | python3 pathx.py -s %22pathx
echo https://google.com/api/XSS/services/test | python3 pathx.py -s %22pathx
python3 pathx.py -u https://google.com/api/XSS/services/test -s %22pathx
```
### Output:
```bash
https://google.com/api%22pathx/XSS/services/test
https://google.com/api/XSS%22pathx/services/test
https://google.com/api/XSS/services%22pathx/test
https://google.com/api/XSS/services/test%22pathx
```
