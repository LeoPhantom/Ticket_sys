import json
import os

def clean_up(type):
    try:
        if type == 'tickets':
            ticket_file = "data/tickets.json"
            index_file = "data/ticket_indexs.json"

            if os.path.exists(ticket_file) and os.path.exists(index_file):

                # Clear the main tickets file
                with open(ticket_file, "w") as f:
                    f.write("[]")

                # Reset the index
                with open(index_file, "r") as d:
                    data = json.load(d)
                    data["id"] = 0

                with open(index_file, "w") as d:
                    json.dump(data, d, indent=4)

                print(" Tickets cleanup completed successfully")
            else:
                print(" Ticket files not found")

        elif type == 'jobs':
            job_file = "data/jobs.json"
            job_index = "data/job_indexs.json"

            if os.path.exists(job_file) and os.path.exists(job_index):

                # Clear jobs
                with open(job_file, "w") as f:
                    f.write("[]")

                # Reset job index
                with open(job_index, "r") as d:
                    data = json.load(d)
                    data["id"] = 0

                with open(job_index, "w") as d:
                    json.dump(data, d, indent=4)

                print(" Jobs cleanup completed successfully")
            else:
                print(" Job files not found")

        else:
            print(" Unknown cleanup type. Use: 'tickets' or 'jobs'")

    except Exception as e:
        print(f" Error during cleanup: {e}")


