# IRIS Chatbot

## Overview

IRIS (Interface de Reconhecimento e Informação Sistematizada) is a Portuguese-language chatbot application built with Flask and powered by Google's Gemini AI. The system provides an intelligent conversational interface through a web-based chat interface, designed to answer questions in a friendly and contextual manner in Brazilian Portuguese.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template-based rendering**: Uses Flask's template system with Jinja2 templating engine
- **Single-page chat interface**: HTML/CSS/JavaScript interface located in `templates/index.html`
- **Responsive design**: Modern CSS with gradient backgrounds and responsive layout
- **Real-time chat interface**: Client-side JavaScript for dynamic message handling

### Backend Architecture
- **Flask web framework**: Lightweight Python web application using Flask 3.0.0
- **Factory pattern**: Application created using `create_app()` factory function in `src/app.py`
- **Modular structure**: Separated application logic from entry point (`run.py`)
- **Environment-based configuration**: Uses python-dotenv for environment variable management

### AI Integration
- **Google Gemini AI**: Primary AI service using `google-genai` library version 0.8.0
- **Conversation context**: Maintains conversation history in memory (last 5 exchanges)
- **Portuguese language optimization**: System prompt specifically designed for Brazilian Portuguese responses
- **Error handling**: Basic exception handling for AI service failures

### Data Storage
- **In-memory storage**: Conversation history stored in application memory using Python lists
- **No persistent database**: Current implementation uses temporary storage (suitable for development/small scale)
- **Session-based conversations**: No user authentication or persistent sessions

### Production Configuration
- **Gunicorn WSGI server**: Production-ready server configuration with 2 sync workers
- **Process management**: Configured with proper timeouts, logging, and worker recycling
- **Scalability settings**: Worker connections (1000), max requests (1000), and jitter configuration

## External Dependencies

### AI Services
- **Google Gemini API**: Core AI functionality through `google-genai` library
- **API Key requirement**: Requires `GEMINI_API_KEY` environment variable

### Python Packages
- **Flask 3.0.0**: Web framework for HTTP handling and routing
- **google-genai 0.8.0**: Google's Generative AI client library
- **python-dotenv 1.1.1**: Environment variable management
- **Gunicorn 21.2.0**: WSGI HTTP server for production deployment

### Development Dependencies
- **Python 3.8+**: Minimum Python version requirement
- **Virtual environment**: Recommended for dependency isolation

### Infrastructure Requirements
- **Environment variables**: Requires proper configuration of AI API keys
- **Network access**: Requires internet connectivity for Gemini API calls
- **Memory considerations**: In-memory conversation storage limits scalability