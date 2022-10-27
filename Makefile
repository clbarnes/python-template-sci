clean:
	rm -rf mypackage

package: clean
	cookiecutter --no-input .

test: package
	cd mypackage \
	&& python -m venv --prompt mypackage env \
	&& source env/bin/activate \
	&& make install-dev \
	&& make lint \
	&& make test \
	|| deactivate
