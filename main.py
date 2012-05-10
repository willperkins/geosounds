try:
    from bottle import run, route, static_file
except ImportError:
    import sys
    sys.exit('please install bottle.py to run this: pip install bottle')

@route('/')
def index():
    return static_file('index.html',root='.')

@route('/assets/:filename#.*#')
def assets(filename):
    return static_file(filename,root='assets')

if __name__ == '__main__':
    run(host='localhost', port=8080)
