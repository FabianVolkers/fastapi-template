#!/bin/bash 
if ! command -v poetry &> /dev/null;
then
	echo "Poetry could not be found";
	echo "Installing poetry...";
	ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.8/etc/openssl;
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -;
else
	echo "Poetry already installed, skipping..."
fi
