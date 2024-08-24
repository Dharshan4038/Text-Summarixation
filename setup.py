import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "Dharshan4038"
SRC_REPO = "textSummarizier"
AUTHOR_EMAIL = "dharshand9@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is a text Summarizier application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dharshan4038/Text-Summarization",
    project_urls={
        "Bug Tracker": "https://github.com/Dharshan4038/Text-Summarization/issues",
    },
    package_dir={"": "src"},  # Corrected line
    packages=setuptools.find_packages(where="src"),
)
