def score_server():
    from flask import Flask, render_template
    from flask import request

    app = Flask(__name__)
    my_dict = dict()

    @app.route("/", methods=['GET'])
    def get():
        try:
            f = open('scores.txt', 'r')
            res = f.read()
            print(res)
            return render_template('index.html', SCORE=res)
        except:
            return render_template('error.html', ERROR='we have a problem reading from the dataBase')

    app.run(port=5001, debug=True)


score_server()
