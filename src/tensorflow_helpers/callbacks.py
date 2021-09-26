import tensorflow as tf


class EpochDots(tf.keras.callbacks.Callback):
    """Makes 'model.fit' print dots at each epoch and print the
    current epoch number in real time

    Eg.\n
    10   .......... \n
    14   ....

    NOTE: Make sure to set verbose == 0
    """

    def __init__(self, dots):
        """
        Args:
            dots: dots per line
        """
        super().__init__()
        self.dots = dots

    def on_epoch_end(self, epoch, logs={}):
        epoch = epoch + 1  # epochs start counting at 0 for computer, this adds 1 for human
        if epoch % self.dots == 0:
            print(f"\r{epoch}\t".expandtabs(4) + "." * self.dots, logs, end="\n")
        else:
            print(f"\r{epoch}\t".expandtabs(4) + "." * (epoch % self.dots), end="")


class EarlyStopping(tf.keras.callbacks.Callback):
    def __init__(self, accuracy, val_accuracy):
        super().__init__()
        self.accuracy = accuracy
        self.val_accuracy = val_accuracy

    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy') is not None and logs.get('accuracy') >= self.accuracy and
                logs.get('val_accuracy') is not None and logs.get('val_accuracy') >= self.val_accuracy):

            if (logs.get('accuracy') and logs.get('val_accuracy')) is not None:
                print(f"\nEnding training with an accuracy of {logs.get('accuracy')} "
                      f"and a val_accuracy of {logs.get('val_accuracy')}")
            elif logs.get('accuracy') is not None:
                print(f"\nEnding training with an accuracy of {logs.get('accuracy')}")
            elif logs.get('val_accuracy') is not None:
                print(f"\nEnding training with a val_accuracy of {logs.get('val_accuracy')}")

            self.model.stop_training = True
