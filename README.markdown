# Staple - A script for publishing static websites from Jinja templates #

## Initialising a project using PasteScript ##

If you have installed PasteScript before installing Staple, you will be able to initialise a new staple environment using a paster template...

    $ paster create -t staple my_site
	$ cd my_site && cat README.txt

## Initialising a project from a config file ##

To create a template directory based on a series of urls taken from a configuration file you can run...

    $ echo "/home.html" >> urls.config
    $ echo "/about.html" >> urls.config
	$ staple generate templates urls.config
	...
	$ ls templates
	about.html	home.html	master.layout

## Publishing the site ##

    $ staple publish -o htdocs/ templates/
	$ ls htdocs/
	about.html	home.html


