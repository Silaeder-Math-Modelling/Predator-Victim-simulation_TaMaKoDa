class Animal:
    animal_additional_init = lambda self: None

    def __init__(self, x, y, velocity, additional_initializer=None, additional_initializer_args=None, \
            additional_initializer_kwargs=None):
        """Initializes an `Animal` object
        Parameters:
            x and y (int):
                Coordinates of animal
            velocity (int):
                The animal velocity
            additional_initializer (func, optional):
                An additional initializer of a certain strategy.
                Default: automatically imported function, defined by a strategy
                Pass `lambda self: None` (not just `None`) to skip
                additional initialization
            additional_initializer_args (list, optional):
                A list of arguments to be passed to the
                additional initializer
            additional_initializer_kwargs (dict, optional):
                A dict of keyword arguments to be passed to the
                additional initializer
        """
        
        # If initialization is not defined
        if additional_initializer is None:
            additional_initializer = self.animal_additional_init
        
        # If additional arguments are not defined
        if additional_initializer_args is None:
            additional_initializer_args = []

        # If additional keyword arguments are not defined
        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}

        self.x = x
        self.y = y
        self.velocity = velocity
        
        # Special of strategy
        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
       
    
class Predator(Animal):
    predator_additional_init = lambda self: None

    def __init__(self, victim_eating_time, \
            parent_initializer_args=None, parent_initializer_kwargs=None,
            additional_initializer=None, additional_initializer_args=None,
            additional_initializer_kwargs=None):
        """Initializes a `Predator` object
        Parameters:
            victim_eating_time (int): Time (in simulation steps)
                which it takes to eat a victim by the predator
            parent_initializer_args (list, optional):
                A list of argumetns to be passed to the
                `Animal` initializer
            parent_initializer_kwargs (dict, optional):
                A dict of keyword arguments to be passed to the
                `Animal` initializer
            additional_initializer (func, optional):
                An additional initializer of a certain strategy.
                Default: strategy-defined function
                Pass an empty `lambda` (not `None`) to skip
                additional initialization
            additional_initializer_args (list, optional):
                A list of arguments to be passed to the
                additional initializer
            additional_initializer_kwargs (dict, optional):
                A dict of keyword arguments to be passed to the
                additional_initializer     
        """
        
        # If additional parent arguments are not defined
        if parent_initializer_args is None:
            parent_initializer_args = []
            
        # If additional parent keyword arguments are not defined
        if parent_initializer_kwargs is None:
            parent_initializer_kwargs = {}
            
        # Initialization like an animal
        Animal.__init__(self, *parent_initializer_args,
            **parent_initializer_kwargs)

        self.victim_eating_time = victim_eating_time
        self.ready_to_run_in = 0

        # If initialization is not defined
        if additional_initializer is None:
            additional_initializer = self.predator_additional_init
        
        # If additional arguments are not defined
        if additional_initializer_args is None:
            additional_initializer_args = []

        # If additional keyword arguments are not defined
        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}
        
        # Special of strategy
        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
        

class Victim(Animal):
    victim_additional_init = lambda self: None

    def __init__(self, parent_initializer_args=None, parent_initializer_kwargs=None,
            additional_initializer=None, additional_initializer_args=None,
            additional_initializer_kwargs=None):
        """Initializes a `Victim` object
        Parameters:
            parent_initializer_args (list, optional):
                A list of argumetns to be passed to the
                `Animal` initializer
            parent_initializer_kwargs (dict, optional):
                A dict of keyword arguments to be passed to the
                `Animal` initializer
            additional_initializer (func, optional):
                An additional initializer of a certain strategy.
                Default: strategy-defined function
                Pass an empty `lambda` (not `None`) to skip
                additional initialization
            additional_initializer_args (list, optional):
                A list of arguments to be passed to the
                additional initializer
            additional_initializer_kwargs (dict, optional):
                A dict of keyword arguments to be passed to the
                additional_initializer  
        """
        
        # If additional parent arguments are not defined
        if parent_initializer_args is None:
            parent_initializer_args = []
            
        # If additional parent keyword arguments are not defined
        if parent_initializer_kwargs is None:
            parent_initializer_kwargs = {}
            
        # Initialization like an animal
        Animal.__init__(self, *parent_initializer_args,
            **parent_initializer_kwargs)
        
        # If initialization is not defined
        if additional_initializer is None:
            additional_initializer = self.victim_additional_init
        
        # If additional arguments are not defined 
        if additional_initializer_args is None:
            additional_initializer_args = []

        # If additional keyword arguments are not defined
        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}
  
        # Special of strategy
        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
        
