from openai import AzureOpenAI
from pathlib import Path
import json
from config import config, get_azure_openai_client

class PodcastTask:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.client = get_azure_openai_client()
        if self.client is None:
            raise ValueError("Failed to initialize Azure OpenAI client")
        
    def create_prompt_system(self):
        system = {
            "base_prompt": """
            You are a professional podcast producer creating a 6-minute episode about "The Ethics of AI in Hiring."
            
            Structure: Cold Open → Intro → 3 Segments → CTA
            Tone: Conversational, authoritative, engaging
            Target: HR professionals and business leaders
            
            Generate content that maintains consistent pacing and professional insight throughout.
            """,
            
            "cold_open_prompt": """
            Create a 30-second cold open that hooks listeners with a provocative question or scenario about AI bias in hiring.
            Use specific, relatable examples. End with intrigue that leads into the intro.
            """,
            
            "intro_prompt": """
            Create a 45-second intro that:
            - Welcomes listeners warmly
            - Introduces the topic clearly
            - Previews the three main segments
            - Establishes credibility and relevance
            """,
            
            "segment_prompts": [
                "Segment 1 (90 seconds): The Current State - How AI is being used in hiring today, with specific examples and statistics",
                "Segment 2 (90 seconds): The Ethical Dilemmas - Bias, fairness, and transparency issues with real case studies", 
                "Segment 3 (90 seconds): Best Practices - Actionable guidelines for ethical AI implementation in hiring"
            ],
            
            "cta_prompt": """
            Create a 45-second call-to-action that:
            - Summarizes key takeaways
            - Provides specific next steps for listeners
            - Includes subscription request
            - Ends with memorable closing
            """
        }
        return system
    
    def generate_episode_content(self, prompt_system):
        episode_content = {}
        
        for section, prompt in prompt_system.items():
            if section == "segment_prompts":
                episode_content["segments"] = []
                for i, segment_prompt in enumerate(prompt, 1):
                    response = self.client.chat.completions.create(
                        model=config.model_text_deployment,
                        messages=[
                            {"role": "system", "content": prompt_system["base_prompt"]},
                            {"role": "user", "content": segment_prompt}
                        ],
                        temperature=0.7
                    )
                    episode_content["segments"].append({
                        f"segment_{i}": response.choices[0].message.content
                    })
            elif section != "base_prompt":
                response = self.client.chat.completions.create(
                    model=config.model_text_deployment,
                    messages=[
                        {"role": "system", "content": prompt_system["base_prompt"]},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                episode_content[section.replace("_prompt", "")] = response.choices[0].message.content
        
        return episode_content
    
    def create_consistency_notes(self):
        notes = """
        Maintaining Tone and Structure Across 10+ Episodes:

        1. Template System: Use consistent prompt templates with variable topic insertion
        2. Style Guide: Maintain specific vocabulary, sentence patterns, and transition phrases
        3. Timing Control: Strict word count guidelines for each segment (Cold Open: 75-85 words, etc.)
        4. Voice Consistency: Establish host persona guidelines and speaking patterns
        5. Quality Checks: Implement review prompts that verify tone and structure compliance
        6. Content Database: Build library of proven phrases, transitions, and formatting
        7. Feedback Loop: Track successful episodes and refine prompts based on performance

        Key Parameters:
        - Temperature: 0.7 for creativity with consistency
        - Max tokens: Segment-specific limits
        - System prompts: Detailed persona and format requirements
        """
        return notes
    
    def execute(self):
        print("Executing Task 2: Podcast Generation...")
        
        prompt_system = self.create_prompt_system()
        sample_episode = self.generate_episode_content(prompt_system)
        consistency_notes = self.create_consistency_notes()
        
        with open(self.output_dir / "Prompt_System.json", "w") as f:
            json.dump(prompt_system, f, indent=2)
        
        with open(self.output_dir / "Sample_Output.json", "w") as f:
            json.dump(sample_episode, f, indent=2)
        
        with open(self.output_dir / "Notes.md", "w") as f:
            f.write(consistency_notes)
        
        print("Task 2 completed successfully!")
