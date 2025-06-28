import json
from pathlib import Path
from config import config

class VideoTask:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        
    def create_video_prompt_system(self):
        system = {
            "title": "Why Most Productivity Advice Fails",
            "duration": "15-20 seconds",
            "structure": {
                "opening": {
                    "duration": "0-3 seconds",
                    "visual": "Close-up of cluttered desk with productivity books, timer showing, frustrated person",
                    "motion": "Slow zoom out revealing chaos",
                    "text_overlay": "The Problem with Productivity"
                },
                "transition_1": {
                    "duration": "3-8 seconds", 
                    "visual": "Split screen: left shows generic advice (early morning, meditation), right shows real person struggling",
                    "motion": "Smooth transition between scenes",
                    "text_overlay": "Generic vs Reality"
                },
                "revelation": {
                    "duration": "8-15 seconds",
                    "visual": "Person finding their own rhythm, working effectively in their natural environment",
                    "motion": "Confident, steady movements",
                    "text_overlay": "Find YOUR System"
                },
                "closing": {
                    "duration": "15-20 seconds",
                    "visual": "Clean, organized workspace with person working contentedly",
                    "motion": "Gentle fade to logo/CTA",
                    "text_overlay": "Personalized Productivity"
                }
            },
            "technical_specs": {
                "aspect_ratio": "16:9",
                "style": "Modern, clean aesthetic",
                "color_palette": "Muted tones with accent colors",
                "lighting": "Natural, professional",
                "camera_movement": "Smooth, purposeful transitions"
            }
        }
        
        return system
    
    def create_runway_prompts(self):
        prompts = [
            {
                "prompt_1": "A cluttered desk with productivity books scattered around, a timer ticking, showing a frustrated person's hands shuffling through papers. Camera slowly zooms out to reveal the chaos. Cinematic lighting, 4K quality, smooth motion.",
                "settings": "Duration: 4 seconds, Motion: Medium, Camera: Zoom out"
            },
            {
                "prompt_2": "Split screen composition: left side shows generic morning routine (alarm clock, meditation pose), right side shows real person struggling with the same routine. Smooth transition between scenes. Professional lighting, realistic style.",
                "settings": "Duration: 5 seconds, Motion: Low, Camera: Static with transitions"
            },
            {
                "prompt_3": "Person discovering their natural work rhythm, working effectively in their preferred environment (could be evening, with music, in comfortable clothes). Confident body language, steady movements. Warm, natural lighting.",
                "settings": "Duration: 6 seconds, Motion: Medium, Camera: Gentle pan"
            },
            {
                "prompt_4": "Clean, organized workspace with the same person now working contentedly and efficiently. Gentle fade transition to end screen. Soft, professional lighting, minimalist aesthetic.",
                "settings": "Duration: 5 seconds, Motion: Low, Camera: Slow push in"
            }
        ]
        
        return prompts
    
    def create_consistency_notes(self):
        notes = """
        Maintaining Consistency Across 5-Video Series:

        Visual Consistency:
        1. Color Grading: Establish LUT/color profile for uniform look
        2. Lighting Setup: Consistent lighting ratios and temperature
        3. Framing: Maintain similar shot compositions and aspect ratios
        4. Typography: Standardized font, size, and positioning for text overlays

        Technical Consistency:
        1. Duration Control: Strict timing guidelines for each segment
        2. Motion Parameters: Consistent camera movement speeds and styles
        3. Transition Types: Standardized transition effects between scenes
        4. Quality Settings: Uniform resolution, frame rate, and compression

        Content Consistency:
        1. Narrative Structure: Follow same 4-part story arc for each video
        2. Visual Metaphors: Consistent symbolic elements (clutter = confusion, clean = success)
        3. Character Continuity: Same actor/persona across series when possible
        4. Brand Elements: Consistent logo placement, color scheme, and style

        Production Workflow:
        1. Storyboard Templates: Pre-designed layouts for each video type
        2. Asset Library: Reusable elements (fonts, colors, transitions)
        3. Review Process: Consistency checklist before final render
        4. Version Control: Track successful elements for replication

        Platform Optimization:
        - Multiple aspect ratios (16:9, 9:16, 1:1) from same source
        - Subtitle positioning consistency
        - Thumbnail style alignment
        """
        return notes
    
    def execute(self):
        print("Executing Task 3b: Video Generation...")
        
        prompt_system = self.create_video_prompt_system()
        runway_prompts = self.create_runway_prompts()
        consistency_notes = self.create_consistency_notes()
        
        with open(self.output_dir / "Prompt_System.json", "w") as f:
            json.dump(prompt_system, f, indent=2)
        
        with open(self.output_dir / "Runway_Prompts.json", "w") as f:
            json.dump(runway_prompts, f, indent=2)
        
        with open(self.output_dir / "Notes.md", "w") as f:
            f.write(consistency_notes)
        
        with open(self.output_dir / "Output_Link.txt", "w") as f:
            f.write("Video output would be generated using Runway ML or similar platform with the provided prompts.\nExpected output: 15-20 second video following the structured prompt system.")
        
        print("Task 3b completed successfully!")
