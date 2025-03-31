from django.shortcuts import render


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
    # print(sorted(language_list))
    return render(request, "home.html", {'language_list':language_list})
