from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f'''
    <html>
        <head>
            <title>DevOps Docker App</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
                .container {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #2E86AB; }}
                .success {{ color: #28a745; font-weight: bold; }}
                .info {{ background: #e7f3ff; padding: 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 DevOps CI/CD Pipeline Working!</h1>
                <div class="info">
                    <p><strong>Container ID:</strong> {hostname}</p>
                    <p><strong>Environment:</strong> {os.getenv('ENVIRONMENT', 'production')}</p>
                    <p><strong>Status:</strong> <span class="success">✅ Automated Deployment</span></p>
                </div>
                <hr>
                <p>This application was automatically deployed using GitHub Actions CI/CD</p>
                <p>Every code change triggers: <strong>Test → Build → Deploy</strong></p>
                <p>Your DevOps skills are growing! 🎉</p>
            </div>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'devops-docker-app'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)