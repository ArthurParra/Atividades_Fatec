/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.fatec.at2_media_aluno;
import javax.swing.JOptionPane;

/**
 *
 * @author fatec-dsm2
 */
public class AT2_media_aluno {

    public static void main(String[] args) {
        //iniciando instancia ALUNOS:
        Alunos aluno = new Alunos();
        
        //Cadastrando o nome do aluno:
        String name = JOptionPane.showInputDialog("Ola! Seja Bem Vindo(a) ao sistema de notas \n\n\n Por favor digite o nome completo do aluno");
        aluno.setNome(name);
        
        //Capturando notas do aluno:
        for(int i = 0; i < 3; i++){
        String notas = JOptionPane.showInputDialog("Digite a" + (i + 1) + " nota do aluno " + aluno.GetNome());
        int notasParseInt = Integer.parseInt(notas);
        aluno.setNotas(notasParseInt, i);
        
    }
        
        //avaliando desempenho:
        String message;
        if(aluno.Media() < 6 ){
            message = "reprovado";
        } else if(aluno.Media() >=6 && aluno.Media() <= 9) {
            message= "Aprovado";
        } else {
            message = "Aprovado com otimo aproveitamento";
        }
        
        JOptionPane.showMessageDialog(null,
                "O aluno " + aluno.GetNome() + 
                " foi " + message +
                "\n nota 1: " + aluno.GetNotas(0) + 
                "\n nota 2: " + aluno.GetNotas(1) +
                "\n nota 3: " + aluno.GetNotas(2)
                );
        
    }
}
