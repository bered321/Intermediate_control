package Model;



public class Toy {
    private int id;
    private String name;
    private int weight;
    private int quantity;

    public Toy(int id, String name, int weight, int quantity) {
        this.id = id;
        this.name = name;
        this.weight = Math.min(weight, 100);
        this.quantity = quantity;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = Math.min(weight, 100);
    }

    public int getQuantity() {
        return quantity;
    }

    public void decreaseQuantity() {
        if (quantity > 0) {
            quantity--;
        }
    }
}

