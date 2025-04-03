import google.generativeai as genai
import os
from django.shortcuts import render
from django.contrib import messages
from dotenv import load_dotenv


load_dotenv()

def home(request):
    language_list = [
        "c", "clike", "cpp", "csharp", "css", "csv", "dart", "django",
        "go", "groovy", "javascript", "markup", "markup-templating", "php", "python",
    ]
    
    context = {"language_list": language_list}
    
    # Configure Gemini API Key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    if request.method == "POST":
        code = request.POST.get("code", "").strip()
        language = request.POST.get("language", "").strip()

        if not language or language == "Select Programming Language":
            messages.error(request, "Please select a programming language")
            context["code"] = code
            return render(request, "home.html", context)
        
        context["code"] = code
        context["language"] = language
        context["selected_language"] = language  # For keeping the selected option
        
        try:
            if not code:
                messages.error(request, "Please provide some code to fix")
                return render(request, "home.html", context)
                
            # Generate a response using Google Gemini API
            response = model.generate_content(
                f"Fix this {language} code. Return only the fixed code without any additional explanation:\n\n{code}"
            )
            
            # Extract AI response
            fixed_code = response.text if hasattr(response, "text") else "Error: No response received."
            # Clean up the response
            fixed_code = fixed_code.strip().replace("```", "").strip()
            context["fixed_code"] = fixed_code
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            context["fixed_code"] = f"Error: {str(e)}"
    
    return render(request, "home.html", context)

