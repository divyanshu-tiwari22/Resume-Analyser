# 📄 CV Assessor

An AI-powered resume analysis tool that provides intelligent feedback on your CV using advanced language models. Upload your resume and get comprehensive analysis on content clarity, skills presentation, and targeted improvement suggestions for specific job roles.

---

## 🔗 Live Link :- https://ai-resume-analyser-dgz8.onrender.com/

---

## ✨ Features

- **📤 PDF & Text Upload**: Support for both PDF and plain text resume formats
- **🤖 AI-Powered Analysis**: Leverages Groq's Llama 3.1 8B model for intelligent resume evaluation
- **💼 Job-Specific Feedback**: Tailor analysis to specific job roles you're targeting
- **📊 Structured Analysis**: Clear, organized feedback covering:
  - Content clarity and impact
  - Skills presentation effectiveness
  - Specific improvement recommendations
- **⚡ Real-Time Processing**: Fast analysis powered by Groq API
- **🎨 User-Friendly Interface**: Built with Streamlit for an intuitive experience
- **🔒 Environment-Based Configuration**: Secure API key management using `.env` files

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.13+ |
| **AI Model** | Groq API (Llama 3.1 8B Instant) |
| **PDF Processing** | PyPDF2 |
| **API Client** | Groq Python SDK |
| **Environment Management** | python-dotenv |
| **Package Manager** | UV (with Poetry support) |

### Dependencies
- **groq** (≥0.37.1): Groq API client for LLM integration
- **streamlit**: Web app framework
- **PyPDF2**: PDF text extraction
- **python-dotenv**: Environment variable management

---

## 📋 Prerequisites

Before you begin, ensure you have:

1. **Python 3.13** or higher installed ([Download Python](https://www.python.org/downloads/))
2. **Git** for version control ([Download Git](https://git-scm.com/))
3. **Groq API Key** - Get it free at [Groq Console](https://console.groq.com/keys)
4. **pip** or **uv** package manager (uv recommended for faster installation)

### System Requirements
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: ~500MB for dependencies

---

## 🚀 Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/divyanshu-tiwari22/Resume-Analyser.git
cd Resume-Analyser
```

### 2. Create a Virtual Environment (Recommended)

**Using venv:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**Using uv (faster alternative):**
```bash
uv venv
```

### 3. Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv:**
```bash
uv sync
```

Or install packages individually:
```bash
pip install groq>=0.37.1 streamlit PyPDF2 python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# On Windows (Command Prompt)
copy .env.example .env

# On macOS/Linux
cp .env.example .env
```

Or manually create `.env` with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ **Important**: Never commit your `.env` file to version control. It's already listed in `.gitignore`.

### 5. Verify Installation

```bash
python -c "import streamlit; import groq; print('✓ All dependencies installed successfully!')"
```

---

## 💻 Usage Instructions

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`

### Step-by-Step Usage

1. **Upload Your Resume**
   - Click "Browse files" button
   - Select a PDF or TXT file containing your resume
   - Supported formats: `.pdf`, `.txt`

2. **Enter Target Job Role (Optional)**
   - Type the job title you're applying for (e.g., "Data Scientist", "Frontend Developer")
   - This personalizes the analysis to the specific role
   - Leave blank for general application feedback

3. **Analyze Resume**
   - Click the "Analyse Resume" button
   - Wait for the AI to process and generate feedback
   - Typical processing time: 5-15 seconds

4. **Review Recommendations**
   - Read through the structured analysis
   - Focus on the specific improvement suggestions
   - Tailor your resume based on the feedback

### Example Output

```
### Resume Analysis:

**Content Clarity and Impact**
- Your resume effectively communicates your professional experience
- Consider using action verbs to strengthen impact statements

**Skills Presentation**
- Technical skills are well-organized
- Recommend quantifying skill proficiency levels

**Recommendations for Data Scientist Role**
- Add specific metrics from ML projects
- Include relevant frameworks (TensorFlow, PyTorch, Scikit-learn)
- Highlight experience with data visualization tools
```

---

## 🤝 Contributing Guidelines

We welcome contributions from the community! Here's how you can help:

### Getting Started

1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Resume-Analyser.git
   cd Resume-Analyser
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # Examples:
   # git checkout -b feature/add-docx-support
   # git checkout -b feature/improve-analysis
   # git checkout -b fix/pdf-parsing-issue
   ```

### Development Workflow

4. **Make Your Changes**
   - Write clean, readable code
   - Add comments for complex logic
   - Follow Python PEP 8 style guide
   - Test your changes locally

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   # Use clear commit messages:
   # ✓ "Add support for DOCX file format"
   # ✗ "fixed stuff"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Provide a clear description of your changes
   - Reference any related issues

### Contribution Ideas

- **Features**:
  - Add support for DOCX/DOC file formats
  - Implement batch resume analysis
  - Add export functionality (PDF reports)
  - Support for multiple languages
  - Alternative AI model options

- **Improvements**:
  - Enhance PDF text extraction accuracy
  - Optimize processing speed
  - Improve UI/UX design
  - Add error handling

- **Documentation**:
  - Add API documentation
  - Create video tutorials
  - Improve inline code comments
  - Add deployment guides

### Code Standards

- **Python Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- **Docstrings**: Add docstrings to functions and classes
- **Testing**: Test your changes before submitting
- **Commits**: Write descriptive commit messages

### Reporting Issues

- **Bug Reports**: Include steps to reproduce, expected vs actual behavior
- **Feature Requests**: Explain the use case and expected behavior
- **Questions**: Use GitHub Discussions for general questions


---

## 🙋 Support & Feedback

- **Issues**: [Report bugs or request features](https://github.com/divyanshu-tiwari22/Resume-Analyser/issues)
- **Discussions**: [Join community discussions](https://github.com/divyanshu-tiwari22/Resume-Analyser/discussions)
- **Email**: Contact the maintainers via GitHub

---

## 🔗 Useful Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API Documentation](https://console.groq.com/docs)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

## ⭐ Show Your Support

If you find this project helpful, please consider:
- Starring the repository ⭐
- Sharing with others 📢
- Contributing improvements 🚀

---

**Happy resume analyzing! 🎉**
