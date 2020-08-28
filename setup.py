from setuptools import find_packages, setup


setup(
	name="ccm",
	version="1.0.0",
	packages=find_packages(),
	include_package_data=True,
	zip_file=False,
	install_required=[
		'flask',
	],
)
