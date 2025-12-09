
import json
import os

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
    