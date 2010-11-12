# -*- coding: utf-8 -*-

"""
PyForrst is a simple module for quick access to the Forrst API.
"""

import urllib
import urllib2
import json

# Based on http://forrst.com/apidocs.html
# Last Updated 2010-11-12

class Forrst ( object ):

	def __init__ ( self, version ):
		self.version = version
		self.method = ''

	def __getattr__ ( self, name ):
		self.method = '/'.join ( ( self.method, name ) )
		return self

	def __call__ ( self, **kwargs ):
		data = urllib.urlencode( kwargs )
		url = 'http://api.forrst.com/api/v%d%s?%s' % ( self.version, self.method, data )

		self.method = ''

		try:
			req = urllib2.Request( url )
			response = urllib2.urlopen( req )
			value = response.read()
			return json.loads( value )
		except HTTPError, e:
			if 404 == e.code:
				return False
			else:
				raise e
