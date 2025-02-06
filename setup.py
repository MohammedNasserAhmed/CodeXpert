import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0"

REPO_NAME = "CodeXpert"
AUTHOR_USER_NAME = "MohammedNasserAhmed"
SRC_REPO = "codexpert"
AUTHOR_EMAIL = "abunasserip@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="CodeXpert: A cutting-edge AI-powered code analysis tool leveraging CodeLlama, FAISS, and HuggingFace for efficient code understanding, explanation, and optimization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "codexpert"},
    packages=setuptools.find_packages(where="codexpert"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "streamlit",
        "openai",
        "langchain",
        "transformers",
        "accelerate",
        "sentence-transformers",
        "faiss-cpu",
        "langchainhub",
        "langchain-community",
        "chardet",
        "langchain_huggingface",
    ],
)
