<h1>Listagem de Bicicletas </h1>
    <ul>                

%for bicicleta in bicicletas:
        <li>Cor: {{bicicleta.cor}},
         Modelo: {{bicicleta.modelo}}, 
         Ano: {{bicicleta.ano}}, 
         Valor: {{bicicleta.valor}}
%end
    </ul>
    % include('botao', texto_botao='Voltar' , url_rota='/')