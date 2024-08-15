# Routes Directory

This directory contains the route definitions for the Flask application. Each file in this directory corresponds to a specific set of API endpoints.

## Files

### `fetch_data.py`
- **Purpose:** Defines the `/fetch-data` endpoint.
- **Functionality:** Simulates fetching data from an external service using mock data.

### `process_data.py`
- **Purpose:** Defines the `/process-data` endpoint.
- **Functionality:** Processes the fetched data (e.g., converts product names to uppercase) and stores the processed data in temporary in-memory storage.

### `get_processed_data.py`
- **Purpose:** Defines the `/get-processed-data` endpoint.
- **Functionality:** Retrieves the processed data stored in memory and returns it to the client.

