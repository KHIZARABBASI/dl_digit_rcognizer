import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from Digit_Recognizer.entity.config_entity import DataTransformationConfig
from Digit_Recognizer import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.datagen = ImageDataGenerator(
            rotation_range=10,
            width_shift_range=0.1,
            height_shift_range=0.1,
            zoom_range=0.1
        )

    def load_data(self):
        x_train = np.load("artifacts/data_ingestion/x_train.npy")
        y_train = np.load("artifacts/data_ingestion/y_train.npy")
        x_test = np.load("artifacts/data_ingestion/x_test.npy")
        y_test = np.load("artifacts/data_ingestion/y_test.npy")

        # Reshape data to add channel dimension
        x_train = x_train.reshape(-1, 28, 28, 1)
        x_test = x_test.reshape(-1, 28, 28, 1)
        return (x_train, y_train), (x_test, y_test)

    # def augment_and_save_data(self):
    #     (x_train, y_train), (x_test, y_test) = self.load_data()

    #     # Fit the generator on training data
    #     self.datagen.fit(x_train)

    #     # Use the generator to save augmented data
    #     for i, (img, label) in enumerate(zip(x_train, y_train)):
    #         img = img.reshape((1, 28, 28, 1))  # Reshape each image for augmentation
    #         # for batch in self.datagen.flow(img, batch_size=1, save_to_dir=self.config.transformed_train_dir, save_prefix='aug', save_format='npy'):
    #         #     break  # Only generate one augmented image per input image
            
    #         for batch in self.datagen.flow(img, batch_size=1):
    #             augmented_image = batch[0]  # Extract the augmented image from the batch
    #             np.save(os.path.join(self.config.transformed_train_dir, 'augmented_image.npy'), augmented_image)


    #     np.save(os.path.join(self.config.transformed_test_dir, 'x_test.npy'), x_test)
    #     np.save(os.path.join(self.config.transformed_test_dir, 'y_test.npy'), y_test)

    def augment_and_save_data(self):
        (x_train, y_train), (x_test, y_test) = self.load_data()

        # Fit the generator on training data
        self.datagen.fit(x_train)

        # Set a larger batch size for faster processing
        batch_size = 32  # Adjust this based on your system's memory capacity
        num_augments_per_image = 5  # Define how many augmentations you want per image

        # Augment and save training data
        for i in range(0, len(x_train), batch_size):
            batch_images = x_train[i:i + batch_size]
            batch_labels = y_train[i:i + batch_size]

            # Generate multiple augmented images per batch
            for j, batch in enumerate(self.datagen.flow(batch_images, batch_size=batch_size)):
                for k, augmented_image in enumerate(batch):
                    if k >= num_augments_per_image:
                        break  # Limit the number of augmented images per input image

                    filename = f"augmented_train_{i+k}_{j}.npy"
                    np.save(os.path.join(self.config.transformed_train_dir, filename), augmented_image)
                    logger.info(f"Saved augmented image: {filename}")
                if j >= num_augments_per_image - 1:
                    break  # Move to the next batch after desired augmentations are created

        # Save test data without augmentation
        np.save(os.path.join(self.config.transformed_test_dir, 'x_test.npy'), x_test)
        np.save(os.path.join(self.config.transformed_test_dir, 'y_test.npy'), y_test)
        logger.info("Saved test data without augmentation.")
