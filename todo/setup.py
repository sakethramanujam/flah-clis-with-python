from setuptools import setup, find_packages

setup(
    name="td",
    version="0.0.1",
    include_package_data=True,
    install_requires=["click"],
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        td=todo.cli:cli
    """,
)