#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from baby import Baby

class TestBaby(unittest.TestCase):

	# check encoded baby_language is consists of only baby words.
	def check_encoded(self, encoded, baby_words):
		blocks = encoded.strip().split(' ')
		for block in blocks:
			while block != '':
				is_found = False
				for i in range(len(baby_words)):
					if block.startswith(baby_words[i]):
						block = block[len(baby_words[i]):]
						is_found = True
						break
				self.assertTrue(is_found)
		
	def test_normal(self):
		test_patterns = ['test', 'hello, world!', 'Baby Language is Fun']
		baby = Baby()
		baby_words = list(baby.baby_map['English'].values())
		for message in test_patterns:
			with self.subTest(message = message):
				encoded = baby.enc(message)
				self.check_encoded(encoded, baby_words)
				decoded = baby.dec(encoded)
				self.assertEqual(decoded, message.upper())
		
	def test_japanese(self):
		test_patterns = ['test', 'hello, world!', 'Baby Language is Fun']
		baby = Baby()
		baby.lang_type = 'Japanese'
		baby_words = list(baby.baby_map['Japanese'].values())
		
		for message in test_patterns:
			with self.subTest(message = message):
				encoded = baby.enc(message)
				self.check_encoded(encoded, baby_words)
				decoded = baby.dec(encoded)
				self.assertEqual(decoded, message.upper())
		
	def test_invalid_message(self):
		test_patterns = [
				('%test', '*%* ga goo googoogoo ga'),
				('i%u', 'googoo *%* googooga')
				]
		baby = Baby()
		baby_words = list(baby.baby_map['English'].values())
		for message, expect in test_patterns:
			with self.subTest(message = message, expect = expect):
				encoded = baby.enc(message)
				self.assertEqual(encoded, expect)
	
	def test_invalid_babylang(self):
		test_patterns = [
				('gogogo', '*gogogo*'),
				('', '**'),
				('googa gaagoo', 'A*-agoo*'),
				]
		baby = Baby()
		baby_words = list(baby.baby_map['English'].values())
		for babylang, expect in test_patterns:
			with self.subTest(babylang = babylang, expect = expect):
				decoded = baby.dec(babylang)
				self.assertEqual(decoded, expect)


if __name__ == "__main__":
	unittest.main()