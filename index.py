from app import app
from routes import render_page_content

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)
