def even(func):
    # создаем переменную в которой будем хранить ответ
    cur_exec_count = 0
    # создаем враппер, который принимает все аргументы и именованные аргументы
    def wrapper(*args, **kwargs):
        nonlocal cur_exec_count
        cur_exec_count += 1

        if cur_exec_count % 2 == 1:
            return None

        return func(*args, **kwargs)

    return wrapper

def clip(func):
    # просто получаем именнованные аргументы и не передаем дальше
    def wrapper(*args, **kwargs):
        return func(*args)

    return wrapper

# декоратор с еще одним параметром просто оборачиваем снаружи
def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator

def cash(func):
    import json
    arguments_to_response = dict()

    def wrapper(*args, **kwargs):
        # превращаем все аргументы в строку, чтобы потом их было легко хэшировать
        args_json = json.dumps(args)
        kwargs_json = json.dumps(kwargs)

        # вычисляем хэш
        full_str = args_json + kwargs_json
        hashed_params = hash(full_str)

        # если хэш есть в мапе, то просто возвращаем его
        if hashed_params in arguments_to_response:
            return arguments_to_response[hashed_params]

        # если нет, то вычисляем функцию, сохраняем в мапу и возвращаем вычесленный ответ
        arguments_to_response[hashed_params] = func(*args, **kwargs)
        return arguments_to_response[hashed_params]

    return wrapper
