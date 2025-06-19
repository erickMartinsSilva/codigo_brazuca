// Interface para tipagem de objetos

interface Produto {
    nome: string;
    preco: number;
    disponivel: boolean;
    categoria?: string
}

function filtrarDisponiveis(produtos: Produto[]): Produto[] {
    return produtos.filter(produto => produto.disponivel);
}

function filtrarHardware(produtos: Produto[]): Produto[] {
    return produtos.filter(produto => produto.categoria == "Hardware");
}

const produtos: Produto[] = [
    {nome: "Teclado", preco: 100, disponivel: true, categoria: "Periférico"},
    {nome: "Mouse", preco: 50, disponivel: false, categoria: "Periférico"},
    {nome: "Monitor", preco: 300, disponivel: true, categoria: "Periférico"},
    {nome: "Processador", preco: 700, disponivel: true, categoria: "Hardware"},
    {nome: "Placa de vídeo", preco: 1000, disponivel: false, categoria: "Hardware"}
];

console.log(filtrarDisponiveis(produtos));
console.log(filtrarHardware(produtos));