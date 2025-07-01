from setuptools import setup, find_packages

setup(
    name="weather-mcp-server",
    version="1.0.0",
    description="Weather MCP Server using Open-Meteo API",
    author="Weather MCP Team",
    packages=find_packages(),
    install_requires=[
        "mcp>=1.0.0",
        "requests>=2.25.0"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "weather-mcp=server:main",
        ],
    },
)
