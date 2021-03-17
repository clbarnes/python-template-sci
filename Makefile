clean:
	rm -rf mypackage

package: clean
	cookiecutter --no-input .

test: package
	cd mypackage \
	&& make install-dev \
	&& make lint \
	&& make test
