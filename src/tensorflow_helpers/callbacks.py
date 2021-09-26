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
            print(f"\r{epoch}\t".expandtabs(4) + "."*self.dots, f"Loss: {logs['loss']}", end="\n")
        else:
            print(f"\r{epoch}\t".expandtabs(4) + "."*(epoch % self.dots), end="")

