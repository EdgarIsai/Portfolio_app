from django.shortcuts import render
from projects.models import Project
from django.conf import settings

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.


def project_index(request):
    
    if request.method == "POST" and request.POST["message"]:
        user_info = {
            "first_name":request.POST["first_name"],
            "last_name":request.POST["last_name"],
            "mail":request.POST["mail"],
            "message":request.POST["message"]
        }

        message = MIMEMultipart("alternative")
        message["Subject"] = "Contact Form Entry"
        message["From"] = settings.SENDER_MAIL
        message["To"] = settings.RECEIVER_MAIL

        text = f"""\
            {user_info["first_name"]} {user_info["last_name"]}
            E-mail: {user_info["mail"]}
            
            {user_info["message"]}"""

        html = f"""\
        <html>
            <body>
                <h2>{user_info["first_name"]} {user_info["last_name"]}<h2>
                <h3>E-mail: {user_info["mail"]}</h3>
                <br>
                <p>{user_info["message"]}</p>
            </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
                            settings.SMTP_SERVER,
                            settings.PORT, 
                            context=context,
                            ) as server:
            server.login(settings.SENDER_MAIL, settings.PASSWORD)
            server.sendmail(
                settings.SENDER_MAIL,
                 settings.RECEIVER_MAIL,
                  message.as_string()
            )

    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
