def get_msg():
	return 'Hello python world'

message = get_msg()
print(message)

def get_some_other_msg():
	return 'Some other message!!!'

get_msg = get_some_other_msg
print(get_msg())