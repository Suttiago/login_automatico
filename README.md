# 📜 Automação de Download do Histórico Escolar  

Este projeto automatiza o acesso ao portal da **UNIPAR** (ou de qualquer outra faculdade), realizando o login, baixando o **histórico escolar** do aluno e enviando-o por **e-mail** automaticamente.  

⚡ **Ideal para quem deseja obter seu histórico sem precisar acessá-lo manualmente sempre!**  

---

## 🛠️ Tecnologias Utilizadas  

- **Python** 🐍  
- **Selenium** (para automação do navegador)  
- **PyAutoGUI** (para navegação em menus específicos, mapeando o mouse)  
- **BeautifulSoup** (para extração de informações, se necessário)  
- **SMTP (smtplib)** (para envio de e-mail)  
- **dotenv** (para armazenar credenciais com segurança)  

---

## 📌 Pré-requisitos  

Antes de rodar o script, você precisará:  

✅ **Ter o Python instalado** (3.x recomendado)  
✅ **Instalar os pacotes necessários** (listados abaixo)  
✅ **Ter o Google Chrome + ChromeDriver instalado** (ou outro navegador compatível)  
✅ **Uma conta de e-mail configurada para envio automático**  

---

## 📥 Instalação  

### 1️⃣ Clone o repositório  
```bash
git clone https://github.com/seu-usuario/automacao-historico-unipar.git
cd automacao-historico-unipar
```

### 2️⃣ Crie um ambiente virtual (opcional, mas recomendado)  
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3️⃣ Instale as dependências  
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure suas credenciais  

Crie um arquivo **`.env`** na raiz do projeto e adicione:  
```env
UNIPAR_USERNAME=seu_usuario
UNIPAR_PASSWORD=sua_senha
EMAIL_REMETENTE=seuemail@gmail.com
EMAIL_SENHA=sua_senha_do_email
EMAIL_DESTINO=seuemail@gmail.com
```
⚠️ **Use senhas de aplicativos caso seu e-mail exija autenticação em duas etapas.**  

---

## 🚀 Como Usar  

### 1️⃣ Execute o script principal:  
```bash
python main.py
```

### 2️⃣ O script irá:  
✅ Abrir o navegador e acessar o portal da **UNIPAR**  
✅ Fazer **login automaticamente**  
✅ Navegar até a página do **histórico escolar**  
✅ Baixar o **PDF** do histórico  
✅ **Enviar o histórico por e-mail**  

### 3️⃣ **Pronto!** 🎉 O histórico escolar chegará no seu e-mail!  

---

## 📝 Configurações Adicionais  

🔹 **Alterar navegador:** Modifique o WebDriver no código para usar **Firefox, Edge, etc.**  
🔹 **Mudar provedor de e-mail:** Caso não use **Gmail**, adapte o SMTP para **Outlook, Yahoo, etc.**  
🔹 **Agendar execução automática:** Use o **Task Scheduler** (Windows) ou **cron** (Linux/Mac) para rodar o script periodicamente.  

---

## ❓ Problemas Comuns  

🔸 **O ChromeDriver está desatualizado?**  
→ Atualize baixando a versão correta [aqui](https://chromedriver.chromium.org/downloads).  

🔸 **Login falhou?**  
→ Verifique seu **usuário/senha** e possíveis **mudanças no portal da UNIPAR**.  

🔸 **O e-mail não foi enviado?**  
→ Confirme que as permissões de envio de e-mail estão ativadas no seu provedor.  

---

## 📜 Licença  

Este projeto está licenciado sob a **MIT License** - sinta-se livre para usá-lo e modificá-lo.  

---

## 👨‍💻 Autor  

**Desenvolvido por Tiago de lima Barbieri Sversut**  
📧 **Contato:** tiagobsversut@gmail.com  
