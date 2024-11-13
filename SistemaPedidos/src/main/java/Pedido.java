
public class Pedido {
    private final boolean urgente; 
    private int num;
    
    // Definir constantes para los estados usando números
    public static final int PROCESANDO_PAGO = 0;
    public static final int EMPAQUETANDO = 1;
    public static final int ENVIANDO = 2;

    private int estado; // Cambia estado a int

    public Pedido(boolean urgente, int num) {
        this.urgente = urgente;
        this.estado = PROCESANDO_PAGO; //estado inicial
        this.num = num;
    }

    public boolean esUrgente() {
        return urgente;
    }

    public void setEstado(int e) {
        this.estado = e;
    }

    public int getEstado() {
        return estado;
    }

    public void setNum(int n){
        this.num = n;
    }

    public int getNum() {
        return num;
    }
    
}

