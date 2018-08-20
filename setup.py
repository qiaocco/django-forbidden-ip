from setuptools import find_packages, setup

with open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='django-forbidden-ip',
    version=0.1,
    description='IP forbidding utilities for Django2.0',
    long_description=long_description,
    author='Jason Qiao',
    author_email='jasonqiao36@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/jasonqiao36/django-forbidden-ip',
    packages=find_packages(),
    install_requires=[
        'Django>=2.0',
    ],
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)