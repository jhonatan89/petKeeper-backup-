from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def send_petkeeper_email(context, email, template):
    template_html = get_template(template)
    subject, from_email, to = 'Confirmacion PetKeeper', 'PetKeeper <petkeeper.services@gmail.com>', email
    ctx = Context(context)
    html_content = template_html.render(ctx)
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=from_email,
        to=[to],
        headers={"Reply-To": "support@sendgrid.com"})
    msg.attach_alternative(html_content, "text/html")
    msg.send()