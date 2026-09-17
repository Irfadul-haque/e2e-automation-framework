# Enterprise E2E Automation Framework

A production-grade, three-tier test automation framework built to demonstrate modern software testing patterns, resilient UI synchronization, and deterministic data management. Targeting the [Restful Booker Platform](https://automationintesting.online/), this framework is engineered for stability in fast-paced agile Scrum environments.

## Architectural Overview

1. **API Service Layer (pi_clients/):** HTTP client wrappers (Requests) handling authentication and direct database seeding.
2. **UI Page Object Model (pages/):** Encapsulated Selenium WebDriver logic handling SPA routing and React eventual consistency.
3. **Hybrid Execution Layer (	ests/hybrid/):** E2E workflows combining API setup with UI validation.

## Key Features

* **Intelligent State Management:** Custom pytest fixtures for automated entity cleanup.
* **Resilient Synchronization:** Explicit waits and polling strategies for React DOM rendering.
* **Dynamic Data Generation:** Faker-driven collision-free payloads.

## Setup & Execution

`ash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -v --tb=short
`
