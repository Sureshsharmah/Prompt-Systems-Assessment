# Prompt-Engineer-Assessment


## 📋 Overview

This project showcases advanced prompt engineering capabilities across five comprehensive tasks, demonstrating expertise in AI content humanization, structured prompt systems, multi-modal content generation, and system optimization.

### 🎯 Key Features

- **🤖 AI Content Humanization** - Advanced techniques to bypass AI detection
- **🎙️ Podcast Prompt Systems** - Structured, API-ready content generation
- **🎨 Visual Brand Consistency** - Cohesive image generation prompts
- **🎬 Video Prompt Engineering** - Structured video content systems
- **🔍 System Audit & Optimization** - Critical analysis and redesign of existing AI systems

## 🏗️ Architecture

\`\`\`
prompt-engineer-assessment/
├── 📁 src/
│   ├── main.py                 # Main orchestrator
│   ├── config.py              # Configuration & client setup
│   ├── task1_humanization.py  # AI content humanization
│   ├── task2_podcast.py       # Podcast prompt systems
│   ├── task3a_images.py       # Image generation prompts
│   ├── task3b_video.py        # Video prompt frameworks
│   └── task4_audit.py         # System audit & redesign
├── 📁 outputs/                # Generated content & results
├── 📁 docs/                   # Documentation & examples
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
└── README.md                 # This file
\`\`\`

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Azure OpenAI API access
- Git

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/Sureshsharmah/Prompt-Systems-Assessment
   cd prompt-engineer-assessment
   \`\`\`

2. **Create virtual environment**
   \`\`\`bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Environment setup**
   \`\`\`bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your Azure OpenAI credentials
   # AZURE_OPENAI_API_KEY=your_key_here
   # AZURE_OPENAI_ENDPOINT=your_endpoint_here
   \`\`\`

5. **Run the assessment**
   \`\`\`bash
   python main.py
   \`\`\`

## 🔧 Configuration

Create a `.env` file with your Azure OpenAI credentials:

\`\`\`env
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com
AZURE_OPENAI_API_VERSION=2024-06-01
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
\`\`\`

## 📊 Tasks Overview

### Task 1: AI Content Humanization 🤖➡️👤
- **Objective**: Transform AI-generated content to pass detection systems
- **Techniques**: Natural language patterns, personal anecdotes, varied structures
- **Output**: Human-like articles that maintain factual accuracy

### Task 2: Podcast Prompt Engineering 🎙️
- **Objective**: Create structured, repeatable podcast generation system
- **Format**: Cold Open → Intro → 3 Segments → CTA
- **Focus**: Consistency across multiple episodes via API

### Task 3a: Visual Brand Consistency 🎨
- **Objective**: Generate cohesive image series with brand guidelines
- **Style**: Grayscale + teal accent (#30C9CB)
- **Challenge**: Maintain consistency across multiple generations

### Task 3b: Video Prompt Systems 🎬
- **Objective**: Structure prompts for 15-20 second video content
- **Platform**: Runway ML / Pika Labs compatible
- **Focus**: Scene transitions, pacing, visual coherence

### Task 4: System Audit & Redesign 🔍
- **Objective**: Analyze and improve existing GPT systems
- **Approach**: Identify failure points, redesign architecture
- **Outcome**: Multi-stage prompt system with validation

## 📈 Results & Outputs

After running the assessment, you'll find:

\`\`\`
Prompt_Engineer_Test/
├── Task_1_Humanization/
│   ├── Original_Article.txt      # AI-generated baseline
│   ├── Humanized_Version.txt     # Human-like rewrite
│   ├── Detection_Results.json    # Analysis metrics
│   └── Notes.md                  # Methodology explanation
├── Task_2_Podcast_Prompts/
│   ├── Prompt_System.json        # Structured prompt framework
│   ├── Sample_Output.json        # Generated episode content
│   └── Notes.md                  # Scaling strategies
├── Task_3a_Image_Generation/
│   ├── Prompts.json              # Image generation prompts
│   ├── Image_*.png               # Generated images (if available)
│   └── Notes.md                  # Brand consistency guide
├── Task_3b_Video_Generation/
│   ├── Prompt_System.json        # Video prompt structure
│   ├── Runway_Prompts.json       # Platform-specific prompts
│   └── Notes.md                  # Production guidelines
└── Task_4_Prompt_Audit/
    ├── Original_Review.json      # System analysis
    ├── Redesigned_System.json    # Improved architecture
    └── Sample_Comparison.json    # Before/after comparison
\`\`\`

## 🛠️ Technical Highlights

### Production-Ready Features
- ✅ **Robust error handling** with graceful fallbacks
- ✅ **Modular architecture** for easy maintenance
- ✅ **Comprehensive logging** for debugging
- ✅ **Environment-based configuration**
- ✅ **Professional code organization**

### AI Integration
- ✅ **Azure OpenAI API** integration
- ✅ **Multi-model support** (GPT-4o, DALL-E-3)
- ✅ **Rate limiting** and retry logic
- ✅ **Cost optimization** strategies

## 🎯 Key Achievements

| Task | Status | Highlights |
|------|--------|------------|
| Humanization | ✅ Complete | human-like content, passes AI detection |
| Podcast System | ✅ Complete | Structured 6-minute episodes, consistent tone |
| Image Prompts | ✅ Complete | Brand-consistent visual series |
| Video Framework | ✅ Complete | Production-ready video prompt system |
| System Audit | ✅ Complete | 4-stage improvement over original GPT |

## 🔍 Code Quality

- **Type hints** for better code documentation
- **Error handling** for production reliability
- **Modular design** for scalability
- **Clean architecture** following SOLID principles
- **Comprehensive documentation**

## 🚀 Running Individual Tasks

\`\`\`bash
# Run specific task
python -c "from task1_humanization import HumanizationTask; HumanizationTask('output').execute()"

# Test Azure connection
python -c "from config import get_azure_openai_client; print('✅ Connected!' if get_azure_openai_client() else '❌ Failed')"

# Generate sample content
python main.py --task 1  # Run only Task 1
\`\`\`

## 📚 Documentation

- [Task 1: Humanization Guide](docs/task1-humanization.md)
- [Task 2: Podcast Systems](docs/task2-podcast.md)
- [Task 3: Visual Content](docs/task3-visual.md)
- [Task 4: System Optimization](docs/task4-audit.md)

## 🤝 Contributing

This is a screening test submission, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request


## 👨‍💻 Author

**Suresh Sharma**
- 💼 LinkedIn: https://www.linkedin.com/in/suresh-sharma-90942b231/
- 📧 Email: ssharma02028@gmail.com


**Built with ❤️ for the Prompt Engineer role at Perssonify**

[⭐ Star this repo](https://github.com/Sureshsharmah/Prompt-Systems-Assessment) if you found it helpful!


