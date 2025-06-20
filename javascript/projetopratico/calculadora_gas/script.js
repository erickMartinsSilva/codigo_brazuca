var contador = 0; // conta quantas transações foram simuladas na sessão atual
const historico = document.getElementById('historico');
const historicoh2 = document.getElementById('historico-h2');

function adicionarAoHistorico(resultado) { // adiciona uma transação ao histórico quando for simulada
    let entrada = document.createElement('div'); // cria uma nova entrada no histórico

    historico.classList.remove('oculto'); // exibe as divs historico e historico-h2
    historicoh2.classList.remove('oculto');
    
    entrada.innerHTML = resultado.innerHTML; // define o html da nova entrada

    historico.appendChild(entrada); // adiciona a nova entrada ao histórico
};

function limparHistorico() { 
    while(historico.firstChild) { // remove o primeiro nó filho enquanto houver nós filhos
        historico.removeChild(historico.firstChild);
    }

    historico.classList.add('oculto'); // oculta as divs historico e historico-h2
    historicoh2.classList.add('oculto');
};

function temporizador() { 
    let intervalo = null;
    let segundos = 0;

    intervalo = setInterval(() => { // temporizador em segundos
        segundos++;
        console.log(segundos);
        if(segundos % 60 == 0) { // limpa o histórico a cada minuto
            limparHistorico();
        } 
    }, 1000)
};

temporizador();

document.getElementById('calcular').addEventListener('click', function() {
    // obtém valores do index.html
    let valorTransacao = parseFloat(document.getElementById('valor-transacao').value);
    let moeda = document.getElementById('moeda').value;
    let complexidade = document.getElementById('complexidade').value;
    let resultado = document.getElementById('resultado');
    let precoGas;

    switch(complexidade) { // define preço do gas com base na complexidade
        case 'baixa':
            precoGas = 0.01; break;
        case 'media':
            precoGas = 0.05; break;
        case 'alta':
            precoGas = 0.1; break;
    }

    let custoGas = valorTransacao * precoGas;

    resultado.classList.remove('oculto');
    if (valorTransacao > 0) { // calcula custo do gas se o valor da transação foi maior que 0
        resultado.innerHTML = `
            <p>Valor da Transação: ${valorTransacao} $${moeda.toUpperCase()}</p>
            <p>Complexidade: ${complexidade.charAt(0).toUpperCase() + complexidade.slice(1)}</p>
            <p><strong>Custo Estimado do Gas: ${custoGas.toFixed(2)} $${moeda.toUpperCase()}</strong></p>
        `;
        contador += 1;
        document.getElementById('contador').innerHTML = `
            <p>Transações simuladas nesta sessão: ${contador}</p>
        `;
        adicionarAoHistorico(resultado);
    } else { // se o valor da transação for 0 ou negativo, uma mensagem de erro é exibida na tela
        resultado.innerHTML = '<p class="erro">Por favor, insira um valor de transação válido.</p>';
    }
});