#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yaml
import morse

class Baby():
	lang_type = 'English'
	baby_map = {}
	morse = morse.Morse()
	
	def __init__(self):
		with open('baby.yml', 'r') as f:
			self.baby_map = yaml.safe_load(f)
					
	def dec(self, baby):
		morse = ''
		for m in baby.split(' '):
			while m != '':
				if m.startswith(self.baby_map[self.lang_type]['first']):
					morse += '.'
					m = m[len(self.baby_map[self.lang_type]['first']):]
				elif m.startswith(self.baby_map[self.lang_type]['second']):
					morse += '-'
					m = m[len(self.baby_map[self.lang_type]['second']):]
				elif m.startswith(self.baby_map[self.lang_type]['newline']):
					morse += '\n'
					m = m[len(self.baby_map[self.lang_type]['newline']):]
				else:
					morse += m  # for invalid input
					m = ''
			if not morse.endswith('\n'):
				morse += ' '
		message = self.morse.dec(morse)
		return message
	
	def enc(self, message):
		baby = ''
		morse = self.morse.enc(message)
		for m in morse:
			if m == '.':
				baby += self.baby_map[self.lang_type]['first']
			elif m == '-':
				baby += self.baby_map[self.lang_type]['second']
			elif m == '\n':
				baby += self.baby_map[self.lang_type]['newline']
				baby += ' '
			elif m == ' ':
				baby += ' '
			elif m == '*':  # for error morse code
				baby += ''
			else:
				baby += '*' + m + '*'
		return baby

if __name__ == '__main__':
	baby = Baby()
	m_mode = input('input mode (d: decode, e: encode) > ')
	if m_mode == 'd' or m_mode == 'D' or m_mode == 'decode':
		m_mode = 'd'
	elif m_mode == 'e' or m_mode == 'E' or m_mode == 'encode':
		m_mode = 'e'
	else:
		raise Exception('[ERRROR] invalid mode input!')
	
	while(True):
		source = input('input your message > ')
		if m_mode == 'd':
			result = baby.dec(source)
		elif m_mode == 'e':
			result = baby.enc(source)
		print(result)