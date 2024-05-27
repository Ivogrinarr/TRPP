from setuptools import setup

# Чтение requirements.txt и подготовка списка зависимостей
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'aaaa',
    install_requires=requirements,
)