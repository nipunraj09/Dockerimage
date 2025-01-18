from app import app

def test_home():
    response=app.test_client().GET("/")


    