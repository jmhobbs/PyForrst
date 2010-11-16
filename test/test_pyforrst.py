# -*- coding: utf-8 -*-
import unittest

import sys, os

# Fix it so we import the dev version of PyForrst before anything else
lib_path = os.path.abspath( os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), '..', 'lib' ) )
sys.path.insert( 0, lib_path )
import PyForrst
del sys.path[0]

class TestUsers ( unittest.TestCase ):

	def __init__ ( self, *args ):
		unittest.TestCase.__init__( self, *args )

		self.forrst = PyForrst.Forrst( 1 )

	def test_get_user_by_id ( self ):
		user = self.forrst.users.info( id=1 )
		self.assertEquals( user['resp']['stat'], 'ok' )
		self.assertEquals( user['resp']['user']['id'], '1' )

	def test_get_user_by_invalid_id ( self ):
		user = self.forrst.users.info( id=0 )
		self.assertEquals( user, False )

if __name__ == '__main__':
	unittest.main()