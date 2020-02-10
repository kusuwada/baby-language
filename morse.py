#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yaml

class Morse():
	morse_map = {}
	
	def __init__(self):
		with open('morse.yml', 'r') as f:
			self.morse_map = yaml.safe_load(f)
			
	def dec(self, morse):
		message = ''
		lines = morse.split('\n')
		for line in lines:
			for m in line.strip().split(' '):
				try:
					message += [k for k, v in self.morse_map.items() if v == m][0]
				except:
					print('[ERROR] There\'s invalid character: ' + m)
					message += '*' + m + '*'
			message += ' '
		return message.strip()
	
	def enc(self, message):
		morse = ''
		for m in message:
			if m == ' ':
				morse += '\n'
			else:
				try:
					morse += self.morse_map[m.upper()]
				except:
					print('[ERROR] There\'s invalid character: ' + m)
					morse += '*' + m + '*'
				morse += ' '
		return morse.strip()

if __name__ == '__main__':
	morse = Morse()
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
			result = morse.dec(source)
		elif m_mode == 'e':
			result = morse.enc(source)
		print(result)