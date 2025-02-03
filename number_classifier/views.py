from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import math

class NumberClassifierView(APIView):
    def __init__(self):
        self.session = requests.Session()
        
        # Enable retries for session
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        
    def validate_number(self, request):
        # Get raw number from query params
        raw_number = request.query_params.get('number')
        
        # Check if number parameter exists
        if not raw_number:
            return None, Response(
                {"error": "Number parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        # Convert string to integer
        try:
            number = int(raw_number)
            return number, None
        except ValueError:
            return None, Response(
                {
                    "number": "alphabet" if raw_number.isalpha() else raw_number,
                    "error": True
                },
                status=status.HTTP_400_BAD_REQUEST
            )

    def is_prime(self, n: int) -> bool:
        # Handle edge cases
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Check odd numbers up to square root
        sqrt_n = math.sqrt(n)
        for i in range(3, int(sqrt_n) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_perfect(self, n: int) -> bool:
        """Check if a number is perfect (sum of proper divisors equals the number)."""
        if n < 2:
            return False
        
        # Start with 1 as it's always a proper divisor
        divisor_sum = 1
        sqrt_n = math.sqrt(n)
        
        # Check divisors up to square root
        for i in range(2, int(sqrt_n) + 1):
            if n % i == 0:
                divisor_sum += i
                # Add the pair divisor if it's different
                pair_divisor = n // i
                if pair_divisor != i:
                    divisor_sum += pair_divisor
                    
        return divisor_sum == n

    def is_armstrong(self, n: int) -> bool:
        """Check if a number is an Armstrong number."""
        num_str = str(n)
        power = len(num_str)
        
        digit_sum = 0
        for digit in num_str:
            digit_sum += int(digit) ** power
            # Early exit if sum exceeds original number
            if digit_sum > n:
                return False
                
        return digit_sum == n

    def calculate_digit_sum(self, n: int) -> int:
        """Calculate the sum of digits in a number."""
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digit_sum

    def get_fun_fact(self, number: int) -> str:
        """Fetch fun fact from Numbers API."""
        try:
            response = self.session.get(
                f"http://numbersapi.com/{number}/math",
                timeout=3  
            )
            if response.status_code == 200:
                return response.text
            return None
        except requests.RequestException:
            return None

    def get(self, request):
        """Handle GET requests for number classification."""
        # Validate the number
        number, error_response = self.validate_number(request)
        if error_response:
            return error_response
            
        # Get fun fact
        fun_fact = self.get_fun_fact(number)
        if fun_fact is None:
            return Response(
                {"error": "Unable to fetch fun fact from Numbers API"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        # Determine number properties
        properties = ["even" if number % 2 == 0 else "odd"]
        if self.is_armstrong(number):
            properties.append("armstrong")
        
        # Prepare and return response
        response_data = {
            "number": number,
            "is_prime": self.is_prime(number),
            "is_perfect": self.is_perfect(number),
            "properties": properties,
            "digit_sum": self.calculate_digit_sum(number),
            "fun_fact": fun_fact
        }
        
        return Response(response_data)