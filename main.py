import frontend.input_process

p = frontend.input_process.Processor()

while True:
    text = input()
    if text[0] == "{":
        p.from_data(text)
    else:
        p.from_human(text)
    print(p.registry.id_registry)
