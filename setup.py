from setuptools import setup, find_packages
setup(
    name='dxl-shape',
    version='0.1.2',
    description='Shape library.',
    url='https://github.com/tech-pi/dxshape',
    author='Hong Xiang',
    author_email='hx.hongxiang@gmail.com',
    license='MIT',
    namespace_packages=['dxl'],
    packages=find_packages('src/python'),
    package_dir={'': 'src/python'},
    install_requires=[
        'doufo==0.0.4',
        'matplotlib',
        'typing',
        'numba',
        'numpy',
    ],
    scripts=[],
    #   namespace_packages = ['dxl'],
    zip_safe=False)
