/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.fatec.at2_media_aluno;


/**
 *
 * @author fatec-dsm2
 */
public class Alunos {
    //Criando atributos
    private String nome;
    private double notas[] = new double[3];
    private double media;
    
    //Criando Getters:
    public String GetNome(){
        return nome;
    }
    
    public double GetNotas(int id){
        return notas[id];
    }
    
    public double GetMedia(){
        return media;
    }
    
    //criando Setters:
    public void setNome(String nome){
        this.nome = nome;
    }
    
    public void setNotas(int notas, int id){
        this.notas[id] = notas;
    }
    
    //Criando métodos
    public double Media(){
        media = (GetNotas(0) + GetNotas(1) + GetNotas(2))/3.0;
        return media;
    }
    
}
