package Presenter;

import Model.Toy;
import View.ToyView;

import java.io.FileWriter;
import java.io.IOException;
import java.util.*;




public class ToyPresenter {
    private ToyView view;
    private PriorityQueue<Toy> toyQueue;

    public ToyPresenter(ToyView view) {
        this.view = view;
        this.toyQueue = new PriorityQueue<>(Comparator.comparingInt(Toy::getWeight).reversed());
    }

    public void addToy(int id, String name, int weight, int quantity) {
        int clampedWeight = Math.min(weight, 100);
        Toy toy = new Toy(id, name, clampedWeight, quantity);
        toyQueue.add(toy);
    }

    public void updateWeight(int toyId, int weight) {
        int clampedWeight = Math.min(weight, 100);
        for (Toy toy : toyQueue) {
            if (toy.getId() == toyId) {
                toy.setWeight(clampedWeight);
                break;
            }
        }
    }

    public void startRaffle() {
        List<Toy> prizes = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            Toy prize = drawPrize();
            if (prize == null) {
                break;
            }

            prizes.add(prize);
            prize.decreaseQuantity();
            view.displayToy(prize);
        }

        writePrizesToFile(prizes);
    }

    private Toy drawPrize() {
        Random random = new Random();
        List<Toy> availableToys = new ArrayList<>();

        for (Toy toy : toyQueue) {
            if (toy.getQuantity() > 0) {
                availableToys.add(toy);
            }
        }

        if (availableToys.isEmpty()) {
            return null;
        }

        int totalWeight = availableToys.stream().mapToInt(Toy::getWeight).sum();
        int randomNumber = random.nextInt(totalWeight);

        int accumulatedWeight = 0;
        for (Toy toy : availableToys) {
            accumulatedWeight += toy.getWeight();
            if (randomNumber < accumulatedWeight) {
                return toy;
            }
        }

        return null;
    }

    private void writePrizesToFile(List<Toy> prizes) {
        try (FileWriter writer = new FileWriter("prizes.txt")) {
            for (Toy toy : prizes) {
                writer.write("Игрушка: " + toy.getName() + ", вес: " + toy.getWeight() + "\n");
            }
            writer.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
