/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.fatec.sistemaestoque;
import POO.Produto;


/**
 *
 * @author fatec-dsm2
 */
public class SistemaEstoque {

    public static void main(String[] args) {
        System.out.println("\n=== BEM-VINDO(A) AO GERENCIADOR DE ESTOQUE ===\n");
        System.out.println("____________________________________________________");
        System.out.println("");
        
        Menu menu = new Menu();
        Produto[] produtos = new Produto[3];
        
        for (int i = 0 ;i < 3; i++){
        produtos[i] = menu.cadastrarProduto(i + 1);
    }
        
        menu.exibirProdutos(produtos);
    }
}
