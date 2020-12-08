def update_object(obj, **kwargs):
    for key, value in kwargs.items():
        setattr(obj, key, value)
    obj.save()
    return obj
