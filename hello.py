import sys

def french():
	print('Bon Jour Madame ')

def ahoj():
	print('Ahojte Vsetci')

def hello():
	print('Hello Everyone')
	
def main():
	if sys.argv[1] == "fr":
		french()
	elif sys.argv[1] == "sk":
		ahoj()
	else
		hello()
	
if __name__ = "__main__" :
	main()
	
