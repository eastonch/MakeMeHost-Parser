from distutils.core import setup 
import py2exe 
setup(console=['mmh.py'], 
	options = {
	'py2exe': { 
	'packages': ['requests', 'Tkinter']}
	})