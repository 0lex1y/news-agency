from datetime import datetime


def year_context(request):
    return {"now": datetime.now()}
