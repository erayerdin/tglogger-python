from setuptools import setup

import tglogger

with open("README.md", "r") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    DEPS = f.readlines()

with open("dev.requirements.txt", "r") as f:
    TEST_DEPS = f.readlines()

GITHUB_RELEASE_URL = "https://github.com/erayerdin/tglogger/archive/v{}.tar.gz"

setup(
    name="tglogger",
    version=tglogger.__version__,
    description="tglogger is a logger handler and formatter for Telegram bots.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/erayerdin/tglogger",
    download_url=GITHUB_RELEASE_URL.format(tglogger.__version__),
    packages=("tglogger",),
    include_package_data=True,
    keywords="telegram messaging communication logging",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Topic :: Communications :: Chat",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
    ],
    author=tglogger.__author__,
    author_email="eraygezer.94@gmail.com",
    license="Apache License 2.0",
    tests_require=TEST_DEPS,
    install_requires=DEPS,
    zip_safe=False,
)
