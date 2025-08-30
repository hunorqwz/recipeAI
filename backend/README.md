
# Recipe Generator API

The Recipe Generator API is a simple web application that allows users to generate random recipes based on the ingridients they provide.

## Getting Started

To start using the Recipe Generator API, you will need to have Python installed on your machine. You can download and install Python from [python.org](https://www.python.org/downloads/).

Once you have Python installed, you can create a new virtual environment for the project by running the following command in your terminal:
```
python -m venv venv
```

Activate the virtual environment by running one of the following commands, depending on your operating system:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

With the virtual environment activated, you can install the required dependencies for the project by running the following command:
```
pip install -r requirements.txt
```

Finally, you can start the Recipe Generator API by running the following command in your terminal:
```
uvicorn main:app --reload
```

This will start the API on `http://localhost:8000`, and you should be able to access it in your web browser.

You can find the API's documentation on 

```
http://localhost:8000/docs
```
