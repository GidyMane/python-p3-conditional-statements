#!/usr/bin/env python3

def admin_login(username, password):
    if (username.lower() == "admin" or username.upper() == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
      if temperature < 40:
        return "It's brisk out there!"
      elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
      elif temperature > 85:
        return "It's too dang hot out there!"
      else:
        return "It's perfect out there!"

def fizzbuzz(num):
      if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
      elif num % 3 == 0:
        return "Fizz"
      elif num % 5 == 0:
        return "Buzz"
      else:
        return num

def calculator(operation, num1, num2):
      if operation == "+":
        return num1 + num2
      elif operation == "-":
        return num1 - num2
      elif operation == "*":
        return num1 * num2
      elif operation == "/":
        # Check if num2 is not zero to avoid division by zero
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
      else:
        print("Invalid operation!")
        return None
