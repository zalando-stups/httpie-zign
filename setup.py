from setuptools import setup


setup(
    name='httpie-zign',
    description='Zign OAuth 2 plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.1',
    author='Henning Jacobs',
    author_email='henning.jacobs@zalando.de',
    license='Apache 2.0',
    url='https://github.com/zalando-stups/httpie-zign',
    py_modules=['httpie_zign'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_zign = httpie_zign:ZignPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'stups-zign'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
