from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Level 6: The Command Room</title>
    <style>
        body { font-family: sans-serif; text-align: center; padding: 50px; background-color: #ede7f6; }
        .container { background: white; padding: 20px; border-radius: 8px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        input { padding: 10px; width: 250px; }
        button { padding: 10px; }
        pre { text-align: left; background: #f4f4f4; padding: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Level 6: The Command Room</h1>
        <p>Use our network tool to ping a server!</p>
        <form method="POST">
            <input type="text" name="ip" placeholder="e.g., 127.0.0.1" required>
            <button type="submit">Ping</button>
        </form>
        {% if output %}
        <h2>Result:</h2>
        <pre>{{ output }}</pre>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        ip = request.form.get("ip")
        # VULNERABLE: Direct command execution
        command = f"ping -c 1 {ip}" if os.name != 'nt' else f"ping -n 1 {ip}"
        try:
            output = os.popen(command).read()
        except Exception as e:
            output = str(e)
    return render_template_string(HTML_TEMPLATE, output=output)

if __name__ == "__main__":
    # Ensure flag.txt exists
    with open("flag.txt", "w") as f:
        f.write("CTF{the_final_command_executed}")
    app.run(host="0.0.0.0", port=5000)
