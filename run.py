from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/master_design_files/<path:path>')
def send_static(path):
        return send_from_directory('master_design_files', path)



@app.route("/")
def template_test():
    executors={'master': {'executors': 2, 'jobs_active': [], 'offline': False},
 'slaveek': {'executors': 4,
             'jobs_active': [{'name': {'color': 'blue_anime',
                                       'name': 'tete',
                                       'url': 'http://localhost:8080/job/tete/',
                                       'time':{'remaining':'kek', 'started':'lol'},
                                       },
                              'number': '23'},
                             {'name': {'color': 'blue_anime',
                                       'name': 'tete',
                                       'url': 'http://localhost:8080/job/tete/',
                                       'time':{'remaining':'kek', 'started':'lol'},
                                       },
                              'number': '22'},
                             {'name': {'color': 'blue_anime',
                                       'name': 'tete',
                                       'url': 'http://localhost:8080/job/tete/',
                                       'time':{'remaining':'kek', 'started':'lol'},
                                       },
                              'number': '21'},
                             {'name': {'color': 'blue_anime',
                                       'name': 'tete',
                                       'url': 'http://localhost:8080/job/tete/',
                                       'time':{'remaining':'kek', 'started':'lol'},
                                       },
                              'number': '20'}],
             'offline': False}}

    
    return render_template('main.html', executors=executors)


if __name__ == '__main__':
    app.run(debug=True)
