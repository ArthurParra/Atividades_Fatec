/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.fatec.controlecaixa;
import java.util.Scanner;
/**
 *
 * @author fatec-dsm2
 */
public class ControleCaixa {

    public static void main(String[] args) {
        Scanner input = new  Scanner(System.in);
        Caixa caixa = new Caixa(0.0);
        
        int opcao;
        
        do{
            System.out.println("\n==== Controle de Caixa ====\n");
            System.out.println("1 - Consultar Saldo ");
            System.out.println("2 -  Depositar");
            System.out.println("3 - Sacar");
            System.out.println("0 - Sair");
            System.out.println("Digite a Opcao desejada: ");
            opcao = input.nextInt();
            
            switch(opcao){
                case 1:
                    System.out.println("Seu Saldo atual é de R$"+ caixa.getSaldo());
                    break;
                case 2:
                    System.out.println("Informe o valor do Deposito: ");
                    double deposito = input.nextDouble();
                    caixa.depositar(deposito);
                    break;
                case 3:
                    System.out.println("Informe o valor do Saque: ");
                    double saque = input.nextDouble();
                    caixa.sacar(saque);
                    break;
                case 0:
                    System.out.println("Encerrando o Sistema... ");
                    break;
                default:
                    System.out.println("Operacao Invalida!");
                    break;
            }
        } while (opcao != 0);
        
        input.close();
    }
}
