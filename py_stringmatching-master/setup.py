from setuptools import find_packages, setup, Extension
import subprocess
import sys
import os

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

# make sure numpy is installed, as we need numpy to compile the C extensions.
# If numpy is not installed, automatically install it using pip.
install_and_import('numpy')

def generate_cython():
    cwd = os.path.abspath(os.path.dirname(__file__))
    print("Cythonizing sources")
    p = subprocess.call([sys.executable, os.path.join(cwd,
                                                      'build_tools',
                                                      'cythonize.py'),
                         'py_stringmatching'],
                        cwd=cwd)
    if p != 0:
        raise RuntimeError("Running cythonize failed!")


if __name__ == "__main__":

    no_frills = (len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
                                         sys.argv[1] in ('--help-commands',
                                                         'egg_info', '--version',
                                                         'clean')))

    cwd = os.path.abspath(os.path.dirname(__file__))
    if not os.path.exists(os.path.join(cwd, 'PKG-INFO')) and not no_frills:
        # Generate Cython sources, unless building from source release
        generate_cython()

    # specify extensions that need to be compiled
    extensions = [Extension("py_stringmatching.similarity_measure.cython_levenshtein",
                            ["py_stringmatching/similarity_measure/cython_levenshtein.c"],
                            include_dirs=[numpy.get_include()])]

    # find packages to be included. exclude benchmarks.
    packages = find_packages(exclude=["benchmarks"])

    setup(
        name='py_stringmatching',
        version='0.1.1',
        description='Python library for string matching.',
        long_description="""
    String matching is an important problem in many settings such as data integration, natural language processing,etc.
    This package aims to implement most commonly used string matching measures.
    """,
        url='http://github.com/anhaidgroup/py_stringmatching',
        author='Paul Suganthan G. C.',
        author_email='paulgc@cs.wisc.edu',
        license=['BSD'],
        packages=packages,
        install_requires=[
            'numpy >= 1.7.0',
            'six'
        ],
        ext_modules=extensions,
        include_package_data=True,
        zip_safe=False
    )

