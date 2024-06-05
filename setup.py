from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf8") as reqs:
    required_packages = reqs.read().splitlines()

setuptools.setup(
    name="nfl-player-stats",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=required_packages,
)
