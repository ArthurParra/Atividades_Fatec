/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.fatec.controlecaixa;

/**
 *
 * @author fatec-dsm2
 */
public class Caixa {
    private double saldo;
    
    
    //Criando o construtor:
    public Caixa(double saldo_inicial){
        this.saldo = saldo_inicial;
    }
    
    //Getter:
    public double getSaldo(){
        return saldo;
    }
    
    //Setter:
    public void setSaldo(double novo_saldo){
        this.saldo = novo_saldo;
        
    }
    
    //metodos de operação:
    public void depositar(double valor){
        String valorInput = JOptionPane.show
    }
    
    public void sacar(double valor){
        if (valor > 0 && valor <= saldo){
            saldo -= valor;
            System.out.println("Saque de R$"+ valor +" relaizado com sucesso!");
        }else{
            System.out.println("Atencao! - Saldo insuficiente/valor invalido>");
        }
    }
}
