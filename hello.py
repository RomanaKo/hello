import sys

def french():
	print('Bon Jour')

def ahoj():
	print('Ahoj')

def hello():
	print('Hello')
	
def main():
	if sys.argv[1] == "fr":
		french()
	elif sys.argv[1] == "sk":
		ahoj()
	else
		hello()
	
if __name__ = "__main__" :
	main()
	
