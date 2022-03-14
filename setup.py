from setuptools import setup, find_packages

setup(
    name='social-apis',
    version='0.2',
    url='https://github.com/azavodov/social-apis',
    license='MIT',
    author='Andrey Zavodov',
    author_email='a.p.zavodov@gmail.com',
    description='Make requests to different APIs with one library',
    packages=find_packages(exclude=['tests']),
    package_dir={'': 'src'},
    long_description=open('README.rst').read(),
    keywords='social networks API',
    zip_safe=False
)
