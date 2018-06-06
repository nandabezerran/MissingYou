package br.ufc.missingyou.model;

import java.io.Serializable;

public class Quadro implements Serializable {

    private int foto_id;
    private String nome, local_desaparecimento;
    private String data_desaparecimento;

    public Quadro(){

    }

    public Quadro(int foto_id, String nome, String local_desaparecimento, String data_desaparecimento){
        this.foto_id = foto_id;
        this.nome = nome;
        this.local_desaparecimento = local_desaparecimento;
        this.data_desaparecimento = data_desaparecimento;
    }


    public int getFoto_id() {
        return foto_id;
    }

    public void setFoto_id(int foto_id) {
        this.foto_id = foto_id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getLocal_desaparecimento() {
        return local_desaparecimento;
    }

    public void setLocal_desaparecimento(String local_desaparecimento) {
        this.local_desaparecimento = local_desaparecimento;
    }

    public String getData_desaparecimento() {
        return data_desaparecimento;
    }

    public void setData_desaparecimento(String data_desaparecimento) {
        this.data_desaparecimento = data_desaparecimento;
    }
}
