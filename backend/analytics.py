from models import Application

def generate_trends(user_id):
    applications = Application.query.filter_by(user_id=user_id).all()
    trends = {
        "total_applications": len(applications),
        "decluttered_count": len([app for app in applications if app.status == "No"]),
        "success_rate": len([app for app in applications if app.status == "Yes"]) / len(applications) * 100 if applications else 0
    }
    return trends
