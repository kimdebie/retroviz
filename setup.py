import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="retroviz",
    version="0.4",
    author="Kim de Bie",
    author_email="kimdebie@outlook.com",
    description="RETRO-VIZ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kimdebie/retroviz-tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy',
          'scikit-learn>=0.21.3'
      ],
    python_requires='>=3.6',
)
