from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Embedding, LSTM, Dense, Input, Add, Concatenate
from tensorflow.keras.models import Model

# Parameters
max_caption_length = 32
vocab_size = 10000

# 1. Feature extractor (CNN)
image_input = Input(shape=(224, 224, 3))
base_model = ResNet50(include_top=False, weights='imagenet', pooling='avg')
for layer in base_model.layers:
    layer.trainable = False  # optional: freeze base layers for faster training

image_features = base_model(image_input)
image_features = Dense(256, activation='relu')(image_features)  # reduce dimension

# 2. Caption generator (LSTM)
caption_input = Input(shape=(max_caption_length,))
caption_embedding = Embedding(input_dim=vocab_size, output_dim=256, mask_zero=True)(caption_input)
lstm_output = LSTM(256)(caption_embedding)

# 3. Combine both modalities
combined = Add()([image_features, lstm_output])  # same shape (256)
# Alternatively: combined = Concatenate()([image_features, lstm_output])

# 4. Final prediction
final_output = Dense(vocab_size, activation='softmax')(combined)

# 5. Define the model
model = Model(inputs=[image_input, caption_input], outputs=final_output)
model.compile(loss='categorical_crossentropy', optimizer='adam')

model.summary()
