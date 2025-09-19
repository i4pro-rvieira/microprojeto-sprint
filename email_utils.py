from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def enviar_tarefas_email(tarefas, colorama=None):
    if not tarefas:
        if colorama:
            print(colorama.Fore.YELLOW + 'Nenhuma tarefa para enviar.')
        else:
            print('Nenhuma tarefa para enviar.')
        return
    if colorama:
        api_key = input(colorama.Fore.MAGENTA + 'Informe sua chave de API SendGrid: ' + colorama.Style.RESET_ALL)
        destinatario = input(colorama.Fore.MAGENTA + 'Informe o e-mail de destino: ' + colorama.Style.RESET_ALL)
        remetente = input(colorama.Fore.MAGENTA + 'Informe o e-mail remetente: ' + colorama.Style.RESET_ALL)
    else:
        api_key = input('Informe sua chave de API SendGrid: ')
        destinatario = input('Informe o e-mail de destino: ')
        remetente = input('Informe o e-mail remetente: ')
    corpo = '\n'.join([f"{i+1}. {t}" for i, t in enumerate(tarefas)])
    message = Mail(
        from_email=remetente,
        to_emails=destinatario,
        subject='Lista de Tarefas',
        plain_text_content=corpo
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        if 200 <= response.status_code < 300:
            if colorama:
                print(colorama.Fore.GREEN + 'E-mail enviado com sucesso!')
            else:
                print('E-mail enviado com sucesso!')
        else:
            if colorama:
                print(colorama.Fore.RED + f'Falha ao enviar e-mail. Código: {response.status_code}')
            else:
                print(f'Falha ao enviar e-mail. Código: {response.status_code}')
    except Exception as e:
        if colorama:
            print(colorama.Fore.RED + f'Erro ao enviar e-mail: {e}')
        else:
            print(f'Erro ao enviar e-mail: {e}')
