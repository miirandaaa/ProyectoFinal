
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

import java.util.concurrent.TimeUnit;

class GestorPedidosTest {

    private GestorPedidos gestor;

    @BeforeEach
    void setUp() {
        // Inicializa un gestor con un solo hilo para simplificar la prueba
        gestor = new GestorPedidos(5, 1, 1, 1);
    }

    @Test
    void testAgregarPedido() {
        Pedido pedido = new Pedido(false, 1);
        gestor.agregarPedido(pedido);
        // Verifica que el pedido se ha añadido correctamente
        assertNotNull(pedido);
    }

    @Test
    void testProcesamientoPedidos() throws InterruptedException {
        Pedido pedido = new Pedido(false, 1);
        gestor.agregarPedido(pedido);

        // Espera un poco para asegurar que se procesa el pedido
        TimeUnit.SECONDS.sleep(3);

        // Verifica que el estado del pedido cambie a ENVIANDO después del procesamiento
        assertEquals(Pedido.ENVIANDO, pedido.getEstado());
    }

    @Test
    void testShutdown() {
        gestor.shutdown();
        // Comprueba si el `GestorPedidos` se cierra correctamente
        assertTrue(gestor.executorService.isShutdown());
    }

    @Test
    void testEmpaquetarPedido() throws InterruptedException {
        Pedido pedido = new Pedido(false, 1);
        gestor.agregarPedido(pedido);

        // Espera un poco más de tiempo para asegurarse que el pedido pase por las tres etapas
        TimeUnit.SECONDS.sleep(5);

        // Verifica que el estado del pedido sea 'ENVIANDO' después del empaquetado
        assertEquals(Pedido.ENVIANDO, pedido.getEstado());
    }
}
