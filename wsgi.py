from app import app

if __name__ == '__main__':
    app.run()

# persist:
# gunicorn --bind 0.0.0.0:<your-desired-port-here> wsgi:app -D

# kill:
# ps ax | grep gunicorn
# kill <processid>