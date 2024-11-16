ord(97)						# ASCII 	-> base10
chr("a")					# base10	-> ASCII

bytearray.fromhex("7061756c").decode()		# hex 		-> ASCII
hex(ord('a'))					# ASCII		-> hex

bytes(str, 'utf-8')				# ASCII		-> byte string

bytes.fromhex("68656c6c6f")			# hex		-> byte string
b"hello".hex()					# byte string	-> hex

import base64
base64.b64encode(b'\x85\xe9e\xa3')		# bytes		-> base-64
base64.b64decode(b'hellow==')			# base-64	-> bytes

from Crypto.Util.number import *
bytes_to_long(b'hello')				# byte string	-> base-10
i.to_bytes(len, byteorder='big')		# base-10	-> byte string

int(hex_value, 16)				# hex		-> base-10
hex(decimal_value)				# base-10	-> hex

bin(4785)[2:]					# base-10	-> base-2
int(0b01001, 2)					# base-2	-> base-10

format(121, '08b')  #(keeps leading zeroes)	# base-10	-> base-2


#.zfill(bits) to add starting zeroes
#message: HELLO
#ascii bytes: [72, 69, 76, 76, 79]
#hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
#base-16: 0x48454c4c4f
#base-10: 310400273487
#base-2: 0b01000001
#byte string: b'\x03\x34\nhello'


