# Data Sweeper App

## 🚀 Overview
Data Sweeper is a powerful Streamlit web application designed to help users clean, transform, and visualize their CSV and Excel files effortlessly. It allows for easy duplicate removal, filling missing values, column selection, and file conversion.

## 📌 Features
- 📂 Upload and preview CSV and Excel files
- 🧹 Remove duplicate rows
- 📊 Fill missing values with column averages
- 🎯 Select specific columns for analysis
- 📈 Visualize numerical data with bar charts
- 🔄 Convert and download files in CSV or Excel format

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.12** installed on your system.

### Using Poetry
Poetry is used for dependency management. Follow these steps:

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/muzaffar401/Data_Sweeper_App.git
   cd data_sweeper_app
   ```

2. **Install Poetry (if not installed):**
   ```sh
   pip install poetry
   ```

3. **Set up the Virtual Environment:**
   ```sh
   poetry install
   ```

4. **Activate the Virtual Environment:**
   ```sh
   poetry shell
   ```

## 🚀 Running the App
To start the Streamlit app, run:
```sh
streamlit run src/data_sweeper_app/app.py
```

## 📂 Project Structure
```
DATA_SWEEPER_APP/
│── .venv/                     # Virtual environment
│── src/
│   ├── data_sweeper_app/
│   │   ├── __init__.py
│   │   ├── app.py              # Main Streamlit application
│── tests/                      # Unit tests
│── poetry.lock                 # Poetry lock file
│── pyproject.toml              # Poetry project configuration
│── README.md                   # Project documentation
│── requirements.txt             # Dependencies
```

## 🔧 Commands Used
Here are the key commands used during development:

- **Lock Dependencies:**
  ```sh
  poetry lock
  ```
- **Export Dependencies:**
  ```sh
  poetry export -f requirements.txt --output requirements.txt --without-hashes
  ```
- **Run the App:**
  ```sh
  streamlit run src/data_sweeper_app/app.py
  ```

## ✨ Contributing
Feel free to contribute by opening issues or submitting pull requests!

## 📜 License
This project is licensed under the MIT License.

