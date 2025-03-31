from django.shortcuts import render
from django.contrib import messages


def home(request):
    language_list = [
        "c",
        "clike",
        "cpp",
        "csharp",
        "css",
        "csv",
        "dart",
        "django",
        "go",
        "groovy",
        "javascript",
        "json",
        "json5",
        "markup",
        "markup-templating",
        "mongodb",
        "nginx",
        "php",
        "powershell",
    ]
    if request.method == "POST":
        code = request.POST.get("code", "")
        language = request.POST.get("language", "")

        if language == "Select Programming Language":
            messages.success(request, "Please Pick a Programming Language")
        return render(
            request,
            "home.html",
            {"language_list": language_list, "code": code, "language": language},
        )

    return render(
        request,
        "home.html",
        {"language_list": language_list, "code": code, "language": language},
    )
