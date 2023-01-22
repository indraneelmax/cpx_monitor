from setuptools import setup

setup(
    name='cpx_monitor',
    version='0.1.0',
    description='A simple CPX Monitoring Tool',
    url='https://github.com/indraneelmax/cpx_monitor',
    author='Indraneel Srivastava',
    author_email='indraneel.max@gmail.com',
    packages=['cpx_monitor'],
    python_requires='>=3',
    install_requires=['mock',
                      'pytest',
                      'requests',
                      'prettytable',
                      ],
    scripts=["bin/cpx_monitor"],
)
