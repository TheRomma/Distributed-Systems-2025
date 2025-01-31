from locust import HttpUser, task, between

class VideoServiceUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:8000"
    
    @task(2)
    def add_video(self):
        self.client.post("/add", 
            json={
                "link": "https://archive.org/details/archive-video-files",
                "title": "Test Video"
            })
    
    @task(1)
    def remove_video(self):
        self.client.post("/remove",
            json={
                "filename": "test.mp4"
            })
