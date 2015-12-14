from setuptools import setup


setup(
    name='httpie-zign',
    description='Zign OAuth 2 plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.2',
    author='Henning Jacobs',
    author_email='henning.jacobs@zalando.de',
    license='Apache License 2.0',
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
        'stups-zign>=1.0.17'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Plugins',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
    keywords='httpie oauth oauth2 stups zign access token',
)
