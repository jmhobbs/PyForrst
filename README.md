# PyForrst

PyForrst is a quick little file to access the [Forrst API](http://forrst.com/apidocs.html).

It doesn't do much yet, no bound checking or object translation, but it works!

# Usage

    from PyForrst import Forrst

		api = Forrst( 1 ) # API Version is the constructor argument
		me = api.users.info( username = 'jmhobbs' )

Returns an object like this one:

    { 
		  u'resp': {
		    u'stat': u'ok',
				u'user': {
				  u'username': u'jmhobbs',
					u'id': u'3199'
				}
		  }
		}

All API calls will either return a response object or a False is the API returned 404.

Network problems and the like will raise exceptions of a wide variety :-)

# Testing

PyForrst is in flux at the moment (like the Forrst API) so it has minimal test suites.

You can run what it has with nose.

    $ cd PyForrst
		$ nosetests
		..
		----------------------------------------------------------------------
		Ran 2 tests in 0.454s

		OK
		$

# Installation

    $ python setup.py install
