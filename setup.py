# setup.py
from setuptools import setup, find_packages

setup(
    name='sujith',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.2',
        # List your project dependencies here
        # 'requests', 'numpy', etc.
    ],
    entry_points={
        'console_scripts': [
            'your-script-name=your_package.module:first build',  # For creating command-line tools
        ],
    },
)
