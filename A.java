class A{
    private int a;
    private int b;
    private int c;
    private B b1 = new B(this);

    A(){
        System.out.println("A constructor called");
    }

}