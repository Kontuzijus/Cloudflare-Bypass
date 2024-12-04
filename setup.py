[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "Cloudflare-Bypass"
version = "0.1"
description = "A tool to bypass Cloudflare protection."
authors = [
    { name = "LOBYXLYX", email = "author@example.com" }
]
readme = "README.md"  # Optional, if a README.md exists
requires-python = ">=3.11.8"
dependencies = []  # Add dependencies like ["requests", "numpy"]

[tool.setuptools.packages.find]
where = ["."]
