
from setuptools import setup, find_packages
import sim

VERSION = sim.Version().get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name=sim.AppInfo.name,
    version=VERSION,
    description=sim.AppInfo.description,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="{0} @{1}".format(sim.Autor.name, sim.Autor.alias),
    author_email=sim.Autor.email,
    url=sim.AppInfo.url,
    license=sim.AppInfo.license,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        sim = sim.main:main
    """,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
