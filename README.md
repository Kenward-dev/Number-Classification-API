# Number Classifier API

A REST API that analyzes numbers and returns their mathematical properties along with interesting facts. The API takes a number as a query parameter and returns various properties like whether it's prime, perfect, Armstrong, even/odd, along with the sum of its digits and a fun mathematical fact.

## Features

- Number classification (prime, perfect, Armstrong)
- Basic properties (odd/even)
- Digit sum calculation
- Fun mathematical facts from Numbers API
- Input validation
- CORS support
- JSON responses

## API Documentation

### Endpoint

```
GET /classify-number
```

### Live Demo
The API is deployed and accessible at:
```
https://legislative-pierrette-kenward-dc9303b6.koyeb.app/classify-number?number=<your-number>
```

Example:
```
https://legislative-pierrette-kenward-dc9303b6.koyeb.app/classify-number?number=401
```

### Query Parameters

| Parameter | Type    | Required | Description           |
|-----------|---------|----------|-----------------------|
| number    | integer | Yes      | Number to analyze     |

### Response Format

#### Successful Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}
```

### Properties Combinations

The `properties` field can have the following combinations:
1. `["armstrong", "odd"]` - for Armstrong numbers that are odd
2. `["armstrong", "even"]` - for Armstrong numbers that are even
3. `["odd"]` - for non-Armstrong odd numbers
4. `["even"]` - for non-Armstrong even numbers

## Technical Details

- Framework: Django REST Framework
- External APIs: Numbers API (http://numbersapi.com)
- Response Time: < 500ms
- CORS: Enabled for all origins
- Hosting: Deployed on Koyeb

## Installation

1. Clone the repository
```bash
git clone https://github.com/Kenward-dev/Number-Classification-API.git
cd Number-Classification-API
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
venv\Scripts\activate     # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Start the development server
```bash
python manage.py runserver
```

## Production Deployment

The API is deployed and accessible at:
```
https://legislative-pierrette-kenward-dc9303b6.koyeb.app/
```

For production deployment:
1. Set `DEBUG=False` in settings
2. Configure your production database
3. Set up proper CORS settings
4. Use a production-grade server (e.g., Gunicorn)
5. Set up proper error logging

## Error Handling

- 400 Bad Request: Invalid input (non-integer or missing number)
- 503 Service Unavailable: Numbers API service unavailable
- 500 Internal Server Error: Unexpected server errors

## Development

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

- [Numbers API](http://numbersapi.com) for providing mathematical facts
- Django REST Framework for the API framework