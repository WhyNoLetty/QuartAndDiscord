from setuptools import setup

with open("README.md", "r") as ld:
    long_description = ld.read()

setup(
    name="discord-quart",
    author="Mr-Letty",
    url="https://github.com/WhyNoLetty/QuartAndDiscord",
    version="1.0",
    packages=["discord.ext.dashboard"],
    license="MIT",
    description="Um extersão que permite a conexão entre discord.py e quart.",
    install_requires=["discord.py>=1.4.1"],
    python_requires=">=3.6"
)