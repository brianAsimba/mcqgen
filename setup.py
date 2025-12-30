from setuptools import setup, find_packages

setup(
    name="mcqgenerator",
    version="0.1.0",
    author="Brian Asimba",
    description="Multiple choice question generator",
    authot_email='brian377@gmail.com',
    packages=find_packages(),
    install_requires=[
        "openai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
    ],
)
