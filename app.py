from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

#tickets = []
def load_tickets():
    if os.path.exists("data/tickets.json"):
        with open("data/tickets.json", "r") as f:
            return json.load(f)
    return [] 


def save_ticket(tickets):
    with open ("data/tickets.json", "w") as f:
        json.dump(tickets, f , indent=4)


#Job 
def load_jobs():
    if os.path.exists("data/jobs.json"):
        with open("data/jobs.json", "r") as f:
            return json.load(f)
    return [] 


def save_job(jobs):
    with open ("data/jobs.json", "w") as f:
        json.dump(jobs, f , indent=4)

@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs)

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

@app.route('/jobs', methods=['GET', 'POST'])
def new_job():
    if request.method == 'POST':
        name = request.form['name']
        operator = request.form['operator']
        description = request.form['description']
        impact = request.form.get('impact', 'no')
        impact_customer = request.form.get('impactCustomer', 'no')
        impact_desc = request.form.get('impactDesc', '')
        start_time = request.form['time_start']
        end_time = request.form['time_end']

        jobs = load_jobs()

        jobs.append({
            'name': name,
            'operator': operator,
            'description': description,
            'impact': impact,
            'impact_customer': impact_customer,
            'impact_desc': impact_desc,
            'start_time': start_time,
            'end_time': end_time
        })

        save_job(jobs)

        return redirect(url_for('new_job'))  # refresh page after saving

    jobs = load_jobs()
    return render_template('job_list.html', jobs=jobs)

    


if __name__ == "__main__":
    app.run(debug=True)
