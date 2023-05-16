from tensorflow.keras import layers
from tensorflow import keras
import tensorflow as tf

from sklearn.model_selection import train_test_split
from ast import literal_eval

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Nodes for Machine Learning Graph G4

def getData(url):
  arxiv_data = pd.read_csv(url)
  return arxiv_data

def filter_data(arxiv_data):
  arxiv_data = arxiv_data[~arxiv_data["titles"].duplicated()]
  # Filtering the rare terms.
  arxiv_data_filtered = arxiv_data.groupby("terms").filter(lambda x: len(x) > 1)
  return arxiv_data_filtered

def create_list_string(arxiv_data_filtered):
  arxiv_data_filtered["terms"] = arxiv_data_filtered["terms"].apply(
    lambda x: literal_eval(x))
  return arxiv_data_filtered


def split_train_test(arxiv_data_filtered):
  test_split = 0.1
  # Initial train and test split.
  train_df, test_df = train_test_split(arxiv_data_filtered, test_size=test_split, stratify=arxiv_data_filtered["terms"].values)
  # Splitting the test set further into validation
  # and new test sets.
  val_df = test_df.sample(frac=0.5)
  test_df.drop(val_df.index, inplace=True)
  return train_df, test_df, val_df

def get_preprocess_data(train_df):
  terms = tf.ragged.constant(train_df["terms"].values)
  lookup = tf.keras.layers.StringLookup(output_mode="multi_hot")
  lookup.adapt(terms)
  vocab = lookup.get_vocabulary()
  max_seqlen = 150
  batch_size = 128
  padding_token = "<pad>"
  auto = tf.data.AUTOTUNE
  return terms, lookup, vocab, max_seqlen, batch_size, padding_token, auto

def invert_multi_hot(encoded_labels, vocab):
    """Reverse a single multi-hot encoded label to a tuple of vocab terms."""
    hot_indices = np.argwhere(encoded_labels == 1.0)[..., 0]
    return np.take(vocab, hot_indices)

def make_dataset(dataframe, max_seqlen, batch_size, padding_token, auto, lookup, is_train=True):
  labels = tf.ragged.constant(dataframe["terms"].values)
  label_binarized = lookup(labels).numpy()
  dataset = tf.data.Dataset.from_tensor_slices((dataframe["summaries"].values, label_binarized))
  dataset = dataset.shuffle(batch_size * 10) if is_train else dataset
  return dataset.batch(batch_size)

def vectorize(train_df, train_dataset, validation_dataset, test_dataset, auto):
  vocabulary = set()
  train_df["summaries"].str.lower().str.split().apply(vocabulary.update)
  vocabulary_size = len(vocabulary)
  text_vectorizer = layers.TextVectorization(max_tokens=vocabulary_size, ngrams=2, output_mode="tf_idf")
  # `TextVectorization` layer needs to be adapted as per the vocabulary from our
  # training set.
  with tf.device("/CPU:0"):
    text_vectorizer.adapt(train_dataset.map(lambda text, label: text))

  train_dataset = train_dataset.map(
    lambda text, label: (text_vectorizer(text), label), num_parallel_calls=auto
  ).prefetch(auto)
  validation_dataset = validation_dataset.map(
    lambda text, label: (text_vectorizer(text), label), num_parallel_calls=auto
  ).prefetch(auto)
  test_dataset = test_dataset.map(
    lambda text, label: (text_vectorizer(text), label), num_parallel_calls=auto
  ).prefetch(auto)
  return train_dataset, validation_dataset, test_dataset

def make_model(lookup):
  shallow_mlp_model = keras.Sequential([
      layers.Dense(512, activation="relu"),
      layers.Dense(256, activation="relu"),
      layers.Dense(lookup.vocabulary_size(), activation="sigmoid"),
      ]  # More on why "sigmoid" has been used here in a moment.
    )
  return shallow_mlp_model

def train_model(shallow_mlp_model, train_dataset, validation_dataset):
  epochs = 5
  shallow_mlp_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["categorical_accuracy"])
  shallow_mlp_model.fit(train_dataset, validation_data=validation_dataset, epochs=epochs)
  return shallow_mlp_model

