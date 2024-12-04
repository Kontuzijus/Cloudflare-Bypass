from setuptools import setup, find_packages

setup(
    name="Cloudflare-Bypass",  # Replace with the desired package name
    version="0.1",  # Replace with the correct version
    author="Author Name",  # Replace with the author's name
    author_email="author@example.com",  # Replace with the author's email
    description="A tool to bypass Cloudflare protection.",
    url="https://github.com/Kontuzijus/Cloudflare-Bypass",  # Link to the GitHub repository
    packages=find_packages(),  # Automatically find Python packages in the directory
    install_requires=[],  # List required dependencies here, e.g., ['requests']
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with the appropriate license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',  # Specify the minimum Python version
)
