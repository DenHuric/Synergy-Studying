#include <iostream>

class BinarySearchTree {
public:
    // Конструктор для создания пустого дерева
    BinarySearchTree() : root(nullptr) {}

    // Публичный метод для вставки нового значения в дерево
    void insert(int value) {
        root = insert(root, value);
    }

    // Публичный метод для удаления значения из дерева
    void remove(int value) {
        root = remove(root, value);
    }

    // Публичный метод для поиска значения в дереве
    bool search(int value) {
        return search(root, value) != nullptr;
    }

    // Публичный метод для печати дерева в консоль
    void print() {
        inorder();
        std::cout << std::endl;
    }

private:
    // Определение структуры узла дерева
    struct Node {
        int value; // Значение узла
        Node* left; // Указатель на левого потомка
        Node* right; // Указатель на правого потомка

        // Конструктор для создания нового узла с заданным значением
        Node(int value) : value(value), left(nullptr), right(nullptr) {}
    };

    Node* root; // Корень дерева

    // Приватный метод для вставки нового значения в дерево
    Node* insert(Node* root, int value) {
        if (root == nullptr) {
            return new Node(value);
        }
        if (value < root->value) {
            root->left = insert(root->left, value);
        } else {
            root->right = insert(root->right, value);
        }
        return root;
    }

    // Приватный метод для поиска значения в дереве
    Node* search(Node* root, int value) {
        if (root == nullptr || root->value == value) {
            return root;
        }
        if (value < root->value) {
            return search(root->left, value);
        } else {
            return search(root->right, value);
        }
    }

    // Приватный метод для нахождения узла с минимальным значением в дереве
    Node* findMin(Node* root) {
        while (root->left != nullptr) {
            root = root->left;
        }
        return root;
    }

    // Приватный метод для удаления значения из дерева
    Node* remove(Node* root, int value) {
        if (root == nullptr) {
            return nullptr;
        }
        if (value < root->value) {
            root->left = remove(root->left, value);
        } else if (value > root->value) {
            root->right = remove(root->right, value);
        } else {
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            } else {
                Node* temp = findMin(root->right);
                root->value = temp->value;
                root->right = remove(root->right, temp->value);
            }
        }
        return root;
    }

    // Приватный метод для печати узлов дерева в порядке возрастания
    void inorder() {
        inorderHelper(root);
    }

    // Приватный рекурсивный метод-помощник для печати
    void inorderHelper(Node* root) {
        if (root != nullptr) {
            inorderHelper(root->left);
            std::cout << root->value << ' ';
            inorderHelper(root->right);
        }
    }
};

// Тесты в функции main()
int main() {
    BinarySearchTree tree;

    // Вставляем элементы
    tree.insert(8);
    tree.insert(3);
    tree.insert(10);
    tree.insert(1);
    tree.insert(6);
    tree.insert(14);
    tree.insert(4);
    tree.insert(7);
    tree.insert(13);

    tree.print();

    // Проверка поиска элементов
    std::cout << "Search 3: " << (tree.search(3) ? "найден" : "не найден") << std::endl;
    std::cout << "Search 9: " << (tree.search(9) ? "найден" : "не найден") << std::endl;

    // Удаление элемента и повторный вывод дерева
    tree.remove(3);
    std::cout << "Search 3: " << (tree.search(3) ? "найден" : "не найден") << std::endl;
    tree.print();

    return 0;
}
