<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Análise de Vendas de Viagem</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #333;
      color: #fff;
      text-align: center;
      padding: 1rem 0;
    }

    h1 {
      font-size: 2rem;
    }

    .content {
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
    }

    h2 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    a {
      color: #007bff;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    pre {
      background-color: #f8f9fa;
      padding: 1rem;
      overflow-x: auto;
    }

    code {
      font-family: "Courier New", Courier, monospace;
    }
  </style>
</head>

<body>
  <header>
    <h1>Análise de Vendas de Viagem</h1>
  </header>

  <section class="content">
    <h2>Instalações necessárias</h2>
    <p>Antes de executar o projeto, é necessário instalar algumas bibliotecas Python. Você pode fazer isso
      facilmente utilizando o comando pip. Certifique-se de ter o Python instalado em seu ambiente. Caso ainda não
      tenha, você pode baixá-lo em <a href="https://www.python.org/" target="_blank">https://www.python.org/</a>.</p>

    <p>Para instalar as bibliotecas necessárias, abra um terminal ou prompt de comando e digite os seguintes comandos:
    </p>
    <pre><code>pip install pandas
pip install twilio
pip install openpyxl
    </code></pre>

    <h2>Configuração do Twilio</h2>
    <p>Para utilizar a funcionalidade de envio de SMS, você precisará ter uma conta no Twilio ou criar uma nova caso
      não possua uma. O Twilio é uma plataforma que permite o envio de mensagens de texto (SMS) e chamadas telefônicas
      programaticamente.</p>

    <p>Caso ainda não possua uma conta no Twilio, você pode criar uma acessando o link:
      <a href="https://console.twilio.com" target="_blank">https://console.twilio.com</a>.</p>

    <h2>Como funciona o projeto</h2>
    <p>O objetivo deste projeto é realizar uma análise das vendas de viagens. As bases de dados serão carregadas
      utilizando a biblioteca pandas para manipulação e processamento dos dados. Através da biblioteca openpyxl, os
      arquivos Excel serão abertos e seus conteúdos serão analisados.</p>

    <p>Além disso, será utilizada a plataforma Twilio para enviar mensagens SMS com informações relevantes sobre as
      vendas ou quaisquer outros alertas importantes.</p>

    <h2>Como executar o projeto</h2>
    <p>Para executar o projeto, siga os seguintes passos:</p>
    <ol>
      <li>Instale as bibliotecas necessárias conforme descrito na seção "Instalações necessárias".</li>
      <li>Certifique-se de ter uma conta no Twilio ou crie uma nova seguindo o link fornecido na seção "Twilio".</li>
      <li>Baixe os arquivos de base de dados em formato Excel e coloque-os em uma pasta acessível pelo projeto.</li>
      <li>Abra o código-fonte em Python e modifique-o, se necessário, para atender às suas necessidades específicas.</li>
      <li>Execute o código Python para realizar a análise das vendas e, opcionalmente, o envio de SMS via Twilio.</li>
    </ol>

    <p>Lembre-se de sempre utilizar o código de forma ética e respeitando todas as políticas do Twilio e dos provedores
      de serviços. Este projeto é apenas uma demonstração e pode ser adaptado para fins comerciais ou de aprendizado.
    </p>
  </section>

</body>

</html>

