/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package POO;

/**
 *
 * @author fatec-dsm2
 */
public class Produto {
    private String nome;
    private double preco;
    private int quantidade;
    private String codigo;
    
    public Produto(String nome, double preco, int quantidade, String codigo){
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
        this.codigo = codigo;
    }
    
    public void exibirDetalhes(){
        System.out.println("--- DETALHES DO PRODUTO ---");
        System.out.println("Nome: " + nome);
        System.out.println("Preco: "+ preco);
        System.out.println("Quantidade: "+ quantidade);
        System.out.println("Codigo: "+ codigo);
        System.out.println("");
    }
}
