from setuptools import setup, find_packages


VERSION = '0.0.1'


def readme():
    with open("README.md") as f:
        return f.read()


with open("requirements.txt") as file:
    REQUIREMENTS = [line.strip() for line in file]


setup(
    name='html-to-editorjs',
    version=VERSION,
    description='Convert HTML to Editor.js JSON format.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/vastray/html_to_editorjs',
    author='Kirill Glushkov',
    author_email='vastray@icloud.com',
    license='MIT',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)