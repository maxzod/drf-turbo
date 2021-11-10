import distutils.core
import Cython.Build

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = False

distutils.core.setup(
    ext_modules = Cython.Build.cythonize("fields.pyx",annotate=False))
