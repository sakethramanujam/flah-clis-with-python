from setuptools import setup

setup(
    name="todo",
    version="0.0.1",
    py_modules=["todo"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        todo=todo:cli
    """,
)