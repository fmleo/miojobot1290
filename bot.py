import random
import tweepy

consumer_secret = 'OYBKOIFuFMdqp9mbUgf1reosnu5ZvmJwyA3s8R2hEVEjGwctEy'
consumer_key = 'fSp3RCeHib4i1xZGvLJe1WERO'
access_token = '1176693420863184896-aMxTr82aYwaY2UUHr5H7zGpn5ALzKr'
access_token_secret = 'YEq4f9MFZtgUxeaFqvWjVYKPg7NT6Bw85LbLvoP1LRbFm'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

sabores = open('sabores.txt', 'r').read().split('\n')
comps = open('complementos.txt', 'r').read().split('\n')
frases = open('frases.txt', 'r').read().split('\n')
logs = open('logs.txt', '+w')

n = random.randint(1, 5)

try:
	generic_string = ('com ')
	sabor = random.choice(sabores)
	frase = random.choice(frases)
	a = ('{} {} '.format(frase, sabor))
	for i in range(n):
	    comp = random.choice(comps)
	    while comp in generic_string:
	        comp = random.choice(comps)
	        if comp not in generic_string:
	            break
	        if comp != '' and comp != ' ':
	            break
	    generic_string += ('{}'.format(comp))
	    if i == n-2:
	        generic_string += ' e '
	    elif i != n-1:
	        generic_string += ', '
	status = a+generic_string
	print(status)

	api.update_status(status=status)
except Exception as exception:
	logs.write(exception)
