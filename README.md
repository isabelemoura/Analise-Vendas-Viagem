# Análise de Vendas de Viagem

Este projeto consiste em uma Análise de Vendas utilizando a linguagem Python. Nele, serão abertas 6 bases de dados em formato Excel com o auxílio da biblioteca openpyxl, e também envios de SMS serão realizados utilizando a plataforma Twilio.

## Instalações necessárias

Antes de executar o projeto, é necessário instalar algumas bibliotecas Python. Você pode fazer isso facilmente utilizando o comando pip. Certifique-se de ter o Python instalado em seu ambiente. Caso ainda não tenha, você pode baixá-lo em [https://www.python.org/](https://www.python.org/).

Para instalar as bibliotecas necessárias, abra um terminal ou prompt de comando e digite os seguintes comandos:

```bash
pip install pandas
pip install twilio
pip install openpyxl
```

## Configuração do Twilio
Para utilizar a funcionalidade de envio de SMS, você precisará ter uma conta no Twilio ou criar uma nova caso não possua uma. O Twilio é uma plataforma que permite o envio de mensagens de texto (SMS) e chamadas telefônicas programaticamente.

Caso ainda não possua uma conta no Twilio, você pode criar uma acessando o link: https://console.twilio.com.

## Como funciona o projeto
O objetivo deste projeto é realizar uma análise das vendas de viagens. As bases de dados serão carregadas utilizando a biblioteca pandas para manipulação e processamento dos dados. Através da biblioteca openpyxl, os arquivos Excel serão abertos e seus conteúdos serão analisados.

Além disso, será utilizada a plataforma Twilio para enviar mensagens SMS com informações relevantes sobre as vendas ou quaisquer outros alertas importantes.

## Como executar o projeto

Para executar o projeto, siga os seguintes passos:

1. Instale as bibliotecas necessárias conforme descrito na seção "Instalações necessárias".
2. Certifique-se de ter uma conta no Twilio ou crie uma nova seguindo o link fornecido na seção "Twilio".
3. Baixe os arquivos de base de dados em formato Excel e coloque-os em uma pasta acessível pelo projeto.
4. Abra o código-fonte em Python e modifique-o, se necessário, para atender às suas necessidades específicas.
5. Execute o código Python para realizar a análise das vendas e, opcionalmente, o envio de SMS via Twilio.

Lembre-se de sempre utilizar o código de forma ética e respeitando todas as políticas do Twilio e dos provedores de serviços. Este projeto é apenas uma demonstração e pode ser adaptado para fins comerciais ou de aprendizado.
