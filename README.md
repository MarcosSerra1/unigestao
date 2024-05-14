# Uni Gestão

Uni Gestão é uma aplicação web desenvolvida em Django para gerenciamento de funcionários. Permite registrar, visualizar, editar e excluir informações de funcionários, como nome, e-mail, CPF, dados de contato, endereço e detalhes de pagamento.

## Funcionalidades

- Registro de novos funcionários com informações detalhadas.
- Visualização de todos os funcionários cadastrados.
- Edição e exclusão de informações de funcionários existentes.
- Gestão de dados de contato, endereço e pagamento de funcionários.

## Instalação

1. Certifique-se de ter o Python instalado. Você pode baixá-lo em https://www.python.org/.
2. Clone este repositório para o seu ambiente local.
3. Navegue até o diretório do projeto no terminal.
4. Crie um ambiente virtual:

    ```
    python -m venv venv
    ```

5. Ative o ambiente virtual:

    - No Windows:

    ```
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```
    source venv/bin/activate
    ```

6. Instale as dependências do projeto:

    ```
    pip install -r requirements.txt
    ```

7. Execute as migrações do Django para criar o banco de dados:

    ```
    python manage.py migrate
    ```

8. Inicie o servidor:

    ```
    python manage.py runserver
    ```

9. Acesse a aplicação em seu navegador em http://localhost:8000.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações de recebimento.

## Autor

Marcos Serra

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
