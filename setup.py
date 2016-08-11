from setuptools import setup


setup(name="roboot",
	  version="0.0.1",
	  description="Scaffolding for Robot Framework Test Cases",
	  author="Akash Shende",
	  author_email="akash0x53s@gmail.com",
	  url="https://github.com/akash0x53/roboot",
	  packages=["roboot"],
	  license="MIT",
	  entry_points={
		  'console_scripts': ['roboot = roboot.__main__:main']
		  },
	  install_requires=['robotframework', 'robotframework-selenium2library']
	  )
