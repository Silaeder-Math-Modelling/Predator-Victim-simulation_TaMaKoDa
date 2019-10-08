class Animal:
    # Объявим по дефолту пустую доп. инициализацию:
    animal_additional_init = lambda self: None

    def __init__(self, additional_initializer=None, additional_initializer_args=None,
            additional_initializer_kwargs=None):
        """Initializes an `Animal` object
        Parameters:
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
                additional initializer
        """
        # Стиль docstring-ов к функциям давайте сохранять такой же, как
        # в NiMaTa LentaBot (покажите Даше, прошарьте ее слегка)

        # Среди аргументов выше, как вы могли прочитать в докстринге,
        # additional_initializer - это функция, которую мы принимаем, чтобы
        # провести инициализацию под стратегию. У меня хреново получается
        # писать докстринги, поэтому я поясню: если чувак при инициализации
        # вообще ничего не передает на это место, то мы заюзаем функцию
        # animal_additional_init, которая объявлена в самом начале класса,
        # еще перед __init__ (если импортируется какая-то стратегия, то эта
        # функция будет подменяться другой). Если же чувак хочет, чтобы
        # дополнительная инициализация не произошла вовсе, либо
        # еще там в одной сложной ситуации он должен явно передать свою
        # функцию как аргумент в __init__

        # Если доп. инициализация не указана явно, то используем strategy-defined:
        if additional_initializer is None:
            additional_initializer = self.animal_additional_init
        # self.animal_additional_init - это то, что мы объявили над __init__
        # но если мы импортировали какую-то стратегию, то она
        # заменит эту функцию другой

        # Если доп. аргументы не указаны, то оставим их пустыми:
        if additional_initializer_args is None:
            additional_initializer_args = []

        # Если доп. keyaord arguments не указаны, то оставим их пустыми:
        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}

        # Возможно, в этом месте у вас уже возник вопрос:
        # почему в заголовке функции __init__ мы написали
        # additional_..._args=None, additional_..._kwargs=None,
        # а в теле функции мы заменили их в том случае, если они
        # остались None? Не проще ли было бы сразу написать
        # additional_..._args=[], additional_..._kwargs={}?
        # Ответ: нет, не проще, это некоторые
        # необычные (я бы сказал advanced) тонкости питона, если кому
        # интересны подробности, пишите в ЛС, я расскажу

        pass # ЗДЕСЬ ПРОВОДИМ ИНИЦИАЛИЗАЦИЮ ЖИВОТНОГО
        # ВОТ ЗДЕСЬ
        # НЕ ТАМ
        # И НЕ ТУТ
        # А ВОТ ЗДЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕСЬ
        # Обратите внимание: в этом месте должна происходить инициализация,
        # которая: 1) происходит для всех животных (и жертв, и хищников)
        # 2) не зависит от стратегии, т. е. общее для всех

        # Теперь инициализируем то, что специфично для стратегии:
        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
        # Обратите внимание: self как первый аргумент передастся автоматически
        # Если вы не знаете, что значат * и ** в конструкции выше, это
        # немалое упущение в вашем знании синтаксиса питона и если
        # вы прошаритесь, это, скорее всего, немало поможет вам в жизни,
        # так что погуглите про передачу args и kwargs в функцию
        # как list и dict соответственно

class Predator(Animal):
    # Объявим по дефолту пустую доп. инициализацию:
    predator_additional_init = lambda self: None

    def __init__(self, parent_initializer_args=None, paranet_initializer_kwargs=None,
            additional_initializer=None, additional_initializer_args=None,
            additional_initializer_kwargs=None):
        """Initializes a `Predator` object
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
        if parent_initializer_args is None:
            parent_initializer_args = []
        if parent_initializer_kwargs is None:
            parent_initializer_kwargs = {}
        # Сначала делаем инициализацию нас как животного:
        Animal.__init__(self, *parent_initializer_args,
            **parent_initializer_kwargs)

        if additional_initializer is None:
            additional_initializer = self.predator_additional_init
        # self.predator_additional_init - это то, что мы объявили над __init__
        # но если мы импортировали какую-то стратегию, то она
        # заменит эту функцию другой

        if additional_initializer_args is None:
            additional_initializer_args = []

        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}

        pass # ЗДЕСЬ ПРОВОДИМ ИНИЦИАЛИЗАЦИЮ ЖИВОТНОГО
        # ВОТ ЗДЕСЬ
        # НЕ ТАМ
        # И НЕ ТУТ
        # А ВОТ ЗДЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕСЬ

        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
        # Обратите внимание: self как первый аргумент передастся автоматически

class Victim(Animal):
    # Объявим по дефолту пустую доп. инициализацию:
    victim_additional_init = lambda self: None

    def __init__(self, parent_initializer_args=None, paranet_initializer_kwargs=None,
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
        if parent_initializer_args is None:
            parent_initializer_args = []
        if parent_initializer_kwargs is None:
            parent_initializer_kwargs = {}
        # Сначала делаем инициализацию нас как животного:
        Animal.__init__(self, *parent_initializer_args,
            **parent_initializer_kwargs)

        if additional_initializer is None:
            additional_initializer = self.victim_additional_init
        # self.victim_additional_init - это то, что мы объявили над __init__
        # но если мы импортировали какую-то стратегию, то она
        # заменит эту функцию другой

        if additional_initializer_args is None:
            additional_initializer_args = []

        if additional_initializer_kwargs is None:
            additional_initializer_kwargs = {}

        pass # ЗДЕСЬ ПРОВОДИМ ИНИЦИАЛИЗАЦИЮ ЖИВОТНОГО
        # ВОТ ЗДЕСЬ
        # НЕ ТАМ
        # И НЕ ТУТ
        # А ВОТ ЗДЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕСЬ

        additional_initializer(*additional_initializer_args,
            **additional_initializer_kwargs)
        # Обратите внимание: self как первый аргумент передастся автоматически
