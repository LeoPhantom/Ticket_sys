# Ticket_sys

======= Ticket & Job Management System =======

A lightweight Flask-based web application for managing tickets, approvals, and scheduled jobs with a clean Bootstrap UI.

 Features
 Ticket Management

Create, view, and delete tickets

Track severity, urgency, operator, time window, and description

Status options: Acknowledge, Approved, Denied, Resolved

Color-coded status & severity indicators

Smooth category filter: All / High / Medium / Low

Automatic status updates via AJAX (fetch)

======= Ticket → Job Linking =======

When approving a ticket, the system:

Prompts confirmation

Prefills a “Create Job” modal

Links the new job to the ticket automatically

Updates the ticket status to approved

======= Job Management =======

Create jobs manually or from approved tickets

Display job list with:

Operator

Description

Impact details

Customer impact

Jobs can optionally include:

Start & end time

Linked ticket ID

Delete jobs safely with confirmation

 UI / UX

Fully responsive Bootstrap 5 interface

Modal-based job creation

Dropdown action menu for ticket status

Pre-filled modal fields when approving tickets

Each ticket has a unique id="ticket-123" anchor for linking

Optional linking back from job → ticket


==== Note ==== 
Can run app.py -c Jobs or app.py -c tickets to clean json files in /data 
