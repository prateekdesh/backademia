# Backademia API

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-blueviolet.svg)](https://fastapi.tiangolo.com/)

**Backademia** is a REST API designed to simplify scraping data from SRM Academia. It provides an easy-to-use abstraction, allowing developers to retrieve information with simple API calls.\
\
I plan on adding more endpoints to the API soon. Contributions are welcome.

## Features (Work In Progress)

* **Attendance Retrieval:** Fetches attendance data from SRM Academia.

## Getting Started

### Prerequisites

* Python 3.8+
* pip (Python package installer)

### Installation

1.  Clone the repository

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1.  Start the FastAPI application:

    ```bash
    uvicorn app:app --reload
    ```

    This will start the API server, and you can access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

## API Endpoints

### `/attendance` (POST)

* **Description:** Fetches attendance data from SRM Academia.
* **Method:** `POST`
* **Request Body Format:**

    ```json
    {
      "email": "your_srm_email@srmist.edu.in",
      "password": "your_srm_password"
    }
    ```

