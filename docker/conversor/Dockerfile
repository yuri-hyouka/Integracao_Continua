#Imagem da Aplicação
FROM python:3.12-slim

#Diretório de trabalho
WORKDIR /app

#Copia arquivos de dependências
COPY src/requirements.txt .

#Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto
COPY src/ .

#Expõe a porta que o Flask vai rodar
EXPOSE 5000

#Comando para rodar a Aplicação
CMD [ "python", "app.py"]