def score_server():
    from flask import Flask, render_template
    from flask import request

    app = Flask(__name__)
    my_dict = dict()

    @app.route("/", methods=['GET'])
    def get():
        try:
            f = open('Scores.txt', 'r')
            res = f.read()
            return render_template('index.html', SCORE=res)
        except:
            return render_template('error.html', ERROR='we have a problem reading from the dataBase')
        finally:
            f.close()

    app.run(host="0.0.0.0",port=5001, debug=True)


score_server()
