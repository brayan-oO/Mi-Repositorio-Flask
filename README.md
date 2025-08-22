# 🧠 Character API with Flask and SQLite

A RESTful API built with Flask to manage fictional characters and their pets. Designed for integration with frontends, mobile apps, or as a backend for creative products like interactive books.

---

## 🚀 Features

- Full CRUD for characters
- One-to-one relationship with pets (Foreign Key)
- Persistent storage using SQLite
- RESTful endpoints (`GET`, `POST`, `PUT`, `DELETE`)
- Ready for deployment on Render or Railway

---

## 📦 Installation

```bash
git clone https://github.com/ISC/my-flask-api.git
cd my-flask-api
pip install -r requirements.txt
python app.py

🔌 Available Endpoints
Method	Route	Description
GET	/characters	List all characters
POST	/characters	Create a new character
GET	/characters/<name>	Search character by name
PUT	/characters/<name>	Update character's favorite color

🧠 Data Structure
{
  "name": "Aria Mendoza",
  "age": 13,
  "favorite_color": "emerald green",
  "pet": {
    "type": "miniature dragon",
    "name": "Centella"
  }
}

🛠️ Technologies Used
Python 3.10+
Flask
SQLite3
Gunicorn (for production)

Render / Railway (for deployment)

🌐 Deployment
This project is ready to be deployed on platforms like Render or Railway. Simply push it to GitHub and follow the setup instructions.

👤 Author
ISC – A creative and technical developer passionate about building solutions that merge art, data,
and technology. Specialized in backend development, visualization, and unique editorial products.



