class BaseModel(object):

    def update(self, data):
        for key, value in data.items():
            if key in data and getattr(self, key) != value:
                setattr(self, key, value)
