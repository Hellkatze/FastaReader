class Seq:
    """
    Класс для представления биологической последовательности.

    Attributes:
        head (str): Заголовок последовательности (из FASTA файла).
        seq (str): Сама последовательность (нуклеотиды или аминокислоты).
    """

    def __init__(self, head, sequence):
        """
        Инициализирует объект последовательности.

        Args:
            head (str): Заголовок.
            sequence (str): Последовательность.
        """
        self.head = head
        self.seq = sequence

    def str(self):
        """Выводит информацию о последовательности в консоль."""
        print("Name:", self.head.strip('>'), "\nSequence:", self.seq)

    def len(self):
        """
        Вычисляет длину последовательности, сохраняет её в self.len и выводит на экран.
        """
        self.len = len(self.seq)
        print(self.len)

    def seq_alphabet(self):
        """
        Определяет тип последовательности (ДНК/РНК или Белок).

        Returns:
            str: 'Nucleotide', если в строке только ATGCU, иначе 'Protein'.
        """
        nuq_chars = set("ATGCU")
        seq_chars = set(self.seq.upper())

        if seq_chars.issubset(nuq_chars):
            return "Nucleotide"
        else:
            return "Protein"


class FastaReader:
    """
    Класс для чтения и парсинга файлов формата FASTA.

    Args:
        path (str): Путь к файлу .fasta.
    """

    def __init__(self, path):
        self.path = path

    def __format_check(self):
        """
        Проверяет, начинается ли файл с символа '>'.
        
        Raises:
            ValueError: Если файл не соответствует формату FASTA.
        """
        with open(self.path, 'r') as file:
            first_line = file.readline().strip()
            if not first_line.startswith('>'):
                raise ValueError("Not Fasta")

    def read(self):
        """
        Построчно читает файл и генерирует объекты Seq.

        Yields:
            Seq: Объект класса Seq для каждой записи в файле.
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
test_filename = "test_data.fasta"
with open(test_filename, "w") as f:
    f.write(">Human_DNA_Fragment\nATGCATGC\nATGC\n") # ДНК в две строки
    f.write(">Insulin_Protein\nMALWMRLLPLLALLALWGPDPAAA\n") # Белок

reader = FastaReader(test_filename)
for bb in reader.read():
    bb.str()
    bb.len()
    print(bb.seq_alphabet())
    print("-" * 30)