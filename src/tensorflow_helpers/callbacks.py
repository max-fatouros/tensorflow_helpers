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
    """Stops training at the threshold values you provide"""
    def __init__(self, accuracy=None, val_accuracy=None, loss=None, mae=None):
        super().__init__()
        self.stop_at = {}

        if accuracy is not None:
            self.stop_at['accuracy'] = accuracy

        if val_accuracy is not None:
            self.stop_at['val_accuracy'] = val_accuracy

        if loss is not None:
            self.stop_at['loss'] = loss

        if mae is not None:
            self.stop_at['mae'] = mae

    def on_epoch_end(self, epoch, logs={}):
        metrics = logs.keys() & self.stop_at.keys()
        stop_training = True
        for metric in metrics:
            if metric in ['mae', 'mse', 'loss']:
                if logs.get(metric) >= self.stop_at.get(metric):
                    stop_training = False
            else:
                if logs.get(metric) <= self.stop_at.get(metric):
                    stop_training = False

        if stop_training:
            print("\nStopping training at", logs)
        self.model.stop_training = stop_training
