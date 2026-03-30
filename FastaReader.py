class Seq:
    """
    Класс для представления биологической последовательности.

    Args:
        head : Имя последовательности.
        seq : Собсвенно последовательность.
    """

    def __init__(self, head, sequence): #creating class properties
        self.head = head
        self.seq = sequence

    def str(self):
        """Приводит последовательность к строковому виду."""
        print("Name:", self.head.strip('>'), "\nSequence:", self.seq) #sequence in string

    def len(self):
        """
        Вычисляет длину последовательности и выводит в консоль результат.
        """
        self.len = len(self.seq) #get sequence lenght
        print(self.len)

    def seq_alphabet(self):
        """
        Определяет тип последовательности (нуклеотиды или протеины).

        Returns:
            str: 'Nucleotide', если в последовательности встречаются только нуклеотиды, иначе 'Protein'.
        """
        nuq_chars = set("ATGCU") #creating set of nucleotide
        seq_chars = set(self.seq.upper()) #creating set from our sequence(all symbols r big)

        if seq_chars.issubset(nuq_chars): #check for subset
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
        with open(self.path, 'r') as file: #reading file
            first_line = file.readline().strip()
            if not first_line.startswith('>'):
                raise ValueError("Not Fasta")

    def read(self):
        """
        Построчно читает файл и генерирует объекты Seq, если прошёл порверку формата.

        """
        self.__format_check() #check validating format

        with open(self.path, 'r') as file:
            head = None
            seq_list = []

            for lines in file:
                lines = lines.strip() #remove spaces
                if not lines: continue  #skip empty lines

                if lines.startswith('>'): #check for new cell
                    if head is not None: #remove zero cell
                        yield Seq(head, "".join(seq_list)) #creating Seq object
                    head = lines
                    seq_list = []
                else: #appending line to current sequence
                    seq_list.append(lines)
            
            if head is not None: #for last cell
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