# IMDB Sentiment Analysis

This project uses an RNN-based model to classify movie reviews from the IMDB dataset as Positive or Negative.

## Directory Structure

- `app.py` - Streamlit web app for sentiment prediction.
- `model.ipynb` - Jupyter notebook for model training and saving.
- `testing.ipynb` - Jupyter notebook for testing the trained model.
- `IMDB Dataset.csv` - Dataset containing movie reviews and sentiments.
- `model.keras` - Saved Keras model.
- `tokenizer.pkl` - Saved tokenizer for text preprocessing.
- `requirements.txt` - Python dependencies.
- `.gitignore` - Git ignore file.

## Usage

### 1. Train the Model

Train and save the model using [`model.ipynb`](model.ipynb).

### 2. Test the Model

Test predictions using [`testing.ipynb`](testing.ipynb).

### 3. Run the Web App

Run the Streamlit app for interactive predictions:

```sh
streamlit run app.py
```

## Requirements

Install dependencies with:

```sh
pip install -r requirements.txt
```

## Files

- [`app.py`](app.py): Streamlit app for sentiment prediction.
- [`model.ipynb`](model.ipynb): Model training notebook.
- [`testing.ipynb`](testing.ipynb): Model testing notebook.

## License

This project is