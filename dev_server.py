import os
import sys
import json
import sqlite3
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

DB_FILE = "stories_local.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        text TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('pending', 'approved')) DEFAULT 'pending',
        timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """)
    # Check if empty
    cursor.execute("SELECT COUNT(*) FROM stories")
    if cursor.fetchone()[0] == 0:
        # Insert initial data
        sample_stories = [
            ("Anonymous", "Using the heat therapy tips on this website helped relieve my period cramps. So grateful for this resource!", "approved"),
            ("Aaradhya", "Menstrual health education in school was non-existent. I'm glad platforms like Maa are changing the conversation.", "approved"),
            ("Priya", "I was hesitant to talk about PCOD, but seeing the detailed breakdown here motivated me to visit a gynecologist.", "approved"),
            ("Riya", "A story waiting for approval to test the admin features.", "pending")
        ]
        cursor.executemany("INSERT INTO stories (name, text, status) VALUES (?, ?, ?)", sample_stories)
        conn.commit()
    conn.close()

class DevServerHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        
        # Normalize double slashes if any
        if path.startswith("//"):
            path = path[1:]

        # Handle API routes
        if path == "/api/get_stories.php":
            self.handle_get_stories()
        elif path == "/api/admin_get_stories.php":
            self.handle_admin_get_stories(parsed_url.query)
        else:
            # Serve static files normally
            super().do_GET()

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        if path.startswith("//"):
            path = path[1:]

        if path == "/api/add_story.php":
            self.handle_add_story()
        elif path == "/api/admin_action.php":
            self.handle_admin_action()
        elif path == "/api/admin_add_approved.php":
            self.handle_admin_add_approved()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def handle_get_stories(self):
        try:
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, text, timestamp FROM stories WHERE status = 'approved' ORDER BY timestamp DESC")
            rows = cursor.fetchall()
            stories = []
            for row in rows:
                ts = row[3]
                if "T" not in ts:
                    ts = ts.replace(" ", "T") + "Z"
                stories.append({
                    "id": row[0],
                    "name": row[1],
                    "text": row[2],
                    "timestamp": ts
                })
            conn.close()
            
            response_data = json.dumps(stories).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data)
        except Exception as e:
            self.send_error_response(500, f"Failed to fetch stories: {str(e)}")

    def handle_admin_get_stories(self, query_str):
        try:
            params = urllib.parse.parse_qs(query_str)
            status = params.get('status', ['pending'])[0]
            if status not in ['pending', 'approved']:
                self.send_error_response(400, "Invalid status.")
                return

            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, text, timestamp, status FROM stories WHERE status = ? ORDER BY timestamp DESC", (status,))
            rows = cursor.fetchall()
            stories = []
            for row in rows:
                ts = row[3]
                if "T" not in ts:
                    ts = ts.replace(" ", "T") + "Z"
                stories.append({
                    "id": row[0],
                    "name": row[1],
                    "text": row[2],
                    "timestamp": ts,
                    "status": row[4]
                })
            conn.close()

            response_data = json.dumps(stories).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data)
        except Exception as e:
            self.send_error_response(500, f"Failed to fetch stories: {str(e)}")

    def handle_add_story(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            name = data.get('name', '').strip()
            text = data.get('text', '').strip()

            if not name or not text:
                self.send_error_response(400, "Name and text are required.")
                return

            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stories (name, text, status) VALUES (?, ?, 'pending')", (name, text))
            last_id = cursor.lastrowid
            conn.commit()
            conn.close()

            response_data = json.dumps({"success": True, "id": last_id}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data)
        except Exception as e:
            self.send_error_response(500, f"Failed to add story: {str(e)}")

    def handle_admin_action(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            story_id = data.get('id')
            action = data.get('action')

            if not story_id or action not in ['approve', 'reject', 'delete']:
                self.send_error_response(400, "Invalid ID or action.")
                return

            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            if action == 'approve':
                cursor.execute("UPDATE stories SET status = 'approved' WHERE id = ?", (story_id,))
            elif action in ['reject', 'delete']:
                cursor.execute("DELETE FROM stories WHERE id = ?", (story_id,))
            conn.commit()
            conn.close()

            response_data = json.dumps({"success": True}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data)
        except Exception as e:
            self.send_error_response(500, f"Failed to process admin action: {str(e)}")

    def handle_admin_add_approved(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            name = data.get('name', '').strip()
            text = data.get('text', '').strip()

            if not name or not text:
                self.send_error_response(400, "Name and text are required.")
                return

            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stories (name, text, status) VALUES (?, ?, 'approved')", (name, text))
            last_id = cursor.lastrowid
            conn.commit()
            conn.close()

            response_data = json.dumps({"success": True, "id": last_id}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(response_data)
        except Exception as e:
            self.send_error_response(500, f"Failed to add approved story: {str(e)}")

    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}).encode('utf-8'))

def run(port=8000):
    init_db()
    server_address = ('', port)
    httpd = HTTPServer(server_address, DevServerHandler)
    print(f"Development server running locally at http://localhost:{port}")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run(port)
