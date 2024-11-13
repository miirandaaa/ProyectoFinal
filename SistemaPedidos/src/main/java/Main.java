
public class Main {
    public static void main(String[] args) {
        //GestorPedidos gestor = new GestorPedidos(10); // Crea un gestor con 10 hilos

        GestorPedidos gestor = new GestorPedidos(10,3,4,3);

        long startTime = System.nanoTime();

        // Añade algunos pedidos normales y urgentes
        for (int i = 0; i < 20; i++) {
            boolean urgente = i % 5 == 0; // Cada 5 pedidos será un pedido urgente
            Pedido pedido = new Pedido(urgente,i);
            gestor.agregarPedido(pedido);
        }

        // Cierra el sistema de manera ordenada
        gestor.shutdown();

        long endTime = System.nanoTime();

        long duration = (endTime - startTime) / 1_000_000; // Convertir a milisegundos
        System.out.println("Tiempo total de ejecución: " + duration + " ms");
    }
}
