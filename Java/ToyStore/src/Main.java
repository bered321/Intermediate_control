import Presenter.ToyPresenter;
import View.ConsoleToyView;
import View.ToyView;

public class Main {
    public static void main(String[] args) {
        ToyView view = new ConsoleToyView();
        ToyPresenter presenter = new ToyPresenter(view);


        presenter.addToy(1, "Робот", 50, 2);
        presenter.addToy(2, "Кукла", 30, 3);
        presenter.addToy(3, "Машина", 10, 4);
        presenter.addToy(4, "Конструктор", 10, 1);


        presenter.updateWeight(1, 70);


        presenter.startRaffle();
    }
}
