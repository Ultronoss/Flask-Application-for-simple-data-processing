# Flask Data Retrieval and Processing Application

## Setup and Run the Application

### Prerequisites
- Python 3
- Virtual environment

### Installation

1. Clone the repository.

#### For Virtual Environment
python -m venv venv

#### Activate virtual environment
venv\Scripts\activate

#### Install the dependencies
pip install -r requirements.txt

#### Run the app
python app.py

The application will be available at `http://127.0.0.1:5000`.

# API Endpoints
- GET /fetch-data: Fetch mock data.
- POST /process-data: Process and store data.
- GET /get-processed-data: Retrieve processed data.

# Running Unit Tests
Ensure your virtual environment is activated and dependencies are installed.
Run the tests using the following command:
`python -m unittest test_app.py`

## Test Cases
 - test_process_and_store_data: Tests the /process-data endpoint to ensure data is processed and stored correctly.
 - test_get_processed_data: Tests the /get-processed-data endpoint to ensure the processed data is retrieved correctly.

### Example Usage
#### Fetch data:
`curl http://127.0.0.1:5000/fetch-data`

#### Process and store data:
`
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "products" = @(
        @{
            "id" = 1
            "name" = "Product 1"
            "price" = 100
        },
        @{
            "id" = 2
            "name" = "Product 2"
            "price" = 200
        },
        @{
            "id" = 3
            "name" = "Product 3"
            "price" = 300
        }
    )
}

Invoke-WebRequest -Uri "http://127.0.0.1:5000/process-data" -Method POST -Headers $headers -Body ($body | ConvertTo-Json)
`

#### Retrieve processed data:
`curl http://127.0.0.1:5000/get-processed-data`

