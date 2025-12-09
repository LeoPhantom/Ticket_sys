from flask import Flask, render_template, request, redirect, url_for
from scripts import *
from controler import *
import sys



app = Flask(__name__)


@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('index.html', jobs=jobs)

@app.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form.get('title')
        operator = request.form.get('operator')
        urgency = request.form.get('urgency')
        description = request.form.get('description')
        severity = request.form.get('severity_impact')   # from dropdown/badge
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        # Load current tickets
        tickets = load_tickets()

        # Generate new ticket ID
        ticket_id = set_id('ticket')

        # Append new ticket
        tickets.append({
            'id': ticket_id,
            'title': title,
            'operator' : operator,
            'urgency' : urgency,
            'description': description,
            'severity': severity,
            'start_time': start_time,
            'end_time': end_time
        })

        # Save all tickets
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
        
        id = set_id('job')

        jobs.append({
            'id' : id,
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

@app.route('/delete_job/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    jobs = load_jobs()
    jobs = [j for j in jobs if j.get("id") != job_id]
    save_job(jobs)
    return redirect(url_for('new_job'))    

@app.route('/delete_ticket/<int:ticket_id>', methods=['POST'])
def delete_ticket(ticket_id):
    tickets = load_tickets()
    tickets = [t for t in tickets if t.get("id") != ticket_id]
    save_ticket(tickets)
    return redirect(url_for('view_tickets'))

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "-c":
        cleanup_type = sys.argv[2].lower()

        if cleanup_type in ["tickets", "jobs"]:
            clean_up(cleanup_type)
            print(f" Cleanup for {cleanup_type} completed.")
            sys.exit(0)
        else:
            print(" Unknown cleanup type. Use: tickets or jobs")
            sys.exit(1)

    app.run(debug=True)
