#!/usr/bin/python
from datetime import datetime
import asyncore
from smtpd import SMTPServer

class SpamPot(SMTPServer):
	no = 0
	def process_message(self, peer, mailfrom, rcpttos, data):
		filename = '%s-%d.txt'  % (datetime.now().strftime('%Y%m%d%H%M%S'), self.no)
		f = open(filename, 'w')
		f.write(data)
		f.close
		print 'Email received at %s and saved as %s' % (datetime.now().strftime('%H:%M:%S'), filename)
		self.no += 1

def run():
	print "SMTP Server HoneyTrap"
	print "QUit the server with Control-C"
	server = SpamPot(('0.0.0.0', 2525), None)
	try:
		asyncore.loop()
	except KeyboardInterupt:
		pass

if __name__ == '__main__':
	run()