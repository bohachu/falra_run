import setuptools

setuptools.setup(
    name='falra_run',
    version='0.1.0',
    author="Bowen Chiu",
    author_email="cbh@cameo.tw",
    description="FastAPI dynamic run python package",
    url="https://github.com/bohachu/falra_run",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
'''
# upload package to pip pypi, build make my own package
# pypi 密碼
帳號 bohachu
密碼 fu. 1i6cj06

rm dist/*.whl
python3 setup.py bdist_wheel
echo bohachu password:fu. 1i6cj06
python3 -m twine upload dist/*
'''