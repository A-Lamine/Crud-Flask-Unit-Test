from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from . import db
from .models import Video


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def movie():
    all_data = Video.query.all()
    return render_template("movies.py", movies=all_data)


@main.route('/insert', methods=['POST'])
def insert():
    request_data = request.get_json()

    if not request_data:
        lien = request.form['url']
        title = request.form['title']

        my_data = Video(url=lien, title=title)
        db.session.add(my_data)
        db.session.commit()

        flash("Movie Inserted Successfully")

        return redirect(url_for('main.movie'))
    elif request_data:
        lien = request_data['url']
        title = request_data['title']

        my_data = Video(url=lien, title=title)
        db.session.add(my_data)
        db.session.commit()
        data = {
            "Movie added": "✅",
            "ID" : my_data.id,
            "Url" : my_data.url,
            "title" : my_data.title
        }
        return jsonify(data), 201


@main.route('/update', methods=['POST', 'PUT'])
def update():
    if request.method == 'POST':

        my_data = Video.query.get(request.form.get('id'))

        my_data.url = request.form['url']
        my_data.title = request.form['title']

        db.session.commit()
        flash("Movie Updated Successfully")

        return redirect(url_for('main.movie'))

    elif request.method == 'PUT':

        request_data = request.get_json()

        my_data = Video.query.get(request_data['id'])

        my_data.url = request_data['url']
        my_data.title = request_data['title']
        db.session.commit()
        data = {
            "Movie Updated" : "✅",
            "ID" : my_data.id,
            "Url" : my_data.url,
            "title" : my_data.title
        }

        return  jsonify(data),200


@main.route('/delete/<int:id>/', methods=['GET', 'DELETE'])
def delete(id):
    my_data = Video.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    if request.method == 'GET':
        flash("Movie Deleted Successfully")
        return redirect(url_for('main.movie'))
    else:
        data = {
            "Movie Deleted" : "✅",
            "ID" : my_data.id,
            "Url" : my_data.url,
            "title" : my_data.title
        }
        return jsonify(data)
