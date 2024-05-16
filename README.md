<h1 align="center"> Uni Gestão </h1>

<p align="center"> :construction: Projeto em construção :construction: </p>

Uni Gestão é uma aplicação web que está sendo desenvolvida em Django para gerenciamento de funcionários. Permite registrar, visualizar, editar e excluir informações de funcionários, como nome, e-mail, CPF, dados de contato, endereço e detalhes de pagamento.

## :hammer: Funcionalidades do projeto

- `Cadastro de funcionários`: Registro de novos funcionários com informações detalhadas.
    - Endereço;
    - Pix;
    - Contato.
- `Tela de visualização`: Visualização de todos os funcionários cadastrados.
- `Tela de edição`:
    - Edição;
    - Exclusão de informações de funcionários existentes;
    - Exclusão de funcionários.

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


## Autores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/78652932?v=4" width=115><br><sub>Marcos Serra</sub>](https://github.com/MarcosSerra1) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/167050569?v=4" width=115><br><sub>Levi Maycom</sub>](https://github.com/guilhermeonrails) |
| :---: | :---: |

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
