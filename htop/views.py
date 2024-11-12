# myproject/htop/views.py
from django.http import HttpResponse
import os
from datetime import datetime
import subprocess

def htop(request):
    name = "Sai Nikhila"  # Replace with your actual name
    username = "nikhila"
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre><strong>Top Output:</strong>\n{top_output}</pre>
    """
    return HttpResponse(response)