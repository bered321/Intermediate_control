package View;

import Model.Toy;

public class ConsoleToyView implements ToyView {
    @Override
    public void displayToy(Toy toy) {
        System.out.println("Выпал приз: " + toy.getName() + ", вес: " + toy.getWeight());
    }
}
