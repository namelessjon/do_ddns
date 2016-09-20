from setuptools import setup

setup(
	name='do_ddns',
	version='0.1',
	scripts=['do_ddns'],
	url='http://github.com/namelessjon/do_ddns',
	author='namelessjon',
	author_email='jonathan.stott@gmail.com',
	license='APL2',
	install_requires=[
		'requests',
		'click'
	],
)
