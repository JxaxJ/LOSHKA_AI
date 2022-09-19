try:
    import nltk
    import numpy
    import sys
    from nltk.tokenize import RegexpTokenizer
    import tensorflow
    from nltk.corpus import stopwords
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, LSTM
    from keras.utils import np_utils
    from keras.callbacks import ModelCheckpoint
    import pandas as pd
except ModuleNotFoundError:
    from MODULE import install_module
    install_module.install_module()


data = open("DATA/data_on_text_generate.mgt", encoding='utf-8').read()
file = data.lower()


def train(epoch, batch_size=0):
    model.fit(X, y, epochs=epoch, batch_size=batch_size, callbacks=desired_callbacks)


def tokenize_words(input):
    try:
        input = input.lower()

        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(input)

        filtered = filter(lambda token: token not in stopwords.words('russian'), tokens)
        return " ".join(filtered)
    except LookupError:
        nltk.download('stopwords')
        input = input.lower()

        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(input)

        filtered = filter(lambda token: token not in stopwords.words('russian'), tokens)
        return " ".join(filtered)


def save_lengths(length):
    dataframe = pd.DataFrame([length], columns=['lenght'])
    dataframe.to_csv('../DATA/data.csv', index=False)


def set_lengths():
    try:
        lenght = pd.read_csv('DATA/data.csv')
        return lenght['lenght'][0]

    except FileNotFoundError:
        save_lengths(100)
        return 100


processed_inputs = tokenize_words(file)
chars = sorted(list(set(processed_inputs)))
char_to_num = dict((c, i) for i, c in enumerate(chars))
input_len = len(processed_inputs)
vocab_len = len(chars)
# print ("Total number of characters:", input_len)
# print ("Total vocab:", vocab_len)

seq_length = int(set_lengths())


def generate_poems():

    x_data = []
    y_data = []

    for i in range(0, input_len - seq_length, 1):
        in_seq = processed_inputs[i:i + seq_length]

        out_seq = processed_inputs[i + seq_length]

        x_data.append([char_to_num[char] for char in in_seq])
        y_data.append(char_to_num[out_seq])

    n_patterns = len(x_data)
    # print ("Total Patterns:", n_patterns)

    X = numpy.reshape(x_data, (n_patterns, seq_length, 1))
    X = X / float(vocab_len)

    y = np_utils.to_categorical(y_data)

    #Создние нейронной сети и добавление нейронов
    model = Sequential()
    model.add(LSTM(512, input_shape=(X.shape[1], X.shape[2]), return_sequences=True)) #Значение 512 можно уменьшить для сокращения использования видеопамяти
    model.add(Dropout(0.2))
    model.add(LSTM(256, return_sequences=True)) #Значение 256 можно уменьшить для сокращения использования видеопамяти
    model.add(LSTM(256)) #Значение 256 можно уменьшить для сокращения использования видеопамяти
    model.add(Dense(y.shape[1], activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    filepath = "DATA/model_weights_saved_more_dense.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    desired_callbacks = [checkpoint]

    filename = "DATA/model_weights_saved_more_dense.hdf5"
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    num_to_char = dict((i, c) for i, c in enumerate(chars))
    start = numpy.random.randint(0, len(x_data) - 1)
    pattern = x_data[start]

    return ''.join([num_to_char[value] for value in pattern])