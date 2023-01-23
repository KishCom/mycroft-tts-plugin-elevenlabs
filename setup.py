#!/usr/bin/env python3
from os.path import join, abspath, dirname
from setuptools import setup

with open(join(dirname(abspath(__file__)), 'requirements.txt')) as f:
    requirements = f.readlines()

PLUGIN_ENTRY_POINT = 'elevenlabs = mycroft_tts_plugin_elevenlabs:ElevenlabsTTSPlugin'
setup(
    name='mycroft-tts-plugin-elevenlabs',
    version='0.2.1',
    description='A tts plugin for mycroft',
    url='http://github.com/kishcom/mycroft-tts-plugin-elevenlabs',
    author='Andy Kish',
    author_email='mycroft@weedmark.systems',
    license='Apache-2.0',
    packages=['mycroft_tts_plugin_elevenlabs'],
    install_requires=requirements,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin tts',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)
