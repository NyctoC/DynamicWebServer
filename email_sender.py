from mailersend import emails
import pandas as pd
import base64
import os


def generar_y_enviar_reporte():
    api_key = os.environ['MAILERSENDAPI']

    mailer = emails.NewEmail(api_key)

    # define an empty dict to populate with mail values
    mail_body = {}

    mail_from = {
        "name": "Cristian Sender Testing",
        "email": "info@test-2p0347zqwr3lzdrn.mlsender.net",
    }

    recipients = [{
        "name": "Cristian Cardenas",
        "email": "camilocardenas2705@gmail.com",
    }]

    # Generar DataFrame de ejemplo
    df = pd.DataFrame({"Fecha": ["2025-07-10"], "Precio": [192.45]})
    # Guardar Excel
    nombre_archivo = "reporte_diario.xlsx"
    df.to_excel(nombre_archivo, index=False)

    # Codificar a base64
    with open(nombre_archivo, "rb") as file:
        contenido_base64 = base64.b64encode(file.read()).decode()

    attachments = [{
        "content": contenido_base64,
        "disposition": "attachment",
        "filename": nombre_archivo
    }]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Hello!", mail_body)
    mailer.set_html_content("This is the HTML content", mail_body)
    mailer.set_plaintext_content("This is the text content", mail_body)
    mailer.set_attachments(attachments, mail_body)
    #mailer.set_reply_to(reply_to, mail_body)

    # using print() will also return status code and data
    print(mailer.send(mail_body))
