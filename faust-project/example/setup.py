from setuptools import setup, find_packages

requires = [
    "colorlog>=3.1.4",
    "dataclasses-avroschema",
    "faust",
    "python-schema-registry-client",
    "yarl<1.6.0,>=1.0",
    "multidict<5.0,>=4.5",
    "simple-settings",
    "typing-extensions",

]

setup(
    name='faust-example',
    version='0.0.1',
    description='Faust faust-streaming example with Docker Compose',
    long_description='''
    Example running Faust faust-streaming with Docker Compose (zookeeper, kafka)
    ''',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Sebastian Orzechowski',
    author_email='rewersq@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=[],
    setup_requires=[],
    dependency_links=[],
    entry_points={
        'console_scripts': [
            'example = example.app:main',
        ],
    },
)
