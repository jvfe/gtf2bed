from setuptools import setup

setup(
    name="gtf2bed",
    version="0.1",
    py_modules=["repo"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        gtf2bed=gtf2bed:gtf2bed
    """,
)