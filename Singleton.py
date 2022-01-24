class Singleton(type):
    instances={}
    def __call__(cls):
        if cls not in cls.instances :
            cls.instances[cls] = super().__call__()
        return cls.instances[cls]