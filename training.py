from src.create_model import create_model
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import matplotlib.pyplot as plt 
import os

if __name__ == "__main__":

    base_dir = "./dataset/"


    train_dir = os.path.join(base_dir, "train")
    test_dir = os.path.join(base_dir, "test")
    validate_dir = os.path.join(base_dir, "validate")

    #initializing the classifer
    classifer = create_model((150,150,3))

    #configuring the classifier for training
    classifer.compile(loss="binary_crossentropy", 
                      optimizer=tf.keras.optimizers.RMSprop(lr=1e-4),
                      metrics=['acc'])

    #data preprocessing for the model
    train_datagen = ImageDataGenerator(rescale=1./255,
                                        rotation_range=40,
                                        width_shift_range=0.2,
                                        height_shift_range=0.2,
                                        shear_range=0.2,
                                        zoom_range=0.2,
                                        horizontal_flip=True)
    val_datagen = ImageDataGenerator(rescale=1./255)

    batch_size = 32

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode="binary"
    )

    validation_generator = val_datagen.flow_from_directory(
        validate_dir,
        target_size=(150,150),
        batch_size=batch_size,
        class_mode='binary'
    )
            
    history = classifer.fit(
        train_generator,
        epochs=100,
        validation_data=validation_generator,
        steps_per_epoch=int(700/batch_size),
        validation_steps=int(350/batch_size)
    )

    classifer.save("skinCancerDiagnoser.h5")

    #plotting the loss and accuracy curves of the classifier
    #  during training
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()
