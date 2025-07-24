## ⚡️ API REST async com Python, Quart, SQLModel e Pytest

## 👨🏻‍💻 Como rodar a aplicação?

### **1. Intele o UV, gerenciador de pacotes/ambiente utilizado no projeto:**

**Comando(Linux):** `curl -LsSf https://astral.sh/uv/install.sh | sh`

**Comando(Windows):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`


### **2. Crie um ambiente virtual para isolar as dependências do projeto:**

**Comando:** `uv venv .venv`

### **3. instale as dependências do projeto:**

**Comando:** `uv sync --all-groups` ou `uv pip install -r requirements.txt`

### **4. Ative o ambiente no terminal(opcional):**

**Comando(Linux):** `source .venv/bin/activate`

**Comando(Windows):** `.\.venv\Scripts\activate.ps1`

**obs:** Caso opte por não ativar o ambiente os comandos das dependências precisam de um "uv run" antes do comando para funcionar **(Ex: uv run pytest)**.

Mais informações sobre o UV na <a href="https://docs.astral.sh/uv/">Documentação</a>.

### **5. Comando para rodar a aplicação:**

**comando(Linux):** `uv run python3 main.py`

**comando(Windows):** `uv run python main.py`

Alternativa seguindo a documentação do framework <a href="https://quart.palletsprojects.com/en/latest/">Quart</a>:

```Python
$ export QUART_APP=main:app
$ quart run

```

---