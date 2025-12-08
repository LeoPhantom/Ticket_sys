from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

#tickets = []
def load_tickets():
    if os.path.exists("tickets.json"):
        with open("tickets.json", "r") as f:
            return json.load(f)
    return [] 


def save_ticket(tickets):
    with open ("tickets.json", "w") as f:
        json.dump(tickets, f , indent=4)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        severity = request.form['severity']

        tickets = load_tickets()

        tickets.append({
            'title': title,
            'description': description,
            'severity': severity
        })

        save_ticket(tickets)

        return redirect(url_for('view_tickets'))

    return render_template('new_ticket.html')

@app.route('/tickets')
def view_tickets():
    tickets = load_tickets()
    return render_template('view_tickets.html', tickets=tickets)


if __name__ == "__main__":
    app.run(debug=True)
