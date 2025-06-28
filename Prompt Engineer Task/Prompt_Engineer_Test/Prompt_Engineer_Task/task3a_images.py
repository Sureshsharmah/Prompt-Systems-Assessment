from openai import AzureOpenAI
from pathlib import Path
import json
import requests
from config import config, get_azure_openai_client

class ImageTask:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.client = get_azure_openai_client()
        if self.client is None:
            raise ValueError("Failed to initialize Azure OpenAI client")
        
    def create_image_prompts(self):
        base_style = "Photorealistic grayscale image with single teal accent color #30C9CB, professional lighting, minimalist composition, high contrast, modern aesthetic"
        
        prompts = [
            f"{base_style}, business professional woman in modern office, teal accent on laptop screen, clean background, confident pose, natural lighting",
            f"{base_style}, abstract geometric shapes with teal highlights, architectural elements, shadows and depth, corporate minimalism",
            f"{base_style}, modern workspace setup, teal accent on single design element, clean desk, natural textures, professional atmosphere"
        ]
        
        return prompts
    
    def generate_images(self, prompts):
        image_data = []
        
        # Check if DALL-E deployment is available
        try:
            # Test with a simple prompt first
            test_response = self.client.images.generate(
                model="dall-e-3",  # Try standard DALL-E name first
                prompt="test image",
                size="1024x1024",
                quality="hd",
                n=1
            )
            image_model = "dall-e-3"
        except Exception as e:
            print(f"DALL-E-3 not available: {e}")
            print("Creating placeholder image data instead...")
            
            # Create placeholder data when image generation isn't available
            for i, prompt in enumerate(prompts, 1):
                image_data.append({
                    "filename": f"Image_{i}_placeholder.txt",
                    "prompt": prompt,
                    "status": "Image generation not available - DALL-E-3 deployment required",
                    "placeholder_url": f"https://placeholder.com/1024x1024?text=Image+{i}"
                })
                
                # Create placeholder file
                with open(self.output_dir / f"Image_{i}_placeholder.txt", "w") as f:
                    f.write(f"Image {i} Prompt:\n{prompt}\n\nNote: Actual image generation requires DALL-E-3 deployment in Azure OpenAI")
            
            return image_data
        
        # If DALL-E is available, generate actual images
        for i, prompt in enumerate(prompts, 1):
            try:
                response = self.client.images.generate(
                    model=image_model,
                    prompt=prompt,
                    size="1024x1024",
                    quality="hd",
                    n=1
                )
                
                image_url = response.data[0].url
                image_response = requests.get(image_url)
                
                if image_response.status_code == 200:
                    filename = f"Image_{i}.png"
                    with open(self.output_dir / filename, "wb") as f:
                        f.write(image_response.content)
                    
                    image_data.append({
                        "filename": filename,
                        "prompt": prompt,
                        "url": image_url,
                        "status": "Generated successfully"
                    })
                
            except Exception as e:
                print(f"Error generating image {i}: {e}")
                # Create placeholder for failed generation
                image_data.append({
                    "filename": f"Image_{i}_failed.txt",
                    "prompt": prompt,
                    "error": str(e),
                    "status": "Generation failed"
                })
        
        return image_data
    
    def create_scaling_notes(self):
        notes = """
        Scaling to 10-Image Series Strategy:

        Consistency Framework:
        1. Color Palette: Strict adherence to grayscale + #30C9CB teal accent
        2. Lighting: Consistent natural/professional lighting across all images
        3. Composition: Maintain minimalist, clean aesthetic with similar framing
        4. Subject Matter: Rotate between people, objects, and abstract elements
        5. Accent Placement: Strategic teal placement as focal point in each image

        Technical Specifications:
        - Resolution: 1024x1024 for all images
        - Style Keywords: "photorealistic", "grayscale", "minimalist", "professional"
        - Lighting: "natural lighting", "high contrast", "clean shadows"
        - Quality: HD generation for crisp details

        Variation Strategy:
        - 3-4 images with human subjects (different poses/settings)
        - 3-4 images with objects/workspaces
        - 2-3 abstract/geometric compositions
        - Consistent teal accent integration across all variations

        Quality Control:
        - Test prompts for color accuracy
        - Verify grayscale consistency
        - Ensure professional aesthetic alignment
        
        Azure Deployment Requirements:
        - DALL-E-3 deployment required for actual image generation
        - Alternative: Use external image generation APIs (Midjourney, Stable Diffusion)
        - Fallback: Generate detailed prompts for manual image creation
        """
        return notes
    
    def execute(self):
        print("Executing Task 3a: Image Generation...")
        
        prompts = self.create_image_prompts()
        image_data = self.generate_images(prompts)
        scaling_notes = self.create_scaling_notes()
        
        with open(self.output_dir / "Prompts.json", "w") as f:
            json.dump({
                "prompts": prompts,
                "generated_images": image_data,
                "note": "Image generation requires DALL-E-3 deployment in Azure OpenAI"
            }, f, indent=2)
        
        with open(self.output_dir / "Notes.md", "w") as f:
            f.write(scaling_notes)
        
        print("Task 3a completed successfully!")
