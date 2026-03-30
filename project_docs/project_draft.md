# End-to-End Recommender System

## Project Overview
The **End-to-End Recommender System** is a machine learning application created to provide book suggestions to users using collaborative filtering techniques. This project demonstrates a full MLOps lifecycle, including data collection, validation, preprocessing, model development, and a web-based interface for user interaction.

## Project Structure
The project is designed as a Python package named `books_recommender`, which holds the complete implementation. The code is divided into multiple modules to improve clarity, scalability, and maintainability.

### Key Directories and Files
- **`books_recommender/`**: The core package containing all implementation files.
    - **`components/`**: Responsible for executing different stages of the ML workflow:
        - `stage_00_data_ingestion.py`: Downloads and loads the dataset.
        - `stage_01_data_validation.py`: Performs data checks to ensure correctness.
        - `stage_02_data_transformation.py`: Cleans and reshapes data for modeling.
        - `stage_03_model_trainer.py`: Develops and trains the recommendation model.
    - **`pipeline/`**: Handles the complete execution flow via `training_pipeline.py`.
    - **`config/`**, **`entity/`**, **`constant/`**: Store configuration details and structured definitions.
    - **`logger/`**, **`exception/`**: Manage logging processes and error handling.
- **`app.py`**: A Streamlit-based application that allows users to interact with the system and get recommendations.
- **`main.py`**: Used to run the training pipeline from code.
- **`setup.py`**: Helps in packaging and installing the project.
- **`Dockerfile`**: Specifies the environment setup for container-based deployment.
- **`requirements.txt`**: Includes all required dependencies.

## Architecture & Workflow
The application follows a structured machine learning workflow:

1. **Data Ingestion**: Gathers and imports raw data into the system.
2. **Data Validation**: Ensures the dataset meets expected formats and standards.
3. **Data Transformation**: Processes and organizes data (e.g., pivot tables) for training.
4. **Model Training**: Builds a recommendation model using the Nearest Neighbors approach.
5. **Inference**: The `app.py` uses trained models and processed data to suggest similar books.

## Tech Stack
- **Language**: Python 3.7+
- **Web Framework**: Streamlit
- **Machine Learning**: Scikit-Learn (NearestNeighbors)
- **Data Processing**: Pandas, NumPy
- **Containerization**: Docker
- **MLOps**: Structured pipeline design, logging, and exception management

## Features
- **Book Recommendations**: Enables users to select a book and get related suggestions.
- **Visual Interface**: Shows book titles along with their cover images.
- **Training Pipeline**: Allows retraining of the model through UI or command line.
- **Dockerized**: Suitable for deployment on cloud platforms such as AWS.