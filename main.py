import numpy

class Perceptron(object):
    """Perceptron classifier.

    Parameters
    -----------
    eta: float
        Learning rate (between 0.0 and 1.0)
    n_iter: int
        Passes over the training dataset.
    random_state: int
        Random number generator seed for random weight Initialization.
    
    Attributes
    -----------
    w_: 1d-array
        Weights after fitting.
    errors_: list
        Number of misclassifications (updates) in each epoch.
    
    
    """

    def __init__(self, eta = 0.01, n_iter = 50, random_state = 1) -> None:
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
    
    def fit(self, x, y):
        """Fit training data.
        
        Parameters
        -----------
        x: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and n_features is the number of features.
        y: array-like, shape = [n_samples]
            Target values.
        
        Returs
        -------
        self: object: {
            self.eta,
            self.n_iter,
            self.random_state,
            self.w_,
            self.errors_
        }
        
        """

        random_generator = numpy.random.RandomState(self.random_state)
        self.w_ = random_generator.normal(loc = 0.0, scale = 0.01, size = 1 + x.shape[1])

        self.errors_ = [] # conjunto de la cantidad de errores en las distintas iteraciones

        for _ in range(self.n_iter):
            errors = 0

            for xi, target in zip(x, y): # zip(x, y) devuelve un array con un dos elementos: xi y target
                # Para cada par de atributos de la muestra obtenemos el valor de actualización del peso:
                update = self.eta * (target - self.predict(xi))
                # Luego procedemos a la actualización del vector de pesos
                # Primero actualizando los pesos relativos a los atributos de la muestra:
                self.w_[1:] += xi * update
                # Segundo actualizando el sesgo:
                self.w_[0] += update
                # se suma un error por cada muestra que arroje un valor de actualización distinto de 0 - o sea, no la pegó el perceptron
                errors += int(update != 0.0)
            
            self.errors_.append(errors)
        
        return self
    
    def predict(self, x):
        # Return class label after unit step
        return numpy.where(self.net_input(x) >= 0.0, 1, -1)
    
    def net_input(self, x):
        # Calculate net input
        return numpy.dot(x, self.w_[1:]) + self.w_[0]
