import setuptools 

with open("Readme.md", "r", encoding= "utf-8") as f:
    long_description = f.read()



version ="0.0.0"

REPO_NAME = "Text_Summarisation"
AUTHOR_USER_NAME="Anarchist4"
SRC_REP0="textsummariser"
AUTHOR_EMAIL="kashanabdullah19@gmail.com"

setuptools.setup(
    name=SRC_REP0,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
        description="A small python package for NLP app",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_url={
            "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
        package_dir={"":"src"},
        packages=setuptools.find_packages(where="src")
)