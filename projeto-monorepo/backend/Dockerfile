#1. Define a imagem de origem base
FROM node:24-alpine
 
#2. Define o diretório de trabalho (interno do container, que vai ficar la no Linux com esse nome mesmo)
WORKDIR /app
 
#3. Instalar o pnpm globalmente par gerenciar as depêndencias
RUN npm install -g pnpm@11.20
 
# Desativa a restrição do pnpm 11
RUN echo "strictDepBuilds: false" > pnpm-workspace.yaml
 
#4. Copia apenas o manifesto de dependências
COPY package.json ./
 
#5. Instalar as dependências do projeto
RUN pnpm install
 
#6. Copia todo o restante do código
COPY . .
 
#7. Expõem a porta padrão LDW
EXPOSE 3000
 
#8. Comando para inicializar a aplicação
CMD ["pnpm", "dev"]