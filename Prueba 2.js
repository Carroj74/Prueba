// Función para sumar los cuadrados de los dígitos de un número
    public static int sumarCuadradosDigitos(int n) {
        int suma = 0;
        while (n > 0) {
            int digito = n % 10;
            suma += digito * digito;
            n /= 10;
        }
        return suma;
    }
    
    // Función para verificar si un número es feliz
    public static boolean esFeliz(int n) {
        int happy = n;  // Mueve una vez
        int infinite = n;   // Mueve dos veces

        do {
            happy = sumarCuadradosDigitos(happy);
            infinite = sumarCuadradosDigitos(sumarCuadradosDigitos(infinite));

            if (happy == 1 || infinite == 1) {
                return true;  // El número es feliz
            }
        } while (happy != infinite);

        return false;  // Se ha detectado un ciclo infinito
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numero = scanner.nextInt();
        
        if (numero > 0) {
            if (esFeliz(numero)) {
                System.out.println(numero + " es un número feliz.");
            } else {
                System.out.println(numero + " no es un número feliz.");
            }
        } else {
            System.out.println("Debe ingresar un número entero positivo");
        }
    }