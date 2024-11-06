from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # biblioteca para manipulação de imagens
    ],
)
