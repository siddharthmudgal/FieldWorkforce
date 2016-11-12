package LoktraTest;

import Loktra.ReverseHashProblem;
import org.junit.Test;

import static org.junit.Assert.*;


public class ReverseHashProblemTest {
    @Test
    public void reverseHashTest() throws Exception {
        assertEquals("leepadg", ReverseHashProblem.reverseHash(680131659347L));
    }

}