import os
from pathlib import Path
from task1_humanization import HumanizationTask
from task2_podcast import PodcastTask
from task3a_images import ImageTask
from task3b_video import VideoTask
from task4_audit import AuditTask

def setup_directories():
    base_dir = Path("Prompt_Engineer_Test")
    directories = [
        "Task_1_Humanization",
        "Task_2_Podcast_Prompts", 
        "Task_3a_Image_Generation",
        "Task_3b_Video_Generation",
        "Task_4_Prompt_Audit"
    ]
    
    for dir_name in directories:
        (base_dir / dir_name).mkdir(parents=True, exist_ok=True)
    
    return base_dir

def main():
    base_dir = setup_directories()
    
    print("Starting Prompt Engineer Screening Test...")
    
    task1 = HumanizationTask(base_dir / "Task_1_Humanization")
    task1.execute()
    
    task2 = PodcastTask(base_dir / "Task_2_Podcast_Prompts")
    task2.execute()
    
    task3a = ImageTask(base_dir / "Task_3a_Image_Generation")
    task3a.execute()
    
    task3b = VideoTask(base_dir / "Task_3b_Video_Generation")
    task3b.execute()
    
    task4 = AuditTask(base_dir / "Task_4_Prompt_Audit")
    task4.execute()
    
    print("All tasks completed successfully!")

if __name__ == "__main__":
    main()
