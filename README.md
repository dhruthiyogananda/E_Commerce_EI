# E_Commerce_EI
I have created a simple e-commerce cart system where users can add products to their cart, update quantities, and view the total bill.
It demonstrates the use of object-oriented programming principles and design patterns such as the Strategy Pattern and the Prototype Pattern.

## Table of Contents
A) Project Structure
B) Getting Started
C) Usage
D) Testing


## Project Structure
This project is organized into the following files and directories:
- `main.py`: Entry point of the application.
- `products.py`: Contains product classes and their attributes.
- `discount_strategies.py`: Defines discount strategy classes.
- `cart.py`: Implements the Cart class for managing the shopping cart.
- `tests/`: Contains test cases for the Cart class and discount strategies.
- `venv/`: (Optional) Virtual environment directory for isolating dependencies.
- `requirements.txt`: (Optional) List of project dependencies.

## Getting started
1. Clone the repository to your local machine:
   git clone https://github.com/dhruthiyogananda/E_Commerce_EI.git

2. Navigate to the project directory:
cd e-commerce_EI

3.Create and activate a virtual environment:(i have created)
python -m venv venv
 venv\Scripts\activate
 
4.Install dependencies:
pip install -r requirements.txt

## Usage
You can use this e-commerce_EI by running the main.py file. Here's how to interact with the application:
python main.py

Follow the on-screen instructions to add products to your cart, update quantities, and view the total bill.

## Testing
To run the test cases, you can use the unittest framework. Run the following command:
python -m unittest discover tests


