class Seq:
    """
    Класс для представления биологической последовательности.

    Args:
        head : Имя последовательности.
        seq : Собсвенно последовательность.
    """

    def __init__(self, head, sequence):
        self.head = head
        self.seq = sequence

    def str(self):
        """Приводит последовательность к строковому виду."""
        print("Name:", self.head.strip('>'), "\nSequence:", self.seq)

    def len(self):
        """
        Вычисляет длину последовательности и выводит в консоль результат.
        """
        self.len = len(self.seq)
        print(self.len)

    def seq_alphabet(self):
        """
        Определяет тип последовательности (нуклеотиды или протеины).

        Returns:
            str: 'Nucleotide', если в последовательности встречаются только нуклеотиды, иначе 'Protein'.
        """
        nuq_chars = set("ATGCU")
        seq_chars = set(self.seq.upper())

        if seq_chars.issubset(nuq_chars):
            print("Nucleotide")
        else:
            print("Protein")


class FastaReader:
    """
    Класс для чтения формата .fasta, создания записей из объектов класса Seq.

    Args:
        path : Путь к файлу .fasta. Задаётся пользователем.
    """

    def __init__(self, path):
        self.path = path

    def __format_check(self):
        """
        Проверяет соответсвие формата заданного файла.
        
        """
        with open(self.path, 'r') as file:
            first_line = file.readline().strip()
            if not first_line.startswith('>'):
                raise ValueError("Not Fasta")

    def read(self):
        """
        Построчно читает файл и генерирует объекты Seq, если прошёл порверку формата.

        """
        self.__format_check()

        with open(self.path, 'r') as file:
            head = None
            seq_list = []

            for lines in file:
                lines = lines.strip()
                if not lines:
                    continue

                if lines.startswith('>'):
                    if head is not None:
                        yield Seq(head, "".join(seq_list))
                    head = lines
                    seq_list = []
                else:
                    seq_list.append(lines)
            
            if head is not None:
                yield Seq(head, "".join(seq_list))

# ---демнострация
print("Введите название вашего файла или полный путь до него:")
filename = input()


reader = FastaReader(filename)

for out in reader.read():
    ''''Менять выводные данные здесь:'''
    out.str()
    out.len()
    out.seq_alphabet()
    print("-" * 30)