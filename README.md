# CityWeather - FastAPI
CityWeather is a simple web application built with FastAPI that provides current weather information for cities around the world. It fetches data from a public weather API and serves it through a RESTful interface.
## Features
- Get current weather information for any city.

## Installation
1. cloning the repository and navigate to the project directory.
```bash
  git clone https://github.com/MahinShahriar/fast-weather.giteather.git
```

2. If have not <strong>uv</strong> installed, Install uv(ultra fast package manager) in through terminal. And verify the installation.
```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  uv --version
```
or go to official website  [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) for more installation options.

3. Initialize uv in the project directory and install the dependencies.
```bash
  uv init
  uv sync
```

4. Create a `.env` file in the project root directory and add your weather API key.
```env
  API_KEY=your_api_key_here
```
5. Run the FastAPI application using uv.
```bash
   uv run fastapi dev main.py
```

## Technologies Used
- FastAPI
- Uvicorn
- Requests
- Pydantic
- Python-dotenv
- Public Weather API
- UV (Ultra Fast Package Manager)

