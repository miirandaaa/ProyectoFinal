
import java.util.concurrent.*;

public class GestorPedidos {
    final ExecutorService executorService; // Un solo pool de hilos
    private final PriorityBlockingQueue<Pedido> colaPedidos; 
    
    private ForkJoinPool poolEmpaquetado = new ForkJoinPool();

    // Semáforos para limitar los hilos de cada tarea
    private final Semaphore semaforo0;
    private final Semaphore semaforo1;
    private final Semaphore semaforo2;

    public GestorPedidos(int numHilos, int hilos0, int hilos1, int hilos2) {
        this.executorService = Executors.newFixedThreadPool(numHilos); // Un solo pool de hilos
        
        this.colaPedidos = new PriorityBlockingQueue<>(100, (p1, p2) -> Boolean.compare(p2.esUrgente(), p1.esUrgente()));
        //PriorityBlockingQueue<> -> crea cola de prioridad para pedidos y se procesan en un orden
        //(100 ...) -> capacidad inicial de la cola
        //(p1, p2) -> Boolean.compare(p2.esUrgente(), p1.esUrgente()) -> logica para comparar ordenes y dar prioridad

        // Inicializa los semáforos con el límite de hilos para cada tarea
        this.semaforo0 = new Semaphore(hilos0);
        this.semaforo1 = new Semaphore(hilos1);
        this.semaforo2 = new Semaphore(hilos2);
        
        iniciarProcesamiento();
    }

    public void agregarPedido(Pedido pedido) {
        colaPedidos.offer(pedido); // Inserta el pedido en la cola de prioridad
        System.out.println("Pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL") + " añadido a la cola.");
    }

    // Método que mantiene un bucle para procesar los pedidos de la cola
    private void iniciarProcesamiento() {
        executorService.submit(() -> {
            while (true) {
                try {
                    Pedido pedido = colaPedidos.take(); // Toma el siguiente pedido de la cola
                    System.out.println("Pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL") + " tomado de la cola para procesar pago.");

                    // Adquirir un permiso para procesar el pago
                    semaforo0.acquire();
                    // Procesar el pago y luego pasar al empaquetado
                    procesarPago(pedido);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break; // Sale del bucle si el hilo es interrumpido
                }
            }
        });
    }

    private void procesarPago(Pedido pedido) {
        try {
            System.out.println("Procesando pago del pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));
            Thread.sleep(1000); // Simula el procesamiento de pago
            pedido.setEstado(1);
            System.out.println("Pago procesado para el pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));

            // Liberar el permiso del semáforo de procesamiento de pago
            semaforo0.release();

            // Adquirir un permiso para empaquetar
            semaforo1.acquire();
            // Pasa el pedido al empaquetado
            empaquetarPedido(pedido);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    // private void empaquetarPedido(Pedido pedido) {
    //     try {
    //         System.out.println("Empaquetando pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));
    //         Thread.sleep(1500); // Simula el empaquetado
    //         pedido.setEstado(2);
    //         System.out.println("Pedido empaquetado " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));

    //         // Liberar el permiso del semáforo de empaquetado
    //         semaforo1.release();

    //         // Adquirir un permiso para enviar
    //         semaforo2.acquire();
    //         // Pasa el pedido al envío
    //         enviarPedido(pedido);
    //     } catch (InterruptedException e) {
    //         Thread.currentThread().interrupt();
    //     }
    // }

    private void empaquetarPedido(Pedido pedido) {
        System.out.println("Empaquetando pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));
    
        // Usa un runnable simple para empaquetar el pedido en paralelo
        poolEmpaquetado.submit(() -> {
            try {
                Thread.sleep(1500);
                pedido.setEstado(Pedido.ENVIANDO);
                System.out.println("Pedido empaquetado " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));

                semaforo1.release();
                semaforo2.acquire();
                enviarPedido(pedido);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
    }

    private void enviarPedido(Pedido pedido) {
        try {
            System.out.println("Enviando pedido " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));
            Thread.sleep(500); // Simula el envío
            System.out.println("Pedido enviado " + (pedido.getNum()) + " " + (pedido.esUrgente() ? "URGENTE" : "NORMAL"));

            // Liberar el permiso del semáforo de envío
            semaforo2.release();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public void shutdown() {
        executorService.shutdown();
        try {
            if (!executorService.awaitTermination(60, TimeUnit.SECONDS)) {
                executorService.shutdownNow();
            }
        } catch (InterruptedException e) {
            executorService.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
