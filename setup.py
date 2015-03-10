# coding=utf-8
"""
setup for extension
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from future import standard_library
standard_library.install_aliases()
from distutils.core import setup
from Cython.Build import cythonize
from Cython.Compiler import Options
from Cython.Distutils import build_ext

directives = {
		'profile': False,
		'cdivision': True,
		'nonecheck': False,
		'wraparound': False,
		'boundscheck': False,
		'embedsignature': True,
		'warn.unused': False,
		'warn.unreachable': True,
		'warn.maybe_uninitialized': True,
		'warn.undeclared': False,
		'warn.unused_arg': False,
		'warn.unused_result': False,
		}

if __name__ == '__main__':
    Options.fast_fail = True
    Options.extra_link_args = ["-O3"]  # ["-g"],
    setup(cmdclass=dict(build_ext=build_ext),
          ext_modules = cythonize(
              'speedtestcythonmain.pyx',
              force=True,
              compiler_directives=directives)
    )
