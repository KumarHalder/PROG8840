from locust import HttpUser, task, between

class MyAppUser(HttpUser):    
    @task
    def view_homepage(self):
        self.client.get("/")  # Simulate a GET request to the homepage

