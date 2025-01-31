import cProfile
import requests
import pstats

def profile_add_video():
    response = requests.post(
        "http://localhost:8000/add",
        json={
            "link": "https://archive.org/details/archive-video-files",
            "title": "Test Video"
        }
    )
    return response

def main():
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Run the function multiple times
    for _ in range(100):
        profile_add_video()
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()

if __name__ == "__main__":
    main()