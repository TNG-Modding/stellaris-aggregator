from setuptools import setup, find_packages

setup(
    name = "stellarisfiles",
    version = "0.0.0",
    author = "Oliver Barnum",
    author_email = "oliverbarnum32@gmail.com",
    description = "Creates a ui to view Stellaris event information",
    url = "",
    packages=find_packages(),
    install_requires=["click", "ensure", "luaparser", "pyyaml", "lark-parser"],
    entry_points = {
        "console_scripts": ["stellarisfiles=stellarisfiles.cli:cli"]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)