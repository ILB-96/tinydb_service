# TinyDB Database Service

This repository contains a Python-based service built on TinyDB, a lightweight document-oriented database. This service provides a simple and flexible interface for performing basic CRUD (Create, Read, Update, Delete) operations on a TinyDB database. The service also includes utilities for generating queries based on specific keys.

## Features

- **Flexible Query Generation**: Generate queries based on a customizable list of keys, allowing for targeted searches.
- **CRUD Operations**: Easily perform CRUD operations (`create_one`, `find_by_id`, `get_all`) on items in the database.
- **Table Management**: Quickly manage database tables, including the ability to truncate (empty) tables.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/tinydb-database-service.git
    cd tinydb-database-service
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    pip install poetry
    poetry shell
    ```

3. **Install Dependencies**:
    ```bash
    poetry install
    ```

## Usage

### Initialization

First, initialize the `TinyDatabase` class with your database name, table name, and a list of keys to use for query generation:

```python
from tinydb_service import TinyDatabase
```

# Example: Using a TinyDB database with a specific table and query keys
`db = TinyDatabase("my_database.json", "my_table", ["key1", "key2"])`

## Performing Operations
#### Insert or Update an Item:

```python
item = {"key1": "value1", "key2": "value2", "data": "example"}
db.create_one(item)
```
#### Find an Item by Keys:

```python
search_keys = {"key1": "value1", "key2": "value2"}
result = db.find_by_id(search_keys)
print(result)
```
#### Retrieve All Items:

```python
all_items = db.get_all()
print(all_items)
```
#### Drop (Truncate) the Table:

```python
db.drop_table()
```
Example Workflow
```python
def main():
    # Initialize the database
    db = TinyDatabase("my_database.json", "my_table", ["id"])

    # Add a new item
    item = {"id": 1, "name": "John Doe", "age": 30}
    db.create_one(item)

    # Retrieve the item
    retrieved_item = db.find_by_id({"id": 1})
    print(f"Retrieved Item: {retrieved_item}")

    # Get all items
    all_items = db.get_all()
    print(f"All Items: {all_items}")

    # Drop the table (delete all data)
    db.drop_table()

if __name__ == "__main__":
    main()
```
### Dependencies
`TinyDB`: A lightweight document-oriented database.
`Python`: Ensure Python 3.12 or higher is installed.
Install the required dependencies using:

```bash
pip install tinydb
```
# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements, bug fixes, or feature requests.