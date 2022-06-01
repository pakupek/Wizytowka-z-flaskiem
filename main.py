from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/website/aboutme')
def aboutme():
     return render_template('aboutme.html')

@app.route('/website/contact')
def contact():
    return render_template('contact.html')

@app.route('/website/contact', methods=['POST'])
def message4():
    print(request.form)
    return redirect('/website/contact')


@app.route('/website/homepage')
def message2():
    return render_template('homepage.html')


@app.route('/website/hobbies')
def message3():
    return render_template('hobbies.html')







if __name__ == '__main__':
    app.run(debug=True)