# Production-Ready Application

## Overview
A containerized Python application configured with automated `pytest` test suites, structured logging, environment-based configuration, and monitoring endpoints.

---

## Prerequisites
* Python 3.11+
* Docker & Docker Compose
* Pytest

---

## Environment Configuration
Create a `.env` file in the root directory:
```env
PORT=8000
LOG_LEVEL=INFO
SECRET_KEY=your_secret_key_here

# Day 24: Production Readiness & Deployment

## Overview
A containerized FastAPI application featuring automated `pytest` test suites, structured logging, environment-based configuration, and monitoring endpoints.

---

## Running Tests
Run the test suite using pytest:
```bash
python -m pytest tests/