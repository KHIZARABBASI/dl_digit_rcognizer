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
    
    # def load_data_aug(self):
    #     # Load training data
    #     train_files = [file for file in os.listdir(self.config.transformed_train_dir) if file.endswith('.npy')]
    #     x_train = np.array([np.load(os.path.join(self.config.transformed_train_dir, file)) for file in train_files])

    #     # Load test data
    #     x_test = np.load(os.path.join(self.config.transformed_test_dir, 'x_test.npy'))
    #     y_test = np.load(os.path.join(self.config.transformed_test_dir, 'y_test.npy'))

    #     return x_train, x_test, y_test

    def load_data_aug(self):
        # Load augmented training data
        x_train = np.load(os.path.join(self.config.transformed_train_dir, 'augmented_train_images.npy'))
        y_train = np.load(os.path.join(self.config.transformed_train_dir, 'augmented_train_labels.npy'))

        # Load test data
        x_test = np.load(os.path.join(self.config.transformed_test_dir, 'x_test.npy'))
        y_test = np.load(os.path.join(self.config.transformed_test_dir, 'y_test.npy'))

        return x_train, y_train, x_test, y_test

    
    def augment_and_save_data(self):
        (x_train, y_train), (x_test, y_test) = self.load_data()

        # Fit the generator on training data
        self.datagen.fit(x_train)

        # Define augmentation parameters
        batch_size = 64  # Adjust based on memory capacity
        num_augments_per_image = 1  # Number of augmentations per image

        augmented_train_images = []
        augmented_train_labels = []

        # Augment the training data
        for i, (images, labels) in enumerate(self.datagen.flow(x_train, y_train, batch_size=batch_size)):
            augmented_train_images.extend(images)
            augmented_train_labels.extend(labels)

            # Stop when the desired number of augmented images is reached
            if len(augmented_train_images) >= num_augments_per_image * len(x_train):
                break

        # Convert to numpy arrays
        augmented_train_images = np.array(augmented_train_images[:num_augments_per_image * len(x_train)])
        augmented_train_labels = np.array(augmented_train_labels[:num_augments_per_image * len(x_train)])

        # Save augmented data as single batch files
        np.save(os.path.join(self.config.transformed_train_dir, 'augmented_train_images.npy'), augmented_train_images)
        np.save(os.path.join(self.config.transformed_train_dir, 'augmented_train_labels.npy'), augmented_train_labels)

        # Save test data without augmentation
        np.save(os.path.join(self.config.transformed_test_dir, 'x_test.npy'), x_test)
        np.save(os.path.join(self.config.transformed_test_dir, 'y_test.npy'), y_test)

        logger.info("Saved augmented training data and test data.")


   


    # def augment_and_save_data(self):
    #     (x_train, y_train), (x_test, y_test) = self.load_data()

    #     # Fit the generator on training data
    #     self.datagen.fit(x_train)

    #     # Set a larger batch size for faster processing
    #     batch_size = 32  # Adjust this based on your system's memory capacity
    #     num_augments_per_image = 5  # Define how many augmentations you want per image

    #     augmented_train_images = []
    #     augmented_train_labels = []

    #     # Augment and save training data
    #     for i in range(0, len(x_train), batch_size):
    #         batch_images = x_train[i:i + batch_size]
    #         batch_labels = y_train[i:i + batch_size]

    #         # Generate multiple augmented images per batch
    #         for j, batch in enumerate(self.datagen.flow(batch_images, batch_size=batch_size)):
    #             for k, augmented_image in enumerate(batch):
    #                 if k >= num_augments_per_image:
    #                     break  # Limit the number of augmented images per input image

    #                 augmented_train_images.append(augmented_image)
    #                 augmented_train_labels.append(batch_labels[k])

    #                 filename = f"augmented_train_{i+k}_{j}.npy"
    #                 np.save(os.path.join(self.config.transformed_train_dir, filename), augmented_image)
    #                 logger.info(f"Saved augmented image: {filename}")

    #             if j >= num_augments_per_image - 1:
    #                 break  # Move to the next batch after desired augmentations are created

    #         # Save augmented training data in a batch
    #         np.save(os.path.join(self.config.transformed_train_dir, 'augmented_train_images.npy'), np.array(augmented_train_images))
    #         np.save(os.path.join(self.config.transformed_train_dir, 'augmented_train_labels.npy'), np.array(augmented_train_labels))
    #         logger.info("Saved augmented training data in batch.")

    #         # Save test data without augmentation
    #         np.save(os.path.join(self.config.transformed_test_dir, 'x_test.npy'), x_test)
    #         np.save(os.path.join(self.config.transformed_test_dir, 'y_test.npy'), y_test)
    #         logger.info("Saved test data without augmentation.")