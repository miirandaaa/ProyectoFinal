

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PedidoTest {

    @Test
    void testCrearPedido() {
        Pedido pedido = new Pedido(true, 1);
        assertTrue(pedido.esUrgente());
        assertEquals(1, pedido.getNum());
        assertEquals(Pedido.PROCESANDO_PAGO, pedido.getEstado());
    }

    @Test
    void testCambiarEstadoPedido() {
        Pedido pedido = new Pedido(false, 2);
        pedido.setEstado(Pedido.EMPAQUETANDO);
        assertEquals(Pedido.EMPAQUETANDO, pedido.getEstado());
        
        pedido.setEstado(Pedido.ENVIANDO);
        assertEquals(Pedido.ENVIANDO, pedido.getEstado());
    }

    @Test
    void testCambiarNumeroPedido() {
        Pedido pedido = new Pedido(false, 3);
        pedido.setNum(5);
        assertEquals(5, pedido.getNum());
    }
}
