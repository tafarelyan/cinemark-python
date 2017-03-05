from setuptools import setup, find_packages


def requirements():
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


setup(name='cinemark-python',
      version='0.0.5',
      description='Wrapper for Cinemark Brasil API',
      author='Tafarel Yan',
      author_email='tafarel.yan@gmail.com',
      url='https://github.com/ArrowsX/cinemark-python',
      packages=['cinemark'],
      install_requires=requirements(),
      )
