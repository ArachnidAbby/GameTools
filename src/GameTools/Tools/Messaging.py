global messageDict
messageDict={}

def send_Message(messageName, index=None, *args,**kwargs):
	'''
    tells functions that are listening to this message to run with whatever args are specified
    You can also specify and index if there are multiple function in that list.
    usage:
      send_Message("Default Message",*args,**Kwargs)
	'''
	global messageDict
	if index==None:
		for func in messageDict[messageName]:
			func(*args,**kwargs)
			#func(*args)
	else:
		messageDict[messageName][index](*args)

def recv_Message(messageName):
	'''
	This is a decorator that can be used to specify that 
	your function is a listener for a specific message
	usage:
      @recv_Message("Message Name")
      def myListener(myArg, myKwarg = None):
          pass
	'''
	global messageDict
	def inner(function,*args,**kwargs):
		global messageDict
		if not messageName in messageDict.keys():
			messageDict[messageName]=[]
		if not function in messageDict[messageName]:
			messageDict[messageName].append(function)
		function
	return inner

@recv_Message("Default Message")
def DefaultHandler(TestKwarg="TestKwarg"):
    print("message works")
    print(TestKwarg)