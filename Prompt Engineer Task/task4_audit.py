from openai import AzureOpenAI
from pathlib import Path
import json
from config import config, get_azure_openai_client

class AuditTask:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.client = get_azure_openai_client()
        if self.client is None:
            raise ValueError("Failed to initialize Azure OpenAI client")
        
    def analyze_existing_gpt(self):
        analysis = {
            "original_gpt": {
                "name": "Email Marketing Assistant",
                "description": "Helps create email marketing campaigns",
                "current_structure": [
                    "Generic greeting",
                    "Ask for campaign details",
                    "Generate email content",
                    "Provide basic suggestions"
                ]
            },
            "strengths": [
                "Simple user interface",
                "Covers basic email marketing needs",
                "Provides templates"
            ],
            "weaknesses": [
                "Lacks audience segmentation consideration",
                "No A/B testing guidance",
                "Generic output without brand voice customization",
                "Missing compliance and deliverability factors",
                "No performance metrics integration"
            ],
            "failure_scenarios": [
                "Generates content that violates CAN-SPAM regulations",
                "Creates emails without considering sender reputation",
                "Produces generic content that doesn't match brand voice",
                "Fails to optimize for mobile devices",
                "Doesn't account for different email client rendering"
            ]
        }
        return analysis
    
    def create_redesigned_system(self):
        redesigned_system = {
            "system_name": "Advanced Email Marketing Strategist",
            "multi_stage_approach": {
                "stage_1_discovery": {
                    "prompt": """
                    You are an expert email marketing strategist. Before creating any content, gather essential information:
                    
                    1. Brand Profile: Industry, voice, tone, values
                    2. Audience Segmentation: Demographics, behavior, preferences
                    3. Campaign Objective: Awareness, conversion, retention, re-engagement
                    4. Technical Requirements: Email client compatibility, mobile optimization
                    5. Compliance Needs: Industry regulations, geographic requirements
                    
                    Ask specific, targeted questions to understand these elements before proceeding.
                    """,
                    "validation_checks": [
                        "Brand voice alignment",
                        "Audience relevance",
                        "Legal compliance",
                        "Technical feasibility"
                    ]
                },
                "stage_2_strategy": {
                    "prompt": """
                    Based on the discovery information, create a comprehensive email strategy:
                    
                    1. Subject Line Variations: Create 3-5 A/B test options
                    2. Content Structure: Header, body, CTA, footer optimization
                    3. Personalization Strategy: Dynamic content recommendations
                    4. Send Time Optimization: Best practices for target audience
                    5. Follow-up Sequence: Multi-touch campaign planning
                    
                    Ensure all recommendations align with brand guidelines and compliance requirements.
                    """,
                    "output_format": "Structured strategy document with actionable recommendations"
                },
                "stage_3_content_creation": {
                    "prompt": """
                    Generate email content following the approved strategy:
                    
                    1. Multiple subject line options with rationale
                    2. Mobile-optimized email body with clear hierarchy
                    3. Compelling CTA with placement recommendations
                    4. Alt text for images and accessibility considerations
                    5. Plain text version for compatibility
                    
                    Include specific metrics to track and optimization suggestions.
                    """,
                    "quality_checks": [
                        "Brand voice consistency",
                        "Mobile responsiveness",
                        "Accessibility compliance",
                        "Spam filter optimization"
                    ]
                },
                "stage_4_optimization": {
                    "prompt": """
                    Provide comprehensive optimization and testing guidance:
                    
                    1. A/B Testing Plan: Elements to test and success metrics
                    2. Performance Monitoring: Key metrics and benchmarks
                    3. Iteration Strategy: How to improve based on results
                    4. Deliverability Optimization: Technical recommendations
                    5. Compliance Checklist: Final review requirements
                    
                    Include specific tools and platforms for implementation.
                    """
                }
            },
            "improvement_features": [
                "Multi-stage prompt system prevents generic outputs",
                "Built-in compliance and accessibility checks",
                "Audience segmentation integration",
                "A/B testing framework included",
                "Performance optimization guidance",
                "Brand voice consistency validation"
            ]
        }
        return redesigned_system
    
    def create_comparison_sample(self):
        comparison = {
            "original_output_example": """
            Subject: Check out our new products!
            
            Hi there,
            
            We have some exciting new products that we think you'll love. Click here to see what's new and get 20% off your first order.
            
            Thanks,
            The Team
            """,
            "redesigned_output_example": """
            Discovery Phase Results:
            - Brand: Sustainable fashion startup
            - Audience: Eco-conscious millennials, 25-40
            - Objective: Product launch with conversion focus
            - Compliance: GDPR, CAN-SPAM
            
            Strategy:
            Subject Line A/B Tests:
            A: "Sarah, your sustainable wardrobe upgrade is here 🌱"
            B: "New eco-friendly collection - 48 hours early access"
            C: "Sustainable fashion that doesn't compromise on style"
            
            Content Structure:
            - Personal greeting with name
            - Value proposition highlighting sustainability
            - Social proof with customer testimonials
            - Clear CTA with urgency element
            - Mobile-optimized design with alt text
            
            Performance Tracking:
            - Open rate benchmark: 22% (industry average)
            - Click-through rate target: 3.5%
            - Conversion rate goal: 2.1%
            
            Optimization Plan:
            - Test send times: Tuesday 10 AM vs Thursday 2 PM
            - Monitor deliverability across major email clients
            - A/B test CTA button colors and placement
            """
        }
        return comparison
    
    def execute(self):
        print("Executing Task 4: Prompt System Audit...")
        
        analysis = self.analyze_existing_gpt()
        redesigned_system = self.create_redesigned_system()
        comparison = self.create_comparison_sample()
        
        with open(self.output_dir / "Original_Review.json", "w") as f:
            json.dump(analysis, f, indent=2)
        
        with open(self.output_dir / "Redesigned_System.json", "w") as f:
            json.dump(redesigned_system, f, indent=2)
        
        with open(self.output_dir / "Sample_Comparison.json", "w") as f:
            json.dump(comparison, f, indent=2)
        
        print("Task 4 completed successfully!")
