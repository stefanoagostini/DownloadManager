from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty

# A PyQT5 Observable object class.
class Observable(QObject):
    valueChanged = pyqtSignal(object)

    def __init__(self, val):
        super().__init__()
        self._value = val

    def observe(self, slot):
        self.valueChanged.connect(slot) #permette di connettere gli ascoltatori, e quando verrà emesso il segnale verranno contattati

    # We access the value through this getter/setter property.
    @pyqtProperty(object, notify=valueChanged)
    def value(self):
        return self._value

    # Note that we need to explicitly emit() the signal. Declaring the
    # pyqtProperty with the notify=valueChanged above will have
    # benefits when we, for example, want to use this model in QML.
    @value.setter
    def value(self, newval):
        self._value = newval
        self.valueChanged.emit(self.value)  #emesso dopo che il valore è stato cambato
