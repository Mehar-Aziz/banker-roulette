# Banker Roulette

## Overview

The **Banker Roulette** is a simple Python script that randomly selects a person from a list of names to buy today's meal. The names are provided by the user as a comma-separated string, and the script uses Python's `random` module to select one name randomly.

## Features

- Takes a comma-separated list of names as input.
- Randomly selects one name from the list(without using .choice() ).
- Prints the name of the person who will buy today's meal.

## Installation

To install and run the Meal Buyer Selector program, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Mehar-Aziz/meal-buyer-selector.git
    ```
2. Navigate to the project directory:
    ```sh
    cd meal-buyer-selector
    ```
3. (Optional) Create and activate a virtual environment:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
4. Install the required dependencies (if any):
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the Meal Buyer Selector program, use the following command:
```sh
python main.py
