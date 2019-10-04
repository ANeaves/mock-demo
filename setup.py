import setuptools

setuptools.setup(
    name="mock_demo",
    author="Adam N",
    description="A demo for mock",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)