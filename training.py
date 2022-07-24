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
    train_datagen = ImageDataGenerator(rescale=1./255)
    val_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(150, 150),
        batch_size=10,
        class_mode="binary"
    )

    validation_generator = val_datagen.flow_from_directory(
        validate_dir,
        target_size=(150,150),
        batch_size=10,
        class_mode='binary'
    )
            
    history = classifer.fit_generator(
        train_generator,
        steps_per_epoch=100,
        epochs=30,
        validation_data=validation_generator,
        validation_steps=50
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
