import frontend.input_process

p = frontend.input_process.Processor()

while True:
    p.from_human(input())
    print(p.registry.id_registry)
