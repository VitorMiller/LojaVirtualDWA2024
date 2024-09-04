from fastapi import APIRouter

from dtos.novo_produto_dto import InserirProdutoDTO
from dtos.excluir_produto_dto import ExcluirProdutoDTO
from models.produto_model import Produto
from repositories.produto_repo import ProdutoRepo

router = APIRouter(prefix="/manager")

@router.get("/obter_produtos")
async def obter_produtos():
    produtos = ProdutoRepo.obter_todos()
    return produtos

@router.post("/inserir_produto")
async def inserir_produtos(produto:InserirProdutoDTO) -> Produto:
    novo_produto = Produto(None, produto.nome, produto.preco, produto.descricao, produto.estoque)
    novo_produto = ProdutoRepo.inserir(novo_produto)
    return novo_produto

@router.post("/excluir_produto")
async def excluir_produtos(id_produto:ExcluirProdutoDTO) :
    if ProdutoRepo.excluir(id_produto.id):
        return ("Produto excluído")
    else:
        return ("Não excluído")