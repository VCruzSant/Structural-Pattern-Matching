from dataclasses import dataclass


def execute_command_if(command: str):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ chanding directory')
    else:
        print('$ command not implemented')

    print('... rest of the code')


def execute_command_match(command: str):
    match command:
        case 'ls':
            print('$ listing files')

        case 'cd':
            print('$ chanding directory')

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')

# Executando comandos:


def execute_command_split(command: str) -> str | None:
    match command.split():
        case ['ls', d, arg]:
            print('$ listing files from', d, arg)
        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_split('ls /home --force')
# execute_command_split('cd /home')


def execute_command_args(command: str) -> str | None:
    match command.split():
        case ['ls', *directories, '--force']:
            for d in directories:
                print('$ listing files FORCED from', d)

        case ['ls', *directories]:
            for d in directories:
                print('$ listing files from', d)

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_args('ls /home /sant /python')
# print()
# execute_command_args('ls /home /sant /python --force')


def execute_command_pipe(command: str) -> str | None:
    match command.split():
        case ['ls' | 'list', *directories, '--force']:
            for d in directories:
                print('$ listing files FORCED from', d)

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_pipe('list /home /sant /python --force')
# print()
# execute_command_pipe('list /home /sant /python --force')


def execute_command_guard(command: str) -> str | None:
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for d in directories:
                print('$ listing all files from', d)

        case ['ls' | 'list', d]:
            print('$ listing files from', d, 'only')

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_guard('ls /home /sant')
# print()
# execute_command_guard('ls /home')

def execute_command_as(command: str) -> str | None:
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list if len(
                directories) > 1:
            for d in directories:
                print('$ listing ALL files from', d)
            print(f'{the_command=}, {the_list=}')

        case ['ls' | 'list', d]:
            print('$ listing files from', d, 'only')

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_as('ls /home /sant')

def execute_command_dict(command: dict) -> str | None:
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            for d in command['directories']:
                print('$ listing ALL files from', d)

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


# execute_command_dict({'command': 'ls', 'directories': ['/users', '/home']})


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command_class(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for d in command.directories:
                print('$ listing ALL files from', d)

        case ['cd', path]:
            print('$ chanding directory to', path)

        case _:  # não obrigatório(caso padrão)
            print('$ command not implemented')

    print('... rest of the code')


execute_command_class(Command('ls', ['/users']))
