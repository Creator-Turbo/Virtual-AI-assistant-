# Virtual AI Assistant

### Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Technical Aspect](#technical-aspect)
- [Installation](#installation)
- [Run](#run)
- [Deployment on Render](#deployment-on-render)
- [Directory Tree](#directory-tree)
- [To Do](#to-do)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [License](#license)
- [Credits](#credits)

---
## Demo
This project is an interactive Virtual AI Assistant capable of responding to voice commands, answering questions, and performing basic automation tasks.<br>
**Link to Demo:** [Coming Soon](#) 

![Song Recommender](https://i.imgur.com/zpHLSGd.png)

---

## Overview
The Virtual AI Assistant leverages speech recognition, text-to-speech, and NLP (Natural Language Processing) to process and respond to user queries.

Key Capabilities:

- Speech-to-text processing

- AI-powered response generation using LLM (Large Language Models)

- Text-to-speech conversion for verbal responses

- Integration with web search for real-time answers

- Task automation (e.g., open applications, set reminders, search queries)

- Multilingual support
---

## Technical Aspect
# Features

- 🎤 Voice Input: Speak and interact with the assistant.

- 🤖 AI-Powered Responses: Uses NLP to generate meaningful responses.

- 🔊 Text-to-Speech (TTS): Converts text responses to speech.

- 🌎 Web Search Integration: Fetches real-time data.

- 📅 Basic Task Automation: Open applications, set reminders, and more.

- 🔄 Continuous Learning: Improves with user interaction.
  
---

## Installation
The Code is written in Python 3.10. Install the required packages and libraries by running:

```bash
pip install -r requirements.txt
```

## Run
To run the Flask web app locally:

```bash
python app.py
```

## Deployment on Render

To deploy the Flask web app on Render:
- Push your code to GitHub.
- Log in to Render and create a new web service.
- Connect the GitHub repository.
- Configure environment variables (if any).
- Deploy and access your app live.

## Directory Tree 
```
multilingual_assistant/
│
├── multilingual_assistant.egg-info/
├── research/
├── src/
├── static/
├── templates/
├── venv/
│
├── .env
├── .gitignore
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── speech.mp3
└── template.py
              # Main Flask application
```

## To Do

<!-- - Expand dataset for better recommendations.
- Experiment with collaborative filtering.
- Integrate user-based recommendations. -->

## Bug / Feature Request
If you encounter any bugs or want to request a new feature, please open an issue on GitHub. Contributions are welcome!

## Technologies Used
- Python: Core programming language

- Flask: Web framework for API development

- SpeechRecognition: Converts speech to text

- pyaudio: Handles microphone input

- gTTS (Google Text-to-Speech): Converts text to speech

- Google Generative AI: Powers intelligent responses

- Flask: Provides a web-based UI

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://www.techzine.eu/wp-content/uploads/2024/04/gemini-768x482.jpg" width=250>](https://pandas.pydata.org/docs/)
[<img target="_blank" src="https://media.istockphoto.com/id/1367728606/vector/conversational-ai-concept-natural-language-processing-nlp-computational-linguistics-concept.jpg?s=612x612&w=0&k=20&c=YB1PDavNi9HCRnFlhb2g5y9lhOl3CIAxbSNvZifB_F0=" width=230>](https://pandas.pydata.org/docs/)
<!-- [<img target="_blank" src="https://icon2.cleanpng.com/20180829/okc/kisspng-flask-python-web-framework-representational-state-flask-stickker-1713946755581.webp" width=170>](https://flask.palletsprojects.com/en/stable/) 
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/doc/)  -->

---

## Team
This project was developed by:
[![Bablu kumar pandey](https://github.com/Creator-Turbo/images-/blob/main/resized_image.png?raw=true)](ressume_link) |
-|

**Bablu Kumar Pandey**

- [GitHub](https://github.com/Creator-Turbo)  
- [LinkedIn](https://www.linkedin.com/in/bablu-kumar-pandey-313764286/)
- **Personal Website**: [My Portfolio](https://creator-turbo.github.io/Creator-Turbo-Portfolio-website/)

## License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software under the terms of the MIT License. For more details, see the [LICENSE](LICENSE) file included in this repository.

## Credits

We are using Gemini Pro from Google Generative AI to enhance the capabilities of our AI Assistant
