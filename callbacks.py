import tensorflow as tf

class Callback(tf.keras.callbacks.Callback):
    # def on_train_begin(self, epoch, logs=None):
    #     print("train_begin")
    def on_epoch_end(self, epoch, logs=None):
        epoch = epoch + 1  # epochs start counting at 0 for computer, this adds 1 for human
        dots = 50
        if epoch % dots == 0:
            print(f"\r{epoch}\t".expandtabs(4) + "."*dots, end="\n")
        else:
            print(f"\r{epoch}\t".expandtabs(4) + "."*(epoch % dots), end="")

# Make sure to set verbose == 0