# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

packages = find_packages()


setup(
    name="TwisTelegram, a.k.a puta bida TT",
    version="0.0.1",
    description="Telegram Bot - Python Twisted based bot",
    author="",
    author_email='',
    url='https://github.com/teclis/TwisTelegram',
    download_url="https://github.com/teclis/TwisTelegram/tarball/v0.0.1",
    license='GNU',
    packages=['TwisTelegram'],
    install_requires=[
                      'TelegramBotAPI==0.3.4',
					  'twisted',
                      ],
    entry_points={
        "console_scripts": [
            "twistelegram=TwisTelegram.service:main",
        ]
    },
)
