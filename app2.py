from flask import Flask, redirect, url_for, request, render_template

# Inisialisasi Flask app
app = Flask(__name__, template_folder='templates')

@app.route('/')  # Tambah route untuk homepage
def home():
    return redirect(url_for('login'))

@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)