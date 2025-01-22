import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws-sdk",
    version="0.0.1",
    author="Chesney Nyame",
    author_email="ches_tech_cloud@outlook.com",
    description="Package to standardise aws boto set-up",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chesney-nyame18/aws-sdk",
    packages=setuptools.find_packages(),
    install_requires=[
          'boto3',
          'botocore'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Proprietary",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)