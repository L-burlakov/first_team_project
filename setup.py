from setuptools import setup, find_namespace_packages

setup(
    name='first_team_project',
    version='1.0',
    description='Virtual personal assistent',
    author='GO_IT_5 first_team',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['pyparsing'],
    entry_points={'console_scripts': [
        'v_assistant = first_team_project.wery_main:main']}
)
