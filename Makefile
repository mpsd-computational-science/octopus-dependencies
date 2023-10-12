spack-package.py:
	# spack's octopus/package.py provides a useful summary of the octopus dependencies (at least those is spack)
	wget --output-document=spack-package.py https://raw.githubusercontent.com/spack/spack/develop/var/spack/repos/builtin/packages/octopus/package.py

clean:
	rm -fv spack-package.py

libs:
	cat spack-package.py | grep depends_on
