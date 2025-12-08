from flask import Flask, render_template, request, redirect, url_for
import json
import os


app = Flask(__name__)

#tickets 
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
#index 
def id_index(type):
    if type =='job' and os.path.exists("data/job_index.json"):
        with open ("data/job_index.json") as f:
            return json.load(f)
    elif type =='ticket' and os.path.exists("data/ticket_index.json"):
        with open ("data/ticket_index.json") as f:
            return json.load(f)
    else:

        return {"id": 0}   # <-- FIX

def save_id_counter(type, counter):
    if type == 'job':
    
        with open("data/job_index.json", "w") as f:
            json.dump(counter, f, indent=4)

    elif type == 'ticket':

        with open("data/ticket_index.json", "w") as f:
            json.dump(counter, f, indent=4)

    else:
        print("NO such luck")

#ID func
def set_id(type):
    if type == 'job':
        counter = id_index(type)
        counter["id"] += 1
        save_id_counter(type, counter)
        return counter["id"]
    elif type == 'ticket':
        counter = id_index(type)
        counter["id"] += 1
        save_id_counter(type, counter)
        return counter["id"]
    

    
     
    


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
        id = set_id('ticket')

        tickets.append({
            'id' : id,
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


if __name__ == "__main__":
    app.run(debug=True)
