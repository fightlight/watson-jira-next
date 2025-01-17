from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="watson_jira_next",
    version="0.3.2",
    description="Format and upload Watson time logs to Jira as Tempo worklogs",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Office/Business :: Scheduling",
    ],
    url="https://github.com/PrimaMateria/watson-jira-next",
    author="Jonathan Medwig, Matus Benko",
    author_email="jonmedwig@gmail.com, matus.benko@gmail.com",
    license="MIT",
    packages=["watson_jira_next", "watson_jira_next.src"],
    install_requires=[
        "td-watson",
        "python-dateutil",
        "click >=7.0,<8.0",
        "simplejson",
        "colorama",
        "jira",
        "pyyaml",
        "pyxdg"
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={"console_scripts": ["watson-jira=watson_jira_next.cli:main"]},
    zip_safe=False,
    include_package_data=True,
)
