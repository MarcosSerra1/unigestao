function limpa_formulário_cep() {
    // Limpa valores do formulário de cep.
    document.getElementById('id_street').value = "";
    document.getElementById('id_neighborhood').value = "";
    document.getElementById('id_city').value = "";
    document.getElementById('id_state').value = "";
    document.getElementById('id_number').value = "";
}

function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        // Atualiza os campos com os valores.
        document.getElementById('id_street').value = (conteudo.logradouro);
        document.getElementById('id_neighborhood').value = (conteudo.bairro);
        document.getElementById('id_city').value = (conteudo.localidade);
        document.getElementById('id_state').value = (conteudo.uf);
    } else {
        // CEP não Encontrado.
        limpa_formulário_cep();
        window.alert("CEP não encontrado.");
    }
}

function pesquisacep() {
    var valor = document.getElementById('id_postal_code').value;
    // Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    // Verifica se campo CEP possui valor informado.
    if (cep != "") {
        // Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        // Valida o formato do CEP.
        if (validacep.test(cep)) {
            // Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('id_street').value = "...";
            document.getElementById('id_neighborhood').value = "...";
            document.getElementById('id_city').value = "...";
            document.getElementById('id_state').value = "...";

            // Cria um elemento JavaScript.
            var script = document.createElement('script');

            // Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';

            // Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } else {
            // CEP é inválido.
            limpa_formulário_cep();
            window.alert("Formato de CEP inválido.");
        }
    } else {
        // CEP sem valor, limpa formulário.
        limpa_formulário_cep();
    }
};
