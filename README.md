# CodeCraft AI 🚀

CodeCraft AI is a powerful web-based code assistant powered by Google's Gemini AI. It helps developers write, fix, and understand code more efficiently through an intuitive interface.

## 🌟 Key Features

### 1. Code Enhancement Tools

- **Code Fixing**: Automatically detects and fixes common coding errors and bugs
- **Code Completion**: Intelligently completes partial code snippets
- **Code Optimization**: Suggests improvements for better performance and readability
- **Code Explanation**: Provides clear, human-readable explanations of complex code

### 2. Multi-Language Support

Supports multiple programming languages including:

- Python
- JavaScript
- Java
- C/C++
- C#
- PHP
- HTML/CSS
- Go
- And more...

### 3. User Features

- **Secure Authentication**: User registration and login system
- **Code History**: Save and access your previous code interactions
- **Personal Dashboard**: Manage your code snippets and history
- **Responsive Interface**: Works seamlessly across desktop and mobile devices

## 🔧 Technical Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **AI Engine**: Google Gemini 1.5
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Authentication**: Django Authentication System

## 🔌 APIs & Endpoints

### External APIs

- **Google Gemini AI 1.5**
  - Used for code analysis, fixing, and generation
  - Model: `gemini-1.5-flash`
  - Capabilities: Code fixing, completion, optimization, and explanation

### Application Endpoints

#### Code Processing Endpoints

1. **Home/Code Fix** (`/`)

   - Method: `GET`, `POST`
   - Purpose: Main code fixing functionality
   - Features:
     - Code error detection and fixing
     - Multiple language support
     - Returns corrected code

2. **Code Suggestions** (`/suggest/`)
   - Method: `GET`, `POST`
   - Purpose: Advanced code assistance
   - Features:
     - Code completion
     - Code optimization
     - Code explanation
     - Multiple programming languages support

#### User Management Endpoints

1. **Authentication**

   - Login (`/login/`)

     - Method: `GET`, `POST`
     - Purpose: User authentication

   - Logout (`/logout/`)

     - Method: `POST`
     - Purpose: User session termination

   - Register (`/register/`)
     - Method: `GET`, `POST`
     - Purpose: New user registration
     - Fields: Username, Email, Password

#### Code History Management

1. **Past Codes** (`/past/`)

   - Method: `GET`
   - Purpose: View previous code interactions
   - Features:
     - Lists all past code submissions
     - Shows original code and AI responses
     - Language-specific formatting

2. **Delete Past Code** (`/delete_past_codes/<Past_id>`)
   - Method: `POST`
   - Purpose: Remove specific code entries
   - Parameter: Past_id (Code entry identifier)

#### Admin Interface

- Admin Panel (`/admin/`)
  - Purpose: Site administration
  - Features:
    - User management
    - Code entry management
    - System configuration

### Authentication Requirements

- Code history features require user authentication
- Admin interface requires superuser credentials
- Public endpoints: Home, Register, Login

## 🚀 Getting Started

1. **Clone the Repository**

```bash
git clone https://github.com/Amen-Zelealem/Code-Craft-AI
cd Code-Craft-AI
```

2. **Set Up Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Environment Variables**
   Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key
```

4. **Run Migrations**

```bash
python manage.py migrate
```

5. **Start Server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 🎯 Problem Solving

CodeCraft AI addresses several common development challenges:

1. **Debugging Efficiency**

   - Reduces time spent debugging common errors
   - Provides instant solutions to syntax issues
   - Helps identify logical errors

2. **Learning Curve**

   - Assists developers in understanding complex code
   - Provides educational explanations
   - Helps with best practices adoption

3. **Code Quality**

   - Ensures consistent code style
   - Suggests optimizations for better performance
   - Promotes clean code principles

4. **Productivity**
   - Speeds up code completion
   - Reduces repetitive coding tasks
   - Streamlines development workflow

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering the code intelligence
- Django community for the robust web framework
- All contributors who help improve the project

### Special Thanks to ALX

This project was developed as part of the **ALX Backend COHORT 4** program. Special appreciation goes to:

- **Blessing Malik** for exceptional mentorship and guidance
- All the dedicated mentors of ALX Backend COHORT 4
- The entire ALX team for creating and delivering this amazing course
- Fellow ALX learners for their support and collaboration

Your commitment to nurturing tech talent in Africa is truly inspiring! 🌍

---

Made with ❤️ by [Amen Zelealem](https://github.com/Amen-Zelealem)
