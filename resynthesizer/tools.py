from pathlib import Path

ROOT = str(Path(__file__).parent.parent.absolute())


def wrapJsCallback(code):
    func = ('(...args) => {'
    f'   {code}'
    '    return [...args];'
    '}')
    return func


def loadJsCallback(file):
    with open(file) as f:
        code = f.read()
    return wrapJsCallback(code)
