from setuptools import setup, find_packages

requires = [
    "simple-settings",
    "faust-streaming",
    "django~=2.2.0",

]

setup(
    name='faust-streaming-example',
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
            'faust_streaming = faust_streaming.app:main',
        ],
    },
)
