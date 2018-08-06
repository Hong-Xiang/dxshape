from setuptools import setup, find_packages
setup(
    name='dxl-shape',
    version='0.1.0',
    description='Shape library.',
    url='https://github.com/Hong-Xiang/dxshape',
    author='Hong Xiang',
    author_email='hx.hongxiang@gmail.com',
    license='MIT',
    namespace_packages=['dxl'],
    packages=find_packages('src/python'),
    package_dir={'': 'src/python'},
    install_requires=[],
    scripts=[],
    #   namespace_packages = ['dxl'],
    zip_safe=False)
