try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="luigi-monitor",
    version="1.1.4",
    description="Send summary messages of your Luigi jobs to MS Teams.",
    long_description=open("README.md").read(),
    author_email="adrian.turcato@initiative.com",
    license="MIT",
    packages=['luigi_monitor'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="luigi",
    install_requires=["requests", "luigi"],
    entry_points={
        "console_scripts": ["luigi-monitor=luigi_monitor.luigi_monitor:run"]
    }
)
