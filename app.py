from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tickets = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        severity = request.form['severity']

        tickets.append({
            'title': title,
            'description': description,
            'severity': severity
        })

        return redirect(url_for('view_tickets'))

    return render_template('new_ticket.html')

@app.route('/tickets')
def view_tickets():
    return render_template('view_tickets.html', tickets=tickets)


if __name__ == "__main__":
    app.run(debug=True)
