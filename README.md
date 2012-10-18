# About

Python script to check a group of server's HTTP Responses. 

# Installation

`pip install -r requirements.txt`

# Example Output

	> ./testServerPool.py 
	http://example.com/ 302 Found
	
	> ./testServerPool.py --help
	usage: testServerPool.py [-h] [--version] [-p PATH] [-s] [-v] [-d]

	Server pool response testing

	optional arguments:
	  -h, --help            show this help message and exit
	  --version             show program's version number and exit
	  -p PATH, --path PATH  target path to check
	  -s, --secure          Use HTTPS
	  -v, --verbose         set verbosity
	  -d, --debug           debug