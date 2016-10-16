from flask import Flask, render_template, request, redirect, url_for, abort
# from time import strftime
import json, datetime, re

app = Flask(__name__)

class Post():
    def __init__(self, name, header, text, time):
        self.name = name
        self.header = header
        self.text = text
        self.id = None
        self.time = time

    def __repr__(self):
        return str(dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__)))

    def to_dict(self):
        d = dict((key, getattr(self, key)) for key in dir(self) if key not in dir(self.__class__))
        return d

    def show_preview(self,num):
        return self.text[:num]+'...'


last_id = 1


def write():
    posts_dump = []
    global last_id
    for post in posts_db:

        if post.id is None:
            post.id = last_id
            last_id += 1

        post_dict = post.to_dict()
        posts_dump.append(post_dict)

    print(posts_dump)
    j = json.dumps(posts_dump)
    f = open('database.json', 'w')
    f.write(j)


def read():
    global last_id
    f = open('database.json')
    j = f.read()
    posts_dump = json.loads(j)
    postz = []
    for d in posts_dump:
        p = Post(name=d['name'], text=d['text'], header=d['header'], time=d['time'])
        p.id = d['id']
        print(p)
        # think about algorythm
        if p.id >= last_id:
            last_id = p.id + 1

        postz.append(p)
    print(postz)
    return postz

posts_db = read()

@app.route('/')
def main():
    return render_template('main.html', posts = reversed(posts_db))

@app.route('/post_entry', methods=['POST'])
def post_add():
    post_header = request.form['post_header']
    post_body = request.form['post_body']
    post_author = request.form['post_author']
    now = datetime.datetime.now()
    post_time = now.strftime("%Y-%m-%d %H:%M:%S")
    m = re.match('^\w+\s\w+$', post_author)

    if post_body is None or post_body == '':
        error_message = 'No text = No post'
    elif m is None:
        error_message = 'Invalid name format'
    else:
        post_entry = Post(header=post_header, text=post_body, name=post_author, time=post_time)
        posts_db.append(post_entry)
        write()
        error_message = None

    return render_template('post_entry.html', error_message = error_message)


@app.route('/post/<int:id>')
def post_render(id):
    post_found = None

    for post in posts_db:
        if post.id == id:
            post_found = post
            break

    if post_found is None:
        abort(404)
    return render_template('post.html', post = post_found)

if __name__ == '__main__':
    app.run(debug=True)

