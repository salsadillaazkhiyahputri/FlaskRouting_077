from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__) # Membuat aplikasi Flask

@app.route('/')
def home():
    return render_template('index.html')  # Menampilkan template index.html

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        return redirect(url_for('home'))

if __name__ == '__main__': # Menjalankan aplikasi Flask
    app.run(debug=True)