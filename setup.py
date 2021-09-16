from setuptools import setup

setup(name='dev_aberto_manoela',
    version="0.0.1",
    author="Manoela Campos",
    author_email="manucirne@gmail.com",
    description="Dev aberto",
    packages=['dev_aberto'],
    python_requires=">=3.6",
    scripts=['scripts/hello.py'],
    install_requires=[
        'requests'
    ],
)
