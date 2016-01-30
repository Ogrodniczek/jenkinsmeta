from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/master_design_files/<path:path>')
def send_static(path):
        return send_from_directory('master_design_files', path)


@app.route("/")
def template_test():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
