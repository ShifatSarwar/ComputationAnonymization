import string
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import Model
from keras.layers import LSTM, Input, TimeDistributed, Dense, Activation, RepeatVector, Embedding
# from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy

# Nodes for Deep Learning Graph G5

def getPairedData(dataLoc):
  # Read file
  translation_file = open(dataLoc,"r", encoding='utf-8') 
  raw_data = translation_file.read()
  translation_file.close()

  # Parse data
  raw_data = raw_data.split('\n')
  pairs = [sentence.split('\t') for sentence in  raw_data]
  pairs = pairs[1000:20000]
  return pairs

def clean_sentence(sentence):
    # Lower case the sentence
    lower_case_sent = sentence.lower()
    # Strip punctuation
    string_punctuation = string.punctuation + "¡" + '¿'
    clean_sentence = lower_case_sent.translate(str.maketrans('', '', string_punctuation))
    return clean_sentence

def tokenize(sentences):
    # Create tokenizer
    text_tokenizer = Tokenizer()
    # Fit texts
    text_tokenizer.fit_on_texts(sentences)
    return text_tokenizer.texts_to_sequences(sentences), text_tokenizer

def makeEqualLength(spa_text_tokenized, eng_text_tokenized):
  
  max_spanish_len = int(len(max(spa_text_tokenized,key=len)))
  max_english_len = int(len(max(eng_text_tokenized,key=len)))
  spa_pad_sentence = pad_sequences(spa_text_tokenized, max_spanish_len, padding = "post")
  eng_pad_sentence = pad_sequences(eng_text_tokenized, max_english_len, padding = "post")

  # Reshape data
  spa_pad_sentence = spa_pad_sentence.reshape(*spa_pad_sentence.shape, 1)
  eng_pad_sentence = eng_pad_sentence.reshape(*eng_pad_sentence.shape, 1)
  return spa_pad_sentence, eng_pad_sentence, max_spanish_len, max_english_len

def getEmbeddingLayer(spanish_vocab, max_spanish_len):
  input_sequence = Input(shape=(max_spanish_len,))
  embedding = Embedding(input_dim=spanish_vocab, output_dim=128,)(input_sequence)

def lstmEncoder(spanish_vocab, max_spanish_len):
  input_sequence = Input(shape=(max_spanish_len,))
  embedding = Embedding(input_dim=spanish_vocab, output_dim=128,)(input_sequence)
  encoder = LSTM(64, return_sequences=False)(embedding)

def lstmDecoder(spanish_vocab, max_spanish_len, max_english_len):
  input_sequence = Input(shape=(max_spanish_len,))
  embedding = Embedding(input_dim=spanish_vocab, output_dim=128,)(input_sequence)
  encoder = LSTM(64, return_sequences=False)(embedding)
  r_vec = RepeatVector(max_english_len)(encoder)

def decoderL2(spanish_vocab, max_spanish_len, max_english_len):
  input_sequence = Input(shape=(max_spanish_len,))
  embedding = Embedding(input_dim=spanish_vocab, output_dim=128,)(input_sequence)
  encoder = LSTM(64, return_sequences=False)(embedding)
  r_vec = RepeatVector(max_english_len)(encoder)
  decoder = LSTM(64, return_sequences=True, dropout=0.2)(r_vec)

def denseLayer(spanish_vocab, max_spanish_len, max_english_len, english_vocab):
  input_sequence = Input(shape=(max_spanish_len,))
  embedding = Embedding(input_dim=spanish_vocab, output_dim=128,)(input_sequence)
  encoder = LSTM(64, return_sequences=False)(embedding)
  r_vec = RepeatVector(max_english_len)(encoder)
  decoder = LSTM(64, return_sequences=True, dropout=0.2)(r_vec)
  logits = TimeDistributed(Dense(english_vocab))(decoder)
  return logits, input_sequence

def getModel(logits, input_sequence):
  enc_dec_model = Model(input_sequence, Activation('softmax')(logits))
  enc_dec_model.compile(loss=sparse_categorical_crossentropy,
              optimizer="adam",
              metrics=['accuracy'])
  return enc_dec_model

def train_model(enc_dec_model, eng_pad_sentence,spa_pad_sentence):
  model = enc_dec_model.fit(spa_pad_sentence, eng_pad_sentence, batch_size=30, epochs=30)
  return model