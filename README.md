# LangChain Learning Repository

This repository contains code examples and implementations based on the [Generative AI using LangChain](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) YouTube playlist by [CampusX](https://www.youtube.com/@campusx-official).

## About This Repository

This is a consolidated collection of code examples from the CampusX LangChain tutorial series. While the original tutorials use separate repositories for each video, this repository combines them into a single, organized project for easier reference and learning.

Key modifications from the original code:
- Added additional comments and documentation
- Modified examples to use Grok instead of OpenAI 
- Reorganized structure for better navigation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/notAvailable73/Langchain-Journey.git
cd Langchain-Journey
```

2. **Create and activate a virtual environment**

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Setting up API Keys

Create a `.env` file in the root directory of the project and add your API key(s):

```
GROK_API_KEY=your_grok_api_key 
```
 

## Running Examples

Navigate to the specific example directory and run the Python file:

```bash 
python '.\4. Chains\4_conditional_chain.py'
```

## Requirements

The main requirements for this project are listed in `requirements.txt` and include:

- langchain
- grok-api (or alternative for Grok integration)
- python-dotenv
- pandas
- numpy
- scikit-learn
- transformers
- torch
- other dependencies as needed

## Learning Resources

- [Generative AI using LangChain Playlist](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) by CampusX
- [LangChain Official Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [Grok API Documentation](https://platform.openai.com/docs/api-reference)

## Contributing

Feel free to submit pull requests or open issues if you find bugs or have suggestions for improvements.
 

## Acknowledgments

- Thanks to [CampusX](https://www.youtube.com/@campusx-official) for the excellent tutorial series
- LangChain team for developing the framework
- The AI/ML community for continuous knowledge sharing

---

**Note:** This repository is for educational purposes and personal learning. It is not affiliated with or endorsed by CampusX.