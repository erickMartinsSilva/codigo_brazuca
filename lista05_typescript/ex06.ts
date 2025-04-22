function buscarDados(): Promise<string> { 
    return new Promise(resolve => { 
        setTimeout(() => resolve("Dados carregados"), 5000); 
    }); 
} 
 
async function exibirDados() { 
    const dados = await buscarDados(); 
    console.log(dados); 
} 
 
exibirDados();