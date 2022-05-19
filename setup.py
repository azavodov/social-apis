from setuptools import setup, find_packages
from src.social_apis import __version__

setup(
    name='social-apis',
    version=f'{__version__}',
    url='https://github.com/azavodov/social-apis',
    license='MIT',
    author='Andrey Zavodov',
    author_email='a.p.zavodov@gmail.com',
    description='Social APIs is a library providing an easy way to access Social Networks APIs.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords='social networks API requests access automation',
    zip_safe=False
)
