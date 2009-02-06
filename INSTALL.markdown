# Staple - Installation #

To install Staple, you will need git and Python 2.5+

It is recommended that you install the package into a [virtualenv](http://pypi.python.org/pypi/virtualenv) so that it will not conflict with your base python install...

    $ sudo easy_install virtualenv
	$ virtualenv --no-site-packages staple_sites
	$ cd staple_sites
	$ source bin/activate
	(staple_sites)...$ 

From here, we can download the source code and install it...

	(staple_sites)...$ git clone git://github.com/junkafarian/staple.git staple
	(staple_sites)...$ cd staple
	(staple_sites)...$ python setup.py install

