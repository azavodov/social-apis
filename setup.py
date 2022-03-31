from setuptools import setup, find_packages
from src.social_apis import __version__

setup(
    name='social-apis',
    version=f'{__version__}',
    url='https://github.com/azavodov/social-apis',
    license='MIT',
    author='Andrey Zavodov',
    author_email='a.p.zavodov@gmail.com',
    description='Make requests to different APIs with one library',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    long_description=open('README.rst').read(),
    keywords='social networks API',
    zip_safe=False
)
