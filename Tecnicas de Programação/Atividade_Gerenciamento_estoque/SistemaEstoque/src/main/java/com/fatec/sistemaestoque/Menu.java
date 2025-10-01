/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.fatec.sistemaestoque;
import java.util.Scanner;
import POO.Produto;

/**
 *
 * @author fatec-dsm2
 */
public class Menu {
    private Scanner scan = new Scanner(System.in);
    
    public Produto cadastrarProduto(int numero){
        
        
        System.out.println("Escreva o nome do produto "+ numero + ":");
        String nome = scan.nextLine();
        
        System.out.println("Agora, informe o preco do produto "+ numero + ": ");
        double preco = scan.nextDouble();
        
        System.out.println("Agora, informe a quantidade do produto "+ numero + ": ");
        int quantidade = scan.nextInt();
        scan.nextLine(); 
        
        System.out.println("Agora informe o codigo do produto "+ numero + " para finalizar: ");
        String codigo = scan.nextLine();
        
        return new Produto(nome, preco, quantidade, codigo);
    }
    
    public void exibirProdutos(Produto[] produtos){
        System.out.println("\n=== PRODUTOS CADASTRADOS ===\n");
        for (Produto p : produtos) {
            p.exibirDetalhes();
        }
    } 
}
