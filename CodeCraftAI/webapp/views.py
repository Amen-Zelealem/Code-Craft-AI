import google.generativeai as genai
import os
from django.shortcuts import redirect, render
from django.contrib import messages
from dotenv import load_dotenv
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from huggingface_hub import User
from .forms import SignUpForm

load_dotenv()


def home(request):
    language_list = [
        "c",
        "clike",
        "cpp",
        "csharp",
        "css",
        "dart",
        "django",
        "go",
        "groovy",
        "html",
        "javascript",
        "php",
        "python",
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
        context["selected_language"] = language

        try:
            if not code:
                messages.error(request, "Please provide some code to fix")
                return render(request, "home.html", context)

            # Generate a response using Google Gemini API
            response = model.generate_content(
                f"Fix this {language} code. Return only the fixed code without any additional explanation:\n\n{code}"
            )

            # Extract AI response
            fixed_code = (
                response.text
                if hasattr(response, "text")
                else "Error: No response received."
            )
            # Clean up the response
            fixed_code = fixed_code.strip().replace("```", "").strip()
            context["fixed_code"] = fixed_code

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            context["fixed_code"] = f"Error: {str(e)}"

    return render(request, "home.html", context)


def suggest(request):
    language_list = [
        "c",
        "clike",
        "cpp",
        "csharp",
        "css",
        "dart",
        "django",
        "go",
        "groovy",
        "html",
        "javascript",
        "php",
        "python",
    ]

    context = {"language_list": language_list}

    # Configure Gemini API Key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    if request.method == "POST":
        code = request.POST.get("code", "").strip()
        language = request.POST.get("language", "").strip()
        intent = request.POST.get(
            "intent", "complete"
        )  # New: 'complete', 'optimize', or 'explain'

        if not language or language == "Select Programming Language":
            messages.error(request, "Please select a programming language")
            context["code"] = code
            return render(request, "suggest.html", context)

        context.update(
            {
                "code": code,
                "language": language,
                "selected_language": language,
                "selected_intent": intent,
            }
        )

        try:
            if not code:
                messages.error(request, "Please provide some code to analyze")
                return render(request, "suggest.html", context)

            # Generate appropriate prompt based on user intent
            if intent == "complete":
                prompt = f"""Complete this {language} code. Return only the completed code without explanations.
                Preserve the existing code and add what's needed to make it work. Here's the code:\n\n{code}"""
            elif intent == "optimize":
                prompt = f"""Optimize this {language} code. Return only the optimized code without explanations.
                Keep the same functionality but improve performance/readability. Here's the code:\n\n{code}"""
            else:
                prompt = f"""Explain this {language} code in simple terms. Provide a clear explanation.
                First show the code block, then the explanation. Code:\n\n{code}"""

            # Generate response
            response = model.generate_content(prompt)
            result = (
                response.text
                if hasattr(response, "text")
                else "Error: No response received."
            )

            # Clean up the response
            if intent in ["complete", "optimize"]:
                result = result.strip().replace("```", "").strip()
                context["suggested_code"] = result
            else:
                context["explanation"] = result

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            context["error"] = f"Error: {str(e)}"

    return render(request, "suggest.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect("home")
        else:
            messages.error(request, "Failed to Login. Please Try Again Later.")
            return redirect("home")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Registerd Successfully!")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form})
