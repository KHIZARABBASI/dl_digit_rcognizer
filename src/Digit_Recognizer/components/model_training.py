import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from Digit_Recognizer.entity.config_entity import ModelTrainingConfig
from Digit_Recognizer.components.data_transformation import DataTransformation  # Import your data loader
from Digit_Recognizer import logger

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def build_model(self):
        """Build and return the CNN model."""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(10, activation='softmax')  # 10 classes for digits 0-9
        ])
        return model

    def train_model(self):
        """Load data, train the model, and save it."""
        # Load transformed data
        data_loader = DataTransformation(self.config)
        x_train, y_train, x_test, y_test = data_loader.load_data_aug()

        # Normalize and reshape data
        x_train, x_test = x_train / 255.0, x_test / 255.0
        x_train = x_train.reshape(-1, 28, 28, 1)
        x_test = x_test.reshape(-1, 28, 28, 1)

        # Build the model
        model = self.build_model()
        model.compile(
            optimizer=Adam(learning_rate=self.config.learning_rate),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        logger.info('fitting oppression')
        logger.info('fitting oppression')
        # Train the model
        history = model.fit(
            x_train, y_train,
            epochs=self.config.epochs,
            batch_size=self.config.batch_size,
            validation_data=(x_test, y_test)
        )

        # Save the model
        model.save(self.config.model_file)
        print(f"Model saved at {self.config.model_file}")

        # Evaluate the model
        test_loss, test_accuracy = model.evaluate(x_test, y_test)
        print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

        # Save evaluation results
        with open(self.config.evaluation_file, 'w') as f:
            f.write(f"Test Loss: {test_loss}\n")
            logger.info(f"Test Loss: {test_loss}\n")
            f.write(f"Test Accuracy: {test_accuracy * 100:.2f}%")
            logger.info(f"Test Accuracy: {test_accuracy * 100:.2f}%\n")
        print(f"Evaluation results saved at {self.config.evaluation_file}")
        logger.info(f'Evaluation results saved at {self.config.evaluation_file}')
