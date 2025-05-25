def highlight_keywords(response):
    keywords = {
        "CGPA": "**CGPA**",
        "backlogs": "**backlogs**",
        "placement portal": "**placement portal**",
        "results": "**results**",
        "procedure": "**procedure**",
        "registration": "**registration**",
        "interview": "**interview**",
        "deadline": "**deadline**",
        "updates": "**updates**"
    }
    for word, highlight in keywords.items():
        response = response.replace(word, highlight)
    return response
