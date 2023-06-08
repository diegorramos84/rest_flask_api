import os
from dotenv import load_dotenv

load_dotenv()

# app init
from . import create_app
app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/')
def hello():
    return "Hello World!"

from .books import urls

if __name__ == "__main__":
    app.run(debug=True)
